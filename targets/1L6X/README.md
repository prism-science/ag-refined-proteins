# 1L6X — FC FRAGMENT OF RITUXIMAB BOUND TO A MINIMIZED VERSION OF THE B-DOMAIN FROM PROTEIN A CALLED Z34C

**Status: re-refined baseline, nothing credited.** See the caveats below.

| | |
|---|---|
| Resolution | 1.65 Å |
| Space group | C 2 2 21 |
| Data | amplitudes (FP,SIGFP), 35198 reflections |
| Free set | 3500 reflections (9.9 %), inherited unchanged from the deposition; select / report halves 1750 / 1750 |
| Deposited refinement program | X-PLOR |
| Released | 2002-04-10 |
| Primary citation | Mapping of the C1q binding site on rituxan, a chimeric antibody with a human IgG1 Fc. (J.Immunol. 2000), DOI — |
| Thresholds version that judged the writing cycle | thresholds_v8 |
| Phenix | 2.1-6048 |

## R-free on the frozen flags

Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, no outlier rejection) and with `phenix.model_vs_data`. "Re-refined, no changes" is the mean of the campaign's ten noise-floor seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.

| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |
|---|---|---|---|---|---|
| Deposited, our flags | 0.2032 | 0.2794 | 0.2739 | 0.2848 | 0.2032 / 0.2788 |
| Re-refined, no changes (10 seeds) | — | 0.2427 ± 0.00585 | — | — | — |
| **This release** | **0.1881** | **0.2390** | 0.2371 | 0.2410 | 0.1881 / 0.2388 |

Δ full R-free vs deposited: **-0.0403**; beyond re-refinement alone: **-0.0037** (-0.6 × the floor's own spread).
Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `noise_floor`): σ_select 0.00548, σ_report 0.00622, σ_full 0.00585; a cycle is credited at ΔR-free-select ≤ -0.01096 (k = 2.0).
Campaign ledger for this model (`refinement/current.json`): R-work 0.1881, R-free full 0.2389, select 0.2366, report 0.2412.

## Geometry and composition (phenix.molprobity, release time, default settings)

| | Deposited | This release |
|---|---|---|
| Atoms (hydrogens) | 2430 (0) | 2430 (0) |
| Waters | 360 | 360 |
| Altloc letters | none | none |
| Clashscore | 11.84 | 3.45 |
| Ramachandran outliers / favored (%) | 0.00 / 98.7 | 0.00 / 100.0 |
| Rotamer outliers (%) | 5.33 | 3.11 |
| Cβ deviations | 0 | 0 |
| RMS bonds (Å) / angles (°) | 0.0112 / 1.61 | 0.0072 / 1.00 |
| MolProbity score | 2.14 | 1.51 |

## What changed in the coordinates

No residue added or removed and no alternate conformation changed: the released model is the deposited model re-refined (coordinates, ADPs and occupancies moved, nothing else). `validation/release/model_diff.json`.

## What the campaign did

Refinement protocol of the released model: phenix.refine 2.1-6048, 5 macro-cycles, isotropic ADPs with 8 TLS groups, no hydrogens in the model, seed 1. ADP decision: n_refl/n_atoms(non-H)=14.48 / d_min=1.6471: isotropic; TLS (d_min>=2.0 or chain>200 res). The verbatim command is `refinement/command.txt`.

The released model is the cycle-0 baseline: one phenix.refine run on the deposited file with nothing changed (`baseline_rerefine`). The run that followed credited no change, so the standing record never moved (D484).

Cycles on record for this target: 9; credited: 0; changes proposed: 51 (`ledger/cycles.csv`, `ledger/changes.csv`).

## Caveats

- Nothing was credited on this target; the released model is the single Phenix re-refinement of the deposited file (D484). For CNS/REFMAC/X-PLOR-era depositions the campaign's noise floor measures convergence variance rather than test-set noise, so its credit bar was effectively unreachable (D506). The gain over the deposited file is what phenix.refine does on its own.

## Verify it yourself

```bash
# independent scorer (cctbx; needs Phenix)
phenix.python scripts/indep_rfree.py targets/1L6X/model/1L6X_refined.cif targets/1L6X/data/1L6X_data.mtz \
  targets/1L6X/data/1L6X_flags.mtz targets/1L6X/data/1L6X_split.mtz out.json
# standard tool
phenix.python scripts/merge_mtz.py targets/1L6X/data/1L6X_data.mtz targets/1L6X/data/1L6X_flags.mtz 1L6X_merged.mtz
phenix.model_vs_data targets/1L6X/model/1L6X_refined.cif 1L6X_merged.mtz
# look at it
coot targets/1L6X/model/1L6X_refined.pdb --auto targets/1L6X/maps/1L6X_refined_map_coeffs.mtz
```

## Provenance

- Campaign record `refinement/current.json`: cycle 0, stage `baseline_rerefine`, updated 2026-09-17T07:15:35+00:00.
- Model on the campaign pod: `/home/dev/runs/1L6X/c000/baseline_rerefine/refine_001.cif`.
- Data: `data.mtz` SHA-256 `e884b8cc75a9586e6d143d8db80eaed22742d1ac8be856f396da3656f1fda9cf`, `flags.mtz` SHA-256 `94f092b8f93c06c3ed70622a734b19141f9a016f88e0f3741c17ee8434ffbd1f`; built from the deposited structure-factor file with SHA-256 `db6637918b292066d48d515f61bc8334da6699b2e10f7c37d0769b39a6c9f569` (`data/prep.json`).
- Deposited header claim: R-work 0.206, R-free 0.284, 3495 free reflections.

## Files

| File | Size | What it is |
|---|---|---|
| `data/1L6X_data.mtz` | 706,760 | The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors. |
| `data/1L6X_flags.mtz` | 565,888 | The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free). |
| `data/1L6X_split.mtz` | 565,888 | The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work). |
| `data/prep.json` | 3,249 | How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims. |
| `data/split.json` | 99,154 | The same split as a list of reflections, with the seed that made it. |
| `deposited/1L6X.cif` | 312,612 | The deposited coordinate file as fetched from RCSB (the starting point). |
| `deposited/1L6X.fasta` | 388 | The entry's sequence as fetched from RCSB. |
| `deposited/FETCHED` | 76 | When the raw files were fetched. |
| `deposited/fetch_manifest.sha256` | 756 | SHA-256 of the raw files at fetch time. |
| `deposited/rcsb_entry.json` | 20,140 | The RCSB entry record (title, citation, experimental details) as fetched. |
| `ledger/bisections.csv` | 246 | Bisection steps when a cycle regressed. |
| `ledger/changes.csv` | 180,478 | Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict. |
| `ledger/checks.csv` | 3,287 | Gate results G0–G8. |
| `ledger/cycles.csv` | 6,447 | Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry. |
| `ledger/defects.csv` | 3,467 | Values that could not be computed, with the reason (never a sentinel). |
| `ledger/deviations.csv` | 13,397 | Decision-log rows that name this target. |
| `ledger/noise_floor.csv` | 1,336 | The noise-floor row that set the credit bar: σ of R-free on every set. |
| `ledger/rfree_consultations.csv` | 226 | How many times R-free-select was consulted (PROTOCOL §3.6). |
| `ledger/runs/1L6X.20260917T071657Z/DECISIONS.md` | 25,673 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/1L6X.20260917T071657Z/run_summary.json` | 2,736 | The per-run summary (cycles, credits, stop reason). |
| `ledger/solvent_disagreements.csv` | 120 | Phenix/Coot disagreements on solvent sites. |
| `maps/1L6X_refined_map_coeffs.mtz` | 2,390,144 | Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot). |
| `model/1L6X_refined.cif` | 413,945 | The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json. |
| `model/1L6X_refined.pdb` | 364,836 | The same model in PDB format, from the same run. |
| `refinement/command.txt` | 4,282 | The verbatim phenix.refine argv that wrote the model. |
| `refinement/current.json` | 350 | The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index. |
| `refinement/refine_001.eff` | 43,079 | The effective parameters of that run. |
| `refinement/refine_001.log` | 193,328 | The phenix.refine log of that run. |
| `refinement/refine_decisions.json` | 2,484 | The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels). |
| `refinement/refine_result.json` | 3,732 | The parsed result of that run (R factors, geometry, seed, wall clock). |
| `validation/campaign/checks/G3_1L6X.json` | 6,234 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/fetch_1L6X.json` | 2,207 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/clash_altloc.json` | 7,363 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/clashscore.json` | 29,375 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/cycle_row.json` | 1,266 | The campaign's per-cycle record for this model (PROTOCOL §7). |
| `validation/campaign/dossier.json` | 111,925 | The campaign dossier: xtriage, model audit, composition hypothesis, baselines. |
| `validation/campaign/molprobity.out` | 10,333 | The campaign's MolProbity run on this model. |
| `validation/campaign/molprobity_result.json` | 8,385 | The campaign's MolProbity run on this model. |
| `validation/campaign/noise_floor.json` | 7,459 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/verify_20260917/1L6X_baseline_rerefine.json` | 607 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/1L6X_current.json` | 607 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/1L6X_deposited.json` | 580 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/release/merge_mtz.log` | 395 | Log of the data+flags merge used by model_vs_data. |
| `validation/release/model_diff.json` | 452 | Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens. |
| `validation/release/model_vs_data.deposited.log` | 2,367 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/model_vs_data.refined.log` | 2,373 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/molprobity.deposited.log` | 17,692 | phenix.molprobity with default settings. |
| `validation/release/molprobity.deposited.out` | 4,845 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.log` | 18,187 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.out` | 4,397 | phenix.molprobity with default settings. |
| `validation/release/rfree_indep.deposited.json` | 621 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.deposited.log` | 1,081 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.json` | 627 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.log` | 1,089 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/summary.json` | 2,493 | Release-time validation of the deposited and refined models (parsed from the logs beside it). |
