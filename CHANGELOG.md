# Changelog

## 2026-10-22 — the citation of the method

The README now says what the repository is (in development) and where the method comes from: the agent was directly
prompted to follow a procedure based on the preprint of Passmore et al. (2026), with PDB 44PS as the reference model,
complemented with additions for an agentic workflow. The citation is in the README, in `docs/METHOD.md` and in
`CITATION.cff` (as the preferred citation). Every card carries one attribution line; the 7KR0 card compares the release
with 44PS on the same free set. The long harness description in the README is shortened.

## 2026-10-21 (d) — history flattened to one commit for the public release

At the operator's direction the repository's history was rewritten: one commit now holds the tree of `main` as it
stood after the release of the re-refined baseline (merge cb44d01). The earlier campaign's materials, the `release-*`
branches and every commit before this point are no longer in the repository; a private bundle holds them. One text
change beside the flattening: the operator's note in `targets/7KR0/refinement/run.json` no longer names a person. The
entries below describe the history that was flattened; their pull-request numbers and branch names refer to it.

## 2026-10-21 (c) — the re-refined baseline and the full geometry set

From the meeting of 2026-10-21: every comparison is now against the re-refined deposited model (S0001, the deposited
model after the common recipe), not the deposited model as scored; every score, the geometry included, is reported for
the baseline and for the released model. Each target gains `model/<ID>_S0001.pdb`, `refinement/S0001/` and `S0000/`
(facts and score records) and the baseline's clashscore, rotalyze and ramalyze logs under `validation/`. The cards
show the three models (S0000, S0001, released) side by side with clashscore, rotamer outliers, Ramachandran outliers
and favoured, bond and angle RMSD, MolProbity score, copies, atoms, waters and ANISOU counts. The README has two tables,
R-free and geometry, both re-refined → ours. `index.json` carries the same score block for the three models and the
status is against S0001. `scripts/write_cards.py` now writes the 7KR0 card too.

## 2026-10-21 — seven targets added: the hierarchical line's first full snapshot

Seven targets from the hierarchical refinement harness join 7KR0 (R-free on our flags, released / deposited): 8C5N
(0.75 Å, six-copy ensemble, 0.0908 / 0.1571), 7R2H (0.79 Å, six copies, 0.0993 / 0.1551), 9ARN (1.41 Å, single model,
0.2769 / 0.2944), 3TC7 (1.5 Å, six copies from the gap fork T431c8e_gap, 0.1475 / 0.1918), 1LZ8 (1.53 Å, two copies
with two chlorides, 0.2408 / 0.2826), 4QO4 (1.7 Å, single model with sulfates and the built loop 69 to 72, 0.2747 /
0.3133) and 3QUE (2.7 Å, single model under reference-model restraints to 3LFF, 0.2642 / 0.2901). Each comes with its
map coefficients from the work reflections, the working data and flags, the deposited model, the full step record, the
chain scripts with their logs, and the validation logs. The 7R2H and 8C5N runs were still going at export. The 3TC7
card states the fork's looser gap bounds and the main run's best under the standing bounds (S0042, 0.1540), whose
record ships beside it. No vault has been read in these runs. `scripts/write_cards.py` wrote the seven cards, the
README rows and the `provenance.json` entries from the files; `scripts/build_index.py` rebuilt the index and manifest.

Later the same day, at the operator's direction, `manzuoni/refinement` was merged into `main`: `main` now carries the
hierarchical line (eight targets). The earlier campaign's targets stayed on the `release-*` branches until the history
was flattened the same evening (entry (d)).

## 2026-10-19 — branch manzuoni/refinement: the hierarchical line starts here

One target, 7KR0, from the hierarchical refinement harness (`prism-science/agentic-refinement`, branch
`manzuoni/hierarchical_refinement`): the six-copy ensemble in force at step S0053 (R-free 0.0726 on the deposited flags;
the deposited model 0.1175 on the same flags), with its map coefficients from the work reflections, the working data and
flags, the deposited model, the full step record (54 steps, 15 accepted) and the validation logs. The earlier campaign's
five targets, the ensemble representations, the campaign documents and the pod scripts are removed from this branch;
they stay on `main` and the `release-*` branches. New `scripts/build_index.py` writes `index.json` and the manifest from
the new layout. README, METHOD and HOW_TO_USE rewritten for the new line.

## 2026-10-10 (b) — D582 caveat: free reflections in the decision maps

No file changes beyond text. Every ensemble R-free in `representations/7KR0/` (E035, E041, E048, E049) and the campaign's
single-model numbers were obtained with maps that included the free reflections (the mmtbx / phenix default). E050 measured
+0.0016 R-free of genuine leakage on one pick with R-work unchanged. Caveat added to the README tables; clean reruns E051–E053
are running and will replace the rows.

## 2026-10-09 — E048 / E049 blind replications (runs in progress)

`representations/7KR0/models/` gains the model in force at the end of each round of E049 (`scripts/portable/sixcopy_waters.py`
in the campaign repository, one phenix.python file, run blind from the deposited 7KR0): `E049_r1_aniso_water.pdb` 0.0856,
`E049_r2_aniso_water.pdb` 0.0789, `E049_r3_pick_cleanup.pdb` 0.0756, `E049_r4_pick.pdb` 0.0749 full R-free (independent scorer,
frozen flags), all with clashscore ≤ 4.9 and rotamer outliers ≤ 1.3 %; and `E048_r2_aniso_water.pdb` (the E044 harness driver
on the same start, 0.0838 after round 2). Trajectories under `representations/7KR0/trajectories/{e049_portable,e048_autosix}`.
Both runs were still going; the rows will be replaced by the final models. Every earlier row re-scored by the same scorer
(unchanged to five decimals). No single-model target changed.

## 2026-10-05c — E041 line R six-copy models added

`representations/7KR0/models/` gains the E041 line R models built from 7KR0: `E041_R4_S.pdb` (0.0680 full R-free, clashscore 26.7),
`E041_CJ_R4_p2.pdb` (after two clash-cleanup passes: 0.0689, clashscore 4.5) and `E041_CJ_R4_polish.pdb` (0.0690, clashscore 4.4), each
scored by the independent scorer on the frozen flags. `scripts/indep_rfree.py` updated to the campaign's split-aware scorer (E047);
the staging guard pins its new checksum. No single-model target changed.

## 2026-10-05 (b) — 7R2H and 8C5N added

Snapshot exported from the pod at 2026-10-05T08:15:10Z (`provenance.json`); release-time validation re-run on all five targets.
New: 7R2H (cyclophilin D, 0.79 Å) and 8C5N (CbpD, 0.75 Å), onboarded 2026-10-05 for the campaign's six-copy ensemble line (E044).
Both are released as their re-refined baselines, nothing credited:

- 7R2H: deposited 0.1546 → 0.1290 full R-free on the deposited free set (independent scorer); ten-seed re-refinement mean 0.1289.
  The gain is the protocol refining the 335 isotropic deposited waters anisotropically; the gap widens 0.011 → 0.014; rotamer
  outliers 0.00 → 0.73 %.
- 8C5N: deposited 0.1570 → 0.1533 (independent scorer); ten-seed mean 0.1533. Scored against the deposited amplitudes, not the
  intensities (campaign row D540). Rotamer outliers 2.3 % in both, above the campaign's cap.

3TC7, 3QUE and 7KR0: models unchanged; their ledger extracts and 3QUE's campaign noise floors refreshed (E043's fixed-weight
floor added under `validation/campaign/`).

## 2026-10-05 — canonical set only

The release now holds the campaign's canonical set: 3TC7, 3QUE and 7KR0. The other thirteen targets (1L6X, 1LZ9, 1N7E, 1V2X,
3DUT, 4QO4, 6CDX, 6UDY, 7DVR, 8IS2, 9ARN, 9D5U, 9D5Y) were removed from `targets/`; they remain in the 2026-10-03 release
(branch `release-20261003`). 7R2H and 8C5N, two ultra-high-resolution entries for the six-copy ensemble line, will be added
once onboarded. No model or number of the three kept targets changed.

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
