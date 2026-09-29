# 1V2X — TrmH

**Status: re-refined baseline, nothing credited.** See the caveats below.

| | |
|---|---|
| Resolution | 1.5 Å |
| Space group | C 1 2 1 |
| Data | amplitudes (FP,SIGFP), 24289 reflections |
| Free set | 2399 reflections (9.9 %), inherited unchanged from the deposition; select / report halves 1199 / 1200 |
| Deposited refinement program | CNS |
| Released | 2004-05-04 |
| Primary citation | Deep Knot Structure for Construction of Active Site and Cofactor Binding Site of tRNA Modification Enzyme (STRUCTURE 2004), DOI 10.1016/j.str.2004.03.003 |
| Thresholds version that judged the writing cycle | thresholds_v8 |
| Phenix | 2.1-6048 |

## R-free on the frozen flags

Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, no outlier rejection) and with `phenix.model_vs_data`. "Re-refined, no changes" is the mean of the campaign's ten noise-floor seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.

| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |
|---|---|---|---|---|---|
| Deposited, our flags | 0.2016 | 0.2559 | 0.2463 | 0.2658 | 0.2016 / 0.2554 |
| Re-refined, no changes (10 seeds) | — | 0.2347 ± 0.00069 | — | — | — |
| **This release** | **0.1881** | **0.2354** | 0.2262 | 0.2450 | 0.1880 / 0.2354 |

Δ full R-free vs deposited: **-0.0204**; beyond re-refinement alone: **0.0007** (+1.0 × the floor's own spread).
Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `noise_floor`): σ_select 0.00079, σ_report 0.00073, σ_full 0.00069; a cycle is credited at ΔR-free-select ≤ -0.00158 (k = 2.0).
Campaign ledger for this model (`refinement/current.json`): R-work 0.1881, R-free full 0.2354, select 0.2262, report 0.2449.

## Geometry and composition (phenix.molprobity, release time, default settings)

| | Deposited | This release |
|---|---|---|
| Atoms (hydrogens) | 1757 (0) | 1757 (0) |
| Waters | 190 | 190 |
| Altloc letters | none | none |
| Clashscore | 31.32 | 13.09 |
| Ramachandran outliers / favored (%) | 2.12 / 95.8 | 1.59 / 96.3 |
| Rotamer outliers (%) | 5.66 | 5.66 |
| Cβ deviations | 0 | 0 |
| RMS bonds (Å) / angles (°) | 0.0233 / 2.10 | 0.0080 / 1.07 |
| MolProbity score | 2.85 | 2.45 |

## What changed in the coordinates

No residue added or removed and no alternate conformation changed: the released model is the deposited model re-refined (coordinates, ADPs and occupancies moved, nothing else). `validation/release/model_diff.json`.

## What the campaign did

Refinement protocol of the released model: phenix.refine 2.1-6048, 5 macro-cycles, isotropic ADPs with 4 TLS groups, no hydrogens in the model, seed 1. ADP decision: n_refl/n_atoms(non-H)=13.82 / d_min=1.5005: isotropic; TLS (d_min>=2.0 or chain>200 res). The verbatim command is `refinement/command.txt`.

The released model is the cycle-0 baseline: one phenix.refine run on the deposited file with nothing changed (`baseline_rerefine`). The run that followed credited no change, so the standing record never moved (D484).

Cycles on record for this target: 9; credited: 0; changes proposed: 62 (`ledger/cycles.csv`, `ledger/changes.csv`).

## Caveats

- Nothing was credited on this target; the released model is the single Phenix re-refinement of the deposited file (D484). For CNS/REFMAC/X-PLOR-era depositions the campaign's noise floor measures convergence variance rather than test-set noise, so its credit bar was effectively unreachable (D506). The gain over the deposited file is what phenix.refine does on its own.

## Verify it yourself

```bash
# independent scorer (cctbx; needs Phenix)
phenix.python scripts/indep_rfree.py targets/1V2X/model/1V2X_refined.cif targets/1V2X/data/1V2X_data.mtz \
  targets/1V2X/data/1V2X_flags.mtz targets/1V2X/data/1V2X_split.mtz out.json
# standard tool
phenix.python scripts/merge_mtz.py targets/1V2X/data/1V2X_data.mtz targets/1V2X/data/1V2X_flags.mtz 1V2X_merged.mtz
phenix.model_vs_data targets/1V2X/model/1V2X_refined.cif 1V2X_merged.mtz
# look at it
coot targets/1V2X/model/1V2X_refined.pdb --auto targets/1V2X/maps/1V2X_refined_map_coeffs.mtz
```

## Provenance

- Campaign record `refinement/current.json`: cycle 0, stage `baseline_rerefine`, updated 2026-09-17T05:56:22+00:00.
- Model on the campaign pod: `/home/dev/runs/1V2X/c000/baseline_rerefine/refine_001.cif`.
- Data: `data.mtz` SHA-256 `1c93a1e723d5f0ec32baa52b19c4f581af4077b305aaa16012a3e3cc7e3dd119`, `flags.mtz` SHA-256 `93a3bc2b61237db7e9b613277629177b8b014095f01f25a2d8e0ca960ad83b11`; built from the deposited structure-factor file with SHA-256 `bf8c2a0f7be4fa0ec2b02a0f2cf38b0bf909b5cbdc22733c90940f0723cd16d9` (`data/prep.json`).
- Deposited header claim: R-work 0.225, R-free 0.277, 2399 free reflections.

## Files

| File | Size | What it is |
|---|---|---|
| `data/1V2X_data.mtz` | 488,260 | The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors. |
| `data/1V2X_flags.mtz` | 391,024 | The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free). |
| `data/1V2X_split.mtz` | 391,024 | The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work). |
| `data/prep.json` | 2,975 | How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims. |
| `data/split.json` | 68,961 | The same split as a list of reflections, with the seed that made it. |
| `deposited/1V2X.cif` | 241,987 | The deposited coordinate file as fetched from RCSB (the starting point). |
| `deposited/1V2X.fasta` | 268 | The entry's sequence as fetched from RCSB. |
| `deposited/FETCHED` | 115 | When the raw files were fetched. |
| `deposited/fetch_manifest.sha256` | 756 | SHA-256 of the raw files at fetch time. |
| `deposited/rcsb_entry.json` | 12,776 | The RCSB entry record (title, citation, experimental details) as fetched. |
| `ledger/bisections.csv` | 1,357 | Bisection steps when a cycle regressed. |
| `ledger/changes.csv` | 230,889 | Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict. |
| `ledger/checks.csv` | 3,116 | Gate results G0–G8. |
| `ledger/cycles.csv` | 6,485 | Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry. |
| `ledger/defects.csv` | 1,405 | Values that could not be computed, with the reason (never a sentinel). |
| `ledger/deviations.csv` | 11,595 | Decision-log rows that name this target. |
| `ledger/noise_floor.csv` | 1,342 | The noise-floor row that set the credit bar: σ of R-free on every set. |
| `ledger/rfree_consultations.csv` | 226 | How many times R-free-select was consulted (PROTOCOL §3.6). |
| `ledger/runs/1V2X.20260917T062029Z/DECISIONS.md` | 28,459 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/1V2X.20260917T062029Z/run_summary.json` | 2,607 | The per-run summary (cycles, credits, stop reason). |
| `ledger/solvent_disagreements.csv` | 120 | Phenix/Coot disagreements on solvent sites. |
| `maps/1V2X_refined_map_coeffs.mtz` | 1,700,736 | Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot). |
| `model/1V2X_refined.cif` | 292,255 | The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json. |
| `model/1V2X_refined.pdb` | 271,575 | The same model in PDB format, from the same run. |
| `refinement/command.txt` | 7,916 | The verbatim phenix.refine argv that wrote the model. |
| `refinement/current.json` | 352 | The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index. |
| `refinement/refine_001.eff` | 42,856 | The effective parameters of that run. |
| `refinement/refine_001.log` | 142,385 | The phenix.refine log of that run. |
| `refinement/refine_decisions.json` | 2,297 | The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels). |
| `refinement/refine_result.json` | 3,237 | The parsed result of that run (R factors, geometry, seed, wall clock). |
| `validation/campaign/checks/G3_1V2X.json` | 6,175 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/fetch_1V2X.json` | 2,207 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/clash_altloc.json` | 19,685 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/clashscore.json` | 84,379 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/cycle_row.json` | 1,252 | The campaign's per-cycle record for this model (PROTOCOL §7). |
| `validation/campaign/dossier.json` | 87,684 | The campaign dossier: xtriage, model audit, composition hypothesis, baselines. |
| `validation/campaign/molprobity.out` | 12,199 | The campaign's MolProbity run on this model. |
| `validation/campaign/molprobity_result.json` | 9,477 | The campaign's MolProbity run on this model. |
| `validation/campaign/noise_floor.json` | 7,430 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/verify_20260917/1V2X_baseline_rerefine.json` | 608 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/1V2X_current.json` | 608 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/1V2X_deposited.json` | 580 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/release/merge_mtz.log` | 395 | Log of the data+flags merge used by model_vs_data. |
| `validation/release/model_diff.json` | 452 | Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens. |
| `validation/release/model_vs_data.deposited.log` | 2,286 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/model_vs_data.refined.log` | 2,294 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/molprobity.deposited.log` | 17,355 | phenix.molprobity with default settings. |
| `validation/release/molprobity.deposited.out` | 6,083 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.log` | 15,492 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.out` | 4,143 | phenix.molprobity with default settings. |
| `validation/release/rfree_indep.deposited.json` | 621 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.deposited.log` | 1,081 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.json` | 628 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.log` | 1,090 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/summary.json` | 2,494 | Release-time validation of the deposited and refined models (parsed from the logs beside it). |
