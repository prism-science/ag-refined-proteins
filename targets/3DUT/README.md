# 3DUT — The high salt (phosphate) crystal structure of deoxy hemoglobin E (GLU26LYS) at physiological pH (pH 7.35)

**Status: re-refined baseline, nothing credited.** See the caveats below.

| | |
|---|---|
| Resolution | 1.55 Å |
| Space group | P 1 21 1 |
| Data | amplitudes (FP,SIGFP), 71980 reflections |
| Free set | 3587 reflections (5.0 %), inherited unchanged from the deposition; select / report halves 1793 / 1794 |
| Deposited refinement program | REFMAC |
| Released | 2009-08-04 |
| Primary citation | The high salt (phosphate) crystal structure of  deoxy             
hemoglobin E (GLU26LYS) at physiological pH (pH 7.35) (To be Published ), DOI — |
| Thresholds version that judged the writing cycle | thresholds_v8 |
| Phenix | 2.1-6048 |

## R-free on the frozen flags

Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, no outlier rejection) and with `phenix.model_vs_data`. "Re-refined, no changes" is the mean of the campaign's ten noise-floor seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.

| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |
|---|---|---|---|---|---|
| Deposited, our flags | 0.2351 | 0.2881 | 0.2962 | 0.2794 | 0.2350 / 0.2877 |
| Re-refined, no changes (10 seeds) | — | 0.2532 ± 0.00039 | — | — | — |
| **This release** | **0.2108** | **0.2537** | 0.2626 | 0.2442 | 0.2105 / 0.2533 |

Δ full R-free vs deposited: **-0.0344**; beyond re-refinement alone: **0.0005** (+1.3 × the floor's own spread).
Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `noise_floor`): σ_select 0.00063, σ_report 0.00034, σ_full 0.00039; a cycle is credited at ΔR-free-select ≤ -0.00126 (k = 2.0).
Campaign ledger for this model (`refinement/current.json`): R-work 0.2108, R-free full 0.2537, select 0.2626, report 0.2442.

## Geometry and composition (phenix.molprobity, release time, default settings)

| | Deposited | This release |
|---|---|---|
| Atoms (hydrogens) | 5013 (0) | 5013 (0) |
| Waters | 430 | 430 |
| Altloc letters | A, B | A, B |
| Clashscore | 15.90 | 3.51 |
| Ramachandran outliers / favored (%) | 0.18 / 97.5 | 0.00 / 98.6 |
| Rotamer outliers (%) | 4.29 | 2.58 |
| Cβ deviations | 4 | 0 |
| RMS bonds (Å) / angles (°) | 0.0183 / 1.93 | 0.0045 / 0.95 |
| MolProbity score | 2.28 | 1.45 |

## What changed in the coordinates

No residue added or removed and no alternate conformation changed: the released model is the deposited model re-refined (coordinates, ADPs and occupancies moved, nothing else). `validation/release/model_diff.json`.

## What the campaign did

Refinement protocol of the released model: phenix.refine 2.1-6048, 5 macro-cycles, isotropic ADPs with 13 TLS groups, no hydrogens in the model, seed 1. ADP decision: n_refl/n_atoms(non-H)=14.36 / d_min=1.55: isotropic; TLS (d_min>=2.0 or chain>200 res). The verbatim command is `refinement/command.txt`.

The released model is the cycle-0 baseline: one phenix.refine run on the deposited file with nothing changed (`baseline_rerefine`). The run that followed credited no change, so the standing record never moved (D484).

Cycles on record for this target: 10; credited: 0; changes proposed: 120 (`ledger/cycles.csv`, `ledger/changes.csv`).

## Caveats

- Nothing was credited on this target; the released model is the single Phenix re-refinement of the deposited file (D484). For CNS/REFMAC/X-PLOR-era depositions the campaign's noise floor measures convergence variance rather than test-set noise, so its credit bar was effectively unreachable (D506). The gain over the deposited file is what phenix.refine does on its own.

## Verify it yourself

```bash
# independent scorer (cctbx; needs Phenix)
phenix.python scripts/indep_rfree.py targets/3DUT/model/3DUT_refined.cif targets/3DUT/data/3DUT_data.mtz \
  targets/3DUT/data/3DUT_flags.mtz targets/3DUT/data/3DUT_split.mtz out.json
# standard tool
phenix.python scripts/merge_mtz.py targets/3DUT/data/3DUT_data.mtz targets/3DUT/data/3DUT_flags.mtz 3DUT_merged.mtz
phenix.model_vs_data targets/3DUT/model/3DUT_refined.cif 3DUT_merged.mtz
# look at it
coot targets/3DUT/model/3DUT_refined.pdb --auto targets/3DUT/maps/3DUT_refined_map_coeffs.mtz
```

## Provenance

- Campaign record `refinement/current.json`: cycle 0, stage `baseline_rerefine`, updated 2026-09-17T08:16:18+00:00.
- Model on the campaign pod: `/home/dev/runs/3DUT/c000/baseline_rerefine/refine_001.cif`.
- Data: `data.mtz` SHA-256 `51489ff2464ca08146231c9056b403bb74602e8d465421f8b962b3ad09d197da`, `flags.mtz` SHA-256 `c9f9460084ab904ae4c4263a75ed8eb45350a27141f97eeb9bbe268bea25bc8b`; built from the deposited structure-factor file with SHA-256 `1407cda3b8e2ec08890dea20fc027b8bcac144b57c0039edf5ec701564b339e0` (`data/prep.json`).
- Deposited header claim: R-work 0.218, R-free 0.277, 3587 free reflections.

## Files

| File | Size | What it is |
|---|---|---|
| `data/3DUT_data.mtz` | 1,441,920 | The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors. |
| `data/3DUT_flags.mtz` | 1,153,920 | The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free). |
| `data/3DUT_split.mtz` | 1,153,920 | The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work). |
| `data/prep.json` | 3,060 | How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims. |
| `data/split.json` | 102,952 | The same split as a list of reflections, with the seed that made it. |
| `deposited/3DUT.cif` | 572,256 | The deposited coordinate file as fetched from RCSB (the starting point). |
| `deposited/3DUT.fasta` | 418 | The entry's sequence as fetched from RCSB. |
| `deposited/FETCHED` | 76 | When the raw files were fetched. |
| `deposited/fetch_manifest.sha256` | 756 | SHA-256 of the raw files at fetch time. |
| `deposited/rcsb_entry.json` | 17,982 | The RCSB entry record (title, citation, experimental details) as fetched. |
| `ledger/bisections.csv` | 246 | Bisection steps when a cycle regressed. |
| `ledger/changes.csv` | 410,042 | Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict. |
| `ledger/checks.csv` | 3,115 | Gate results G0–G8. |
| `ledger/cycles.csv` | 7,815 | Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry. |
| `ledger/defects.csv` | 1,718 | Values that could not be computed, with the reason (never a sentinel). |
| `ledger/deviations.csv` | 9,486 | Decision-log rows that name this target. |
| `ledger/noise_floor.csv` | 1,332 | The noise-floor row that set the credit bar: σ of R-free on every set. |
| `ledger/rfree_consultations.csv` | 226 | How many times R-free-select was consulted (PROTOCOL §3.6). |
| `ledger/runs/3DUT.20260917T081842Z/DECISIONS.md` | 48,721 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/3DUT.20260917T081842Z/run_summary.json` | 3,406 | The per-run summary (cycles, credits, stop reason). |
| `ledger/solvent_disagreements.csv` | 120 | Phenix/Coot disagreements on solvent sites. |
| `maps/3DUT_refined_map_coeffs.mtz` | 4,778,656 | Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot). |
| `model/3DUT_refined.cif` | 792,744 | The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json. |
| `model/3DUT_refined.pdb` | 767,132 | The same model in PDB format, from the same run. |
| `refinement/command.txt` | 4,680 | The verbatim phenix.refine argv that wrote the model. |
| `refinement/current.json` | 348 | The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index. |
| `refinement/refine_001.eff` | 43,316 | The effective parameters of that run. |
| `refinement/refine_001.log` | 250,855 | The phenix.refine log of that run. |
| `refinement/refine_decisions.json` | 2,733 | The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels). |
| `refinement/refine_result.json` | 4,533 | The parsed result of that run (R factors, geometry, seed, wall clock). |
| `validation/campaign/checks/G3_3DUT.json` | 6,279 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/fetch_3DUT.json` | 2,207 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/clash_altloc.json` | 16,245 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/clashscore.json` | 66,417 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/cycle_row.json` | 1,264 | The campaign's per-cycle record for this model (PROTOCOL §7). |
| `validation/campaign/dossier.json` | 116,517 | The campaign dossier: xtriage, model audit, composition hypothesis, baselines. |
| `validation/campaign/molprobity.out` | 15,081 | The campaign's MolProbity run on this model. |
| `validation/campaign/molprobity_result.json` | 9,518 | The campaign's MolProbity run on this model. |
| `validation/campaign/noise_floor.json` | 7,437 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/verify_20260917/3DUT_baseline_rerefine.json` | 617 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/3DUT_current.json` | 617 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/3DUT_deposited.json` | 593 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/release/merge_mtz.log` | 395 | Log of the data+flags merge used by model_vs_data. |
| `validation/release/model_diff.json` | 452 | Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens. |
| `validation/release/model_vs_data.deposited.log` | 3,169 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/model_vs_data.refined.log` | 3,175 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/molprobity.deposited.log` | 22,301 | phenix.molprobity with default settings. |
| `validation/release/molprobity.deposited.out` | 7,601 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.log` | 19,866 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.out` | 5,131 | phenix.molprobity with default settings. |
| `validation/release/rfree_indep.deposited.json` | 634 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.deposited.log` | 1,087 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.json` | 637 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.log` | 1,092 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/summary.json` | 2,534 | Release-time validation of the deposited and refined models (parsed from the logs beside it). |
