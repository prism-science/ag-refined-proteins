#!/usr/bin/env python3
"""Build index.json and MANIFEST.sha256 from targets/. Run from the repository root; no dependencies beyond Python 3.

For each targets/<ID>/ the index records the entry (from deposited/rcsb_entry.json), the data (from data/prep.json),
the released step (the one folder under refinement/, its FACTS.txt and score.json) and the deposited model's score
(the S0000 row of refinement/score_history.jsonl). The results table in README.md is written by hand; this script
checks that its numbers agree with the index and says so."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load(p: Path, default=None):
    return json.loads(p.read_text()) if p.exists() else default


def target_record(t: Path) -> dict:
    tid = t.name
    entry = load(t / "deposited" / "rcsb_entry.json", {})
    prep = load(t / "data" / "prep.json", {})
    steps = sorted(d for d in (t / "refinement").iterdir() if d.is_dir() and re.match(r"^S\d{4}$", d.name))
    if not steps:
        raise SystemExit("%s: no released step under refinement/" % tid)
    step = steps[-1]
    score = load(step / "score.json", {})
    after = score.get("after", {})
    facts = (step / "FACTS.txt").read_text().strip() if (step / "FACTS.txt").exists() else ""
    deposited = {}
    jl = t / "refinement" / "score_history.jsonl"
    if jl.exists():
        for ln in jl.read_text().splitlines():
            rec = json.loads(ln)
            if rec.get("step") == "S0000":
                deposited = rec.get("metrics", {})
    if not deposited:
        # a record whose jsonl starts after S0000 (7KR0): the facts line of S0000 in score_history.txt carries the numbers
        txt = t / "refinement" / "score_history.txt"
        for ln in (txt.read_text().splitlines() if txt.exists() else []):
            if ln.startswith("S0000 "):
                m = re.search(r"R-free ([0-9.]+) R-work ([0-9.]+) gap ([0-9.]+) clash ([0-9.]+) rota ([0-9.]+) %", ln)
                if m:
                    deposited = {"r_free": float(m.group(1)), "r_work": float(m.group(2)), "gap": float(m.group(3)),
                                 "clashscore": float(m.group(4)), "rota_pct": float(m.group(5)), "source": "score_history.txt S0000 facts line"}
    cite = (entry.get("rcsb_primary_citation") or {})
    return {
        "id": tid,
        "title": (entry.get("struct") or {}).get("title"),
        "resolution_a": ((entry.get("rcsb_entry_info") or {}).get("resolution_combined") or [None])[0],
        "initial_release_date": (entry.get("rcsb_accession_info") or {}).get("initial_release_date"),
        "primary_citation": {k: cite.get(k) for k in ("title", "journal_abbrev", "year", "pdbx_database_id_DOI", "pdbx_database_id_PubMed")},
        "data": {k: prep.get(k) for k in ("data_labels", "n_reflections", "n_free", "n_work", "n_select", "n_report", "d_min",
                                           "data_mtz_sha256", "flags_mtz_sha256")},
        "released_step": step.name,
        "facts": facts,
        "released": {k: after.get(k) for k in ("r_free", "r_work", "gap", "r_free_select", "r_free_report", "clashscore", "rota_pct",
                                                "rama_outliers_pct", "rama_favored_pct", "bond_rmsd", "angle_rmsd", "n_atoms", "n_h",
                                                "n_water_atoms", "water_occ_sum", "n_anisou", "copies", "altlocs")},
        "deposited_on_our_flags": {k: deposited.get(k) for k in ("r_free", "r_work", "gap", "r_free_select", "r_free_report", "clashscore",
                                                                  "rota_pct", "n_atoms", "n_water_atoms")},
        "status": "improved" if (after.get("r_free") is not None and deposited.get("r_free") is not None and after["r_free"] < deposited["r_free"]) else "not below deposited",
        "files": {str(p.relative_to(ROOT)): sha256(p) for p in sorted(t.rglob("*")) if p.is_file()},
    }


def main() -> int:
    targets = [target_record(t) for t in sorted((ROOT / "targets").iterdir()) if t.is_dir()]
    index = {"name": "ag-refined-proteins", "generated_by": "scripts/build_index.py", "n_targets": len(targets),
             "line": "hierarchical refinement (C-copy ensembles), prism-science/autoresearch branch manzuoni/hierarchical_refinement",
             "targets": targets}
    (ROOT / "index.json").write_text(json.dumps(index, indent=1) + "\n")
    lines = []
    for p in sorted(ROOT.rglob("*")):
        rel = p.relative_to(ROOT)
        if not p.is_file() or rel.parts[0] in (".git", "scripts", "__pycache__") or rel.name in ("MANIFEST.sha256",):
            continue
        lines.append("%s  %s" % (sha256(p), rel))
    (ROOT / "MANIFEST.sha256").write_text("\n".join(lines) + "\n")
    readme = (ROOT / "README.md").read_text()
    for t in targets:
        rf = t["released"]["r_free"]
        if rf is not None and ("%.4f" % rf) not in readme:
            print("README: the results table does not show %.4f for %s" % (rf, t["id"]))
    print("index.json: %d target(s); MANIFEST.sha256: %d files" % (len(targets), len(lines)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
