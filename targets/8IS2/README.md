# 8IS2 — Crystal structure of a polyketide aromatase/cyclase Abx(+)D from Actinomycetes sp. MA7150.

**Status: re-refined baseline, nothing credited.** See the caveats below.

| | |
|---|---|
| Resolution | 1.32 Å |
| Space group | P 31 |
| Data | amplitudes (FP,SIGFP), 49541 reflections |
| Free set | 2404 reflections (4.9 %), inherited unchanged from the deposition; select / report halves 1202 / 1202 |
| Deposited refinement program | PHENIX |
| Released | 2024-02-28 |
| Primary citation | An unusual aromatase/cyclase programs the formation of the phenyldimethylanthrone framework in anthrabenzoxocinones and fasamycin. (Proc.Natl.Acad.Sci.USA 2024), DOI 10.1073/pnas.2321722121 |
| Thresholds version that judged the writing cycle | thresholds_v8 |
| Phenix | 2.1-6048 |

## R-free on the frozen flags

Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, no outlier rejection) and with `phenix.model_vs_data`. "Re-refined, no changes" is the mean of the campaign's ten noise-floor seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.

| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |
|---|---|---|---|---|---|
| Deposited, our flags | 0.2246 | 0.2756 | 0.2605 | 0.2900 | 0.2241 / 0.2754 |
| Re-refined, no changes (10 seeds) | — | 0.2666 ± 0.00061 | — | — | — |
| **This release** | **0.2265** | **0.2668** | 0.2502 | 0.2827 | 0.2263 / 0.2671 |

Δ full R-free vs deposited: **-0.0088**; beyond re-refinement alone: **0.0002** (+0.3 × the floor's own spread).
Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `noise_floor`): σ_select 0.00100, σ_report 0.00072, σ_full 0.00061; a cycle is credited at ΔR-free-select ≤ -0.00200 (k = 2.0).
Campaign ledger for this model (`refinement/current.json`): R-work 0.2265, R-free full 0.2670, select 0.2504, report 0.2828.

## Geometry and composition (phenix.molprobity, release time, default settings)

| | Deposited | This release |
|---|---|---|
| Atoms (hydrogens) | 1829 (0) | 1829 (0) |
| Waters | 152 | 152 |
| Altloc letters | none | none |
| Clashscore | 1.51 | 2.71 |
| Ramachandran outliers / favored (%) | 0.00 / 98.0 | 0.00 / 97.5 |
| Rotamer outliers (%) | 0.56 | 0.56 |
| Cβ deviations | 0 | 0 |
| RMS bonds (Å) / angles (°) | 0.0059 / 1.14 | 0.0072 / 0.96 |
| MolProbity score | 0.90 | 1.17 |

## What changed in the coordinates

No residue added or removed and no alternate conformation changed: the released model is the deposited model re-refined (coordinates, ADPs and occupancies moved, nothing else). `validation/release/model_diff.json`.

## What the campaign did

Refinement protocol of the released model: phenix.refine 2.1-6048, 5 macro-cycles, anisotropic ADPs, no hydrogens in the model, seed 1. ADP decision: n_refl/n_atoms(non-H)=27.09 >= 5.0 and d_min=1.3218 <= 1.5. The verbatim command is `refinement/command.txt`.

The released model is the cycle-0 baseline: one phenix.refine run on the deposited file with nothing changed (`baseline_rerefine`). The run that followed credited no change, so the standing record never moved (D484).

Cycles on record for this target: 9; credited: 0; changes proposed: 89 (`ledger/cycles.csv`, `ledger/changes.csv`).

## Caveats

- Nothing was credited on this target; the released model is the single Phenix re-refinement of the deposited file (D484). For CNS/REFMAC/X-PLOR-era depositions the campaign's noise floor measures convergence variance rather than test-set noise, so its credit bar was effectively unreachable (D506). The gain over the deposited file is what phenix.refine does on its own.

## Verify it yourself

```bash
# independent scorer (cctbx; needs Phenix)
phenix.python scripts/indep_rfree.py targets/8IS2/model/8IS2_refined.cif targets/8IS2/data/8IS2_data.mtz \
  targets/8IS2/data/8IS2_flags.mtz targets/8IS2/data/8IS2_split.mtz out.json
# standard tool
phenix.python scripts/merge_mtz.py targets/8IS2/data/8IS2_data.mtz targets/8IS2/data/8IS2_flags.mtz 8IS2_merged.mtz
phenix.model_vs_data targets/8IS2/model/8IS2_refined.cif 8IS2_merged.mtz
# look at it
coot targets/8IS2/model/8IS2_refined.pdb --auto targets/8IS2/maps/8IS2_refined_map_coeffs.mtz
```

## Provenance

- Campaign record `refinement/current.json`: cycle 0, stage `baseline_rerefine`, updated 2026-09-17T06:41:27+00:00.
- Model on the campaign pod: `/home/dev/runs/8IS2/c000/baseline_rerefine/refine_001.cif`.
- Data: `data.mtz` SHA-256 `138fcfdeecdbd625c47b35aa8e6220e249e31257e32d96249cb8d07539857016`, `flags.mtz` SHA-256 `c16c5d7666ee8cf233d785247a86c9a2b761161d2ad5fd9546b4a2677c9bbbeb`; built from the deposited structure-factor file with SHA-256 `b406373d7db423e3e79b6ca07b3bbbac4163fba9d3292a407e9eef1ba176c53f` (`data/prep.json`).
- Deposited header claim: R-work 0.224, R-free 0.275, 2404 free reflections.

## Files

| File | Size | What it is |
|---|---|---|
| `data/8IS2_data.mtz` | 993,220 | The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors. |
| `data/8IS2_flags.mtz` | 794,976 | The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free). |
| `data/8IS2_split.mtz` | 794,976 | The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work). |
| `data/prep.json` | 3,661 | How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims. |
| `data/split.json` | 68,430 | The same split as a list of reflections, with the seed that made it. |
| `deposited/8IS2.cif` | 402,882 | The deposited coordinate file as fetched from RCSB (the starting point). |
| `deposited/8IS2.fasta` | 179 | The entry's sequence as fetched from RCSB. |
| `deposited/FETCHED` | 76 | When the raw files were fetched. |
| `deposited/fetch_manifest.sha256` | 756 | SHA-256 of the raw files at fetch time. |
| `deposited/rcsb_entry.json` | 10,687 | The RCSB entry record (title, citation, experimental details) as fetched. |
| `ledger/bisections.csv` | 246 | Bisection steps when a cycle regressed. |
| `ledger/changes.csv` | 337,102 | Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict. |
| `ledger/checks.csv` | 3,056 | Gate results G0–G8. |
| `ledger/cycles.csv` | 6,410 | Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry. |
| `ledger/defects.csv` | 1,961 | Values that could not be computed, with the reason (never a sentinel). |
| `ledger/deviations.csv` | 9,152 | Decision-log rows that name this target. |
| `ledger/noise_floor.csv` | 1,337 | The noise-floor row that set the credit bar: σ of R-free on every set. |
| `ledger/rfree_consultations.csv` | 226 | How many times R-free-select was consulted (PROTOCOL §3.6). |
| `ledger/runs/8IS2.20260917T064133Z/DECISIONS.md` | 35,791 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/8IS2.20260917T064133Z/run_summary.json` | 2,901 | The per-run summary (cycles, credits, stop reason). |
| `ledger/solvent_disagreements.csv` | 120 | Phenix/Coot disagreements on solvent sites. |
| `maps/8IS2_refined_map_coeffs.mtz` | 3,258,352 | Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot). |
| `model/8IS2_refined.cif` | 302,089 | The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json. |
| `model/8IS2_refined.pdb` | 296,997 | The same model in PDB format, from the same run. |
| `refinement/command.txt` | 3,644 | The verbatim phenix.refine argv that wrote the model. |
| `refinement/current.json` | 351 | The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index. |
| `refinement/refine_001.eff` | 42,675 | The effective parameters of that run. |
| `refinement/refine_001.log` | 69,260 | The phenix.refine log of that run. |
| `refinement/refine_decisions.json` | 2,081 | The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels). |
| `refinement/refine_result.json` | 2,760 | The parsed result of that run (R factors, geometry, seed, wall clock). |
| `validation/campaign/checks/G3_8IS2.json` | 4,651 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/fetch_8IS2.json` | 2,207 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/clash_altloc.json` | 5,012 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/clashscore.json` | 19,114 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/cycle_row.json` | 1,251 | The campaign's per-cycle record for this model (PROTOCOL §7). |
| `validation/campaign/dossier.json` | 100,959 | The campaign dossier: xtriage, model audit, composition hypothesis, baselines. |
| `validation/campaign/molprobity.out` | 7,297 | The campaign's MolProbity run on this model. |
| `validation/campaign/molprobity_result.json` | 7,554 | The campaign's MolProbity run on this model. |
| `validation/campaign/noise_floor.json` | 7,490 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/verify_20260917/8IS2_baseline_rerefine.json` | 603 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/8IS2_current.json` | 603 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/8IS2_deposited.json` | 580 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/release/merge_mtz.log` | 395 | Log of the data+flags merge used by model_vs_data. |
| `validation/release/model_diff.json` | 452 | Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens. |
| `validation/release/model_vs_data.deposited.log` | 2,364 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/model_vs_data.refined.log` | 2,368 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/molprobity.deposited.log` | 14,776 | phenix.molprobity with default settings. |
| `validation/release/molprobity.deposited.out` | 3,661 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.log` | 15,092 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.out` | 3,829 | phenix.molprobity with default settings. |
| `validation/release/rfree_indep.deposited.json` | 621 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.deposited.log` | 1,081 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.json` | 623 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.log` | 1,085 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/summary.json` | 2,488 | Release-time validation of the deposited and refined models (parsed from the logs beside it). |
