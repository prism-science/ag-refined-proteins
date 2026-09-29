# 7DVR — Crystal structure of heme sensor protein PefR from Streptococcus agalactiae in complex with heme

**Status: re-refined baseline, nothing credited.** See the caveats below.

| | |
|---|---|
| Resolution | 1.7 Å |
| Space group | C 1 2 1 |
| Data | intensities (IMEAN,SIGIMEAN), 18057 reflections |
| Free set | 882 reflections (4.9 %), inherited unchanged from the deposition; select / report halves 441 / 441 |
| Deposited refinement program | REFMAC |
| Released | 2021-09-29 |
| Primary citation | Heme controls the structural rearrangement of its sensor protein mediating the hemolytic bacterial survival. (Commun Biol 2021), DOI 10.1038/s42003-021-01987-5 |
| Thresholds version that judged the writing cycle | thresholds_v8 |
| Phenix | 2.1-6048 |

## R-free on the frozen flags

Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, no outlier rejection) and with `phenix.model_vs_data`. "Re-refined, no changes" is the mean of the campaign's ten noise-floor seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.

| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |
|---|---|---|---|---|---|
| Deposited, our flags | 0.2422 | 0.2948 | 0.3269 | 0.2698 | 0.2421 / 0.2943 |
| Re-refined, no changes (10 seeds) | — | 0.2871 ± 0.00072 | — | — | — |
| **This release** | **0.2527** | **0.2873** | 0.3083 | 0.2710 | 0.2526 / 0.2875 |

Δ full R-free vs deposited: **-0.0075**; beyond re-refinement alone: **0.0003** (+0.4 × the floor's own spread).
Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `noise_floor`): σ_select 0.00096, σ_report 0.00078, σ_full 0.00072; a cycle is credited at ΔR-free-select ≤ -0.00192 (k = 2.0).
Campaign ledger for this model (`refinement/current.json`): R-work 0.2527, R-free full 0.2872, select 0.3077, report 0.2713.

## Geometry and composition (phenix.molprobity, release time, default settings)

| | Deposited | This release |
|---|---|---|
| Atoms (hydrogens) | 1295 (0) | 1295 (0) |
| Waters | 37 | 37 |
| Altloc letters | A, B | A, B |
| Clashscore | 7.02 | 3.12 |
| Ramachandran outliers / favored (%) | 0.00 / 95.2 | 0.00 / 95.9 |
| Rotamer outliers (%) | 1.48 | 0.74 |
| Cβ deviations | 1 | 0 |
| RMS bonds (Å) / angles (°) | 0.0212 / 2.06 | 0.0068 / 0.65 |
| MolProbity score | 1.85 | 1.39 |

## What changed in the coordinates

No residue added or removed and no alternate conformation changed: the released model is the deposited model re-refined (coordinates, ADPs and occupancies moved, nothing else). `validation/release/model_diff.json`.

## What the campaign did

Refinement protocol of the released model: phenix.refine 2.1-6048, 5 macro-cycles, isotropic ADPs, no hydrogens in the model, seed 1. ADP decision: n_refl/n_atoms(non-H)=13.94 / d_min=1.7043: isotropic. The verbatim command is `refinement/command.txt`.

The released model is the cycle-0 baseline: one phenix.refine run on the deposited file with nothing changed (`baseline_rerefine`). The run that followed credited no change, so the standing record never moved (D484).

Cycles on record for this target: 8; credited: 0; changes proposed: 36 (`ledger/cycles.csv`, `ledger/changes.csv`).

## Caveats

- Nothing was credited on this target; the released model is the single Phenix re-refinement of the deposited file (D484). For CNS/REFMAC/X-PLOR-era depositions the campaign's noise floor measures convergence variance rather than test-set noise, so its credit bar was effectively unreachable (D506). The gain over the deposited file is what phenix.refine does on its own.

## Verify it yourself

```bash
# independent scorer (cctbx; needs Phenix)
phenix.python scripts/indep_rfree.py targets/7DVR/model/7DVR_refined.cif targets/7DVR/data/7DVR_data.mtz \
  targets/7DVR/data/7DVR_flags.mtz targets/7DVR/data/7DVR_split.mtz out.json
# standard tool
phenix.python scripts/merge_mtz.py targets/7DVR/data/7DVR_data.mtz targets/7DVR/data/7DVR_flags.mtz 7DVR_merged.mtz
phenix.model_vs_data targets/7DVR/model/7DVR_refined.cif 7DVR_merged.mtz
# look at it
coot targets/7DVR/model/7DVR_refined.pdb --auto targets/7DVR/maps/7DVR_refined_map_coeffs.mtz
```

## Provenance

- Campaign record `refinement/current.json`: cycle 0, stage `baseline_rerefine`, updated 2026-09-17T05:26:23+00:00.
- Model on the campaign pod: `/home/dev/runs/7DVR/c000/baseline_rerefine/refine_001.cif`.
- Data: `data.mtz` SHA-256 `330b512de2517d38ee14036d1a73a4d3bb6f44f344f1e8194be7ab617752fa26`, `flags.mtz` SHA-256 `2a551b5c07c51fdc3b0a18b1f1cbb41fa2fd895f031116beeff16bd30937d115`; built from the deposited structure-factor file with SHA-256 `28a82ab5f64062955d57b87d940a74365f58332f81fb4a91ad27e6d9d78980cd` (`data/prep.json`).
- Deposited header claim: R-work 0.237, R-free 0.285, 882 free reflections.

## Files

| File | Size | What it is |
|---|---|---|
| `data/7DVR_data.mtz` | 363,620 | The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors. |
| `data/7DVR_flags.mtz` | 291,312 | The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free). |
| `data/7DVR_split.mtz` | 291,312 | The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work). |
| `data/prep.json` | 4,110 | How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims. |
| `data/split.json` | 25,427 | The same split as a list of reflections, with the seed that made it. |
| `deposited/7DVR.cif` | 312,751 | The deposited coordinate file as fetched from RCSB (the starting point). |
| `deposited/7DVR.fasta` | 273 | The entry's sequence as fetched from RCSB. |
| `deposited/FETCHED` | 76 | When the raw files were fetched. |
| `deposited/fetch_manifest.sha256` | 756 | SHA-256 of the raw files at fetch time. |
| `deposited/rcsb_entry.json` | 16,466 | The RCSB entry record (title, citation, experimental details) as fetched. |
| `ledger/bisections.csv` | 1,357 | Bisection steps when a cycle regressed. |
| `ledger/changes.csv` | 163,948 | Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict. |
| `ledger/checks.csv` | 3,189 | Gate results G0–G8. |
| `ledger/cycles.csv` | 5,978 | Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry. |
| `ledger/defects.csv` | 423 | Values that could not be computed, with the reason (never a sentinel). |
| `ledger/deviations.csv` | 15,300 | Decision-log rows that name this target. |
| `ledger/noise_floor.csv` | 1,329 | The noise-floor row that set the credit bar: σ of R-free on every set. |
| `ledger/rfree_consultations.csv` | 226 | How many times R-free-select was consulted (PROTOCOL §3.6). |
| `ledger/runs/7DVR.20260917T052749Z/DECISIONS.md` | 20,018 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/7DVR.20260917T052749Z/run_summary.json` | 2,135 | The per-run summary (cycles, credits, stop reason). |
| `ledger/solvent_disagreements.csv` | 120 | Phenix/Coot disagreements on solvent sites. |
| `maps/7DVR_refined_map_coeffs.mtz` | 1,196,800 | Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot). |
| `model/7DVR_refined.cif` | 137,096 | The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json. |
| `model/7DVR_refined.pdb` | 108,827 | The same model in PDB format, from the same run. |
| `refinement/command.txt` | 3,660 | The verbatim phenix.refine argv that wrote the model. |
| `refinement/current.json` | 351 | The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index. |
| `refinement/refine_001.eff` | 42,863 | The effective parameters of that run. |
| `refinement/refine_001.log` | 70,334 | The phenix.refine log of that run. |
| `refinement/refine_decisions.json` | 2,104 | The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels). |
| `refinement/refine_result.json` | 2,967 | The parsed result of that run (R factors, geometry, seed, wall clock). |
| `validation/campaign/checks/G3_7DVR.json` | 6,378 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/fetch_7DVR.json` | 2,207 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/clash_altloc.json` | 5,208 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/clashscore.json` | 17,004 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/cycle_row.json` | 1,248 | The campaign's per-cycle record for this model (PROTOCOL §7). |
| `validation/campaign/dossier.json` | 80,357 | The campaign dossier: xtriage, model audit, composition hypothesis, baselines. |
| `validation/campaign/molprobity.out` | 7,013 | The campaign's MolProbity run on this model. |
| `validation/campaign/molprobity_result.json` | 7,260 | The campaign's MolProbity run on this model. |
| `validation/campaign/noise_floor.json` | 7,506 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/verify_20260917/7DVR_baseline_rerefine.json` | 673 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/7DVR_current.json` | 673 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/7DVR_deposited.json` | 650 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/release/merge_mtz.log` | 397 | Log of the data+flags merge used by model_vs_data. |
| `validation/release/model_diff.json` | 450 | Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens. |
| `validation/release/model_vs_data.deposited.log` | 2,216 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/model_vs_data.refined.log` | 2,221 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/molprobity.deposited.log` | 16,547 | phenix.molprobity with default settings. |
| `validation/release/molprobity.deposited.out` | 4,851 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.log` | 15,872 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.out` | 3,841 | phenix.molprobity with default settings. |
| `validation/release/rfree_indep.deposited.json` | 691 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.deposited.log` | 1,144 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.json` | 693 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.log` | 1,148 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/summary.json` | 2,647 | Release-time validation of the deposited and refined models (parsed from the logs beside it). |
