# 4QO4 — co-crystal structure of MDM2 (17-111) with compound 16, {(3R,5R,6S)-5-(3-CHLOROPHENYL)-6-(4-CHLOROPHENYL)-1-[(1S)-1-(6-CYCLOPROPYLPYRIDIN-2-YL)PROPYL]-3-METHYL-2-OXOPIPERIDIN-3-YL}ACETIC ACID

**Status: credited, not below deposited.** See the caveats below.

| | |
|---|---|
| Resolution | 1.7 Å |
| Space group | P 61 2 2 |
| Data | intensities (IMEAN,SIGIMEAN), 11011 reflections |
| Free set | 528 reflections (4.8 %), inherited unchanged from the deposition; select / report halves 264 / 264 |
| Deposited refinement program | CNS |
| Released | 2014-07-16 |
| Primary citation | Discovery of Potent and Simplified Piperidinone-Based Inhibitors of the MDM2-p53 Interaction. (ACS Med Chem Lett 2014), DOI 10.1021/ml500142b |
| Thresholds version that judged the writing cycle | thresholds_v8 |
| Phenix | 2.1-6048 |

## R-free on the frozen flags

Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, no outlier rejection) and with `phenix.model_vs_data`. "Re-refined, no changes" is the mean of the campaign's ten noise-floor seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.

| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |
|---|---|---|---|---|---|
| Deposited, our flags | 0.2629 | 0.3128 | 0.3087 | 0.3175 | 0.2627 / 0.3127 |
| Re-refined, no changes (10 seeds) | — | 0.3502 ± 0.00402 | — | — | — |
| **This release** | **0.2599** | **0.3243** | 0.3184 | 0.3307 | 0.2597 / 0.3248 |

Δ full R-free vs deposited: **0.0114**; beyond re-refinement alone: **-0.0259** (-6.4 × the floor's own spread).
Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `noise_floor`): σ_select 0.00187, σ_report 0.00670, σ_full 0.00402; a cycle is credited at ΔR-free-select ≤ -0.00374 (k = 2.0).
Campaign ledger for this model (`refinement/current.json`): R-work 0.2599, R-free full 0.3250, select 0.3187, report 0.3319.

## Geometry and composition (phenix.molprobity, release time, default settings)

| | Deposited | This release |
|---|---|---|
| Atoms (hydrogens) | 845 (0) | 826 (0) |
| Waters | 78 | 59 |
| Altloc letters | none | none |
| Clashscore | 16.02 | 4.49 |
| Ramachandran outliers / favored (%) | 0.00 / 97.7 | 0.00 / 98.8 |
| Rotamer outliers (%) | 6.02 | 2.41 |
| Cβ deviations | 0 | 0 |
| RMS bonds (Å) / angles (°) | 0.0106 / 1.56 | 0.0145 / 1.43 |
| MolProbity score | 2.38 | 1.52 |

## What changed in the coordinates

From `validation/release/model_diff.json` (deposited vs released, by chain and residue number):

- Waters added (2): A 5001, A 5002
- Waters removed (21): A 309, A 310, A 317, A 325, A 329, A 338, A 339, A 340, A 341, A 346, A 349, A 352, A 353, A 354, A 363, A 364, A 365, A 370, A 371, A 372, A 373

## What the campaign did

Refinement protocol of the released model: phenix.refine 2.1-6048, 5 macro-cycles, isotropic ADPs, no hydrogens in the model, seed 1. ADP decision: n_refl/n_atoms(non-H)=13.33 / d_min=1.7004: isotropic. The verbatim command is `refinement/command.txt`.

The released model was written by cycle 8 (`rerefine`, run `4QO4.20260917T052656Z`), verdict **accepted**, attributable ΔR-free-select -0.01270 against its paired null, ΔR-gap -0.00369.
That run ended: max_cycles=8 reached.

Cycles on record for this target: 12; credited: 3; changes proposed: 74 (`ledger/cycles.csv`, `ledger/changes.csv`).

Credited cycles on record, all runs and experiment lines. A credit is relative to that cycle's own paired null; not every credit moved the standing model (promotion rules D484/D499/D508), and experiment-line cycles judged candidates against their own base.

| Cycle | Run | Attributable ΔR-free-select | R-free full after | ΔR-gap vs null | Geometry flag |
|---|---|---|---|---|---|
| 1 | `4QO4.20260917T052656Z` | -0.00838 | 0.3596 | -0.00839 | rota_outliers 2.41 > 1.5 |
| 4 | `4QO4.20260917T052656Z` | -0.00717 | 0.3444 | -0.00796 | rota_outliers 2.41 > 1.5 |
| 8 | `4QO4.20260917T052656Z` | -0.01270 | 0.3250 | -0.00369 |  |

## Caveats

- Credited but still worse than the deposited file recomputed on these flags: Phenix's default re-refinement of this CNS-refined model costs 0.037 in R-free and the run recovers 0.026 of it. The campaign reports this as a program artifact, not a result (D509, PROTOCOL §6).

## Verify it yourself

```bash
# independent scorer (cctbx; needs Phenix)
phenix.python scripts/indep_rfree.py targets/4QO4/model/4QO4_refined.cif targets/4QO4/data/4QO4_data.mtz \
  targets/4QO4/data/4QO4_flags.mtz targets/4QO4/data/4QO4_split.mtz out.json
# standard tool
phenix.python scripts/merge_mtz.py targets/4QO4/data/4QO4_data.mtz targets/4QO4/data/4QO4_flags.mtz 4QO4_merged.mtz
phenix.model_vs_data targets/4QO4/model/4QO4_refined.cif 4QO4_merged.mtz
# look at it
coot targets/4QO4/model/4QO4_refined.pdb --auto targets/4QO4/maps/4QO4_refined_map_coeffs.mtz
```

## Provenance

- Campaign record `refinement/current.json`: cycle 8, stage `rerefine`, updated 2026-09-17T08:16:13+00:00.
- Model on the campaign pod: `/home/dev/runs/4QO4/runs/4QO4.20260917T052656Z/cycles/c008/escape/candidate_arm/refine_001.cif`.
- Data: `data.mtz` SHA-256 `487de5e62c315a2ed9d6f7b2c739d592421b4ed0a26d8ebfea808eac69190776`, `flags.mtz` SHA-256 `a3862cf320bf7b8e0e8c1f748ed9c6edd8c39454cd7c12b43acde9a9862ba7e7`; built from the deposited structure-factor file with SHA-256 `f62ef89b85ffd72aeb08d942fe49ba0ef503d0dded4450c5f77df2fb1d8a6cb3` (`data/prep.json`).
- Deposited header claim: R-work 0.264, R-free 0.302, 528 free reflections.

## Files

| File | Size | What it is |
|---|---|---|
| `data/4QO4_data.mtz` | 223,340 | The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors. |
| `data/4QO4_flags.mtz` | 179,216 | The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free). |
| `data/4QO4_split.mtz` | 179,216 | The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work). |
| `data/prep.json` | 3,530 | How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims. |
| `data/split.json` | 15,698 | The same split as a list of reflections, with the seed that made it. |
| `deposited/4QO4.cif` | 133,368 | The deposited coordinate file as fetched from RCSB (the starting point). |
| `deposited/4QO4.fasta` | 166 | The entry's sequence as fetched from RCSB. |
| `deposited/FETCHED` | 76 | When the raw files were fetched. |
| `deposited/fetch_manifest.sha256` | 756 | SHA-256 of the raw files at fetch time. |
| `deposited/rcsb_entry.json` | 10,756 | The RCSB entry record (title, citation, experimental details) as fetched. |
| `ledger/bisections.csv` | 1,346 | Bisection steps when a cycle regressed. |
| `ledger/changes.csv` | 265,993 | Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict. |
| `ledger/checks.csv` | 3,059 | Gate results G0–G8. |
| `ledger/cycles.csv` | 9,624 | Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry. |
| `ledger/defects.csv` | 97 | Values that could not be computed, with the reason (never a sentinel). |
| `ledger/deviations.csv` | 19,507 | Decision-log rows that name this target. |
| `ledger/noise_floor.csv` | 1,332 | The noise-floor row that set the credit bar: σ of R-free on every set. |
| `ledger/rfree_consultations.csv` | 226 | How many times R-free-select was consulted (PROTOCOL §3.6). |
| `ledger/runs/4QO4.20260917T052656Z/DECISIONS.md` | 38,464 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/4QO4.20260917T052656Z/run_summary.json` | 2,688 | The per-run summary (cycles, credits, stop reason). |
| `ledger/solvent_disagreements.csv` | 120 | Phenix/Coot disagreements on solvent sites. |
| `maps/4QO4_refined_map_coeffs.mtz` | 730,944 | Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot). |
| `model/4QO4_refined.cif` | 95,392 | The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json. |
| `model/4QO4_refined.pdb` | 70,755 | The same model in PDB format, from the same run. |
| `refinement/command.txt` | 1,537 | The verbatim phenix.refine argv that wrote the model. |
| `refinement/current.json` | 469 | The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index. |
| `refinement/experiment_paired_cycle.json` | 6,357 | Record of the experiment cycle that produced this model (paired null control, geometry of both arms). |
| `refinement/model_vs_data.campaign.log` | 2,817 | phenix.model_vs_data as run by the campaign on this model. |
| `refinement/refine_001.eff` | 42,795 | The effective parameters of that run. |
| `refinement/refine_001.log` | 68,744 | The phenix.refine log of that run. |
| `refinement/refine_decisions.json` | 2,086 | The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels). |
| `refinement/refine_result.json` | 3,000 | The parsed result of that run (R factors, geometry, seed, wall clock). |
| `validation/campaign/checks/G3_4QO4.json` | 4,724 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/fetch_4QO4.json` | 2,207 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/dossier.json` | 61,502 | The campaign dossier: xtriage, model audit, composition hypothesis, baselines. |
| `validation/campaign/noise_floor.json` | 7,549 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/verify_20260917/4QO4_baseline_rerefine.json` | 655 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/4QO4_current.json` | 693 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/4QO4_deposited.json` | 630 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/release/merge_mtz.log` | 397 | Log of the data+flags merge used by model_vs_data. |
| `validation/release/model_diff.json` | 703 | Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens. |
| `validation/release/model_vs_data.deposited.log` | 2,132 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/model_vs_data.refined.log` | 3,009 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/molprobity.deposited.log` | 15,391 | phenix.molprobity with default settings. |
| `validation/release/molprobity.deposited.out` | 4,046 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.log` | 15,644 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.out` | 3,898 | phenix.molprobity with default settings. |
| `validation/release/rfree_indep.deposited.json` | 671 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.deposited.log` | 1,131 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.json` | 676 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.log` | 1,138 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/summary.json` | 2,593 | Release-time validation of the deposited and refined models (parsed from the logs beside it). |
