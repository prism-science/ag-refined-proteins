#!/usr/bin/env python3
"""Build the table in representations/<ID>/README.md and representations/<ID>/provenance.json from the staged files.

Every number in the table is read from representations/<ID>/scores/<row>.json (independent scorer) and
<row>.composition.json (atom, water and occupancy counts), both written on the pod by scripts/stage_representations_on_pod.py.
The row list and pod paths come from provenance_pod.json.

    python3 scripts/build_representations.py            # rebuild
    python3 scripts/build_representations.py --check    # exit 1 if a generated file would change
Set AGRP_CAMPAIGN_REPO to the campaign checkout (default ../autoresearch) to record its commit.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BEGIN, END = "<!-- rep-table:begin -->", "<!-- rep-table:end -->"


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def f4(x) -> str:
    return "—" if x is None else f"{x:.4f}"


def f5(x) -> str:
    return "—" if x is None else f"{x:.5f}"


def table(d: Path, prov: dict) -> str:
    L = ["| Stage | Arm | Model | R-free full | select | report | R-work | Gap | Atoms (H) | Copies × protein occ. | Water atoms | Σ water occ. | ANISOU | File |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in prov["rows"]:
        s = json.loads((d / r["score_json"]).read_text())
        c = json.loads((d / r["composition_json"]).read_text())
        gap = s["r_free_manual"] - s["r_work_manual"]
        occ = c["protein_occupancy_per_copy"]
        alts = [k for k in occ if k != "_"]
        if alts:
            vals = sorted({round(occ[k], 3) for k in alts})
            copies = f"{len(alts)} × {'/'.join(f'{v:.3f}' for v in vals)}"
        else:
            copies = "1 (single model)"
        if r["stage"] == "context" and alts:
            copies = f"multiconformer ({len(alts)} letters)"
        f = r.get("frozen_model")
        files = f"[{Path(f).name}]({f})" if f else "pod only"
        if r.get("frozen_mtz"):
            files += f", [map]({r['frozen_mtz']})"
        bold = r["stage"] == "reference"
        name = f"**{r['what']}**" if bold else r["what"]
        L.append(f"| {r['stage']} | {r['arm'] or '—'} | {name} | {f5(s['r_free_manual'])} | {f5(s['r_free_select_manual'])} | "
                 f"{f5(s['r_free_report_manual'])} | {f5(s['r_work_manual'])} | {f5(gap)} | {c['n_atoms']:,} ({c['n_hydrogen']:,}) | "
                 f"{copies} | {c['n_water_atoms']:,} | {c['water_occupancy_sum']:.1f} | {c['n_anisou']:,} | {files} |")
    return "\n".join(L)


def campaign_commit(prev: dict) -> dict:
    repo = Path(os.environ.get("AGRP_CAMPAIGN_REPO", ROOT.parent / "autoresearch"))
    try:
        sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, capture_output=True, text=True, check=True).stdout.strip()
        br = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repo, capture_output=True, text=True, check=True).stdout.strip()
        return {"repository": "prism-science/agentic-refinement", "commit": sha, "branch": br,
                "note": "local checkout the pod workspace syncs from; the pod copy is not a git repository"}
    except Exception:
        return prev.get("campaign", {})


def main() -> int:
    check = "--check" in sys.argv
    changed = []
    for d in sorted(p for p in (ROOT / "representations").iterdir() if p.is_dir()):
        prov = json.loads((d / "provenance_pod.json").read_text())
        outputs: dict[Path, str] = {}
        readme = d / "README.md"
        if readme.exists():
            txt = readme.read_text()
            if BEGIN in txt and END in txt:
                a, b = txt.index(BEGIN) + len(BEGIN), txt.index(END)
                outputs[readme] = txt[:a] + "\n" + table(d, prov) + "\n" + txt[b:]
        prev = json.loads((d / "provenance.json").read_text()) if (d / "provenance.json").exists() else {}
        files = [{"path": p.relative_to(d).as_posix(), "bytes": p.stat().st_size, "sha256": sha256(p)}
                 for p in sorted(x for x in d.rglob("*") if x.is_file() and x.name not in ("README.md", "provenance.json"))]
        out = {k: prov[k] for k in ("exported_at", "pod_hostname", "phenix_version", "untangler", "untangler_patch_scripts_sha256",
                                    "independent_scorer", "frozen_data", "merged_data_flags_mtz_used_by_untangler")}
        out["campaign"] = campaign_commit(prev)
        out["rows"] = [{k: r.get(k) for k in ("id", "stage", "arm", "what", "model", "model_sha256", "model_bytes", "frozen_model",
                                               "mtz", "mtz_sha256", "mtz_bytes", "frozen_mtz", "mtz_columns", "score_json", "composition_json")}
                       for r in prov["rows"]]
        out["files"] = files
        outputs[d / "provenance.json"] = json.dumps(out, indent=1) + "\n"
        for p, s in outputs.items():
            if not p.exists() or p.read_text() != s:
                changed.append(p)
                if not check:
                    p.write_text(s)
    for p in changed:
        print(("would change " if check else "wrote ") + str(p.relative_to(ROOT)))
    return 1 if (check and changed) else 0


if __name__ == "__main__":
    raise SystemExit(main())
