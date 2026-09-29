# ag-refined-proteins

Crystallographic models re-refined by an autonomous agent (the *autoresearch* campaign, Astera Institute, August–September
2026), released with everything needed to use, check and extend them: the model, the map coefficients, the frozen data
and free-reflection flags it was scored on, the deposited model it started from, the verbatim refinement command, a
uniform release-time validation, and the campaign's complete per-target decision log.

Sixteen PDB entries. Seven released models have a lower R-free than the deposited file on the same free set; one is
credited but still above the deposited file; eight are plain Phenix re-refinements of the deposited file because the
campaign credited no change on them. The table says which is which. Nothing here is a ceiling: the campaign is still
running and this repository is a dated snapshot of its standing records.

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
| [6CDX](targets/6CDX/README.md) | 1.0 | High-resolution crystal structure of fluoropropylated cystine… | 0.2258 / 0.2233 | 0.1901 | **0.1716 / 0.1725** | -0.0542 / -0.0184 (-36.9σ) | 9.6, 1.8 → 20.7, 1.7 | improved |
| [3TC7](targets/3TC7/README.md) | 1.5 | Crystal Structure of Engineered Protein. Northeast Structural… | 0.1916 / 0.1893 | 0.1885 | **0.1728 / 0.1673** | -0.0188 / -0.0157 (-7.7σ) | 2.9, 1.4 → 2.1, 0.8 | improved |
| [6UDY](targets/6UDY/README.md) | 1.7 | X-ray co-crystal structure of compound 5 with Mcl-1 | 0.2592 / 0.2655 | 0.2567 | **0.2479 / 0.2555** | -0.0113 / -0.0088 (-1.1σ) | 12.9, 1.1 → 4.2, 0.8 | improved |
| [3QUE](targets/3QUE/README.md) | 2.7 | Human p38 MAP Kinase in Complex with Skepinone-L | 0.2879 / 0.2901 | 0.2668 | **0.2597 / 0.2652** | -0.0283 / -0.0071 (-4.2σ) | 10.6, 7.6 → 3.7, 4.0 | improved |
| [7KR0](targets/7KR0/README.md) | 0.77 | Crystal structure of SARS-CoV-2 NSP3 macrodomain (C2 crystal… | 0.1174 / 0.1189 | 0.1163 | **0.1125 / 0.1147** | -0.0048 / -0.0038 (-15.9σ) | 4.7, 0.9 → 6.7, 1.3 | improved |
| [1N7E](targets/1N7E/README.md) | 1.5 | Crystal structure of the sixth PDZ domain of GRIP1 | 0.2746 / 0.2620 | 0.2474 | **0.2447 / 0.2437** | -0.0299 / -0.0027 (-3.0σ) | 13.3, 1.3 → 8.4, 1.3 | improved |
| [9D5U](targets/9D5U/README.md) | 1.35 | Nitrile hydratase S112A mutant | 0.2853 / 0.2917 | 0.2549 | **0.2532 / 0.2580** | -0.0321 / -0.0016 (-6.2σ) | 10.1, 0.3 → 4.5, 0.3 | improved |
| [4QO4](targets/4QO4/README.md) | 1.7 | co-crystal structure of MDM2 (17-111) with compound 16,… | 0.3128 / 0.3175 | 0.3502 | 0.3243 / 0.3307 | 0.0114 / -0.0259 (-6.4σ) | 16.0, 6.0 → 4.5, 2.4 | credited, not below deposited |
| [1L6X](targets/1L6X/README.md) | 1.65 | FC FRAGMENT OF RITUXIMAB BOUND TO A MINIMIZED VERSION OF THE… | 0.2794 / 0.2848 | 0.2427 | 0.2390 / 0.2410 | -0.0403 / -0.0037 (-0.6σ) | 11.8, 5.3 → 3.5, 3.1 | re-refined baseline, nothing credited |
| [9ARN](targets/9ARN/README.md) | 1.41 | Structure and interactions of HIV-1 gp41 CHR-NHR reverse… | 0.2952 / 0.2875 | 0.2983 | 0.2962 / 0.2908 | 0.0010 / -0.0021 (-0.6σ) | 1.6, 0.0 → 1.6, 1.5 | re-refined baseline, nothing credited |
| [9D5Y](targets/9D5Y/README.md) | 1.35 | Nitrile hydratase S112T mutant | 0.2888 / 0.2936 | 0.2347 | 0.2342 / 0.2412 | -0.0546 / -0.0005 (-2.6σ) | 11.1, 0.3 → 3.5, 1.1 | re-refined baseline, nothing credited |
| [8IS2](targets/8IS2/README.md) | 1.32 | Crystal structure of a polyketide aromatase/cyclase Abx(+)D… | 0.2756 / 0.2900 | 0.2666 | 0.2668 / 0.2827 | -0.0088 / 0.0002 (+0.3σ) | 1.5, 0.6 → 2.7, 0.6 | re-refined baseline, nothing credited |
| [7DVR](targets/7DVR/README.md) | 1.7 | Crystal structure of heme sensor protein PefR from… | 0.2948 / 0.2698 | 0.2871 | 0.2873 / 0.2710 | -0.0075 / 0.0003 (+0.4σ) | 7.0, 1.5 → 3.1, 0.7 | re-refined baseline, nothing credited |
| [3DUT](targets/3DUT/README.md) | 1.55 | The high salt (phosphate) crystal structure of deoxy hemoglobin… | 0.2881 / 0.2794 | 0.2532 | 0.2537 / 0.2442 | -0.0344 / 0.0005 (+1.3σ) | 15.9, 4.3 → 3.5, 2.6 | re-refined baseline, nothing credited |
| [1V2X](targets/1V2X/README.md) | 1.5 | TrmH | 0.2559 / 0.2658 | 0.2347 | 0.2354 / 0.2450 | -0.0204 / 0.0007 (+1.0σ) | 31.3, 5.7 → 13.1, 5.7 | re-refined baseline, nothing credited |
| [1LZ9](targets/1LZ9/README.md) | 1.7 | ANOMALOUS SIGNAL OF SOLVENT BROMINES USED FOR PHASING OF… | 0.2738 / 0.2649 | 0.2758 | 0.2822 / 0.2690 | 0.0084 / 0.0064 (+1.2σ) | 7.6, 2.8 → 3.5, 1.9 | re-refined baseline, nothing credited |
<!-- results-table:end -->

Status meanings:

- **improved**: a credited change moved the standing model and its full R-free is below the deposited model's.
- **credited, not below deposited**: a change was credited against the run's own paired null, but the model is still
  above the deposited file recomputed on these flags (4QO4: Phenix's default re-refinement of a CNS model costs more
  than the run recovers; a program artifact, not a result).
- **re-refined baseline, nothing credited**: the released model is one Phenix re-refinement of the deposited file. The
  gain over the deposited value is what phenix.refine does on its own, not the agent's work.

Read each target's card (`targets/<ID>/README.md`) before quoting it. The cards carry the caveats the campaign attached to
its own numbers: 7KR0's geometry is above the campaign's own caps, 6UDY's gain is within its noise floor, 3QUE's deposited
header R-free is a REFMAC number, and so on.

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

## Licence and citation

Models, maps, records and documentation: CC BY 4.0. Scripts: MIT. Deposited files under `targets/<ID>/deposited/` and the
structure-factor data they were built from are wwPDB data (CC0); cite the original entry and its primary citation, which
each card lists. To cite this release, see `CITATION.cff`.
