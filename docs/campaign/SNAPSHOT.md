# Campaign document snapshots

Copied verbatim from the campaign repository (prism-science/agentic-refinement) at commit
`a590c774ea530eef2ebcbad4c2b58857aec1e062` (branch `graph-search`) on 2026-10-03. The first release (2026-09-29) used commit
`f19b78076cefb62e21fc2cfefda03fd816164dfc`; PROTOCOL.md, SPEC.md, SPEC_DPDB_RUNS.md, SPEC_LOOP_V2.md and REPRODUCE.md are
unchanged between the two. They are frozen here so this release is self-contained; the living
versions are in that repository.

| File | What it is |
|------|------------|
| PROTOCOL.md | The operator's campaign brief: cross-validation rules, acceptance criteria, reporting rules. |
| SPEC.md | The harness implementation contract: layout, ledgers, stage algorithms, gates G0–G8. |
| SPEC_DPDB_RUNS.md | The per-run discrete driver that produced every deliverable here. |
| SPEC_LOOP_V2.md | The paired null-control cycle. |
| SPEC_GRAPH_SEARCH.md | The generation-based search that wrote the 2026-10-03 records of 3TC7 and 3QUE. |
| REPRODUCE.md | Reproduction levels 0–2 as written for the campaign (pod paths are the campaign's). |
| deviations.md | The campaign decision log, D001 onwards. Every caveat cited in a target card is a row here. |
| experiments.md | The campaign experiment register, E001 onwards. |
| ../thresholds/thresholds_v1..v9.yaml | The frozen acceptance thresholds. Each target card names the version its run used. |
