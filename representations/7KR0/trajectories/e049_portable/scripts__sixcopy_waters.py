"""sixcopy_waters.py - the E041 six-copy water treatment on any protein, in one file, without the harness (E049).

Runs under phenix.python (Phenix 2.1, Python 3.9) with cctbx and numpy only: no autoref, no gemmi, no Untangler.
Everything it does is a consolidation of scripts/experiments/{e044_autosix,e044_build,e044_logic,e041_waters,
e041_clearance,e035_water_hygiene,e041_prune,e041_anisou,e035_merge_mtz}.py, autoref/flags.py, autoref/cctbx/
rfree_split.py, scripts/verify/indep_rfree.py and autoref/tools/phenix_refine.py; the rules are the ones registered in
state/notes/experiments.md (E041, E044, E049) and docs/md/PROTOCOL.md section 3 and 18.

    phenix.python sixcopy_waters.py <PDB_ID> --out DIR [--model deposited|PATH] [--data PATH.mtz|PATH-sf.cif]
                                    [--frozen-dir DIR] [--stop-after fetch|prep|baseline|build|run] [--resume] ...

Stages (each resumable; a finished stage is reused with --resume):
  fetch     RCSB model mmCIF and structure factors (sha256 recorded), or the files given.
  prep      structure factors -> data.mtz (amplitudes preferred when the intensity column is a placeholder, as the
            harness decides), flags.mtz (R-free flags inherited from _refln.status 'f', never regenerated), split.mtz
            (select / report [/ sleep] halves of the free set, seeded, resolution-stratified), data_flags.mtz (one file
            for phenix.refine). --frozen-dir takes an existing frozen set and verifies its free set against the
            deposited status-f set. No free set in the entry: generated ONCE (5 %, seeded) with a loud banner.
  baseline  N seeds of the deposited model re-refined with the campaign's standing recipe: mean and sigma of
            select / report / full / gap (PROTOCOL 4.4).
  build     six copies A-F per residue, cloned conformers shaken 0.2 A per atom, occupancies 0.1667 x4 + 0.1666 x2,
            waters per conformer, ligands and ions single, riding H completed, protein ANISOU completed when d_min <=
            --aniso-protein-below, then 20 restrained macro-cycles = S0.
  run       rounds of paired steps (candidate vs the same refinement without the change, n seeds each): weights
            stack (wc 0.3 / wu 0.25 vs 0.5 / 1), per-conformer water picks at 3.0 -> 2.5 -> 2.0 sigma with own-conformer
            clearance including riding H, hygiene (occupancy floor 0.02, same-altloc merge < 0.6 A), clash cleanup
            (the water copies phenix.clashscore lists in own-conformer clashes, as E041's endpoint; or the element-aware
            vdW rule + margin with --cleanup-rule vdw), anisotropic waters.
            Judge: delta select <= -2 sigma_select, delta report < 0, delta gap <= +0.002, clashscore <= 5.0 or <= the
            control's; the composite pick + cleanup is judged as one move when the pick fails only on clashscore; stop
            after 3 rounds without an adoption, --max-rounds or --budget-h.
Outputs: DIR/TRAJECTORY.md, DIR/models/<step>.pdb, DIR/run.json (every number, argv, sha256, versions), DIR/log.

Cross-validation (PROTOCOL 3): the flag file is hashed at prep and every phenix.refine command is checked before it
runs; a command that would regenerate or ignore the flags, disable the suitability test or move a resolution or sigma
cutoff is refused (FlagIntegrityError). Every evaluation reads the frozen flags; nothing is generated after prep.
The six-copy model is a representation (PROTOCOL 18.1), never a deliverable.
"""
# ruff: noqa: UP006, UP031, UP035, UP037, UP045   (phenix.python is 3.9: no PEP 585/604 syntax; printf formatting kept)
from __future__ import annotations

import argparse
import calendar
import gzip
import hashlib
import json
import math
import os
import queue
import random
import re
import shutil
import subprocess
import sys
import threading
import time
import zlib
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Tuple

try:
    import numpy as np
except ImportError:  # the pure-python parts (tests) do not need it
    np = None

try:  # cctbx is only needed to run; the pure logic below is importable without it (tests/test_portable_sixcopy.py)
    import iotbx.pdb  # noqa: F401
    HAVE_CCTBX = True
except ImportError:
    HAVE_CCTBX = False

VERSION = "sixcopy_waters 1.0 (E049, 2026-10-09)"
ALT = "ABCDEF"
WATER_NAMES = ("HOH", "WAT", "DOD", "H2O")
FLAG_LABEL = "R-free-flags"
FREE_VALUE, WORK_VALUE = 0, 1
SPLIT_LABEL = "SPLIT"
SPLIT_WORK, SPLIT_SELECT, SPLIT_REPORT, SPLIT_SLEEP = 0, 1, 2, 3
STATUS_FREE, STATUS_WORK = "f", "o"
STATUS_UNMEASURED = frozenset({"x", "-", "<", "h", "l"})
RCSB = "https://files.rcsb.org/download/"

# ----------------------------------------------------------------------------------------------- registered rules
GAP_MAX = 0.002          # delta(R-free - R-work), absolute (E041/E044; D570 for the ensemble column)
K_SIGMA = 2.0
CLASH_CAP = 5.0          # thresholds geometry.clashscore.abs_max_highres
ROTA_CAP = 1.5           # thresholds geometry.rota_outliers_pct.abs_max (per cent)
CLASH_DROP = 0.10        # geometry step: relative clashscore reduction required
IMPROVING = ("weights", "pick", "aniso_water", "loop")
GEOMETRY = ("cleanup",)
SIGMA_LADDER = (3.0, 2.5, 2.0)
DEFAULT_WEIGHTS = (0.5, 1.0)     # Untangler Refine.sh defaults: -c 0.5 -u 1
STACK_WEIGHTS = (0.3, 0.25)      # E041's stack: wc 0.3 / wu 0.25
VDW_LIMITS = {"C": 2.7, "S": 2.8, "N": 2.4, "O": 2.4, "Hc": 2.2, "Hp": 1.5}   # e041_prune --vdw 1 (water O to ...)


class FlagIntegrityError(RuntimeError):
    """A PROTOCOL 3 violation: the run halts, nothing is logged-and-continued."""


def read_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def read_json(path: str) -> dict:
    with open(path) as f:
        return json.load(f)


def utc() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def sha256(path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


# ------------------------------------------------------------------------------------ pure logic (e044_logic.py)
def copy_occupancies(k: int = 6) -> List[float]:
    """k occupancies at 4 decimals summing to exactly 1.0000; k = 6 gives 0.1667 x 4 + 0.1666 x 2 (PROTOCOL 18.5)."""
    if k < 1:
        raise ValueError("k >= 1")
    base = 10000 // k
    extra = 10000 - base * k
    return [(base + (1 if i < extra else 0)) / 10000 for i in range(k)]


def allocate(q: Dict[str, float], k: int) -> Dict[str, int]:
    """Largest-remainder allocation of k copies over conformers with occupancies q (ties by letter)."""
    tot = sum(q.values()) or 1.0
    raw = {x: k * v / tot for x, v in q.items()}
    n = {x: math.floor(r) for x, r in raw.items()}
    for x in sorted(raw, key=lambda x: (-(raw[x] - n[x]), x))[: k - sum(n.values())]:
        n[x] += 1
    return n


def copy_order(q: Dict[str, float], k: int = 6) -> List[str]:
    """Conformer letter of copy j = 0..k-1, letters in order (neighbouring split residues stay contiguous)."""
    a = allocate(q, k)
    return [x for x in sorted(a) for _ in range(a[x])]


def mean(xs: Sequence[float]) -> float:
    xs = list(xs)
    if not xs:
        raise ValueError("mean of nothing")
    return sum(xs) / len(xs)


def sd(xs: Sequence[float]) -> float:
    xs = list(xs)
    if len(xs) < 2:
        return 0.0
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def pooled_sd(a: Sequence[float], b: Sequence[float]) -> float:
    a, b = list(a), list(b)
    dfa, dfb = len(a) - 1, len(b) - 1
    if dfa + dfb <= 0:
        return 0.0
    ma, mb = mean(a), mean(b)
    ss = sum((x - ma) ** 2 for x in a) + sum((x - mb) ** 2 for x in b)
    return math.sqrt(ss / (dfa + dfb))


def summarize(rows: Sequence[dict]) -> dict:
    out = {"n": len(rows)}
    for k in ("r_free_select", "r_free_report", "r_free_full", "r_work"):
        v = [float(r[k]) for r in rows]
        out[k] = mean(v)
        out[k + "_sd"] = sd(v)
    g = [float(r["r_free_full"]) - float(r["r_work"]) for r in rows]
    out["gap"] = mean(g)
    out["gap_sd"] = sd(g)
    return out


def median_row(rows: Sequence[dict], key: str = "r_free_select") -> dict:
    """The seed row with the median value of `key` (lower middle for even n): the model a step carries forward."""
    s = sorted(rows, key=lambda r: (float(r[key]), str(r.get("seed", ""))))
    return s[(len(s) - 1) // 2]


def judge(kind: str, cand: Sequence[dict], ctrl: Sequence[dict], floor_sigma: Dict[str, float],
          clash_cand: Optional[float], clash_ctrl: Optional[float],
          rota_cand: Optional[float] = None, rota_ctrl: Optional[float] = None) -> dict:
    """Verdict for one paired step (E044 rule, registered before any run; rotamer clause per D568 / E049).

    improving steps: delta select <= -K_SIGMA sigma_select, delta report < 0, delta gap <= GAP_MAX,
                     clashscore(cand) <= CLASH_CAP or <= clashscore(ctrl), rotamer outliers <= ROTA_CAP or <= ctrl's
    geometry step:   clashscore(cand) >= CLASH_DROP below ctrl (or <= cap with ctrl above), select and report not
                     worse than +K_SIGMA sigma, delta gap <= GAP_MAX
    sigma for a subset = max(floor sigma, pooled seed SD of the two arms).
    """
    if len(cand) < 2 or len(ctrl) < 2:
        return {"adopted": False, "reasons": ["fewer than 2 seeds in an arm"], "kind": kind}
    c, k = summarize(cand), summarize(ctrl)
    sig = {}
    for s in ("r_free_select", "r_free_report"):
        sig[s] = max(float(floor_sigma.get(s, 0.0) or 0.0), pooled_sd([r[s] for r in cand], [r[s] for r in ctrl]))
    d_sel = c["r_free_select"] - k["r_free_select"]
    d_rep = c["r_free_report"] - k["r_free_report"]
    d_full = c["r_free_full"] - k["r_free_full"]
    d_gap = c["gap"] - k["gap"]
    reasons: List[str] = []
    ok = True
    if kind in GEOMETRY:
        if clash_cand is None or clash_ctrl is None:
            ok = False; reasons.append("clashscore missing")
        elif not (clash_cand <= clash_ctrl * (1 - CLASH_DROP) or (clash_cand <= CLASH_CAP < clash_ctrl)):
            ok = False; reasons.append("clashscore %.2f not >= %d%% below control %.2f" % (clash_cand, CLASH_DROP * 100, clash_ctrl))
        if d_sel > K_SIGMA * sig["r_free_select"]:
            ok = False; reasons.append("select worse by %+.5f > %g sigma (%.5f)" % (d_sel, K_SIGMA, sig["r_free_select"]))
        if d_rep > K_SIGMA * sig["r_free_report"]:
            ok = False; reasons.append("report worse by %+.5f > %g sigma (%.5f)" % (d_rep, K_SIGMA, sig["r_free_report"]))
    else:
        if not d_sel <= -K_SIGMA * sig["r_free_select"] or d_sel >= 0:
            ok = False; reasons.append("select %+.5f not <= -%g sigma (%.5f)" % (d_sel, K_SIGMA, sig["r_free_select"]))
        if not d_rep < 0:
            ok = False; reasons.append("report %+.5f does not agree in sign" % d_rep)
        if clash_cand is not None and clash_ctrl is not None:
            if not (clash_cand <= CLASH_CAP or clash_cand <= clash_ctrl):
                ok = False; reasons.append("clashscore %.2f > %g and above control %.2f" % (clash_cand, CLASH_CAP, clash_ctrl))
        elif clash_cand is None:
            ok = False; reasons.append("clashscore missing")
    if rota_cand is not None and rota_ctrl is not None and not (rota_cand <= ROTA_CAP or rota_cand <= rota_ctrl):
        ok = False; reasons.append("rotamer outliers %.2f%% > %g%% and above control %.2f%%" % (rota_cand, ROTA_CAP, rota_ctrl))
    if d_gap > GAP_MAX:
        ok = False; reasons.append("gap widens %+.5f > %g" % (d_gap, GAP_MAX))
    if ok:
        reasons.append("all criteria met")
    return {"kind": kind, "adopted": ok, "reasons": reasons, "d_select": d_sel, "d_report": d_rep, "d_full": d_full,
            "d_gap": d_gap, "sigma_select": sig["r_free_select"], "sigma_report": sig["r_free_report"],
            "z_select": (d_sel / sig["r_free_select"]) if sig["r_free_select"] > 0 else None,
            "cand": c, "ctrl": k, "clash_cand": clash_cand, "clash_ctrl": clash_ctrl,
            "rota_cand": rota_cand, "rota_ctrl": rota_ctrl}


def composite_eligible(verdict: dict) -> bool:
    """True when an improving step was refused ONLY on clashscore: the step and its clash cleanup are then judged as
    one move against the step's own control continued identically (D563)."""
    if not verdict or verdict.get("adopted"):
        return False
    reasons = [str(r) for r in verdict.get("reasons") or [] if str(r) != "all criteria met"]
    return bool(reasons) and all(r.startswith("clashscore") for r in reasons)


def next_sigma(current: float, last_n_sites: Optional[int], min_sites: int = 20) -> float:
    """Stays at `current` unless the last pick placed fewer than `min_sites` sites, then one rung lower."""
    if last_n_sites is None or last_n_sites >= min_sites:
        return current
    lower = [s for s in SIGMA_LADDER if s < current - 1e-9]
    return lower[0] if lower else current


def round_sigma(round_index: int) -> float:
    return 3.0 if round_index <= 1 else 2.5


def should_stop(round_adopted: Sequence[bool], elapsed_h: float, budget_h: float, max_rounds: int,
                patience: int = 3) -> Optional[str]:
    if elapsed_h >= budget_h:
        return "wall-clock budget %g h reached (%.1f h)" % (budget_h, elapsed_h)
    if len(round_adopted) >= max_rounds:
        return "%d rounds completed" % max_rounds
    if len(round_adopted) >= patience and not any(round_adopted[-patience:]):
        return "%d consecutive rounds without an adopted step" % patience
    return None


# ------------------------------------------------------------------------- PROTOCOL 3 guard (tools/phenix_refine.py)
_TRUE = r"(true|yes|1)\b"
_EXEMPT_RES_PREFIXES = ("bulk_solvent_and_scale.", "rigid_body.", "ncs.", "fake_f_obs.")


def argv_violations(argv: Iterable[str]) -> List[str]:
    """Every phenix.refine command is scanned before it runs (typed fields AND the final argv, so nothing can be
    smuggled past the guard): regenerating flags, refining against all data, silencing the suitability test, or a
    resolution / sigma cutoff are refused (PROTOCOL 3.1-3.5)."""
    out: List[str] = []
    for a in argv:
        s = str(a).strip()
        low = s.lower().replace(" ", "")
        if re.search(r"r_free_flags\.generate=" + _TRUE, low) or (re.search(r"(^|\.)generate=" + _TRUE, low) and "r_free" in low):
            out.append("flag generation requested (%r) - PROTOCOL 3.2 forbids regenerating flags" % s)
        if re.search(r"ignore_r_free_flags=" + _TRUE, low):
            out.append("ignore_r_free_flags set (%r) - PROTOCOL 3.5 forbids refining against all data" % s)
        if re.search(r"disable_suitability_test=" + _TRUE, low):
            out.append("disable_suitability_test set (%r) - PROTOCOL 3.1" % s)
        for leaf in ("high_resolution", "low_resolution", "sigma_fobs_rejection_criterion", "sigma_iobs_rejection_criterion"):
            m = re.search(r"(^|\.)(%s)=(.+)$" % leaf, low)
            if not m or m.group(3) in ("none", ""):
                continue
            if any(p.replace(" ", "") in low for p in _EXEMPT_RES_PREFIXES):
                continue
            out.append("%s set (%r) outside a pre-registered paired refinement - PROTOCOL 3.4" % (leaf, s))
    return out


def check_refine_argv(argv: Sequence[str], flags_mtz: Optional[str] = None, flags_sha256: Optional[str] = None) -> None:
    v = argv_violations(argv)
    if flags_mtz and flags_sha256 and os.path.exists(flags_mtz) and sha256(flags_mtz) != flags_sha256:
        v.append("flags file %s changed since prep (sha256 differs) - the frozen test set moved (PROTOCOL 3.1/3.3)" % flags_mtz)
    if v:
        raise FlagIntegrityError("refusing to dispatch phenix.refine: " + "; ".join(v))


# --------------------------------------------------------------------------------------- free-set split (autoref/split.py)
def split_seed(target: str, n_parts: int) -> int:
    """Frozen per-target seed; differs from the harness's v1 (crc32(target)) and v2 (crc32('<T>:split_v2')) seeds
    on purpose, so a generated split is never mistaken for a campaign split."""
    return zlib.crc32(("%s:sixcopy_split%d" % (target, n_parts)).encode())


def shell_bounds(n: int, n_shells: int) -> List[Tuple[int, int]]:
    k = max(1, min(int(n_shells), n)) if n else 1
    edges = [round(i * n / k) for i in range(k + 1)]
    return [(edges[i], edges[i + 1]) for i in range(k)]


def assign_split(free_hkl: Iterable[Tuple[int, int, int]], d_of: Callable, target: str, n_parts: int = 2,
                 n_shells: int = 20) -> dict:
    """Partition the free reflections into n_parts classes (select, report[, sleep]) stratified by resolution: sort
    by (-d, h, k, l), cut into n_shells equal-count shells, shuffle inside each shell with one seeded generator, deal
    round robin; the deal continues across shells so class totals differ by at most one (split v2's method)."""
    classes = ("select", "report", "sleep")[:n_parts]
    hkls = sorted({tuple(int(x) for x in h) for h in free_hkl})
    dvals = {h: float(d_of(h)) for h in hkls}
    order = sorted(hkls, key=lambda h: (-dvals[h], h))
    seed = split_seed(target, n_parts)
    rng = random.Random(seed)
    out: Dict[str, list] = {c: [] for c in classes}
    shells = []
    k = 0
    for i, (a, b) in enumerate(shell_bounds(len(order), n_shells)):
        chunk = order[a:b]
        idx = list(range(len(chunk)))
        rng.shuffle(idx)
        counts = dict.fromkeys(classes, 0)
        for j in idx:
            c = classes[k % n_parts]
            out[c].append(chunk[j]); counts[c] += 1; k += 1
        shells.append({"shell": i + 1, "n": len(chunk), "d_max": round(dvals[chunk[0]], 4) if chunk else None,
                       "d_min": round(dvals[chunk[-1]], 4) if chunk else None, **{"n_" + c: counts[c] for c in classes}})
    return {"seed": seed, "n_parts": n_parts, "n_shells": len(shells), "shells": shells,
            "method": "free reflections sorted by (-d, h, k, l), %d equal-count shells, random.Random(%d).shuffle per "
                      "shell (one generator), dealt round robin to %s" % (len(shells), seed, "/".join(classes)),
            **{c: sorted(out[c]) for c in classes}}


# ------------------------------------------------------------------------------------------ small parsers (pure)
def parse_clashscore_log(text: str) -> Optional[float]:
    for line in text.splitlines():
        if "clashscore = " in line:
            try:
                return float(line.split("=")[-1].strip())
            except ValueError:
                return None
    return None


def parse_rotalyze_log(text: str) -> Optional[float]:
    for line in text.splitlines():
        if "SUMMARY:" in line and "outliers" in line:
            try:
                return float(line.split("SUMMARY:")[1].split("%")[0])
            except (ValueError, IndexError):
                return None
    return None


def clashlog_water_kills(text: str, water_occ: Dict[Tuple[str, int, str], float]) -> set:
    """Water copies named by phenix.clashscore in a clash (overlap >= 0.4 A) with an atom of their own conformer or
    with a blank-altloc atom; of two clashing same-conformer waters the lower-occupancy one (e041_prune --clash-log).
    Keys are (chain, resseq, altloc)."""
    kill = set()
    for line in text.splitlines():
        if not line.startswith(" ") or ":" not in line or "HOH" not in line:
            continue
        left, ov = line.rstrip("\n").rsplit(":", 1)
        try:
            if float(ov) < 0.4:
                continue
        except ValueError:
            continue
        try:
            spec = [(x[0:2].strip(), int(x[2:6]), x[7].strip(), x[8:11]) for x in (left[0:16], left[17:33])]
        except ValueError:
            continue
        (c1, n1, a1, r1), (c2, n2, a2, r2) = spec
        if a1 and a2 and a1 != a2:
            continue
        if r1 == "HOH" and r2 == "HOH":
            k1, k2 = (c1, n1, a1), (c2, n2, a2)
            kill.add(k1 if water_occ.get(k1, 0) <= water_occ.get(k2, 0) else k2)
        elif r1 == "HOH":
            kill.add((c1, n1, a1))
        elif r2 == "HOH":
            kill.add((c2, n2, a2))
    return kill


def parse_refine_log(text: str) -> dict:
    """R-work / R-free at the end of a phenix.refine log (the 'Final R-work = ..., R-free = ...' line)."""
    out = {}
    m = re.findall(r"R-work\s*=\s*([0-9.]+),?\s*R-free\s*=\s*([0-9.]+)", text)
    if m:
        out["r_work_log"], out["r_free_log"] = float(m[-1][0]), float(m[-1][1])
    m2 = re.search(r"n_free\s*=\s*(\d+)|Number of free reflections\s*[:=]\s*(\d+)", text)
    if m2:
        out["n_free_log"] = int(m2.group(1) or m2.group(2))
    return out


def normocc_lines(lines: Iterable[str], k: int = 6) -> Tuple[List[str], int]:
    """PROTOCOL 18.5: phenix.refine writes PDB occupancies to two decimals (0.17 x 6 = 1.02); every non-water atom
    with altloc among the first k letters and occupancy within 0.02 of its copy value is rewritten to
    copy_occupancies(k) (e041_anisou.py normocc). Returns (lines, n_rewritten)."""
    occ = copy_occupancies(k)
    letters = ALT[:k] if k <= 6 else "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:k]
    n = 0; out = []
    for line in lines:
        if line.startswith(("ATOM", "HETATM")) and line[17:20] not in WATER_NAMES and line[16] in letters:
            try:
                q = float(line[54:60])
            except ValueError:
                q = None
            v = occ[letters.index(line[16])]
            if q is not None and abs(q - v) <= 0.02 and ("%6.4f" % v) != line[54:60]:
                line = line[:54] + "%6.4f" % v + line[60:]; n += 1
        out.append(line)
    return out, n


def choose_data_array(arrays: dict, status: Optional[List[str]]) -> dict:
    """autoref.flags.choose_data_array, reduced: merged intensities when present and fully populated (phenix.refine
    applies French-Wilson), else amplitudes; a zero-filled intensity placeholder column is rejected with its counts."""
    def coverage(vt, st):
        v, s = arrays[vt], arrays[st]
        kind = "amplitudes" if vt.startswith("F_") else "intensities"
        n_meas = n_us = n_null = n_zero = n_zero_value = 0
        for i in range(len(v)):
            if status is not None and status[i] in STATUS_UNMEASURED:
                continue
            n_meas += 1
            if v[i] is None or s[i] is None:
                n_null += 1
            elif v[i] == 0.0 and s[i] == 0.0:
                n_zero += 1
            elif kind == "amplitudes" and v[i] == 0.0:
                n_zero_value += 1
            else:
                n_us += 1
        return {"n_measured_rows": n_meas, "n_usable": n_us, "n_null": n_null, "n_zero_placeholder": n_zero, "n_zero_value": n_zero_value}
    has_i = "intensity_meas" in arrays and "intensity_sigma" in arrays
    has_f = "F_meas_au" in arrays and "F_meas_sigma_au" in arrays
    cov_i = coverage("intensity_meas", "intensity_sigma") if has_i else None
    cov_f = coverage("F_meas_au", "F_meas_sigma_au") if has_f else None
    if not has_i and not has_f:
        raise FlagIntegrityError("neither intensity_meas/intensity_sigma nor F_meas_au/F_meas_sigma_au in the structure factors")
    if has_i and (not has_f or cov_i["n_usable"] >= cov_f["n_usable"]):
        return {"kind": "intensities", "value_tag": "intensity_meas", "sigma_tag": "intensity_sigma", "labels": ("IMEAN", "SIGIMEAN"),
                "coverage": {"intensities": cov_i, "amplitudes": cov_f}, "reason": "merged intensities present and populated; phenix.refine applies French-Wilson"}
    return {"kind": "amplitudes", "value_tag": "F_meas_au", "sigma_tag": "F_meas_sigma_au", "labels": ("FP", "SIGFP"),
            "coverage": {"intensities": cov_i, "amplitudes": cov_f},
            "reason": ("intensity column covers only %d of %d measured rows (%d zero placeholders): amplitudes are the complete array"
                       % (cov_i["n_usable"], cov_i["n_measured_rows"], cov_i["n_zero_placeholder"])) if has_i else "no merged intensities; amplitudes are all there is"}


def detect_flag_convention(status: Optional[List[str]], rflag: Optional[List[str]]) -> dict:
    """autoref.flags.detect_convention: _refln.status 'f' when present (with at least one 'f'); else a binary
    _refln.pdbx_r_free_flag whose minority value is the test set; else no inherited free set."""
    if status is not None and any(s == STATUS_FREE for s in status):
        return {"source": "_refln.status", "free_symbol": STATUS_FREE}
    if rflag is not None:
        vals = {}
        for v in rflag:
            if v in (None, "", "?", "."):
                continue
            vals[v] = vals.get(v, 0) + 1
        if len(vals) == 2:
            minority = min(vals, key=lambda x: vals[x])
            return {"source": "_refln.pdbx_r_free_flag", "free_symbol": minority, "counts": vals}
        if len(vals) > 2:
            raise FlagIntegrityError("_refln.pdbx_r_free_flag has %d distinct values and no _refln.status; refusing to guess" % len(vals))
    return {"source": None, "free_symbol": None}


def generate_flags_once(hkls: Sequence[Tuple[int, int, int]], target: str, fraction: float = 0.05) -> set:
    """Only for an entry with NO deposited free set: generated once, before any refinement, seeded, frozen (PROTOCOL 3.2)."""
    rng = random.Random(zlib.crc32(("%s:generated_free_set" % target).encode()))
    idx = list(range(len(hkls)))
    rng.shuffle(idx)
    n = max(1, round(fraction * len(hkls)))
    return {tuple(hkls[i]) for i in idx[:n]}


# ============================================================================================ cctbx-backed parts
def _cctbx():
    if not HAVE_CCTBX:
        raise RuntimeError("cctbx is not importable: run this file under phenix.python")


def read_sf_cif(path: str) -> dict:
    """Structure-factor mmCIF -> plain lists (autoref.flags.read_sf_cif without gemmi). A multi-block file is
    resolved to the single block that carries a deposited free set (D502); several or none -> refuse."""
    _cctbx()
    import iotbx.cif
    cm = iotbx.cif.reader(file_path=path).model()
    blocks = [(k, b) for k, b in cm.items() if b.get("_refln.index_h") is not None]
    if not blocks:
        raise FlagIntegrityError("%s: no _refln loop" % path)

    def has_free(b):
        st = b.get("_refln.status")
        if st is not None and any(str(v) == STATUS_FREE for v in st):
            return True
        rf = b.get("_refln.pdbx_r_free_flag")
        return rf is not None and len({str(v) for v in rf if str(v) not in ("?", ".", "")}) > 1
    if len(blocks) > 1:
        with_free = [kb for kb in blocks if has_free(kb[1])]
        if len(with_free) != 1:
            raise FlagIntegrityError("%s: %d _refln blocks, %d with a deposited free set; exactly one is required (D502)"
                                     % (path, len(blocks), len(with_free)))
        blocks = with_free
    name, b = blocks[0]

    def col(tag):
        v = b.get("_refln." + tag)
        return None if v is None else [str(x) for x in v]

    def fcol(tag):
        v = col(tag)
        if v is None:
            return None
        out = []
        for s in v:
            s = s.strip()
            out.append(None if s in ("?", ".", "") else float(s))
        return out
    h, k, l = col("index_h"), col("index_k"), col("index_l")
    hkl = [(int(a), int(bb), int(c)) for a, bb, c in zip(h, k, l)]
    arrays = {t: fcol(t) for t in ("F_meas_au", "F_meas_sigma_au", "intensity_meas", "intensity_sigma") if col(t) is not None}
    cell = tuple(float(str(b.get("_cell." + t)).strip("'\"")) for t in ("length_a", "length_b", "length_c", "angle_alpha", "angle_beta", "angle_gamma"))
    sg = b.get("_symmetry.space_group_name_H-M") or b.get("_space_group.name_H-M_alt")
    if sg is None:
        raise FlagIntegrityError("%s: no space group" % path)
    return {"path": path, "block": name, "cell": cell, "spacegroup": str(sg).strip().strip("'\""), "n_rows": len(hkl), "hkl": hkl,
            "status": col("status"), "r_free_flag": col("pdbx_r_free_flag"), "arrays": arrays,
            "columns": sorted(t for t in ("status", "pdbx_r_free_flag", "F_meas_au", "F_meas_sigma_au", "intensity_meas", "intensity_sigma") if col(t) is not None)}


def _symmetry(cell, sg):
    from cctbx import crystal
    return crystal.symmetry(unit_cell=cell, space_group_symbol=sg)


def write_mtz(path: str, cs, hkl: List[Tuple[int, int, int]], columns: List[Tuple[str, str, list]]) -> None:
    """columns: [(root_label, kind, values)] with kind 'F' (values = (F, sigF) pairs), 'I' ((I, sigI) pairs) or 'int'."""
    from cctbx import miller
    from cctbx.array_family import flex
    ms = miller.set(crystal_symmetry=cs, indices=flex.miller_index(hkl), anomalous_flag=False)
    if not ms.is_unique_set_under_symmetry():
        raise FlagIntegrityError("%s: the reflection list is not unique under symmetry (unmerged data); refusing to merge it" % path)
    ds = None
    for root, kind, values in columns:
        if kind in ("F", "I"):
            arr = miller.array(ms, data=flex.double([v[0] for v in values]), sigmas=flex.double([v[1] for v in values]))
            arr = arr.set_observation_type_xray_amplitude() if kind == "F" else arr.set_observation_type_xray_intensity()
        else:
            arr = miller.array(ms, data=flex.int([int(v) for v in values]))
        ds = arr.as_mtz_dataset(column_root_label=root) if ds is None else ds.add_miller_array(arr, column_root_label=root)
    ds.mtz_object().write(path)


def read_mtz_column(path: str, label: str):
    """Miller array whose first label is `label` (or whose label string contains it)."""
    from iotbx.reflection_file_reader import any_reflection_file
    arrays = any_reflection_file(path).as_miller_arrays()
    for ma in arrays:
        ls = ma.info().label_string()
        if ls == label or ls.split(",")[0] == label or label in ma.info().labels:
            return ma
    raise FlagIntegrityError("no column %s in %s (have %s)" % (label, path, [m.info().label_string() for m in arrays]))


def flag_set(path: str, label: str = FLAG_LABEL, free_value: int = FREE_VALUE) -> Tuple[set, int]:
    ma = read_mtz_column(path, label)
    free = {tuple(h) for h, v in zip(ma.indices(), ma.data()) if int(v) == free_value}
    return free, ma.indices().size()


def prep_from_sf(sf: dict, target: str, out_dir: str, n_parts: int, log) -> dict:
    """data.mtz, flags.mtz, split.mtz, data_flags.mtz and prep.json from the deposited structure factors (autoref.flags.build)."""
    os.makedirs(out_dir, exist_ok=True)
    conv = detect_flag_convention(sf["status"], sf["r_free_flag"])
    choice = choose_data_array(sf["arrays"], sf["status"])
    val, sig = sf["arrays"][choice["value_tag"]], sf["arrays"][choice["sigma_tag"]]
    keep = []; drop_unmeasured = drop_no_value = drop_zero = 0
    for i in range(sf["n_rows"]):
        s = sf["status"][i] if sf["status"] is not None else STATUS_WORK
        if s in STATUS_UNMEASURED:
            drop_unmeasured += 1; continue
        if val[i] is None or sig[i] is None or (val[i] == 0.0 and sig[i] == 0.0):
            drop_no_value += 1; continue
        if choice["kind"] == "amplitudes" and val[i] == 0.0:
            drop_zero += 1; continue      # D503: F = 0 is not an observation phenix can refine against
        keep.append(i)
    hkl = [sf["hkl"][i] for i in keep]
    generated = False
    if conv["source"] == "_refln.status":
        is_free = [sf["status"][i] == STATUS_FREE for i in keep]
    elif conv["source"] == "_refln.pdbx_r_free_flag":
        is_free = [sf["r_free_flag"][i] == conv["free_symbol"] for i in keep]
    else:
        generated = True
        gen = generate_flags_once(hkl, target)
        is_free = [h in gen for h in hkl]
        banner = ("!" * 100 + "\n!! DEVIATION (PROTOCOL 3.2): %s carries NO deposited R-free set. A 5%% test set was generated ONCE, seeded\n"
                  "!! (crc32('%s:generated_free_set')), frozen in flags.mtz and recorded in prep.json. Never regenerate it.\n" % (sf["path"], target) + "!" * 100)
        print(banner, flush=True); log(banner)
    n_free = sum(is_free)
    if n_free == 0:
        raise FlagIntegrityError("inherited flag column selects zero free reflections")
    cs = _symmetry(sf["cell"], sf["spacegroup"])
    uc = cs.unit_cell()
    free_hkl = [h for h, f in zip(hkl, is_free) if f]
    parts = assign_split(free_hkl, lambda h: uc.d(h), target, n_parts=n_parts)
    code = {}
    for c, v in (("select", SPLIT_SELECT), ("report", SPLIT_REPORT), ("sleep", SPLIT_SLEEP)):
        for h in parts.get(c, []):
            code[h] = v
    data_rows = [(val[i], sig[i]) for i in keep]
    flag_rows = [FREE_VALUE if f else WORK_VALUE for f in is_free]
    split_rows = [code.get(h, SPLIT_WORK) for h in hkl]
    lab = choice["labels"]
    write_mtz(os.path.join(out_dir, "data.mtz"), cs, hkl, [(lab[0], "F" if choice["kind"] == "amplitudes" else "I", data_rows)])
    write_mtz(os.path.join(out_dir, "flags.mtz"), cs, hkl, [(FLAG_LABEL, "int", flag_rows)])
    write_mtz(os.path.join(out_dir, "split.mtz"), cs, hkl, [(SPLIT_LABEL, "int", split_rows)])
    write_mtz(os.path.join(out_dir, "data_flags.mtz"), cs, hkl,
              [(lab[0], "F" if choice["kind"] == "amplitudes" else "I", data_rows), (FLAG_LABEL, "int", flag_rows)])
    d_min = min(uc.d(h) for h in hkl)
    rec = {"target": target, "sf_source": sf["path"], "sf_sha256": sha256(sf["path"]), "sf_block": sf["block"], "columns_present": sf["columns"],
           "space_group": sf["spacegroup"], "unit_cell": list(sf["cell"]), "d_min": d_min,
           "data_mtz": os.path.join(out_dir, "data.mtz"), "flags_mtz": os.path.join(out_dir, "flags.mtz"),
           "split_mtz": os.path.join(out_dir, "split.mtz"), "data_flags_mtz": os.path.join(out_dir, "data_flags.mtz"),
           "flag_label": FLAG_LABEL, "test_flag_value": FREE_VALUE, "data_labels": ",".join(lab), "intensities_or_amplitudes": choice["kind"],
           "data_choice": {k: v for k, v in choice.items()}, "n_reflections": len(keep), "n_free": n_free, "n_work": len(keep) - n_free,
           "fraction_free": round(n_free / len(keep), 6), "n_rows_in_sf": sf["n_rows"], "n_dropped_unmeasured": drop_unmeasured,
           "n_dropped_missing_value": drop_no_value, "n_dropped_zero_amplitude": drop_zero,
           "flags_source": "GENERATED ONCE (no deposited free set; PROTOCOL 3.2 deviation)" if generated else "inherited",
           "convention": conv, "split": {k: v for k, v in parts.items() if k not in ("select", "report", "sleep")},
           "n_select": len(parts["select"]), "n_report": len(parts["report"]), "n_sleep": len(parts.get("sleep", [])),
           "split_version": "stratified %d-way (this file's split v2-style)" % n_parts, "written_at": utc()}
    for key in ("data_mtz", "flags_mtz", "split_mtz", "data_flags_mtz"):
        rec[key + "_sha256"] = sha256(rec[key])
    with open(os.path.join(out_dir, "split.json"), "w") as f:
        json.dump({"seed": parts["seed"], "method": parts["method"], **{c: [list(h) for h in parts[c]] for c in ("select", "report", "sleep") if c in parts}}, f)
    return rec


def prep_from_frozen(frozen_dir: str, sf: Optional[dict], target: str, out_dir: str, log) -> dict:
    """Take an existing frozen set (data.mtz, flags.mtz, split.mtz[, prep.json]) as is - nothing is regenerated - and
    verify: the flags.mtz free set equals the deposited _refln.status 'f' set (identity, not just count), the data
    column matches the deposited values, and the split partitions the free set. The comparison with another run on
    the same flags is then exact."""
    os.makedirs(out_dir, exist_ok=True)
    src = {k: os.path.join(frozen_dir, k + ".mtz") for k in ("data", "flags", "split")}
    for p in src.values():
        if not os.path.exists(p):
            raise FlagIntegrityError("frozen dir %s lacks %s" % (frozen_dir, p))
    pj = os.path.join(frozen_dir, "prep.json")
    prev = read_json(pj) if os.path.exists(pj) else {}
    for k, p in src.items():
        shutil.copy(p, os.path.join(out_dir, k + ".mtz"))
    from iotbx.reflection_file_reader import any_reflection_file
    arrays = any_reflection_file(src["data"]).as_miller_arrays()
    data = arrays[0]
    labels = tuple(data.info().labels)
    kind = "intensities" if data.is_xray_intensity_array() else "amplitudes"
    cs = data.crystal_symmetry()
    free, n_flag_rows = flag_set(src["flags"])
    check = {"n_free_flags_mtz": len(free), "n_reflections_data_mtz": data.indices().size(), "n_rows_flags_mtz": n_flag_rows}
    if sf is not None:
        dep = {sf["hkl"][i] for i in range(sf["n_rows"]) if sf["status"] is not None and sf["status"][i] == STATUS_FREE}
        from cctbx import miller
        from cctbx.array_family import flex
        asu = lambda s: {tuple(h) for h in miller.set(crystal_symmetry=cs, indices=flex.miller_index(sorted(s)), anomalous_flag=False).map_to_asu().indices()}
        dep_asu, free_asu = asu(dep), asu(free)
        check.update(n_status_f_in_sf=len(dep), n_free_differing=len(dep_asu ^ free_asu), identical_to_status_f=(dep_asu == free_asu))
        if dep and dep_asu != free_asu:
            raise FlagIntegrityError("frozen flags.mtz free set (%d) differs from the deposited _refln.status 'f' set (%d): %d reflections differ"
                                     % (len(free), len(dep), len(dep_asu ^ free_asu)))
        vt = "F_meas_au" if kind == "amplitudes" else "intensity_meas"
        if vt in sf["arrays"]:
            dv = {sf["hkl"][i]: sf["arrays"][vt][i] for i in range(sf["n_rows"])}
            n_cmp = n_bad = 0
            for h, v in zip(data.indices(), data.data()):
                x = dv.get(tuple(h))
                if x is not None:
                    n_cmp += 1
                    if abs(x - v) > 1e-3 * max(1.0, abs(x)):
                        n_bad += 1
            check.update(n_data_values_compared=n_cmp, n_data_values_differing=n_bad)
            if n_bad:
                raise FlagIntegrityError("data.mtz %s differs from the deposited %s at %d reflections" % (labels[0], vt, n_bad))
    split = read_mtz_column(src["split"], SPLIT_LABEL)
    codes = {tuple(h): int(v) for h, v in zip(split.indices(), split.data())}
    n_sel = sum(1 for h in free if codes.get(h) == SPLIT_SELECT)
    n_rep = sum(1 for h in free if codes.get(h) == SPLIT_REPORT)
    n_slp = sum(1 for h in free if codes.get(h) == SPLIT_SLEEP)
    if n_sel + n_rep + n_slp != len(free) or any(codes.get(h, 0) != 0 for h in set(codes) - free):
        raise FlagIntegrityError("split.mtz is not a partition of the free set (select %d + report %d + sleep %d != free %d)" % (n_sel, n_rep, n_slp, len(free)))
    # one file for phenix.refine: the data column and the inherited flags copied as they are (e035_merge_mtz.py)
    fl = read_mtz_column(src["flags"], FLAG_LABEL).common_set(data)
    if fl.indices().size() != data.indices().size():
        raise FlagIntegrityError("flags.mtz and data.mtz do not index the same reflections")
    ds = data.as_mtz_dataset(column_root_label=labels[0])
    ds.add_miller_array(fl, column_root_label=FLAG_LABEL)
    merged = os.path.join(out_dir, "data_flags.mtz")
    ds.mtz_object().write(merged)
    free2, _ = flag_set(merged)
    if free2 != free:
        raise FlagIntegrityError("merged data_flags.mtz free set differs from flags.mtz")
    uc = cs.unit_cell()
    rec = {"target": target, "frozen_dir": frozen_dir, "frozen_prep_json": prev or None, "sf_source": sf["path"] if sf else None,
           "sf_sha256": sha256(sf["path"]) if sf else None, "space_group": str(cs.space_group_info()), "unit_cell": list(uc.parameters()),
           "d_min": data.d_min(), "data_mtz": os.path.join(out_dir, "data.mtz"), "flags_mtz": os.path.join(out_dir, "flags.mtz"),
           "split_mtz": os.path.join(out_dir, "split.mtz"), "data_flags_mtz": merged, "flag_label": FLAG_LABEL, "test_flag_value": FREE_VALUE,
           "data_labels": ",".join(labels), "intensities_or_amplitudes": kind, "n_reflections": data.indices().size(), "n_free": len(free),
           "n_work": data.indices().size() - len(free), "fraction_free": round(len(free) / data.indices().size(), 6),
           "flags_source": "inherited (frozen set taken as is from %s)" % frozen_dir, "frozen_check": check,
           "n_select": n_sel, "n_report": n_rep, "n_sleep": n_slp,
           "split_version": "taken from %s (%s)" % (src["split"], "three-way, sleep withheld" if n_slp else "two-way halves"), "written_at": utc()}
    for key in ("data_mtz", "flags_mtz", "split_mtz", "data_flags_mtz"):
        rec[key + "_sha256"] = sha256(rec[key])
    for k in ("data_mtz_sha256", "flags_mtz_sha256", "split_mtz_sha256"):
        if prev.get(k) and prev[k] != rec[k]:
            raise FlagIntegrityError("%s: copied file's sha256 differs from the frozen prep.json record" % k)
    return rec


def prep_from_mtz(mtz: str, target: str, out_dir: str, n_parts: int, flag_label: Optional[str], test_flag_value: Optional[int], log) -> dict:
    """A user MTZ with data and flag columns: the flag column is read, never generated; the free value is the one
    given, else the minority value of a binary column; anything else is refused."""
    os.makedirs(out_dir, exist_ok=True)
    from iotbx.reflection_file_reader import any_reflection_file
    arrays = any_reflection_file(mtz).as_miller_arrays()
    data = flags = None
    for ma in arrays:
        ls = ma.info().label_string().lower()
        if flags is None and (("free" in ls) if flag_label is None else (flag_label in ma.info().labels)):
            flags = ma
        elif data is None and (ma.is_xray_amplitude_array() or ma.is_xray_intensity_array()) and ma.sigmas() is not None:
            data = ma
    if data is None or flags is None:
        raise FlagIntegrityError("%s: need one F/sigF or I/sigI array and one free-flag column (have %s)" % (mtz, [m.info().label_string() for m in arrays]))
    vals = {}
    for v in flags.data():
        vals[int(v)] = vals.get(int(v), 0) + 1
    if test_flag_value is None:
        if len(vals) == 2:
            test_flag_value = min(vals, key=lambda x: vals[x])
        elif 0 in vals and 0.01 < vals[0] / sum(vals.values()) < 0.2:
            test_flag_value = 0
        else:
            raise FlagIntegrityError("%s: cannot decide the free value of %s (%s); pass --test-flag-value" % (mtz, flags.info().label_string(), vals))
    data, flags = data.common_sets(flags)
    cs = data.crystal_symmetry(); uc = cs.unit_cell()
    hkl = [tuple(h) for h in data.indices()]
    is_free = [int(v) == test_flag_value for v in flags.data()]
    free_hkl = [h for h, f in zip(hkl, is_free) if f]
    parts = assign_split(free_hkl, lambda h: uc.d(h), target, n_parts=n_parts)
    code = {}
    for c, v in (("select", SPLIT_SELECT), ("report", SPLIT_REPORT), ("sleep", SPLIT_SLEEP)):
        for h in parts.get(c, []):
            code[h] = v
    kind = "amplitudes" if data.is_xray_amplitude_array() else "intensities"
    lab = ("FP", "SIGFP") if kind == "amplitudes" else ("IMEAN", "SIGIMEAN")
    rows = list(zip(data.data(), data.sigmas()))
    flag_rows = [FREE_VALUE if f else WORK_VALUE for f in is_free]
    write_mtz(os.path.join(out_dir, "data.mtz"), cs, hkl, [(lab[0], "F" if kind == "amplitudes" else "I", rows)])
    write_mtz(os.path.join(out_dir, "flags.mtz"), cs, hkl, [(FLAG_LABEL, "int", flag_rows)])
    write_mtz(os.path.join(out_dir, "split.mtz"), cs, hkl, [(SPLIT_LABEL, "int", [code.get(h, SPLIT_WORK) for h in hkl])])
    write_mtz(os.path.join(out_dir, "data_flags.mtz"), cs, hkl, [(lab[0], "F" if kind == "amplitudes" else "I", rows), (FLAG_LABEL, "int", flag_rows)])
    rec = {"target": target, "sf_source": mtz, "sf_sha256": sha256(mtz), "space_group": str(cs.space_group_info()), "unit_cell": list(uc.parameters()),
           "d_min": data.d_min(), "data_mtz": os.path.join(out_dir, "data.mtz"), "flags_mtz": os.path.join(out_dir, "flags.mtz"),
           "split_mtz": os.path.join(out_dir, "split.mtz"), "data_flags_mtz": os.path.join(out_dir, "data_flags.mtz"), "flag_label": FLAG_LABEL,
           "test_flag_value": FREE_VALUE, "data_labels": ",".join(lab), "intensities_or_amplitudes": kind, "n_reflections": len(hkl),
           "n_free": len(free_hkl), "n_work": len(hkl) - len(free_hkl), "fraction_free": round(len(free_hkl) / len(hkl), 6),
           "flags_source": "inherited from %s column %s, free value %d (rewritten as %s = 0)" % (mtz, flags.info().label_string(), test_flag_value, FLAG_LABEL),
           "split": {k: v for k, v in parts.items() if k not in ("select", "report", "sleep")}, "n_select": len(parts["select"]),
           "n_report": len(parts["report"]), "n_sleep": len(parts.get("sleep", [])), "split_version": "stratified %d-way" % n_parts, "written_at": utc()}
    for key in ("data_mtz", "flags_mtz", "split_mtz", "data_flags_mtz"):
        rec[key + "_sha256"] = sha256(rec[key])
    return rec


# ------------------------------------------------------------------------------------------- scoring (rfree_split.py)
_XTAL_CACHE: Dict[str, object] = {}


def _xtal_data(prep: dict):
    """f_obs and r_free_flags exactly as phenix.refine extracts them (extract_xtal_data; flags read, never generated)."""
    key = prep["data_flags_mtz"]
    if key in _XTAL_CACHE:
        return _XTAL_CACHE[key]
    from iotbx import extract_xtal_data
    from iotbx.reflection_file_reader import any_reflection_file
    from iotbx.reflection_file_utils import reflection_file_server
    from libtbx.utils import null_out
    data_file = any_reflection_file(key)
    cs = data_file.as_miller_arrays()[0].crystal_symmetry()
    rfs = reflection_file_server(crystal_symmetry=cs, force_symmetry=True, reflection_files=[data_file], err=null_out())
    params = extract_xtal_data.data_and_flags_master_params().extract()
    params.labels = prep["data_labels"].split(",")
    params.r_free_flags.label = prep["flag_label"]
    params.r_free_flags.test_flag_value = int(prep["test_flag_value"])
    params.r_free_flags.generate = False              # PROTOCOL 3.2
    params.r_free_flags.ignore_r_free_flags = False   # PROTOCOL 3.5
    params.r_free_flags.required = True
    xtal = extract_xtal_data.run(reflection_file_server=rfs, parameters=params, extract_experimental_phases=False, keep_going=False)
    if xtal.r_free_flags is None:
        raise FlagIntegrityError("no R-free flags extracted from %s" % key)
    split = read_mtz_column(prep["split_mtz"], SPLIT_LABEL).map_to_asu()
    smap = {tuple(h): round(float(v)) for h, v in zip(split.indices(), split.data())}
    _XTAL_CACHE[key] = (xtal.f_obs, xtal.r_free_flags, cs, smap)
    return _XTAL_CACHE[key]


def _model_xrs(model_path: str, cs):
    import iotbx.pdb
    import mmtbx.model
    from libtbx.utils import null_out
    model = mmtbx.model.manager(model_input=iotbx.pdb.input(file_name=model_path), crystal_symmetry=cs, log=null_out())
    model.setup_scattering_dictionaries(scattering_table="n_gaussian")
    return model, model.get_xray_structure()


def build_fmodel(model_path: str, prep: dict, include_sleep: bool = False):
    """fmodel built as the harness evaluator builds it; the sleep third (if any) is removed before fmodel exists."""
    import mmtbx.f_model
    from cctbx.array_family import flex
    from libtbx.utils import null_out
    f_obs, flags, cs, smap = _xtal_data(prep)
    n_sleep_withheld = 0
    if not include_sleep:
        codes = [smap.get(tuple(h), SPLIT_WORK) for h in f_obs.map_to_asu().indices()]
        sleep_sel = flex.bool([c == SPLIT_SLEEP for c in codes])
        if (sleep_sel & ~flags.data()).count(True):
            raise FlagIntegrityError("split marks working reflections as sleep")
        n_sleep_withheld = sleep_sel.count(True)
        if n_sleep_withheld:
            f_obs, flags = f_obs.select(~sleep_sel), flags.select(~sleep_sel)
    model, xrs = _model_xrs(model_path, cs)
    fmodel = mmtbx.f_model.manager(f_obs=f_obs, r_free_flags=flags, xray_structure=xrs)
    fmodel.update_all_scales(remove_outliers=False, log=null_out())
    return model, fmodel, cs, smap, n_sleep_withheld


def score_model(model_path: str, prep: dict, include_sleep: bool = False) -> dict:
    """R-work, R-free on the full free set, on select and on report (and sleep only with include_sleep=True), with
    the counts asserted against prep and a manual re-derivation of every subset R (autoref/cctbx/rfree_split.py)."""
    _cctbx()
    from cctbx.array_family import flex
    _model, fmodel, _cs, smap, n_sleep_withheld = build_fmodel(model_path, prep, include_sleep)
    free = fmodel.f_obs_free()
    codes = [smap.get(tuple(h), -1) for h in free.map_to_asu().indices()]
    if codes.count(-1):
        raise FlagIntegrityError("%d free reflections are absent from the split (PROTOCOL 3.3)" % codes.count(-1))
    sel = {"r_free_select": flex.bool([c == SPLIT_SELECT for c in codes]), "r_free_report": flex.bool([c == SPLIT_REPORT for c in codes]),
           "r_free_sleep": flex.bool([c == SPLIT_SLEEP for c in codes])}
    n = {k: v.count(True) for k, v in sel.items()}
    if n["r_free_sleep"] and not include_sleep:
        raise FlagIntegrityError("sleep reflections reached fmodel outside --final-score")
    if sum(n.values()) != free.size():
        raise FlagIntegrityError("select + report + sleep != free: the split is not a partition")
    want_free = int(prep["n_free"]) - (0 if include_sleep else int(prep.get("n_sleep", 0)))
    if free.size() != want_free or n["r_free_select"] != int(prep["n_select"]) or n["r_free_report"] != int(prep["n_report"]):
        raise FlagIntegrityError("free set size changed: free %d (want %d) select %d (want %d) report %d (want %d) - PROTOCOL 3.3 HALT"
                                 % (free.size(), want_free, n["r_free_select"], prep["n_select"], n["r_free_report"], prep["n_report"]))
    out = {"model": model_path, "model_sha256": sha256(model_path), "r_work": fmodel.r_work(), "r_free_full": fmodel.r_free(),
           "r_free_select": fmodel.r_free(selection=sel["r_free_select"]), "r_free_report": fmodel.r_free(selection=sel["r_free_report"]),
           "n_free": free.size(), "n_select": n["r_free_select"], "n_report": n["r_free_report"], "n_work": fmodel.f_obs_work().size(),
           "n_reflections": fmodel.f_obs().size(), "n_sleep_withheld": n_sleep_withheld, "n_atoms": fmodel.xray_structure.scatterers().size(),
           "flags_mtz_sha256": prep["flags_mtz_sha256"], "split_mtz_sha256": prep["split_mtz_sha256"], "scored_utc": utc()}
    if include_sleep:
        out["n_sleep"] = n["r_free_sleep"]; out["r_free_sleep"] = fmodel.r_free(selection=sel["r_free_sleep"])
    out["gap"] = out["r_free_full"] - out["r_work"]
    fo = free.data()
    fc = flex.abs(fmodel.f_model_scaled_with_k1_t().data())
    for name in ("r_free_select", "r_free_report") + (("r_free_sleep",) if include_sleep else ()):
        s = sel[name]
        den = flex.sum(fo.select(s))
        manual = flex.sum(flex.abs(fo.select(s) - fc.select(s))) / den if den > 0 else None
        out[name + "_manual"] = manual
        if manual is not None and abs(manual - out[name]) > 1e-6:
            raise RuntimeError("%s disagrees with the manual R (%.6f vs %.6f)" % (name, out[name], manual))
    return out


def score_independent(model_path: str, prep: dict) -> dict:
    """scripts/verify/indep_rfree.py: no extract_xtal_data, no outlier rejection, fmodel on ALL common reflections,
    manual R on work / free / select / report. The sleep third, if any, is withheld."""
    _cctbx()
    import mmtbx.f_model
    from cctbx.array_family import flex
    from libtbx.utils import null_out
    lab = prep["data_labels"].split(",")[0]
    fobs = read_mtz_column(prep["data_mtz"], lab)
    if fobs.is_xray_intensity_array():
        from cctbx import french_wilson
        fobs = french_wilson.french_wilson_scale(miller_array=fobs, log=null_out())
    fobs = fobs.map_to_asu()
    flags = read_mtz_column(prep["flags_mtz"], FLAG_LABEL).map_to_asu()
    split = read_mtz_column(prep["split_mtz"], SPLIT_LABEL).map_to_asu()
    fobs, flags = fobs.common_sets(flags)
    free = flags.customized_copy(data=(flags.data() == FREE_VALUE))
    fobs, split = fobs.common_sets(split); free, split = free.common_sets(split)
    code = split.data()
    keep = ~(code == SPLIT_SLEEP)
    n_sleep = (code == SPLIT_SLEEP).count(True)
    fobs, free, split = fobs.select(keep), free.select(keep), split.select(keep)
    code = split.data(); sel_free = free.data()
    _model, xrs = _model_xrs(model_path, fobs.crystal_symmetry())
    fmodel = mmtbx.f_model.manager(f_obs=fobs, r_free_flags=free, xray_structure=xrs)
    fmodel.update_all_scales(remove_outliers=False, log=null_out())
    fo = fmodel.f_obs().data(); fc = flex.abs(fmodel.f_model_scaled_with_k1().data())
    work = ~fmodel.r_free_flags().data()
    mr = lambda s: float(flex.sum(flex.abs(fo.select(s) - fc.select(s))) / flex.sum(fo.select(s)))
    return {"model": model_path, "n_reflections": fobs.size(), "n_free": sel_free.count(True), "n_sleep_withheld": n_sleep,
            "r_work_fmodel": fmodel.r_work(), "r_free_fmodel": fmodel.r_free(), "r_work_manual": mr(work), "r_free_manual": mr(sel_free),
            "r_free_select_manual": mr(sel_free & (code == SPLIT_SELECT)), "r_free_report_manual": mr(sel_free & (code == SPLIT_REPORT)),
            "d_min": fobs.d_min(), "n_atoms": xrs.scatterers().size()}


# ------------------------------------------------------------------------------------------- model I/O (iotbx.pdb)
POLYMER_CLASSES = ("common_amino_acid", "modified_amino_acid", "d_amino_acid", "common_rna_dna", "modified_rna_dna", "ccp4_mon_lib_rna_dna")


def read_model(path: str):
    import iotbx.pdb
    inp = iotbx.pdb.input(file_name=path)
    h = inp.construct_hierarchy()
    return h, inp.crystal_symmetry()


def is_water(resname: str) -> bool:
    return resname.strip() in WATER_NAMES


def is_polymer(ag) -> bool:
    """Protein / nucleic residues are copy-expanded; ligands, ions and anything else stay single. A residue of an
    unknown class written as ATOM (not HETATM) is taken as polymer."""
    import iotbx.pdb
    cls = iotbx.pdb.common_residue_names_get_class(ag.resname)
    if cls in POLYMER_CLASSES:
        return True
    return cls == "other" and not ag.atoms()[0].hetero


def write_model(h, cs, path: str, k: int = 6) -> str:
    """PDB with occupancies at four decimals (iotbx and phenix write two: 0.17 x 6 = 1.02, PROTOCOL 18.5) and the
    copies' occupancies normalised to copy_occupancies(k)."""
    h.atoms().reset_serial()
    tmp = path + ".tmp"
    h.write_pdb_file(file_name=tmp, crystal_symmetry=cs)
    occs = [a.occ for a in h.atoms()]
    lines = read_text(tmp).splitlines(True)
    out = []; i = 0
    for line in lines:
        if line.startswith(("ATOM", "HETATM")):
            line = line[:54] + "%6.4f" % occs[i] + line[60:]; i += 1
        out.append(line)
    if i != len(occs):
        raise RuntimeError("occupancy rewrite matched %d of %d atoms" % (i, len(occs)))
    if k >= 2:
        out, _ = normocc_lines(out, k)
    with open(tmp, "w") as f:
        f.writelines(out)
    os.replace(tmp, path)
    return path


def normocc_file(path: str, k: int = 6) -> int:
    lines, n = normocc_lines(read_text(path).splitlines(True), k)
    if n:
        tmp = path + ".tmp"
        with open(tmp, "w") as f:
            f.writelines(lines)
        os.replace(tmp, path)
    return n


def describe(path: str) -> dict:
    h, _ = read_model(path)
    n = nw = na = nh = w_iso = 0; wocc = 0.0; alts = set(); n_prot_iso = 0; n_res = 0
    for ch in h.only_model().chains():
        for rg in ch.residue_groups():
            water = any(is_water(ag.resname) for ag in rg.atom_groups())
            if not water:
                n_res += 1
            for ag in rg.atom_groups():
                if ag.altloc.strip():
                    alts.add(ag.altloc)
                for a in ag.atoms():
                    n += 1
                    hyd = a.element.strip().upper() in ("H", "D")
                    aniso = a.uij != (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
                    nh += hyd; na += aniso
                    if water:
                        nw += 1; wocc += a.occ; w_iso += not aniso
                    elif not hyd and not aniso:
                        n_prot_iso += 1
    return {"n_atoms": n, "n_h": nh, "n_water_atoms": nw, "water_occ_sum": round(wocc, 2), "n_anisou": na, "n_water_iso": w_iso,
            "n_nonwater_iso_heavy": n_prot_iso, "altlocs": "".join(sorted(alts)), "n_residues_nonwater": n_res}


def atom_table(h) -> List[dict]:
    """One record per atom: labels, element class, altloc, water flag, donor-parent index for polar H (nearest heavy
    atom of the same residue with the same or blank altloc, within 1.3 A, N or O)."""
    rows = []
    for ch in h.only_model().chains():
        for rg in ch.residue_groups():
            start = len(rows)
            for ag in rg.atom_groups():
                water = is_water(ag.resname)
                for a in ag.atoms():
                    el = a.element.strip().upper() or a.name.strip()[0]
                    rows.append({"chain": ch.id.strip(), "resseq": rg.resseq_as_int(), "icode": rg.icode, "altloc": ag.altloc.strip(),
                                 "resname": ag.resname.strip(), "name": a.name.strip(), "element": el, "is_h": el in ("H", "D"),
                                 "water": water, "xyz": a.xyz, "occ": a.occ, "b": a.b, "donor_parent": None, "atom": a})
            res = rows[start:]
            heavy = [r for r in res if not r["is_h"]]
            for r in res:
                if not r["is_h"] or not heavy:
                    continue
                best = None
                for p in heavy:
                    if p["altloc"] not in ("", r["altloc"]):
                        continue
                    d = math.dist(p["xyz"], r["xyz"])
                    if best is None or d < best[0]:
                        best = (d, p)
                if best and best[0] < 1.3 and best[1]["element"] in ("N", "O"):
                    r["_parent_row"] = best[1]   # resolved to an index below
    index = {id(r): i for i, r in enumerate(rows)}
    for r in rows:
        p = r.pop("_parent_row", None)
        if p is not None:
            r["donor_parent"] = index[id(p)]
    return rows


def pair_table(cs, sites_cart: Sequence[Tuple[float, float, float]], cutoff: float):
    """Symmetry-aware neighbour pairs: returns (uc, sites_frac, pst) where pst[i] maps j -> list of rt_mx with
    uc.distance(sites_frac[i], rt * sites_frac[j]) <= cutoff (cctbx pair_asu_table; both directions kept)."""
    from cctbx import xray
    from cctbx.array_family import flex
    uc = cs.unit_cell()
    frac = [uc.fractionalize(x) for x in sites_cart]
    sc = flex.xray_scatterer()
    for i, s in enumerate(frac):
        sc.append(xray.scatterer(label="a%d" % i, site=s, scattering_type="C"))
    xs = xray.structure(crystal_symmetry=cs, scatterers=sc)
    pat = xs.pair_asu_table(distance_cutoff=cutoff)
    pst = pat.extract_pair_sym_table(skip_j_seq_less_than_i_seq=False)
    return uc, frac, pst


def _angle(a, b, c) -> float:
    v1 = tuple(x - y for x, y in zip(a, b)); v2 = tuple(x - y for x, y in zip(c, b))
    n = math.sqrt(sum(x * x for x in v1)) * math.sqrt(sum(x * x for x in v2))
    if n == 0:
        return 180.0
    return math.degrees(math.acos(max(-1.0, min(1.0, sum(x * y for x, y in zip(v1, v2)) / n))))


class Clearance:
    """Own-conformer clearance of a water copy (e041_clearance.py): a water O in conformer X must clear every non-water
    atom of X (or with no altloc): heavy >= heavy_min (2.6 A); H >= h_min (2.0 A) unless the H is a donor H in
    hydrogen-bond geometry (D-H...O >= 120 deg, H...O >= 1.6 A). Other conformers are ignored (the paper's
    dist_min_altloc). Also the plain rules: protein heavy >= dist_protein, same-conformer water >= dist_water.
    Image-aware through cctbx pair tables."""

    def __init__(self, h, cs, rows, dist_protein=2.2, dist_water=2.0, own_clear=True, heavy_min=2.6, h_min=2.0,
                 hbond_angle=120.0, hbond_h_min=1.6, vdw_margin=None):
        self.cs, self.rows = cs, rows
        self.dist_protein, self.dist_water, self.own_clear = dist_protein, dist_water, own_clear
        self.heavy_min, self.h_min, self.hbond_angle, self.hbond_h_min = heavy_min, h_min, hbond_angle, hbond_h_min
        self.vdw = None if vdw_margin is None else {k: v + vdw_margin for k, v in VDW_LIMITS.items()}
        self.reach = max(dist_protein, dist_water, heavy_min if own_clear else 0.0, h_min if own_clear else 0.0,
                         (max(VDW_LIMITS.values()) + vdw_margin) if vdw_margin is not None else 0.0)
        self.uc = cs.unit_cell()

    def violations(self, pos_cart, altloc: str, neighbours) -> list:
        """neighbours: iterable of (row index, rt_mx) within reach of pos. Returns [(altloc, label, d, kind)]."""
        out = []
        pf = self.uc.fractionalize(pos_cart)
        for j, rt in neighbours:
            r = self.rows[j]
            a_alt = r["altloc"]
            if altloc and a_alt not in ("", altloc):
                continue
            jf = self.uc.fractionalize(r["xyz"])
            d = self.uc.distance(pf, rt * jf)
            label = "%s %d%s %s %s" % (r["chain"], r["resseq"], r["resname"], r["name"], a_alt)
            if r["water"]:
                if not r["is_h"] and d < self.dist_water:
                    out.append((a_alt, label, round(d, 3), "water"))
                continue
            if r["is_h"]:
                if not self.own_clear and self.vdw is None:
                    continue
                lim_vdw = self.vdw[("Hp" if r["donor_parent"] is not None else "Hc")] if self.vdw is not None else 0.0
                if self.vdw is not None and d < lim_vdw:
                    out.append((a_alt, label, round(d, 3), "vdw_h")); continue
                if not self.own_clear or d >= self.h_min:
                    continue
                if r["donor_parent"] is not None and d >= self.hbond_h_min:
                    himg = self.uc.orthogonalize(rt * jf)
                    pimg = self.uc.orthogonalize(rt * self.uc.fractionalize(self.rows[r["donor_parent"]]["xyz"]))
                    if _angle(pimg, himg, pos_cart) >= self.hbond_angle:
                        continue
                out.append((a_alt, label, round(d, 3), "h"))
            else:
                if self.vdw is not None and d < self.vdw.get(r["element"], self.vdw["C"]):
                    out.append((a_alt, label, round(d, 3), "vdw")); continue
                if d < self.dist_protein or (self.own_clear and d < self.heavy_min):
                    out.append((a_alt, label, round(d, 3), "heavy"))
        return out

    def blocked(self, pos_cart, neighbours, k: int = 6) -> set:
        bad = set()
        for a_alt, _, _, _ in self.violations(pos_cart, "", neighbours):
            bad.update(ALT[:k] if a_alt == "" else a_alt)
        return bad


def find_water_peaks(fmodel, sigma: float, dist_min: float, dist_max: float, peak_peak_min: float):
    """mmtbx.find_peaks on the mFo-DFc map of the fmodel built as the evaluator builds it (e035_pick_waters.py)."""
    import mmtbx.find_peaks
    from libtbx.utils import null_out
    p = mmtbx.find_peaks.master_params.extract()
    p.map_next_to_model.min_model_peak_dist = dist_min
    p.map_next_to_model.max_model_peak_dist = dist_max
    p.map_next_to_model.min_peak_peak_dist = peak_peak_min
    p.map_next_to_model.use_hydrogens = False
    p.peak_search.min_cross_distance = peak_peak_min
    coeffs = fmodel.electron_density_map().map_coefficients(map_type="mFo-DFc", isotropize=True, fill_missing=False)
    fp = mmtbx.find_peaks.manager(map_cutoff=sigma, xray_structure=fmodel.xray_structure, params=p, log=null_out(), map_coeffs=coeffs)
    mapped = fp.peaks_mapped()
    if mapped is None:
        return [], []
    return list(mapped.sites), list(mapped.heights)


def last_nonwater_resseq(h) -> int:
    last = 0
    for ch in h.only_model().chains():
        for rg in ch.residue_groups():
            if not any(is_water(ag.resname) for ag in rg.atom_groups()):
                last = max(last, rg.resseq_as_int())
    return last


def water_chain(h):
    import iotbx.pdb
    for ch in h.only_model().chains():
        if ch.id.strip() == "z":
            return ch
    ch = iotbx.pdb.hierarchy.chain(id="z")
    h.only_model().append_chain(ch)
    return ch


def pick_waters(model_path: str, prep: dict, out_path: str, sigma: float, k: int = 6, dist_protein=2.2, dist_water=2.0, dist_max=6.0,
                peak_peak_min=1.0, occ=0.33, shake=0.15, seed=42, max_add=2000, own_clear=True, own_heavy=2.6, own_h=2.0) -> dict:
    """Conformation-aware, riding-H-aware per-copy water picking (e041_waters.py --own-clear 1). For each mFo-DFc peak
    >= sigma (highest first) and each conformer X, a copy in X is added only if the peak clears X's (and blank-altloc)
    atoms per Clearance and X's waters, including the copies added in this call; occupancy occ / k per copy, B =
    median water B, position shaken by `shake` A (seeded). Nothing is removed."""
    import iotbx.pdb
    from cctbx.array_family import flex
    model, fmodel, cs, _, _ = build_fmodel(model_path, prep)
    r_before = (fmodel.r_work(), fmodel.r_free())
    sites, heights = find_water_peaks(fmodel, sigma, 0.0, dist_max, peak_peak_min)
    h = model.get_hierarchy()
    uc = cs.unit_cell()
    order = sorted(range(len(sites)), key=lambda i: -heights[i])[:max_add]
    peaks = [uc.orthogonalize(sites[i]) for i in order]
    rows = atom_table(h)
    water_b = [r["b"] for r in rows if r["water"] and not r["is_h"]]
    b_iso = float(flex.median(flex.double(water_b))) if water_b else 15.0
    clr = Clearance(h, cs, rows, dist_protein, dist_water, own_clear, own_heavy, own_h)
    n_model = len(rows)
    added = []; per_alt = {x: 0 for x in ALT[:k]}; n_sites = 0
    accepted_conf: Dict[int, set] = {}      # peak index -> conformers that got a copy
    if peaks:
        _, _, pst = pair_table(cs, [r["xyz"] for r in rows] + peaks, max(clr.reach, dist_water))
        ch_z = water_chain(h)
        resseq = max(last_nonwater_resseq(h), max([rg.resseq_as_int() for rg in ch_z.residue_groups()] or [0]))
        rnd = random.Random(seed)
        for pi, pos in enumerate(peaks):
            gi = n_model + pi
            neigh = []; peak_neigh = []
            for j, ops in pst[gi].items():
                for rt in ops:
                    if j < n_model:
                        neigh.append((j, rt))
                    elif j != gi:
                        peak_neigh.append((j - n_model, rt))
            bad = clr.blocked(pos, neigh, k)
            pf = uc.fractionalize(pos)
            for pj, rt in peak_neigh:
                if pj in accepted_conf and uc.distance(pf, rt * uc.fractionalize(peaks[pj])) < dist_water:
                    bad.update(accepted_conf[pj])
            ok = [x for x in ALT[:k] if x not in bad]
            if not ok:
                continue
            n_sites += 1; accepted_conf[pi] = set(ok)
            for x in ok:
                resseq += 1
                d = [rnd.gauss(0.0, shake / 3 ** 0.5) for _ in range(3)]
                xyz = (pos[0] + d[0], pos[1] + d[1], pos[2] + d[2])
                rg = iotbx.pdb.hierarchy.residue_group(resseq=iotbx.pdb.hy36encode(4, resseq), icode=" ")
                ag = iotbx.pdb.hierarchy.atom_group(altloc=x, resname="HOH")
                at = iotbx.pdb.hierarchy.atom(); at.name = " O  "; at.xyz = xyz; at.occ = occ / k; at.b = b_iso; at.element = " O"; at.hetero = True
                ag.append_atom(at); rg.append_atom_group(ag); ch_z.append_residue_group(rg)
                per_alt[x] += 1
                added.append({"resseq": resseq, "altloc": x, "xyz": [round(v, 3) for v in xyz], "peak_sigma": round(float(heights[order[pi]]), 2)})
    write_model(h, cs, out_path, k)
    rep = {"model": model_path, "out": out_path, "sigma": sigma, "dist_protein": dist_protein, "dist_water": dist_water, "dist_max": dist_max,
           "own_clear": own_clear, "own_heavy": own_heavy, "own_h": own_h, "peak_peak_min": peak_peak_min, "occ_per_copy": occ / k, "b_iso": b_iso,
           "n_peaks": len(sites), "n_sites": n_sites, "n_atoms_added": len(added), "per_altloc": per_alt,
           "r_work_before": r_before[0], "r_free_full_before": r_before[1], "added": added}
    with open(out_path + ".pick.json", "w") as f:
        json.dump(rep, f, indent=1)
    return rep


def hygiene(model_path: str, out_path: str, k: int = 6, min_occ=0.02, merge_dist=0.6, merge_occ_sum=0.35) -> dict:
    """e035_water_hygiene.py: (1) delete water residues whose atoms are all below min_occ; (2) merge same-altloc water
    oxygen pairs closer than merge_dist with summed occupancy < merge_occ_sum into one water at the occupancy-weighted
    position with the summed occupancy (altloc, B, ANISOU of the heavier), to convergence; (3) renumber the surviving
    waters gap-free from the last non-water residue + 1 (hybrid-36 beyond 9999)."""
    import iotbx.pdb
    h, cs = read_model(model_path)
    uc = cs.unit_cell()
    n_deleted = 0
    for ch in h.only_model().chains():
        for rg in list(ch.residue_groups()):
            if any(is_water(ag.resname) for ag in rg.atom_groups()) and all(a.occ < min_occ for a in rg.atoms()):
                ch.remove_residue_group(rg); n_deleted += 1
    n_merged = 0
    for _ in range(6):
        waters = []   # (rg, ag, atom) of water oxygens
        for ch in h.only_model().chains():
            for rg in ch.residue_groups():
                for ag in rg.atom_groups():
                    if is_water(ag.resname):
                        for a in ag.atoms():
                            if a.element.strip().upper() not in ("H", "D"):
                                waters.append((ch, rg, ag, a))
        if len(waters) < 2:
            break
        _, frac, pst = pair_table(cs, [w[3].xyz for w in waters], merge_dist)
        pairs = []
        for i in range(len(waters)):
            for j, ops in pst[i].items():
                if j <= i:
                    continue
                if waters[i][2].altloc != waters[j][2].altloc:
                    continue
                for rt in ops:
                    d = uc.distance(frac[i], rt * frac[j])
                    if 0.0 < d < merge_dist and waters[i][3].occ + waters[j][3].occ < merge_occ_sum:
                        pairs.append((d, i, j, rt))
        if not pairs:
            break
        gone = set()
        for d, i, j, rt in sorted(pairs, key=lambda p: p[0]):
            if i in gone or j in gone:
                continue
            ai, aj = waters[i][3], waters[j][3]
            heavy, light, lrt = (i, j, rt) if ai.occ >= aj.occ else (j, i, rt.inverse())
            ha, la = waters[heavy][3], waters[light][3]
            limg = uc.orthogonalize(lrt * frac[light])
            tot = ha.occ + la.occ
            ha.xyz = tuple((ha.xyz[m] * ha.occ + limg[m] * la.occ) / tot for m in range(3))
            ha.occ = round(tot, 4)
            chl, rgl = waters[light][0], waters[light][1]
            chl.remove_residue_group(rgl)
            gone.add(light); gone.add(heavy); n_merged += 1
    num = last_nonwater_resseq(h) + 1
    n_renum = 0
    for ch in h.only_model().chains():
        for rg in ch.residue_groups():
            if any(is_water(ag.resname) for ag in rg.atom_groups()):
                new = iotbx.pdb.hy36encode(4, num)
                if rg.resseq != new or rg.icode.strip():
                    rg.resseq = new; rg.icode = " "; n_renum += 1
                num += 1
    for ch in list(h.only_model().chains()):
        if ch.residue_groups_size() == 0:
            h.only_model().remove_chain(ch)
    write_model(h, cs, out_path, k)
    rep = {"input": model_path, "output": out_path, "deleted_below_occ": n_deleted, "merged_pairs": n_merged, "renumbered": n_renum,
           "waters_left": num - last_nonwater_resseq(h) - 1, "params": {"min_occ": min_occ, "merge_dist": merge_dist, "merge_occ_sum": merge_occ_sum}}
    with open(out_path + ".hygiene.json", "w") as f:
        json.dump(rep, f, indent=1)
    return rep


def remove_water_copies(h, keys: set) -> int:
    """Remove water atoms whose (chain, resseq, altloc) is in keys; empty residue groups go too."""
    n = 0
    for ch in h.only_model().chains():
        for rg in list(ch.residue_groups()):
            if not any(is_water(ag.resname) for ag in rg.atom_groups()):
                continue
            for ag in list(rg.atom_groups()):
                if (ch.id.strip(), rg.resseq_as_int(), ag.altloc.strip()) in keys:
                    rg.remove_atom_group(ag); n += 1
            if rg.atom_groups_size() == 0:
                ch.remove_residue_group(rg)
    return n


def clean_vdw(model_path: str, out_path: str, k: int = 6, margin: float = 0.2) -> dict:
    """e041_prune.py --vdw 1 --vdw-margin M: remove every water copy closer than (2.7 C, 2.8 S, 2.4 N/O, 2.2 C-bonded H,
    1.5 N/O-bonded H) + margin to a non-water atom of its own conformer or with no altloc, image-aware."""
    h, cs = read_model(model_path)
    rows = atom_table(h)
    clr = Clearance(h, cs, rows, dist_protein=0.0, dist_water=0.0, own_clear=False, vdw_margin=margin)
    _, _, pst = pair_table(cs, [r["xyz"] for r in rows], clr.reach)
    kill = set(); detail = []
    for i, r in enumerate(rows):
        if not r["water"] or r["is_h"]:
            continue
        neigh = [(j, rt) for j, ops in pst[i].items() if j != i and not rows[j]["water"] for rt in ops]
        v = clr.violations(r["xyz"], r["altloc"], neigh)
        if v:
            kill.add((r["chain"], r["resseq"], r["altloc"])); detail.append([r["chain"], r["resseq"], r["altloc"], v[0][1], v[0][2], v[0][3]])
    n = remove_water_copies(h, kill)
    write_model(h, cs, out_path, k)
    rep = {"model": model_path, "out": out_path, "rule": "vdw", "margin": margin, "removed": n, "removed_sites": detail[:5000]}
    with open(out_path + ".prune.json", "w") as f:
        json.dump(rep, f, indent=1)
    return rep


def clean_clashlog(model_path: str, clashlog_path: str, out_path: str, k: int = 6) -> dict:
    """e041_prune.py --clash-log: remove every water copy phenix.clashscore lists in an own-conformer clash."""
    h, cs = read_model(model_path)
    occ = {}
    for ch in h.only_model().chains():
        for rg in ch.residue_groups():
            for ag in rg.atom_groups():
                if is_water(ag.resname):
                    for a in ag.atoms():
                        occ[(ch.id.strip(), rg.resseq_as_int(), ag.altloc.strip())] = a.occ
    kill = clashlog_water_kills(read_text(clashlog_path), occ)
    n = remove_water_copies(h, kill)
    write_model(h, cs, out_path, k)
    rep = {"model": model_path, "out": out_path, "rule": "clashlog", "clash_log": clashlog_path, "removed": n, "removed_sites": sorted(list(x) for x in kill)}
    with open(out_path + ".prune.json", "w") as f:
        json.dump(rep, f, indent=1)
    return rep


def build_sixcopy(single_path: str, out_path: str, k: int = 6, shake: float = 0.2, shake_water: float = 0.1, seed: int = 44) -> dict:
    """e044_build.py: k copies of every polymer residue (existing conformers allocated by largest remainder, letters
    contiguous, blank-altloc atoms into every copy, copies j >= 1 shaken `shake` A rms per atom), ligands and ions
    single, every water atom k copies at occupancy x copy_occupancies (chain z, numbered after the last non-water
    residue), B and ANISOU carried."""
    import iotbx.pdb
    h, cs = read_model(single_path)
    occ = copy_occupancies(k)
    rnd = random.Random(seed)
    s, sw = shake / 3 ** 0.5, shake_water / 3 ** 0.5
    out = iotbx.pdb.hierarchy.root(); mdl = iotbx.pdb.hierarchy.model(id="1"); out.append_model(mdl)
    waters = []; last = 0; n_split = n_res = n_lig = 0
    for ch in h.only_model().chains():
        nc = iotbx.pdb.hierarchy.chain(id=ch.id)
        for rg in ch.residue_groups():
            ags = rg.atom_groups()
            if any(is_water(ag.resname) for ag in ags):
                for ag in ags:
                    for a in ag.atoms():
                        waters.append((a.detached_copy(), ag.resname))
                continue
            last = max(last, rg.resseq_as_int())
            if not is_polymer(ags[0]):
                nc.append_residue_group(rg.detached_copy()); n_lig += 1
                continue
            n_res += 1
            by_name: Dict[Tuple[str, str], Dict[str, object]] = {}
            confs: Dict[str, List[float]] = {}
            for ag in ags:
                alt = ag.altloc.strip()
                for a in ag.atoms():
                    by_name.setdefault((ag.resname, a.name), {})[alt] = a
                    if alt:
                        confs.setdefault(alt, []).append(a.occ)
            if confs:
                n_split += 1
                order = copy_order({x: sum(v) / len(v) for x, v in confs.items()}, k)
            else:
                order = [""] * k
            nrg = iotbx.pdb.hierarchy.residue_group(resseq=rg.resseq, icode=rg.icode)
            groups = {}
            for j, conf in enumerate(order):
                for (resname, name), alts in by_name.items():
                    a = alts.get(conf) if conf else None
                    if a is None:
                        a = alts.get("") or max(alts.values(), key=lambda x: (x.occ, x.parent().altloc))
                    na = a.detached_copy(); na.occ = occ[j]
                    if j:
                        na.xyz = tuple(na.xyz[m] + rnd.gauss(0, s) for m in range(3))
                    key = (ALT[j], resname)
                    if key not in groups:
                        groups[key] = iotbx.pdb.hierarchy.atom_group(altloc=ALT[j], resname=resname)
                        nrg.append_atom_group(groups[key])
                    groups[key].append_atom(na)
            nc.append_residue_group(nrg)
        if nc.residue_groups_size():
            mdl.append_chain(nc)
    z = iotbx.pdb.hierarchy.chain(id="z")
    num = last + 1; w_in = w_out = 0.0
    for w, resname in waters:
        w_in += w.occ
        for j in range(k):
            nrg = iotbx.pdb.hierarchy.residue_group(resseq=iotbx.pdb.hy36encode(4, num), icode=" ")
            ag = iotbx.pdb.hierarchy.atom_group(altloc=ALT[j], resname="HOH")
            na = w.detached_copy(); na.occ = round(w.occ * occ[j], 4)
            if j:
                na.xyz = tuple(na.xyz[m] + rnd.gauss(0, sw) for m in range(3))
            ag.append_atom(na); nrg.append_atom_group(ag); z.append_residue_group(nrg); num += 1; w_out += na.occ
    if z.residue_groups_size():
        mdl.append_chain(z)
    write_model(out, cs, out_path, k)
    # occupancy sums per polymer site must be exactly 1.0000 (over-occupancy is a bug, PROTOCOL 18.5)
    sums: Dict[tuple, float] = {}
    for ch in out.only_model().chains():
        for rg in ch.residue_groups():
            for ag in rg.atom_groups():
                if is_water(ag.resname) or not ag.altloc.strip():
                    continue
                for a in ag.atoms():
                    key = (ch.id, rg.resseq, rg.icode, a.name)
                    sums[key] = sums.get(key, 0.0) + a.occ
    mx = max(sums.values()) if sums else None
    rep = {"k": k, "copy_occupancies": occ, "protein_residues": n_res, "split_residues_in": n_split, "ligand_or_ion_residues_kept": n_lig,
           "water_atoms_in": len(waters), "water_copies_out": len(waters) * k, "water_occ_sum_in": round(w_in, 3), "water_occ_sum_out": round(w_out, 3),
           "shake": shake, "shake_water": shake_water, "seed": seed, "water_resnum_range": [last + 1, num - 1],
           "site_occupancy_sums": {"n_sites": len(sums), "min": round(min(sums.values()), 4) if sums else None, "max": round(mx, 4) if sums else None}}
    if mx is not None and mx > 1.00005:
        raise RuntimeError("over-occupied protein site after the build: %s" % rep["site_occupancy_sums"])
    with open(out_path + ".build.json", "w") as f:
        json.dump(rep, f, indent=1)
    return rep


# ================================================================================================= the driver
class Run:
    STAGES = ("fetch", "prep", "baseline", "build", "run")

    def __init__(self, target: str, a):
        self.T = target.upper()
        self.a = a
        self.D = os.path.abspath(a.out)
        for d in ("fetch", "prep", "baseline", "build", "steps", "models", "verify", "logs"):
            os.makedirs(os.path.join(self.D, d), exist_ok=True)
        self.state_p = os.path.join(self.D, "run.json")
        self.state = read_json(self.state_p) if (os.path.exists(self.state_p) and a.resume) else {}
        self.state.setdefault("target", self.T)
        self.state.setdefault("version", VERSION)
        self.state.setdefault("argv", [sys.argv])
        if a.resume and os.path.exists(self.state_p):
            self.state["argv"].append(sys.argv)
        self.state.setdefault("script_sha256", sha256(os.path.abspath(__file__)))
        self.state.setdefault("stages", {})
        self.state.setdefault("steps", {})
        self.state.setdefault("rounds", [])
        self.state.setdefault("scores", {})
        self.state.setdefault("jobs", [])
        self.lock = threading.Lock()
        self.slots: "queue.Queue[int]" = queue.Queue()
        for i in range(int(a.nproc)):
            self.slots.put(i)
        self.running = 0
        self.last_launch = 0.0
        self.prep: Optional[dict] = self.state.get("prep")
        self.save()

    # ------------------------------------------------------------------ bookkeeping
    def log(self, msg: str) -> None:
        line = "[%s] %s" % (utc(), msg)
        print(line, flush=True)
        with self.lock, open(os.path.join(self.D, "log"), "a") as f:
            f.write(line + "\n")

    def save(self) -> None:
        with self.lock:
            tmp = self.state_p + ".tmp"
            with open(tmp, "w") as f:
                json.dump(self.state, f, indent=1, default=str)
            os.replace(tmp, self.state_p)

    def done(self, stage: str) -> bool:
        return bool(self.state["stages"].get(stage, {}).get("done"))

    def mark(self, stage: str, **info) -> None:
        self.state["stages"][stage] = {"done": True, "at": utc(), **info}
        self.save()

    def tool(self, name: str) -> str:
        p = shutil.which(name)
        if p:
            return p
        for root in (os.environ.get("PHENIX"), os.path.dirname(os.path.dirname(sys.executable))):
            if root:
                for sub in ("build/bin", "bin", "phenix_bin"):
                    c = os.path.join(root, sub, name)
                    if os.path.exists(c):
                        return c
        raise RuntimeError("%s not found: source the Phenix environment (phenix_env.sh) before running" % name)

    def sh(self, argv: Sequence[str], log: str, cwd: Optional[str] = None, record: bool = True) -> int:
        """Run one external command (argv list, recorded verbatim) with stdout+stderr appended to `log`."""
        argv = [str(x) for x in argv]
        argv[0] = self.tool(argv[0])
        t0 = time.time()
        with open(log, "a") as f:
            f.write("\n# %s cwd=%s\n# %s\n" % (utc(), cwd, " ".join(argv)))
            f.flush()
            rc = subprocess.call(argv, cwd=cwd, stdout=f, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        if record:
            with self.lock:
                self.state["jobs"].append({"argv": argv, "cwd": cwd, "log": log, "rc": rc, "wall_s": round(time.time() - t0, 1), "at": utc()})
        return rc

    # ------------------------------------------------------------------ stage: fetch
    def fetch_url(self, url: str, dst: str) -> None:
        tmp = dst + ".part"
        try:
            import urllib.request
            with urllib.request.urlopen(url, timeout=120) as r, open(tmp, "wb") as f:
                shutil.copyfileobj(r, f)
        except Exception as e:  # noqa: BLE001 - any download failure falls back to curl
            self.log("urllib failed for %s (%r); trying curl" % (url, e))
            if subprocess.call(["curl", "-sSfL", "-o", tmp, url]) != 0:
                raise RuntimeError("download failed: %s" % url)
        os.replace(tmp, dst)

    def stage_fetch(self) -> None:
        if self.done("fetch"):
            return
        F = os.path.join(self.D, "fetch")
        info = {}
        model = self.a.model
        if model in (None, "deposited"):
            dst = os.path.join(F, "%s.cif" % self.T)
            if not os.path.exists(dst):
                self.fetch_url(RCSB + "%s.cif" % self.T, dst)
            info["model"] = {"path": dst, "source": RCSB + "%s.cif" % self.T, "sha256": sha256(dst)}
        else:
            dst = os.path.join(F, os.path.basename(model))
            if os.path.abspath(model) != dst:
                shutil.copy(model, dst)
            info["model"] = {"path": dst, "source": os.path.abspath(model), "sha256": sha256(dst)}
        sf = None
        if self.a.data:
            dst = os.path.join(F, os.path.basename(self.a.data))
            if os.path.abspath(self.a.data) != dst:
                shutil.copy(self.a.data, dst)
            sf = {"path": dst, "source": os.path.abspath(self.a.data), "sha256": sha256(dst)}
        elif self.a.frozen_dir:
            pj = os.path.join(self.a.frozen_dir, "prep.json")
            src = read_json(pj).get("sf_source") if os.path.exists(pj) else None
            if src and os.path.exists(src):
                sf = {"path": src, "source": src, "sha256": sha256(src), "note": "deposited structure factors named by the frozen prep.json; used for the free-set identity check"}
        if sf is None:
            dst = os.path.join(F, "%s-sf.cif" % self.T)
            if not os.path.exists(dst):
                gz = dst + ".gz"
                try:
                    self.fetch_url(RCSB + "%s-sf.cif.gz" % self.T, gz)
                    with gzip.open(gz, "rb") as fi, open(dst, "wb") as fo:
                        shutil.copyfileobj(fi, fo)
                    os.remove(gz)
                except Exception as e:  # any download failure falls back to curl
                    if not self.a.frozen_dir:
                        raise
                    self.log("structure factors not downloaded (%r); the frozen set is taken without the identity check" % (e,))
            if os.path.exists(dst):
                sf = {"path": dst, "source": RCSB + "%s-sf.cif.gz" % self.T, "sha256": sha256(dst)}
        info["sf"] = sf
        self.mark("fetch", **info)
        self.log("fetch: model %s (%s) sf %s" % (info["model"]["path"], info["model"]["sha256"][:12], (sf or {}).get("path")))

    # ------------------------------------------------------------------ stage: prep
    def stage_prep(self) -> None:
        if self.done("prep") and self.prep:
            return
        P = os.path.join(self.D, "prep")
        f = self.state["stages"]["fetch"]
        sfp = (f.get("sf") or {}).get("path")
        n_parts = 3 if self.a.sleep else 2
        if self.a.frozen_dir:
            sf = read_sf_cif(sfp) if sfp and sfp.endswith(".cif") else None
            rec = prep_from_frozen(self.a.frozen_dir, sf, self.T, P, self.log)
        elif sfp and sfp.endswith(".mtz"):
            rec = prep_from_mtz(sfp, self.T, P, n_parts, self.a.flag_label, self.a.test_flag_value, self.log)
        else:
            rec = prep_from_sf(read_sf_cif(sfp), self.T, P, n_parts, self.log)
        rec["sleep_requested"] = bool(self.a.sleep)
        self.prep = rec
        self.state["prep"] = rec
        self.mark("prep", n_free=rec["n_free"], n_select=rec["n_select"], n_report=rec["n_report"], n_sleep=rec.get("n_sleep", 0),
                  flags_source=rec["flags_source"], d_min=rec["d_min"])
        self.log("prep: %s %s, %d reflections, %d free (%s), select %d / report %d / sleep %d, d_min %.3f; flags.mtz sha256 %s"
                 % (rec["intensities_or_amplitudes"], rec["data_labels"], rec["n_reflections"], rec["n_free"], rec["flags_source"],
                    rec["n_select"], rec["n_report"], rec.get("n_sleep", 0), rec["d_min"], rec["flags_mtz_sha256"][:12]))
        if "frozen_check" in rec:
            self.log("prep: frozen-set check %s" % json.dumps(rec["frozen_check"]))

    # ------------------------------------------------------------------ refinement (the only phenix.refine dispatcher)
    def _data_args(self) -> List[str]:
        p = self.prep
        return [p["data_flags_mtz"], "refinement.input.xray_data.labels=%s" % p["data_labels"],
                "refinement.input.xray_data.r_free_flags.label=%s" % p["flag_label"],
                "data_manager.fmodel.xray_data.r_free_flags.test_flag_value=%d" % int(p["test_flag_value"]),
                "data_manager.fmodel.xray_data.r_free_flags.generate=False",
                "data_manager.fmodel.xray_data.r_free_flags.ignore_r_free_flags=False"]

    @staticmethod
    def _output_args(prefix: str) -> List[str]:
        return ["output.prefix=%s" % prefix, "output.serial=1", "output.overwrite=True", "output.write_geo_file=False",
                "output.write_def_file=False", "output.write_eff_file=True", "output.write_map_coefficients=False"]

    def step_argv(self, model: str, prefix: str, mc: int, seed: int, wc: float, wu: float) -> List[str]:
        """The restrained step of E041/E044 (Untangler Refine.sh `-c WC -u WU -n MC -s 0.0 -q 0.1 -W -N`, as phenix.refine
        reads it: `phenix.refine --diff_params` of a recorded E041 step), without the wrapper."""
        return (["phenix.refine", model] + self._data_args() +
                ["refinement.main.number_of_macro_cycles=%d" % mc, "refinement.main.random_seed=%d" % seed, "refinement.main.nproc=1",
                 "refinement.refine.strategy=individual_sites+individual_adp+occupancies",
                 "refinement.refine.occupancies.individual=water", "refinement.refine.occupancies.remove_selection=not water",
                 "refinement.main.nqh_flips=False", "refinement.hydrogens.refine=riding",
                 "refinement.pdb_interpretation.c_beta_restraints=False",
                 "refinement.pdb_interpretation.reference_coordinate_restraints.enabled=True",
                 "refinement.pdb_interpretation.reference_coordinate_restraints.exclude_outliers=False",
                 "refinement.pdb_interpretation.reference_coordinate_restraints.selection=water",
                 "refinement.pdb_interpretation.reference_coordinate_restraints.sigma=0.1",
                 "refinement.pdb_interpretation.automatic_linking.link_residues=False",
                 "refinement.pdb_interpretation.automatic_linking.metal_coordination_cutoff=3.5",
                 "refinement.target_weights.wc=%g" % wc, "refinement.target_weights.wu=%g" % wu] + self._output_args(prefix))

    def standing_argv(self, model: str, prefix: str, mc: int, seed: int, stats: dict) -> List[str]:
        """The campaign's standing single-model recipe (autoref/tools/phenix_refine.py build_argv defaults, SPEC 6.1):
        individual sites + ADP (+ occupancies iff altlocs or partial occupancies), anisotropic ADP iff n_refl / n_atoms
        (non-H) >= 5 and d_min <= 1.5 A (else isotropic, TLS from phenix.find_tls_groups when d_min >= 2.0 A or a
        chain is longer than 200 residues), weights optimised, riding H, flat bulk solvent."""
        p = self.prep
        ratio = p["n_reflections"] / max(1, stats["n_heavy"])
        aniso = ratio >= 5.0 and p["d_min"] <= 1.5
        strategy = ["individual_sites", "individual_adp"] + (["occupancies"] if stats["altlocs"] or stats["partial_occ"] else [])
        tls = []
        if not aniso and (p["d_min"] >= 2.0 or stats["max_chain_residues"] > 200):
            tls = self.find_tls_groups(model)
            if tls:
                strategy.append("tls")
        argv = ["phenix.refine", model] + self._data_args() + [
            "refinement.main.number_of_macro_cycles=%d" % mc, "refinement.main.random_seed=%d" % seed, "refinement.main.nproc=1",
            "refinement.refine.strategy=" + "+".join(strategy),
            "refinement.refine.adp.individual.%s=not (element H or element D)" % ("anisotropic" if aniso else "isotropic")]
        argv += ["refinement.refine.adp.tls=%s" % s for s in tls]
        rama = p["d_min"] > 2.5
        argv += ["refinement.target_weights.optimize_xyz_weight=True", "refinement.target_weights.optimize_adp_weight=True",
                 "refinement.pdb_interpretation.ramachandran_plot_restraints.enabled=%s" % rama,
                 "refinement.pdb_interpretation.secondary_structure.enabled=%s" % rama,
                 "refinement.main.ordered_solvent=False", "refinement.main.simulated_annealing=False", "refinement.main.nqh_flips=False",
                 "refinement.hydrogens.refine=riding", "refinement.main.find_and_add_hydrogens=False",
                 "refinement.bulk_solvent_and_scale.mode=fast"] + self._output_args(prefix)
        self.state.setdefault("standing_recipe", {"adp_model": "anisotropic" if aniso else "isotropic", "refl_per_atom": round(ratio, 2),
                                                   "tls_selections": tls, "strategy": strategy, "macro_cycles": mc})
        return argv

    def find_tls_groups(self, model: str) -> List[str]:
        d = os.path.join(self.D, "baseline", "tls"); os.makedirs(d, exist_ok=True)
        lg = os.path.join(d, "find_tls_groups.log")
        self.sh(["phenix.find_tls_groups", "pdb_file=%s" % model, "nproc=1", "random_seed=0"], lg, cwd=d)
        return re.findall(r'^\s*tls\s*=\s*"(.+)"\s*$', read_text(lg), flags=re.MULTILINE)

    def model_stats(self, model: str) -> dict:
        h, _ = read_model(model)
        n_heavy = 0; alts = set(); partial = False; chains = {}
        for ch in h.only_model().chains():
            for rg in ch.residue_groups():
                if not any(is_water(ag.resname) for ag in rg.atom_groups()):
                    chains[ch.id] = chains.get(ch.id, 0) + 1
                for ag in rg.atom_groups():
                    if ag.altloc.strip():
                        alts.add(ag.altloc)
                    for a in ag.atoms():
                        if a.element.strip().upper() not in ("H", "D"):
                            n_heavy += 1
                        if a.occ < 1.0 and not ag.altloc.strip():
                            partial = True
        return {"n_heavy": n_heavy, "altlocs": "".join(sorted(alts)), "partial_occ": partial, "max_chain_residues": max(chains.values()) if chains else 0}

    def acquire(self) -> int:
        """A refinement slot, behind the load gate: wait while the host's 1-min load is above --load-max unless fewer
        than --min-running of this run's jobs are running; launches spaced by --launch-gap-s."""
        while True:
            with self.lock:
                spaced = time.time() - self.last_launch >= float(self.a.launch_gap_s)
                try:
                    load = os.getloadavg()[0]
                except OSError:
                    load = 0.0
                ok = self.running < int(self.a.min_running) or (load < float(self.a.load_max) and spaced)
                if ok and not self.slots.empty():
                    self.running += 1; self.last_launch = time.time()
                    return self.slots.get()
            time.sleep(15)

    def release(self, s: int) -> None:
        with self.lock:
            self.running -= 1; self.slots.put(s)

    def refine(self, argv: List[str], workdir: str, out_pdb: str, k: int = 6) -> str:
        """Dispatch one phenix.refine (guarded) in a slot; the output PDB is normalised (copy occupancies, four
        decimals) to out_pdb. Reused when out_pdb exists."""
        if os.path.exists(out_pdb) and os.path.getsize(out_pdb) > 0:
            return out_pdb
        check_refine_argv(argv, self.prep["flags_mtz"], self.prep["flags_mtz_sha256"])     # PROTOCOL 3, before every run
        os.makedirs(workdir, exist_ok=True)
        prefix = next(x.split("=", 1)[1] for x in argv if x.startswith("output.prefix="))
        inp = argv[1]
        s = self.acquire()
        t0 = time.time()
        try:
            with open(os.path.join(workdir, "command.txt"), "w") as f:
                f.write("argv: %s\ninput sha256 %s\nstart %s\n" % (" ".join(argv), sha256(inp), utc()))
            rc = self.sh(argv, os.path.join(workdir, prefix + ".stdout.log"), cwd=workdir)
            out = os.path.join(workdir, prefix + "_001.pdb")
            if rc != 0 or not os.path.exists(out):
                raise RuntimeError("phenix.refine failed (rc %d): %s" % (rc, os.path.join(workdir, prefix + ".stdout.log")))
            h, cs = read_model(out)
            write_model(h, cs, out_pdb, k)
            with open(os.path.join(workdir, "command.txt"), "a") as f:
                f.write("end %s wall %.0f s output sha256 %s\n" % (utc(), time.time() - t0, sha256(out_pdb)))
            return out_pdb
        finally:
            self.release(s)

    def convert_adp(self, model: str, selection: str, out_pdb: str, workdir: str, k: int = 6) -> str:
        """phenix.refine with 0 macro-cycles and modify_start_model: the selection's ADPs become anisotropic."""
        if os.path.exists(out_pdb):
            return out_pdb
        argv = (["phenix.refine", model] + self._data_args() +
                ["refinement.modify_start_model.modify.adp.atom_selection=%s" % selection,
                 "refinement.modify_start_model.modify.adp.convert_to_anisotropic=True", "refinement.main.number_of_macro_cycles=0",
                 "refinement.main.nproc=1"] + self._output_args("conv"))
        return self.refine(argv, workdir, out_pdb, k)

    # ------------------------------------------------------------------ measurements
    def clashscore(self, p: str) -> Optional[float]:
        lg = p[:-4] + ".clashscore.log"
        if not (os.path.exists(lg) and "clashscore = " in read_text(lg)):
            self.sh(["phenix.clashscore", p, "keep_hydrogens=True"], lg, cwd=os.path.dirname(p))
        return parse_clashscore_log(read_text(lg))

    def rotamer(self, p: str) -> Optional[float]:
        lg = p[:-4] + ".rotalyze.log"
        if not (os.path.exists(lg) and "SUMMARY" in read_text(lg)):
            self.sh(["phenix.rotalyze", p], lg, cwd=os.path.dirname(p))
        return parse_rotalyze_log(read_text(lg))

    def score(self, p: str, label: str, geometry: bool = True) -> dict:
        h = sha256(p)
        with self.lock:
            rec = dict(self.state["scores"].get(h) or {})
        if not rec:
            r = score_model(p, self.prep)
            rec = {k: r[k] for k in ("r_work", "r_free_full", "r_free_select", "r_free_report", "gap", "n_free", "n_select", "n_report", "n_sleep_withheld")}
            rec.update(describe(p)); rec["scored_utc"] = utc()
        if geometry and rec.get("clashscore") is None:
            rec["clashscore"] = self.clashscore(p)
        if geometry and rec.get("rotamer_outliers_pct") is None:
            rec["rotamer_outliers_pct"] = self.rotamer(p)
        with self.lock:
            self.state["scores"][h] = rec
        self.save()
        return {"label": label, "model": p, "sha256": h, **rec}

    # ------------------------------------------------------------------ stage: baseline (noise floor of the single model)
    def stage_baseline(self) -> None:
        if self.done("baseline"):
            return
        model = self.state["stages"]["fetch"]["model"]["path"]
        B = os.path.join(self.D, "baseline")
        stats = self.model_stats(model)
        seeds = list(range(1, int(self.a.floor_seeds) + 1))
        mc = int(self.a.mc_baseline)
        rows = []; outs = []
        with ThreadPoolExecutor(max_workers=len(seeds)) as ex:
            futs = {s: ex.submit(self.refine, self.standing_argv(model, "nf", mc, s, stats), os.path.join(B, "seed%d" % s),
                                 os.path.join(B, "seed%d" % s, "nf_s%d.pdb" % s), 1) for s in seeds}
            for s, fu in futs.items():
                try:
                    outs.append((s, fu.result()))
                except Exception as e:  # noqa: BLE001 - a failed seed is recorded, never a number
                    self.log("baseline seed %d FAILED: %r" % (s, e))
        for s, p in outs:
            rows.append({"seed": s, **self.score(p, "baseline seed %d" % s, geometry=False)})
        if len(rows) < 2:
            raise RuntimeError("baseline: fewer than 2 seeds completed")
        summ = summarize(rows)
        dep = self.score(model, "deposited model, our flags", geometry=False)
        med = median_row(rows)
        self.clashscore(med["model"]); self.rotamer(med["model"])
        geo = self.score(med["model"], "baseline median seed")
        self.state["baseline"] = {"model": model, "seeds": rows, "mean": {k: summ[k] for k in ("r_free_select", "r_free_report", "r_free_full", "r_work", "gap")},
                                  "sigma": {k: summ[k + "_sd"] for k in ("r_free_select", "r_free_report", "r_free_full", "gap")},
                                  "n": summ["n"], "median_seed_model": med["model"], "median_clashscore": geo.get("clashscore"),
                                  "median_rotamer_outliers_pct": geo.get("rotamer_outliers_pct"), "deposited": dep, "macro_cycles": mc}
        shutil.copy(med["model"], os.path.join(self.D, "models", "baseline_median.pdb"))
        self.mark("baseline", n=summ["n"], mean_full=summ["r_free_full"], sigma_select=summ["r_free_select_sd"])
        self.log("baseline: deposited %.5f full; re-refined mean %.5f full / %.5f select / %.5f report, gap %.4f, sigma select %.5f (N %d)"
                 % (dep["r_free_full"], summ["r_free_full"], summ["r_free_select"], summ["r_free_report"], summ["gap"], summ["r_free_select_sd"], summ["n"]))
        self.write_reports()

    # ------------------------------------------------------------------ stage: build (six copies -> S0)
    def add_hydrogens(self, single: str, out: str) -> dict:
        """Riding H completed when missing: phenix.ready_set first (adopted only if it adds H), then mmtbx.reduce2."""
        b = os.path.dirname(out)
        n_before = describe(single)["n_h"]
        n_heavy = describe(single)["n_atoms"] - n_before
        rec = {"before": n_before}
        if n_before >= 0.5 * n_heavy:
            shutil.copy(single, out); rec["note"] = "riding H already present"; return rec
        self.sh(["phenix.ready_set", single, "output_file_name=single_readyset", "add_h_to_water=False", "optimise_final_geometry_of_hydrogens=False"],
                os.path.join(b, "ready_set.log"), cwd=b)
        cand = os.path.join(b, "single_readyset.pdb")
        if os.path.exists(cand) and describe(cand)["n_h"] > n_before:
            rec["after"] = describe(cand)["n_h"]; rec["tool"] = "phenix.ready_set"; shutil.copy(cand, out); return rec
        self.sh(["mmtbx.reduce2", single, "approach=add", "add_flip_movers=False", "output.filename=single_reduce2.pdb"],
                os.path.join(b, "reduce2.log"), cwd=b)
        cand = os.path.join(b, "single_reduce2.pdb")
        if os.path.exists(cand) and describe(cand)["n_h"] > n_before:
            rec["after"] = describe(cand)["n_h"]; rec["tool"] = "mmtbx.reduce2"; shutil.copy(cand, out); return rec
        rec["note"] = "no tool added hydrogens; the model is used as is"
        shutil.copy(single, out)
        return rec

    def stage_build(self) -> None:
        if self.done("build"):
            return
        B = os.path.join(self.D, "build")
        k = int(self.a.k)
        single = self.state["stages"]["fetch"]["model"]["path"]
        pdb = os.path.join(B, "single.pdb")
        if not os.path.exists(pdb):
            h, cs = read_model(single)
            write_model(h, cs, pdb, k)
        h_in = os.path.join(B, "single_h.pdb")
        if not os.path.exists(h_in):
            self.state["hydrogens"] = self.add_hydrogens(pdb, h_in)
        un = os.path.join(B, "six_unrefined.pdb")
        if not os.path.exists(un):
            self.state["build"] = build_sixcopy(h_in, un, k, float(self.a.shake), float(self.a.shake_water), int(self.a.build_seed))
        desc = describe(un)
        start = un
        if desc["n_nonwater_iso_heavy"] and self.prep["d_min"] <= float(self.a.aniso_protein_below):
            start = self.convert_adp(un, "not water and not element H", os.path.join(B, "six_unrefined_aniso.pdb"), os.path.join(B, "aniso_protein"), k)
            self.state["protein_aniso_converted"] = desc["n_nonwater_iso_heavy"]
        self.state["six_unrefined"] = {"path": start, **describe(start)}
        self.save()
        if self.a.stop_after == "build" and self.a.skip_s0:
            self.log("build: six copies at %s; S0 skipped (--skip-s0)" % start); self.mark("build", s0=None); return
        s0 = os.path.join(B, "S0.pdb")
        wc, wu = DEFAULT_WEIGHTS
        self.refine(self.step_argv(start, "S0", int(self.a.mc_s0), 42, wc, wu), os.path.join(B, "S0"), s0, k)
        shutil.copy(s0, os.path.join(self.D, "models", "S0.pdb"))
        refs = [self.score(single, "deposited (our flags)", geometry=False), self.score(un, "six copies unrefined"), self.score(s0, "S0 six copies, %d mc" % int(self.a.mc_s0))]
        self.state["refs"] = refs
        self.mark("build", s0=s0)
        self.log("build: S0 %.5f full / %.5f select / %.5f report, R-work %.5f, clashscore %s, rotamers %s%%"
                 % (refs[2]["r_free_full"], refs[2]["r_free_select"], refs[2]["r_free_report"], refs[2]["r_work"], refs[2].get("clashscore"), refs[2].get("rotamer_outliers_pct")))
        self.write_reports()

    # ------------------------------------------------------------------ steps
    def seeds(self) -> List[int]:
        return list(range(1, int(self.a.seeds) + 1))

    def hygiene(self, base: str, out: str) -> str:
        if not os.path.exists(out):
            hygiene(base, out, int(self.a.k), 0.02, 0.6, 0.35)
        return out

    def _arms(self, d: str, pairs: List[Tuple[int, str, str]], weights_cand: Tuple[float, float], weights_ctrl: Tuple[float, float], mc: int) -> dict:
        """Refine candidate / control inputs per seed in parallel, score, return rows per arm."""
        k = int(self.a.k)
        jobs = []
        with ThreadPoolExecutor(max_workers=2 * max(1, len(pairs))) as ex:
            for s, cin, kin in pairs:
                jobs.append(("cand", s, ex.submit(self.refine, self.step_argv(cin, "cand", mc, s, weights_cand[0], weights_cand[1]), os.path.join(d, "cand_s%d" % s), os.path.join(d, "cand_s%d.pdb" % s), k)))
                jobs.append(("ctrl", s, ex.submit(self.refine, self.step_argv(kin, "ctrl", mc, s, weights_ctrl[0], weights_ctrl[1]), os.path.join(d, "ctrl_s%d" % s), os.path.join(d, "ctrl_s%d.pdb" % s), k)))
            outs = []
            for arm, s, fu in jobs:
                try:
                    outs.append((arm, s, fu.result()))
                except Exception as e:  # noqa: BLE001 - a failed arm is recorded, never a number
                    self.log("%s: %s seed %d FAILED: %r" % (os.path.basename(d), arm, s, e))
        rows = {"cand": [], "ctrl": []}
        for arm, s, p in outs:   # scored one at a time: cctbx objects are not shared between threads
            rec = self.score(p, "%s %s s%d" % (os.path.basename(d), arm, s), geometry=False)
            rec["seed"] = s; rows[arm].append(rec)
        return rows

    def _verdict(self, sid: str, kind: str, info: dict, rows: dict) -> dict:
        info["rows"] = rows
        if len(rows["cand"]) < 2 or len(rows["ctrl"]) < 2:
            info.update(verdict={"adopted": False, "kind": kind, "reasons": ["fewer than 2 seeds completed in an arm"]}, ended=utc())
        else:
            mc, mk = median_row(rows["cand"]), median_row(rows["ctrl"])
            gc, gk = self.score(mc["model"], "median cand"), self.score(mk["model"], "median ctrl")
            for r in rows["cand"]:
                if r["model"] == mc["model"]:
                    r.update(clashscore=gc.get("clashscore"), rotamer_outliers_pct=gc.get("rotamer_outliers_pct"))
            for r in rows["ctrl"]:
                if r["model"] == mk["model"]:
                    r.update(clashscore=gk.get("clashscore"), rotamer_outliers_pct=gk.get("rotamer_outliers_pct"))
            v = judge(kind, rows["cand"], rows["ctrl"], self.state.get("floor_sigma", {}), gc.get("clashscore"), gk.get("clashscore"),
                      gc.get("rotamer_outliers_pct"), gk.get("rotamer_outliers_pct"))
            info.update(verdict=v, median_cand=mc["model"], median_ctrl=mk["model"], ended=utc())
        self.state["steps"][sid] = info
        self.save()
        v = info["verdict"]
        self.log("%s: %s - %s%s" % (sid, "ADOPTED" if v["adopted"] else "not adopted", "; ".join(v["reasons"]),
                                    (" (d_select %+.5f, d_report %+.5f, d_gap %+.5f; clash %s / %s; rota %s / %s)" % (v["d_select"], v["d_report"], v["d_gap"], v.get("clash_cand"), v.get("clash_ctrl"), v.get("rota_cand"), v.get("rota_ctrl"))) if "d_select" in v else ""))
        self.write_reports()
        return info

    def run_step(self, sid: str, kind: str, base: str, weights_cand, weights_ctrl, prepare=None) -> dict:
        """One paired step: base -> hygiene -> [change] -> refinement, against the same hygiene + refinement without the
        change, n seeds each. prepare(hyg, dir, info) -> candidate input or None (nothing to change: skipped)."""
        if sid in self.state["steps"] and self.state["steps"][sid].get("verdict"):
            return self.state["steps"][sid]
        d = os.path.join(self.D, "steps", sid); os.makedirs(d, exist_ok=True)
        self.log("%s: start (%s) base %s" % (sid, kind, base))
        hyg = self.hygiene(base, os.path.join(d, "base_hyg.pdb"))
        info = {"id": sid, "kind": kind, "base": base, "base_sha256": sha256(base), "weights_cand": list(weights_cand), "weights_ctrl": list(weights_ctrl),
                "macro_cycles": int(self.a.mc_step), "started": utc()}
        cand_in = prepare(hyg, d, info) if prepare else hyg
        if cand_in is None:
            info.update(verdict={"adopted": False, "kind": kind, "reasons": [info.get("skip_reason", "no change")]}, skipped=True, ended=utc())
            self.state["steps"][sid] = info; self.save()
            self.log("%s: skipped (%s)" % (sid, info["verdict"]["reasons"][0]))
            return info
        rows = self._arms(d, [(s, cand_in, hyg) for s in self.seeds()], weights_cand, weights_ctrl, int(self.a.mc_step))
        return self._verdict(sid, kind, info, rows)

    def run_composite_step(self, sid: str, step: dict, weights) -> dict:
        """pick + cleanup as ONE move (D563): per seed, the pick's refined candidate is clash-cleaned and the pick's own
        control continued, both by one identical refinement; judged by the improving rule."""
        if sid in self.state["steps"] and self.state["steps"][sid].get("verdict"):
            return self.state["steps"][sid]
        d = os.path.join(self.D, "steps", sid); os.makedirs(d, exist_ok=True)
        by = {arm: {int(r["seed"]): r["model"] for r in step.get("rows", {}).get(arm, [])} for arm in ("cand", "ctrl")}
        seeds = [s for s in self.seeds() if s in by["cand"] and s in by["ctrl"]]
        self.log("%s: start (composite pick + cleanup of %s) seeds %s" % (sid, step["id"], seeds))
        info = {"id": sid, "kind": "pick", "composite_of": [step["id"], "cleanup"], "base": step.get("base"), "base_sha256": step.get("base_sha256"),
                "weights_cand": list(weights), "weights_ctrl": list(weights), "macro_cycles": int(self.a.mc_step), "started": utc(), "per_seed": {}}
        pairs = []
        for s in seeds:
            ds = os.path.join(d, "s%d" % s); os.makedirs(ds, exist_ok=True)
            hc = self.hygiene(by["cand"][s], os.path.join(ds, "cand_base_hyg.pdb"))
            hk = self.hygiene(by["ctrl"][s], os.path.join(ds, "ctrl_base_hyg.pdb"))
            pi: dict = {}
            cin = self.prep_cleanup(hc, ds, pi)
            info["per_seed"]["s%d" % s] = pi
            pairs.append((s, cin if cin is not None else hc, hk))
        if all(info["per_seed"]["s%d" % s].get("n_water_removed", 0) == 0 for s in seeds):
            info.update(verdict={"adopted": False, "kind": "pick", "reasons": ["no own-conformer water clash to remove in any seed"]}, skipped=True, ended=utc())
            self.state["steps"][sid] = info; self.save(); self.log("%s: skipped (nothing to clean)" % sid)
            return info
        rows = self._arms(d, pairs, weights, weights, int(self.a.mc_step))
        return self._verdict(sid, "pick", info, rows)

    def prep_pick(self, sigma: float):
        def f(hyg: str, d: str, info: dict):
            out = os.path.join(d, "pick.pdb")
            if not os.path.exists(out + ".pick.json"):
                pick_waters(hyg, self.prep, out, sigma, int(self.a.k), own_clear=bool(int(self.a.own_clear)), seed=42)
            pj = read_json(out + ".pick.json")
            info.update(sigma=sigma, n_sites=pj["n_sites"], n_copies=pj["n_atoms_added"], n_peaks=pj["n_peaks"])
            self.log("%s: pick at %.1f sigma: %d peaks, %d sites, %d copies" % (os.path.basename(d), sigma, pj["n_peaks"], pj["n_sites"], pj["n_atoms_added"]))
            if pj["n_atoms_added"] == 0:
                info["skip_reason"] = "no site at %.1f sigma" % sigma
                return None
            return out
        return f

    def prep_aniso(self, hyg: str, d: str, info: dict):
        n_iso = describe(hyg)["n_water_iso"]
        info["n_water_iso"] = n_iso
        if n_iso == 0:
            info["skip_reason"] = "every water already anisotropic"
            return None
        return self.convert_adp(hyg, "water", os.path.join(d, "aniso_in.pdb"), os.path.join(d, "convert"), int(self.a.k))

    def prep_cleanup(self, hyg: str, d: str, info: dict):
        out = os.path.join(d, "clean.pdb")
        if not os.path.exists(out):
            raw = os.path.join(d, "clean_raw.pdb")
            if self.a.cleanup_rule == "clashlog":
                c = self.clashscore(hyg); info["clashscore_base"] = c
                rep = clean_clashlog(hyg, hyg[:-4] + ".clashscore.log", raw, int(self.a.k))
            else:
                rep = clean_vdw(hyg, raw, int(self.a.k), float(self.a.vdw_margin))
            info["cleanup"] = {k: v for k, v in rep.items() if k != "removed_sites"}
            self.hygiene(raw, out)
        n0, n1 = describe(hyg)["n_water_atoms"], describe(out)["n_water_atoms"]
        info["n_water_removed"] = n0 - n1
        if n0 == n1:
            info["skip_reason"] = "no own-conformer water clash to remove"
            return None
        return out

    # ------------------------------------------------------------------ stage: run (rounds)
    def stage_run(self) -> None:
        if self.done("run"):
            return
        t0 = self.state.setdefault("run_started", utc())
        s0 = self.state["stages"]["build"]["s0"]
        M = s0
        if self.a.weights_step:
            w = self.run_step("r0_weights", "weights", s0, STACK_WEIGHTS, DEFAULT_WEIGHTS)
            if "rows" in w and "floor_sigma" not in self.state:
                # the representation's floor sigma (PROTOCOL 18.4): pooled seed SD of the weights step's two arms
                self.state["floor_sigma"] = {k: pooled_sd([r[k] for r in w["rows"]["cand"]], [r[k] for r in w["rows"]["ctrl"]])
                                             for k in ("r_free_select", "r_free_report", "r_free_full")}
                self.state["floor_sigma"]["n"] = len(w["rows"]["cand"]) + len(w["rows"]["ctrl"]); self.state["floor_sigma"]["provisional"] = True
            adopted_w = w["verdict"]["adopted"]
            self.state["weights"] = list(STACK_WEIGHTS if adopted_w else DEFAULT_WEIGHTS)
            if adopted_w:
                M = w["median_cand"]
                self.state.setdefault("adopted", [])
                if not any(x["step"] == "r0_weights" for x in self.state["adopted"]):
                    self.state["adopted"].append({"step": "r0_weights", "model": M})
                    shutil.copy(M, os.path.join(self.D, "models", "r0_weights.pdb"))
        else:
            self.state["weights"] = list(DEFAULT_WEIGHTS)
        self.state.setdefault("adopted", [])
        if self.state["adopted"]:
            M = self.state["adopted"][-1]["model"]
        weights = tuple(self.state["weights"])
        self.save()
        r = len(self.state["rounds"])
        while True:
            elapsed = (time.time() - calendar.timegm(time.strptime(t0, "%Y-%m-%dT%H:%M:%SZ"))) / 3600
            stop = should_stop([x["adopted"] for x in self.state["rounds"]], elapsed, float(self.a.budget_h), int(self.a.max_rounds))
            if stop:
                self.state["stopped"] = {"reason": stop, "at": utc(), "final_model": M}
                self.save(); self.log("STOP: %s; final model %s" % (stop, M))
                break
            r += 1
            if r == 1:
                sigma = round_sigma(1)
            elif r == 2:
                sigma = min(float(self.state.get("sigma", 3.0)), round_sigma(2))
            else:
                sigma = float(self.state.get("sigma", round_sigma(r)))
            any_adopted = False
            for kind in ("pick", "aniso_water", "cleanup"):
                sid = "r%d_%s" % (r, kind)
                if kind == "pick":
                    info = self.run_step(sid, kind, M, weights, weights, prepare=self.prep_pick(sigma))
                    sigma = next_sigma(sigma, info.get("n_sites")); self.state["sigma"] = sigma
                    if composite_eligible(info["verdict"]) and not info.get("skipped"):
                        info = self.run_composite_step(sid + "_cleanup", info, weights); sid = info["id"]
                elif kind == "aniso_water":
                    info = self.run_step(sid, kind, M, weights, weights, prepare=self.prep_aniso)
                else:
                    cM = self.score(M, "M").get("clashscore")
                    if cM is not None and cM <= CLASH_CAP:
                        self.log("%s: clashscore of M %.2f <= %g: no cleanup" % (sid, cM, CLASH_CAP)); continue
                    info = self.run_step(sid, kind, M, weights, weights, prepare=self.prep_cleanup)
                if info["verdict"]["adopted"]:
                    M = info["median_cand"]; any_adopted = True
                    if not any(x["step"] == sid for x in self.state["adopted"]):
                        self.state["adopted"].append({"step": sid, "model": M})
                        shutil.copy(M, os.path.join(self.D, "models", sid + ".pdb"))
                self.save()
            g = self.score(M, "M")
            self.state["rounds"].append({"round": r, "adopted": any_adopted, "model": M, "r_free_full": g["r_free_full"], "clashscore": g.get("clashscore"),
                                         "rotamer_outliers_pct": g.get("rotamer_outliers_pct"), "ended": utc()})
            self.save(); self.write_reports()
        self.final(M)
        self.mark("run", final_model=M)

    def final(self, M: str) -> None:
        """Independent scorer (indep_rfree.py logic), clashscore and rotamer outliers on the final model, S0 and the
        baseline median; the final model is copied to models/final.pdb."""
        shutil.copy(M, os.path.join(self.D, "models", "final.pdb"))
        out = {}
        for lab, p in (("final", M), ("S0", self.state["stages"]["build"]["s0"]), ("baseline_median", self.state["baseline"]["median_seed_model"]),
                       ("deposited", self.state["stages"]["fetch"]["model"]["path"])):
            try:
                rec = score_independent(p, self.prep)
            except Exception as e:  # noqa: BLE001 - the independent score of a reference model is reported, never fatal
                rec = {"error": repr(e)}
            if p.endswith(".pdb"):
                rec["clashscore"] = self.clashscore(p); rec["rotamer_outliers_pct"] = self.rotamer(p)
            rec.update(harness_style=self.score(p, lab, geometry=p.endswith(".pdb")))
            out[lab] = rec
        self.state["final"] = out
        self.save(); self.write_reports()
        f = out["final"]
        self.log("final: independent R-work %.5f / R-free %.5f (select %.5f / report %.5f), clashscore %s, rotamers %s%%"
                 % (f.get("r_work_fmodel", float("nan")), f.get("r_free_fmodel", float("nan")), f.get("r_free_select_manual", float("nan")),
                    f.get("r_free_report_manual", float("nan")), f.get("clashscore"), f.get("rotamer_outliers_pct")))

    def final_score(self, reason: str) -> dict:
        """The one logged consultation of the sleep third (PROTOCOL 3.8) on the final model."""
        if not self.prep or not int(self.prep.get("n_sleep", 0)):
            raise RuntimeError("no sleep third in this run's split")
        M = self.state.get("stopped", {}).get("final_model") or os.path.join(self.D, "models", "final.pdb")
        prior = self.state.get("sleep_consultations", [])
        if prior:
            self.log("WARNING: the sleep third of %s was already consulted %d time(s); this call is logged as a repeat" % (self.T, len(prior)))
        import getpass
        r = score_model(M, self.prep, include_sleep=True)
        rec = {"model": M, "sha256": sha256(M), "who": getpass.getuser(), "when": utc(), "reason": reason, "r_free_sleep": r["r_free_sleep"],
               "r_free_select": r["r_free_select"], "r_free_report": r["r_free_report"], "r_free_full_all": r["r_free_full"], "n_sleep": r["n_sleep"]}
        self.state.setdefault("sleep_consultations", []).append(rec)
        self.save(); self.write_reports()
        self.log("final-score: R-free sleep %.5f (select %.5f / report %.5f / all free %.5f) - reason: %s" % (r["r_free_sleep"], r["r_free_select"], r["r_free_report"], r["r_free_full"], reason))
        return rec

    # ------------------------------------------------------------------ reports
    def write_reports(self) -> None:
        st = self.state
        fmt = lambda x, n=5: ("" if x is None else ("%.*f" % (n, x) if isinstance(x, float) else str(x)))
        out = ["# %s - six-copy water treatment trajectory (%s)" % (self.T, VERSION), "",
               "Rewritten %s. Evaluator: cctbx fmodel on the frozen data and inherited flags (flags.mtz sha256 %s), R-free on the full "
               "free set and on the select / report halves (sleep withheld: %s). Gap = R-free(full) - R-work. Clashscore: phenix.clashscore "
               "keep_hydrogens=True. Rotamers: phenix.rotalyze. The six-copy model is a representation (PROTOCOL 18.1), never a deliverable."
               % (utc(), (self.prep or {}).get("flags_mtz_sha256", "?")[:12], (self.prep or {}).get("n_sleep", 0)), ""]
        if st.get("baseline"):
            b = st["baseline"]
            out += ["## Baseline (single model, standing recipe, %d macro-cycles, N = %d)" % (b["macro_cycles"], b["n"]), "",
                    "| model | R-work | full | select | report | gap | clashscore | rotamers % |", "|---|---|---|---|---|---|---|---|",
                    "| deposited, our flags | %s | %s | %s | %s | %s | | |" % (fmt(b["deposited"]["r_work"]), fmt(b["deposited"]["r_free_full"]), fmt(b["deposited"]["r_free_select"]), fmt(b["deposited"]["r_free_report"]), fmt(b["deposited"]["gap"], 4)),
                    "| re-refined mean | %s | %s | %s | %s | %s | %s | %s |" % (fmt(b["mean"]["r_work"]), fmt(b["mean"]["r_free_full"]), fmt(b["mean"]["r_free_select"]), fmt(b["mean"]["r_free_report"]), fmt(b["mean"]["gap"], 4), fmt(b.get("median_clashscore"), 2), fmt(b.get("median_rotamer_outliers_pct"), 2)),
                    "| re-refined sigma | | %s | %s | %s | %s | | |" % (fmt(b["sigma"]["r_free_full"]), fmt(b["sigma"]["r_free_select"]), fmt(b["sigma"]["r_free_report"]), fmt(b["sigma"]["gap"], 5)), ""]
        hdr = ("| model | R-work | full | select | report | gap | water atoms | ANISOU | clashscore | rotamers % |", "|---|---|---|---|---|---|---|---|---|---|")
        row = lambda lab, r: "| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (lab, fmt(r.get("r_work")), fmt(r.get("r_free_full")), fmt(r.get("r_free_select")), fmt(r.get("r_free_report")), fmt(r.get("gap"), 4), r.get("n_water_atoms"), r.get("n_anisou"), fmt(r.get("clashscore"), 2), fmt(r.get("rotamer_outliers_pct"), 2))
        if st.get("refs"):
            out += ["## Build", ""] + list(hdr) + [row(r["label"], r) for r in st["refs"]] + [""]
        out += ["## Steps (every seed of both arms; weights = (wc, wu); floor sigma %s)" % json.dumps({k: (round(v, 6) if isinstance(v, float) else v) for k, v in st.get("floor_sigma", {}).items()}), "",
                "| step | arm | seed | R-work | full | select | report | gap | water atoms | ANISOU | clashscore | rotamers % |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
        dec = ["## Decisions", ""]
        for sid, info in st["steps"].items():
            for arm in ("cand", "ctrl"):
                for r in info.get("rows", {}).get(arm, []):
                    out.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (sid, arm, r["seed"], fmt(r["r_work"]), fmt(r["r_free_full"]), fmt(r["r_free_select"]), fmt(r["r_free_report"]), fmt(r["gap"], 4), r.get("n_water_atoms"), r.get("n_anisou"), fmt(r.get("clashscore"), 2), fmt(r.get("rotamer_outliers_pct"), 2)))
            v = info.get("verdict", {})
            extra = {k: info[k] for k in ("sigma", "n_peaks", "n_sites", "n_copies", "n_water_iso", "n_water_removed", "clashscore_base") if k in info}
            line = "- **%s** (%s, weights cand %s / ctrl %s, %s mc): **%s** - %s" % (sid, info.get("kind"), info.get("weights_cand"), info.get("weights_ctrl"), info.get("macro_cycles"), "ADOPTED" if v.get("adopted") else "not adopted", "; ".join(v.get("reasons", [])))
            if "d_select" in v:
                line += (". dselect %+.5f (sigma %.5f), dreport %+.5f, dfull %+.5f, dgap %+.5f; cand mean full %.5f / ctrl %.5f; clashscore %s / %s; rotamers %s / %s"
                         % (v["d_select"], v["sigma_select"], v["d_report"], v["d_full"], v["d_gap"], v["cand"]["r_free_full"], v["ctrl"]["r_free_full"], fmt(v.get("clash_cand"), 2), fmt(v.get("clash_ctrl"), 2), fmt(v.get("rota_cand"), 2), fmt(v.get("rota_ctrl"), 2)))
            if extra:
                line += ". " + json.dumps(extra)
            if v.get("adopted"):
                line += ". Adopted model `%s`" % info.get("median_cand")
            dec.append(line)
        out += [""] + dec + ["", "## Rounds", "", "| round | adopted | model in force | full | clashscore | rotamers % | ended |", "|---|---|---|---|---|---|---|"]
        for r in st.get("rounds", []):
            out.append("| %s | %s | `%s` | %s | %s | %s | %s |" % (r["round"], r["adopted"], r["model"], fmt(r.get("r_free_full")), fmt(r.get("clashscore"), 2), fmt(r.get("rotamer_outliers_pct"), 2), r["ended"]))
        if st.get("stopped"):
            out += ["", "**Stopped** %s: %s. Final model `%s`." % (st["stopped"]["at"], st["stopped"]["reason"], st["stopped"]["final_model"])]
        if st.get("final"):
            out += ["", "## Final (independent scorer: fmodel on all reflections, no outlier rejection, manual R)", "",
                    "| model | R-work | R-free | select | report | clashscore | rotamers % | atoms |", "|---|---|---|---|---|---|---|---|"]
            for lab, f in st["final"].items():
                out.append("| %s | %s | %s | %s | %s | %s | %s | %s |" % (lab, fmt(f.get("r_work_fmodel")), fmt(f.get("r_free_fmodel")), fmt(f.get("r_free_select_manual")), fmt(f.get("r_free_report_manual")), fmt(f.get("clashscore"), 2), fmt(f.get("rotamer_outliers_pct"), 2), f.get("n_atoms")))
        if st.get("sleep_consultations"):
            out += ["", "## Sleep-third consultations (PROTOCOL 3.8)", ""] + ["- %s %s: R-free sleep %.5f (%s)" % (c["when"], c["who"], c["r_free_sleep"], c["reason"]) for c in st["sleep_consultations"]]
        with open(os.path.join(self.D, "TRAJECTORY.md"), "w") as f:
            f.write("\n".join(out) + "\n")


def main(argv=None) -> int:
    global STACK_WEIGHTS
    ap = argparse.ArgumentParser(description="E041 six-copy water treatment on any protein (one file, cctbx only)")
    ap.add_argument("pdb_id")
    ap.add_argument("--out", required=True, help="run directory")
    ap.add_argument("--model", default="deposited", help="'deposited' (RCSB download) or a model file (PDB / mmCIF)")
    ap.add_argument("--data", default=None, help="structure factors: <ID>-sf.cif or an MTZ with data and free-flag columns (default: RCSB download)")
    ap.add_argument("--frozen-dir", dest="frozen_dir", default=None, help="existing frozen set: data.mtz, flags.mtz, split.mtz[, prep.json]; taken as is and verified")
    ap.add_argument("--flag-label", dest="flag_label", default=None, help="--data MTZ: free-flag column label")
    ap.add_argument("--test-flag-value", dest="test_flag_value", type=int, default=None, help="--data MTZ: the value that marks a free reflection")
    ap.add_argument("--sleep", action="store_true", help="three-way split of the free set; the sleep third is read only by --final-score")
    ap.add_argument("--final-score", dest="final_score", action="store_true", help="score the final model on the sleep third once (logged); needs --reason")
    ap.add_argument("--reason", default=None)
    ap.add_argument("--stop-after", dest="stop_after", choices=Run.STAGES, default="run")
    ap.add_argument("--resume", action="store_true", help="reuse finished stages and refinements in --out")
    ap.add_argument("--nproc", default=6, help="parallel phenix.refine jobs (each single-threaded)")
    ap.add_argument("--load-max", dest="load_max", default=56.0, help="no new job while the host's 1-min load is above this")
    ap.add_argument("--min-running", dest="min_running", default=1)
    ap.add_argument("--launch-gap-s", dest="launch_gap_s", default=120)
    ap.add_argument("--seeds", default=3, help="refinement seeds per arm of a paired step")
    ap.add_argument("--floor-seeds", dest="floor_seeds", default=3, help="seeds of the single-model baseline (10 for a full noise floor)")
    ap.add_argument("--mc-baseline", dest="mc_baseline", default=5)
    ap.add_argument("--mc-s0", dest="mc_s0", default=20)
    ap.add_argument("--mc-step", dest="mc_step", default=10)
    ap.add_argument("--k", default=6, help="copies per residue")
    ap.add_argument("--shake", default=0.2, help="rms per-atom displacement (A) of copies 2..k at the build (D564)")
    ap.add_argument("--shake-water", dest="shake_water", default=0.1)
    ap.add_argument("--build-seed", dest="build_seed", default=44)
    ap.add_argument("--aniso-protein-below", dest="aniso_protein_below", default=1.2, help="complete protein ANISOU at the build when d_min <= this (A)")
    ap.add_argument("--skip-s0", dest="skip_s0", action="store_true", help="with --stop-after build: stop before the S0 refinement")
    ap.add_argument("--wc", default=STACK_WEIGHTS[0], help="weights step: candidate wc (geometry weight); default E041 stack")
    ap.add_argument("--wu", default=STACK_WEIGHTS[1], help="weights step: candidate wu (ADP restraint weight)")
    ap.add_argument("--no-weights-step", dest="weights_step", action="store_false", help="skip the r0 weights step (Untangler defaults throughout)")
    ap.add_argument("--own-clear", dest="own_clear", default=1, help="1 = own-conformer clearance incl. riding H in the picker (2.6 A heavy / 2.0 A H)")
    ap.add_argument("--cleanup-rule", dest="cleanup_rule", choices=("clashlog", "vdw"), default="clashlog",
                    help="clashlog (default; E041's endpoint CJ_R4 and the E044 driver): remove the water copies phenix.clashscore lists in an "
                         "own-conformer clash; vdw: the element-aware own-conformer distance rule + --vdw-margin (on E041's CJ_R4_polish, "
                         "clashscore 4.4, the vdw rule at 0.2 A removes 406 of 2 568 water copies, the clash list 6)")
    ap.add_argument("--vdw-margin", dest="vdw_margin", default=0.2)
    ap.add_argument("--max-rounds", dest="max_rounds", default=8)
    ap.add_argument("--budget-h", dest="budget_h", default=36)
    a = ap.parse_args(argv)
    STACK_WEIGHTS = (float(a.wc), float(a.wu))
    if a.final_score and not a.reason:
        ap.error("--final-score needs --reason")
    _cctbx()
    R = Run(a.pdb_id, a)
    R.log("start %s %s; argv %s" % (VERSION, R.T, " ".join(sys.argv)))
    if a.final_score:
        R.final_score(a.reason)
        return 0
    for stage in Run.STAGES:
        getattr(R, "stage_" + stage)()
        if a.stop_after == stage:
            R.log("stopped after stage %s (--stop-after)" % stage)
            break
    R.write_reports()
    return 0


if __name__ == "__main__":
    sys.exit(main())
