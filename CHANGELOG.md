# Changelog

## 2026-10-03 — 3TC7 and 3QUE refreshed; 7KR0 ensemble representations added

Snapshot of the standing records exported from the pod at 2026-10-03T18:36:33Z (`provenance.json`); release-time validation re-run
on all sixteen targets. Two records moved, both written by the campaign's graph search on 2026-10-03. On both, the held-back
report half improved little or not at all:

- 3TC7: full R-free 0.17276 → 0.17161 (ledger), report 0.16726 → 0.16769 (worse). Rotamer outliers 1.59 % at release time,
  above the campaign's 1.5 % cap. Campaign rows D517, D519.
- 3QUE: full R-free 0.25891 → 0.25246 (ledger), report 0.26441 → 0.26334. The intermediate record of D520 (report 0.25983) was
  superseded by a promotion that raised report by 0.0035; no decision row covers it yet. Rotamer outliers 4.29 % at release
  time (previous model 3.96 %). Campaign rows D518–D520.

The other fourteen models are unchanged; their validation logs were re-run. Caveats on the 3TC7, 3QUE and 7KR0 cards updated.

New section `representations/7KR0/`: the campaign's replication of Passmore et al. 2026 (Untangler, E035 → E035f → E035c →
E035d), six six-copy models with map coefficients, every model in its table re-scored with the independent scorer on
2026-10-03, stage trajectories and provenance. Not a released model (PROTOCOL §18.1). Reference: 44PS on the same flags 0.06566.

Scripts: `pull_from_pod.sh` now releases only the targets already in `targets/` (`AGRP_TARGETS` overrides) and no longer loses
chunks after the first (the chunk loop's `actl pod exec` read the rest of the chunk list from stdin); new
`pull_representations.sh`, `stage_representations_on_pod.py`, `build_representations.py`; `MANIFEST.sha256` covers
`representations/`. Campaign documents re-snapshotted at commit a590c774ea530eef2ebcbad4c2b58857aec1e062, adding
SPEC_GRAPH_SEARCH.md and thresholds_v9.yaml.

## 2026-09-29 — first release

Snapshot of the campaign's standing records as exported from the pod at 2026-09-29T16:09:02Z. Sixteen targets: 3TC7, 3QUE and
7KR0 from phase 1 (records of 2026-09-09 and 2026-08-28) and the thirteen phase-2 targets (records of 2026-09-17).
Release-time validation (independent scorer, phenix.model_vs_data, phenix.molprobity) run on the deposited and
released model of every target at export. Campaign documents snapshotted from prism-science/agentic-refinement at
commit f19b78076cefb62e21fc2cfefda03fd816164dfc.
