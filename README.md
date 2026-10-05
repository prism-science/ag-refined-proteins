# ag-refined-proteins

Crystallographic models re-refined by an autonomous agent (the *autoresearch* campaign, Astera Institute, August–October
2026), released with everything needed to use, check and extend them: the model, the map coefficients, the frozen data
and free-reflection flags it was scored on, the deposited model it started from, the verbatim refinement command, a
uniform release-time validation, and the campaign's complete per-target decision log.

Three PDB entries, the campaign's canonical set: 3TC7 (1.5 Å), 3QUE (2.7 Å) and 7KR0 (0.77 Å). All three released models
have a lower R-free than the deposited file on the same free set. Two more ultra-high-resolution entries, 7R2H (cyclophilin D,
0.79 Å) and 8C5N (CbpD, 0.75 Å), are being onboarded for the six-copy ensemble line and will be added with their baselines.
The thirteen other targets of the August–September campaign are in the 2026-10-03 release (branch `release-20261003`).
Nothing here is a ceiling: the campaign is still running and this repository is a dated snapshot of its standing records.

## Results

Every model is scored on the R-free flags inherited unchanged from its deposition, so all numbers in a row are on the
same held-out reflections. Columns: the deposited coordinate file recomputed on those flags; the mean of ten
independent Phenix re-refinements of the deposited file with nothing changed (what re-refinement alone gives); the
released model; the change in full R-free against each of those two; MolProbity clashscore and rotamer outliers from
the release-time validation; status. "Full" is the whole free set; "report" is the half the campaign never used for
decisions (see *Method*). Every number is read from a file in `targets/<ID>/` by `scripts/build_index.py`.

<!-- results-table:begin -->
| Target | Res. (Å) | Entry | Deposited, our flags (full / report) | Re-refined, no changes (mean of 10) | This release (full / report) | Δ full: vs deposited / beyond re-refinement | Clashscore, rotamer outliers % (deposited → ours) | Status |
|---|---|---|---|---|---|---|---|---|
| [3TC7](targets/3TC7/README.md) | 1.5 | Crystal Structure of Engineered Protein. Northeast Structural… | 0.1916 / 0.1893 | 0.1885 | **0.1717 / 0.1677** | -0.0200 / -0.0168 (-8.2σ) | 2.9, 1.4 → 2.5, 1.6 | improved |
| [3QUE](targets/3QUE/README.md) | 2.7 | Human p38 MAP Kinase in Complex with Skepinone-L | 0.2879 / 0.2901 | 0.2668 | **0.2533 / 0.2642** | -0.0346 / -0.0135 (-8.0σ) | 10.6, 7.6 → 2.8, 4.3 | improved |
| [7KR0](targets/7KR0/README.md) | 0.77 | Crystal structure of SARS-CoV-2 NSP3 macrodomain (C2 crystal… | 0.1174 / 0.1189 | 0.1163 | **0.1125 / 0.1147** | -0.0048 / -0.0038 (-15.9σ) | 4.7, 0.9 → 6.7, 1.3 | improved |
<!-- results-table:end -->

Status meanings:

- **improved**: a credited change moved the standing model and its full R-free is below the deposited model's.
- **re-refined baseline, nothing credited**: the released model is one Phenix re-refinement of the deposited file. The
  gain over the deposited value is what phenix.refine does on its own, not the agent's work. 7R2H and 8C5N will enter
  with this status.

Changed on 2026-10-03 (3TC7 and 3QUE; records written by the campaign's graph search). On both, the held-back report half,
the unbiased estimate, improved little or not at all; the full-set gain sits mostly on the select half the search consults
(campaign row D519):

- **3TC7**: full R-free 0.17276 → 0.17161, but report 0.16726 → 0.16769 (worse; ledger values). Rotamer outliers 1.59 % at
  release time, above the campaign's 1.5 % cap (D517).
- **3QUE**: full R-free 0.25891 → 0.25246, report only 0.26441 → 0.26334 (ledger values). The record before this one (D520) had
  report 0.25983; the promotion that wrote this model lowered full by 0.0004 and raised report by 0.0035 (D518–D520). Rotamer
  outliers 4.29 % at release time (3.96 % in the previous model, 7.59 % deposited; the campaign calls them pre-existing).

Read each target's card (`targets/<ID>/README.md`) before quoting it. The cards carry the caveats the campaign attached to
its own numbers: 7KR0's geometry is above the campaign's own caps, 3QUE's deposited header R-free is a REFMAC number, and so on.

## Ensemble representations

Six-copy ensemble models of the 7KR0 data, from the campaign's replication of Passmore et al. 2026 (connectivity optimization
with Untangler). They are a second representation of the same data, not a released model, and not comparable column for column
with the table above (campaign PROTOCOL §18.1). All numbers are full R-free on the same frozen flags (8 712 free reflections, identical
to the deposited sets of 7KR0 and 44PS).

| Model | Full / report R-free | R-work | Water atoms | Clashscore | Rotamer outliers |
|---|---|---|---|---|---|
| 7KR0 deposited, single model | 0.1174 / 0.1189 | | | 4.7 | 0.9 % |
| 7KR0 released, single model (`targets/7KR0/`) | 0.1125 / 0.1147 | | | 6.7 | 1.3 % |
| E035d, six copies, anisotropic (`representations/7KR0/`) | 0.0879 / 0.0901 | 0.0751 | 1 305 | | |
| E041 line R, six copies (best, not in this release) | 0.0680 / 0.0694 | 0.0457 | 3 198 | 26.7 | 3.0 % |
| E041 line X, 44PS extended (not in this release) | 0.0643 / 0.0649 | 0.0445 | | 5.2 | 2.0 % |
| 44PS deposited (Passmore et al.) | 0.0657 / 0.0660 | 0.0485 | 2 581 | 2.2 | 2.0 % |

- **E035** ran the paper's pipeline as published. Its models are in `representations/7KR0/`, with their own README, per-stage table
  and caveats.
- **E041 line R** starts from the deposited 7KR0 model. Water is the main lever: conformation-aware water picking, where each
  water copy has to clear only its own conformer, then anisotropic waters, then a looser geometry weight with a weaker B-factor
  restraint. Each gain was measured against a paired control from the same model. Line R ends 0.0023 above 44PS.
- **Line R's geometry is not depositable yet.** Its clashscore of 26.7 comes mostly from water copies touching riding hydrogens of
  their own conformer. A clash cleanup is running. The line R models will be added here once they pass the geometry caps.
- **E041 line X** starts from 44PS itself, so it extends the authors' model and does not count as a replication.
- Numbers for E041 come from the campaign ledger, scored by the harness evaluator, not yet by this release's independent scorer.

## What is in a target directory

```
targets/<ID>/
  README.md                       the card: numbers, geometry, what changed, caveats, provenance, file list
  model/<ID>_refined.{cif,pdb}    the released model
  maps/<ID>_refined_map_coeffs.mtz  2mFo-DFc / mFo-DFc coefficients from the run that wrote the model
  data/<ID>_data.mtz              frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN)
  data/<ID>_flags.mtz             frozen R-free flags (R-free-flags, 0 = free), identical to the deposited free set
  data/<ID>_split.mtz, split.json the select/report halves of the free set
  data/prep.json                  how the data files were built, with SHA-256 of the source structure factors
  deposited/<ID>.cif              the deposited model as fetched from RCSB, plus the entry record and sequence
  refinement/                     command.txt (verbatim argv), .eff, .log, decisions and result of the run
  validation/release/             independent scorer, phenix.model_vs_data and phenix.molprobity on both models
  validation/campaign/            the campaign's own noise floor, verification runs, gate checks, dossier
  ledger/                         every cycle, every proposed change, bisections, deviations, per-run DECISIONS.md
```

`index.json` holds the same information for all targets in one machine-readable file. `MANIFEST.sha256` lists every
released file; `scripts/verify_checksums.sh` checks them.

## Use

Open a model with its maps:

```bash
coot targets/3TC7/model/3TC7_refined.pdb --auto targets/3TC7/maps/3TC7_refined_map_coeffs.mtz
```

Recompute R-free on the frozen flags (needs Phenix; the scorer shares no code with the campaign harness):

```bash
phenix.python scripts/indep_rfree.py targets/3TC7/model/3TC7_refined.cif targets/3TC7/data/3TC7_data.mtz \
  targets/3TC7/data/3TC7_flags.mtz targets/3TC7/data/3TC7_split.mtz out.json
```

Continue refining on the same free set (the only way to compare with the numbers here):

```bash
phenix.python scripts/merge_mtz.py targets/3TC7/data/3TC7_data.mtz targets/3TC7/data/3TC7_flags.mtz 3TC7.mtz
phenix.refine targets/3TC7/model/3TC7_refined.cif 3TC7.mtz \
  refinement.input.xray_data.r_free_flags.label=R-free-flags \
  refinement.input.xray_data.r_free_flags.test_flag_value=0
```

The verbatim command that produced each model, including its per-target overrides, is `targets/<ID>/refinement/command.txt`.
Details, including how to reproduce a whole run from raw data: `docs/HOW_TO_USE.md`.

## Method

One paragraph; the rest is in `docs/METHOD.md` and the campaign documents under `docs/campaign/`. The agent starts from
the deposited model and the deposited structure factors, freezes the data and the deposited free-reflection set, and
measures a noise floor (ten re-refinements with different seeds). It then proposes local changes (water additions and
removals, alternate conformations, peptide flips, rotamer fixes, zone real-space refinement, refinement-protocol changes),
gates each on local density support, geometry and altloc-aware clashes, and judges every kept set of changes in a paired
cycle: the same base refined with and without the changes, same seed. A cycle is credited only when the attributable
change in R-free on the consulted half of the free set is beyond k·σ of the noise floor, the held-back half agrees, and
the R-free − R-work gap does not widen. The released model is the standing record after the last credit. The campaign's
own acceptance rule changed under it on 2026-09-17 (sham-null acceptance, PROTOCOL §4.4); every verdict in this release
is a k·σ verdict, disclosed as decision D507.

## Caveats that apply to every target

- R-free is comparable only on the same free set. The deposited header values are not on these flags (and 3QUE's is from
  a different program). Compare against the "deposited, our flags" column, never the header.
- The re-refinement column is the mean of ten seeds of one 5-macro-cycle Phenix re-refinement. For models deposited from
  CNS, REFMAC or X-PLOR that measures convergence variance rather than test-set noise (D506), which is why several
  legacy targets credited nothing even though re-refinement alone moved them a lot.
- MolProbity numbers are from `phenix.molprobity` with default settings at release time, on the file as released
  (hydrogens kept where the model has them). The campaign's own altloc-aware clashscore is a different metric and is
  in the ledger rows.
- 7KR0's released model exceeds the campaign's own frozen geometry caps (rotamer outliers 1.5 %, clashscore 5.0);
  the deposited multiconformer model already exceeds the clashscore cap. Depositable by ordinary standards, not by
  the campaign's bar.

## Provenance

`provenance.json` records when the snapshot was taken from the campaign pod, the Phenix build (2.1-6048, the campaign's
single pinned image), the ledger hash and row counts, and every standing record as it stood. Each card names the pod
path of its model, the run and cycle that wrote it, and the thresholds version that judged it. The campaign repository
(`prism-science/agentic-refinement`) holds the harness code and the living documents; `docs/campaign/SNAPSHOT.md` gives
the commit these snapshots were taken from.

## Refreshing this release

`scripts/pull_from_pod.sh` stages a new snapshot on the campaign pod (`scripts/stage_on_pod.py`: copy, validate, hash,
tar), transfers it in verified chunks, extracts it here and rebuilds the cards, `index.json` and `MANIFEST.sha256` with
`scripts/build_index.py`. Commit the result with the export timestamp in the message and add a line to `CHANGELOG.md`.
`scripts/pull_representations.sh` does the same for `representations/7KR0/` (`scripts/stage_representations_on_pod.py` on the
pod, `scripts/build_representations.py` here).

## Licence and citation

Models, maps, records and documentation: CC BY 4.0. Scripts: MIT. Deposited files under `targets/<ID>/deposited/` and the
structure-factor data they were built from are wwPDB data (CC0); cite the original entry and its primary citation, which
each card lists. To cite this release, see `CITATION.cff`.
