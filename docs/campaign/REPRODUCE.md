# Reproducing and verifying the results

This document is for a researcher on a different machine who wants to check, or fully re-run, the
R-free results of this campaign. It is written to be self-contained; where it points elsewhere, that
document holds the authoritative detail (`CLAUDE.md` for how things run, `PROTOCOL.md` and `SPEC.md`
for the rules and the algorithm).

The results being verified (full R-free, all on the campaign's frozen flags):

| Target | Resolution | Deposited model, our flags | Our deliverable | Δ |
|--------|-----------|----------------------------|-----------------|-----|
| 3TC7   | ~1.5 Å    | 0.1915                     | 0.1728          | −0.0187 |
| 3QUE   | 2.7 Å     | 0.2872                     | 0.2589          | −0.0283 |
| 7KR0   | 0.77 Å    | 0.1175                     | 0.1126          | −0.0049 |

Report-half figures (the headline convention): 3TC7 0.1892 → 0.1673, 3QUE 0.2896 → 0.2644,
7KR0 0.1191 → 0.1148. "Deposited model, our flags" is the deposited coordinate file recomputed at
0 macro-cycles against our data and flags — the only apples-to-apples baseline, because R-free is
comparable only on the same held-out reflection set.

There are three levels of reproduction, cheapest first. Level 0 verifies the *numbers*; Levels 1–2
reproduce the *work* that produced them.

---

## What you need

- **The repo** — this checkout (code, frozen thresholds, ledger exports, decision log).
- **The environment** — one pinned image, `harbor.astera.sh/library/phenix:phenix2.1-6048-2026-06-09`
  (Phenix 2.1-6048). `scripts/bringup_pod.sh` is idempotent and builds the three virtualenvs
  (`autoref`, `qfit`, `coot`) on top of it. On the reference setup this runs as an `actl` pod
  (`actl pod up autoresearch -n diffuse --image phenix`; profile `cpu-medium` until 2026-09-05, `8x`
  since — D457–D461); any host with the
  image and that script works.
- **The data** — not committed (it is public). `autoref fetch --target <ID>` pulls the deposited
  model, structure factors, and FASTA from RCSB plus the PDB-REDO artifacts. `autoref prep` then
  rebuilds `data.mtz` + `flags.mtz` and **re-checks their SHA-256 against the values recorded at
  campaign time**, so a rerun proves it is working on byte-identical data and the identical
  free-reflection set. The recorded hashes live in each target's prep record (see Level 0).

Environment variables (`AUTOREF_*`) resolve the state, runs, data, and thresholds paths; the pinned
values and the `AUTOREF_NPROC=4` concurrency integer are described in `CLAUDE.md`.

---

## Level 0 — verify a headline number (under a minute)

You need two small files: a model (`.cif`/`.pdb`) and the frozen `flags.mtz` for that target. The
single scoring entry point is `autoref.flags.evaluate` — it computes R-free on the frozen flags and
returns the full / report / select split. This is exactly the call used to produce the table above.

```bash
# in the autoref venv, with the target's prep already done (data.mtz + flags.mtz present)
python - <<'PY'
from autoref.flags import evaluate
r = evaluate("<path/to/model.cif>", "7KR0", consult=False, stage="verify")
print({k: round(r[k], 4) for k in ("r_work", "r_free_full", "r_free_report", "r_free_select")})
PY
```

Score our deliverable and the deposited model this way and you reproduce both columns of the table to
the digit. The deposited model recompute is `evaluate("data/raw/<ID>/<ID>.cif", "<ID>", ...)`; our
deliverable path is in `state/current/<ID>.json` (`model` field). No refinement is involved, so the
number is deterministic.

Underneath, `evaluate` calls `phenix.model_vs_data` against `data.mtz` + `flags.mtz`; a reviewer who
prefers to bypass the harness can run that tool directly on the same two files and get the same
R-free.

---

## Level 1 — reproduce one accepted change (minutes)

Every accepted change is a row in the `changes` ledger plus a run directory under
`runs/<target>/…` containing `command.txt` (the verbatim argv), the input models, the seed, the
input hashes, `refine_decisions.json`, and `validation.json`. Re-running the recorded command on the
recorded inputs reproduces the paired **null control**: the same refinement with and without the
change. That lets you re-derive the ΔR-free yourself rather than trust it — the attributable delta is
`candidate − null` on `r_free_select`, and the sign is confirmed on `r_free_report`/full.

The ledgers are committed as flat files in `state/exports/` (`changes.csv`, `cycles.csv`,
`jobs.csv`, `noise_floor.csv`, `rfree_consultations.csv`, `defects.csv`, `roster.csv`, …). Pick a
row, read its `run_dir`, and re-run `command.txt`.

---

## Level 2 — reproduce a target from raw (scripted, ~overnight)

```bash
autoref fetch      --target 7KR0     # RCSB + PDB-REDO -> data/raw, with manifests
autoref prep       --target 7KR0     # data.mtz + flags.mtz (frozen) + select/report split; checks SHA-256
autoref dossier    --target 7KR0     # xtriage + model audit + baselines
autoref verify     --target 7KR0     # gates G0–G8: canaries, altloc-clash case, occ sums,
                                      #   R-free reproduction, round-trip
autoref noise-floor --target 7KR0 --n 10   # sigma of R-free from 10 re-refinements (frozen)
autoref baseline   --target 7KR0     # four-way baselines
autoref run        --target 7KR0     # macro-cycle loop to convergence
```

`prep` halts if the data hash diverges, so you cannot silently reproduce on different data or a
different held-out set. The frozen thresholds files (`autoref/thresholds_v1.yaml` … `_v5`) plus
recorded seeds make the loop deterministic up to the measured noise floor; `autoref verify` is the
built-in self-check that the gates and the R-free reproduction still hold on the new machine.

---

## Why the numbers are trustworthy across machines

- **Cross-validation is frozen and guarded.** The R-free flags are inherited from the deposition and
  never regenerated or resized; `autoref/tools/phenix_refine.py` refuses any command that would touch
  them. A change is accepted only when it clears all four bars at once — R-free beyond k·σ (measured,
  not assumed), local density support, geometry within tolerance, and no altloc-aware clashes.
- **Data is pinned by hash.** Each prep record carries `data_mtz_sha256` and `flags_mtz_sha256`
  (e.g. 7KR0 `ae703738…` / `31939295…`, n_free 8712), so "same data, same test set" is checkable,
  not assumed.
- **Every step is on the record.** ~4,900 job rows (tool, seed, code version, thresholds hash), a run
  directory per step, and a dated decision log (`state/deviations.md` D001–D484,
  `state/notes/experiments.md`). Negative results are logged with the same care as positive ones.

## Portability notes and limits

- The canonical ledger is a SQLite database on the pod and is **not** committed; the
  `state/exports/*.csv` are its portable snapshot. A full re-run rebuilds the SQLite from scratch.
- Bulk `runs/` artifacts (maps, intermediate models, logs) live on the pod's persistent volume and
  are not all committed — but everything needed to *verify* a claim (a model file, `flags.mtz`, and
  one command) is small and portable.
- The lower ensemble reference numbers (3QUE 0.2476; 7KR0 0.0673) are separate, non-depositable
  representations. They are *verifiable* by re-scoring the ensemble model on our flags (Level 0), but
  are not reproducible-from-raw by this harness, which builds single depositable models.

## Independent verification (2026-09-07)

`scripts/verify/` holds a scorer that shares no code with the harness (`indep_rfree.py`: cctbx fmodel on
all reflections, no outlier rejection, manual R over the free / select / report subsets), a flag-identity
check against the raw structure-factor mmCIF (`flag_identity.py`), and a driver that also runs
`phenix.model_vs_data` and `phenix.molprobity`. Run on the pod (`/home/dev/runs/verify_20260907/`), it
reproduced every number in the table above to within 0.001 and confirmed that the free sets are identical
to the deposited `_refln.status == 'f'` sets. Details and caveats: D474 and D475 in `state/deviations.md`.

| Model | R-work | R-free full | select | report |
|-------|--------|-------------|--------|--------|
| 3TC7 deposited | 0.1535 | 0.1916 | 0.1938 | 0.1893 |
| 3TC7 ours (2026-09-07 model, no hydrogens) | 0.1468 | 0.1842 | 0.1886 | 0.1798 |
| 3TC7 ours (2026-09-09 model, riding hydrogens, D488; `verify_20260909/`) | 0.1352 | 0.1728 | 0.1782 | 0.1673 |
| 3TC7 PDB-REDO final | 0.1689 | 0.1873 | 0.1879 | 0.1867 |
| 3QUE deposited | 0.2151 | 0.2879 | 0.2858 | 0.2901 |
| 3QUE ours | 0.2113 | 0.2597 | 0.2544 | 0.2652 |
| 3QUE PDB-REDO final | 0.2269 | 0.2720 | 0.2628 | 0.2815 |
| 7KR0 deposited | 0.1103 | 0.1174 | 0.1159 | 0.1189 |
| 7KR0 ours (2026-09-07 model) | 0.1050 | 0.1137 | 0.1118 | 0.1156 |
| 7KR0 ours (2026-09-09, first 15-macro-cycle pass, D489; `verify_20260909/`) | 0.1043 | 0.1130 | 0.1107 | 0.1154 |
| 7KR0 ours (2026-09-09, second 15-macro-cycle pass, D493; `verify_20260909/`) | 0.1040 | 0.1128 | 0.1104 | 0.1152 |
| 7KR0 ours (2026-09-09, third 15-macro-cycle pass, D494; `verify_20260909/`) | 0.1036 | 0.1126 | 0.1103 | 0.1148 |
| 7KR0 PDB-REDO final (hydrogens stripped) | 0.1249 | 0.1318 | 0.1288 | 0.1348 |
| 7KR0 operator six-copy ensemble | 0.0514 | 0.0673 | 0.0665 | 0.0681 |

PDB-REDO models are REFMAC-refined; rescoring them in Phenix is not neutral (3TC7's REFMAC header is
0.1776), so the comparison holds only under the campaign's scorer.
