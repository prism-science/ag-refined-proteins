# 9D5U — Nitrile hydratase S112A mutant

**Status: improved.** This model has a lower R-free than the deposited file on the same free set.

| | |
|---|---|
| Resolution | 1.35 Å |
| Space group | P 32 2 1 |
| Data | intensities (IMEAN,SIGIMEAN), 100941 reflections |
| Free set | 2012 reflections (2.0 %), inherited unchanged from the deposition; select / report halves 1006 / 1006 |
| Deposited refinement program | PHENIX |
| Released | 2024-11-06 |
| Primary citation | Catalytic and post-translational maturation roles of a conserved active site serine residue in nitrile hydratases. (J.Inorg.Biochem. 2024), DOI 10.1016/j.jinorgbio.2024.112763 |
| Thresholds version that judged the writing cycle | thresholds_v8 |
| Phenix | 2.1-6048 |

## R-free on the frozen flags

Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, no outlier rejection) and with `phenix.model_vs_data`. "Re-refined, no changes" is the mean of the campaign's ten noise-floor seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.

| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |
|---|---|---|---|---|---|
| Deposited, our flags | 0.2612 | 0.2853 | 0.2790 | 0.2917 | 0.2612 / 0.2844 |
| Re-refined, no changes (10 seeds) | — | 0.2549 ± 0.00026 | — | — | — |
| **This release** | **0.2306** | **0.2532** | 0.2486 | 0.2580 | 0.2306 / 0.2526 |

Δ full R-free vs deposited: **-0.0321**; beyond re-refinement alone: **-0.0016** (-6.2 × the floor's own spread).
Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `noise_floor`): σ_select 0.00044, σ_report 0.00029, σ_full 0.00026; a cycle is credited at ΔR-free-select ≤ -0.00087 (k = 2.0).
Campaign ledger for this model (`refinement/current.json`): R-work 0.2306, R-free full 0.2528, select 0.2480, report 0.2577.

## Geometry and composition (phenix.molprobity, release time, default settings)

| | Deposited | This release |
|---|---|---|
| Atoms (hydrogens) | 3735 (8) | 3743 (8) |
| Waters | 251 | 259 |
| Altloc letters | A, B | A, B |
| Clashscore | 10.10 | 4.54 |
| Ramachandran outliers / favored (%) | 0.70 / 97.4 | 0.23 / 97.4 |
| Rotamer outliers (%) | 0.27 | 0.27 |
| Cβ deviations | 1 | 0 |
| RMS bonds (Å) / angles (°) | 0.0246 / 2.22 | 0.0028 / 0.61 |
| MolProbity score | 1.64 | 1.34 |

## What changed in the coordinates

From `validation/release/model_diff.json` (deposited vs released, by chain and residue number):

- Waters added (9): B 5001, B 5002, B 5003, B 5004, B 5005, B 5006, B 5007, B 5008, B 5009
- Waters removed (1): B 422

## What the campaign did

Refinement protocol of the released model: phenix.refine 2.1-6048, 5 macro-cycles, anisotropic ADPs, 8 riding hydrogens, seed 1. ADP decision: n_refl/n_atoms(non-H)=27.03 >= 5.0 and d_min=1.35 <= 1.5. The verbatim command is `refinement/command.txt`.

The released model was written by cycle 2 (`rerefine`, run `9D5U.20260917T095256Z`), verdict **accepted**, attributable ΔR-free-select -0.00098 against its paired null, ΔR-gap -0.00185.
That run ended: escape ladder exhausted (reweight_reseed=failed, rescale_bulk_solvent=failed, simulated_annealing=refused): the model is converged at this minimum.

Cycles on record for this target: 9; credited: 2; changes proposed: 102 (`ledger/cycles.csv`, `ledger/changes.csv`).

Credited cycles on record, all runs and experiment lines. A credit is relative to that cycle's own paired null; not every credit moved the standing model (promotion rules D484/D499/D508), and experiment-line cycles judged candidates against their own base.

| Cycle | Run | Attributable ΔR-free-select | R-free full after | ΔR-gap vs null | Geometry flag |
|---|---|---|---|---|---|
| 1 | `9D5U.20260917T095256Z` | -0.00112 | 0.2538 | -0.00129 |  |
| 2 | `9D5U.20260917T095256Z` | -0.00098 | 0.2528 | -0.00185 |  |

## Caveats

- Two credits, waters removed and added; −0.002 beyond re-refinement at 6σ. The run stopped with its escape ladder exhausted (D510).

## Verify it yourself

```bash
# independent scorer (cctbx; needs Phenix)
phenix.python scripts/indep_rfree.py targets/9D5U/model/9D5U_refined.cif targets/9D5U/data/9D5U_data.mtz \
  targets/9D5U/data/9D5U_flags.mtz targets/9D5U/data/9D5U_split.mtz out.json
# standard tool
phenix.python scripts/merge_mtz.py targets/9D5U/data/9D5U_data.mtz targets/9D5U/data/9D5U_flags.mtz 9D5U_merged.mtz
phenix.model_vs_data targets/9D5U/model/9D5U_refined.cif 9D5U_merged.mtz
# look at it
coot targets/9D5U/model/9D5U_refined.pdb --auto targets/9D5U/maps/9D5U_refined_map_coeffs.mtz
```

## Provenance

- Campaign record `refinement/current.json`: cycle 6, stage `rerefine`, updated 2026-09-17T22:35:32+00:00.
- Model on the campaign pod: `/home/dev/runs/9D5U/runs/9D5U.20260917T095256Z/cycles/c002/paired/candidate_arm/refine_001.cif`.
- Data: `data.mtz` SHA-256 `0ccfd11ee337dda95213150e48f6cad38c3ad211ef51cda81d99455bab3d3714`, `flags.mtz` SHA-256 `3f10fd144b9130bbb99c2b05a0dca4e9750d60bcde500a303a28079e69b1660d`; built from the deposited structure-factor file with SHA-256 `d3e27857aab7137321bb6c32ad5c8e7796f59216837e500d8320f6554c253bfa` (`data/prep.json`).
- Deposited header claim: R-work 0.239, R-free 0.259, 2044 free reflections.

## Files

| File | Size | What it is |
|---|---|---|
| `data/9D5U_data.mtz` | 2,021,460 | The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors. |
| `data/9D5U_flags.mtz` | 1,617,616 | The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free). |
| `data/9D5U_split.mtz` | 1,617,616 | The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work). |
| `data/prep.json` | 3,387 | How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims. |
| `data/split.json` | 58,248 | The same split as a list of reflections, with the seed that made it. |
| `deposited/9D5U.cif` | 434,643 | The deposited coordinate file as fetched from RCSB (the starting point). |
| `deposited/9D5U.fasta` | 633 | The entry's sequence as fetched from RCSB. |
| `deposited/FETCHED` | 76 | When the raw files were fetched. |
| `deposited/fetch_manifest.sha256` | 756 | SHA-256 of the raw files at fetch time. |
| `deposited/rcsb_entry.json` | 9,353 | The RCSB entry record (title, citation, experimental details) as fetched. |
| `ledger/bisections.csv` | 246 | Bisection steps when a cycle regressed. |
| `ledger/changes.csv` | 480,800 | Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict. |
| `ledger/checks.csv` | 3,294 | Gate results G0–G8. |
| `ledger/cycles.csv` | 6,921 | Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry. |
| `ledger/defects.csv` | 1,049 | Values that could not be computed, with the reason (never a sentinel). |
| `ledger/deviations.csv` | 11,607 | Decision-log rows that name this target. |
| `ledger/noise_floor.csv` | 1,328 | The noise-floor row that set the credit bar: σ of R-free on every set. |
| `ledger/rfree_consultations.csv` | 226 | How many times R-free-select was consulted (PROTOCOL §3.6). |
| `ledger/runs/9D5U.20260917T095256Z/DECISIONS.md` | 43,880 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/9D5U.20260917T095256Z/run_summary.json` | 2,506 | The per-run summary (cycles, credits, stop reason). |
| `ledger/solvent_disagreements.csv` | 120 | Phenix/Coot disagreements on solvent sites. |
| `maps/9D5U_refined_map_coeffs.mtz` | 6,624,864 | Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot). |
| `model/9D5U_refined.cif` | 615,785 | The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json. |
| `model/9D5U_refined.pdb` | 597,429 | The same model in PDB format, from the same run. |
| `refinement/command.txt` | 1,535 | The verbatim phenix.refine argv that wrote the model. |
| `refinement/current.json` | 471 | The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index. |
| `refinement/experiment_paired_cycle.json` | 6,300 | Record of the experiment cycle that produced this model (paired null control, geometry of both arms). |
| `refinement/model_vs_data.campaign.log` | 3,301 | phenix.model_vs_data as run by the campaign on this model. |
| `refinement/refine_001.eff` | 42,786 | The effective parameters of that run. |
| `refinement/refine_001.log` | 75,975 | The phenix.refine log of that run. |
| `refinement/refine_decisions.json` | 2,113 | The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels). |
| `refinement/refine_result.json` | 3,008 | The parsed result of that run (R factors, geometry, seed, wall clock). |
| `validation/campaign/checks/G3_9D5U.json` | 6,354 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/fetch_9D5U.json` | 2,207 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/dossier.json` | 121,921 | The campaign dossier: xtriage, model audit, composition hypothesis, baselines. |
| `validation/campaign/noise_floor.json` | 7,425 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/verify_20260917/9D5U_baseline_rerefine.json` | 674 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/9D5U_current.json` | 713 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/9D5U_deposited.json` | 650 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/release/merge_mtz.log` | 399 | Log of the data+flags merge used by model_vs_data. |
| `validation/release/model_diff.json` | 573 | Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens. |
| `validation/release/model_vs_data.deposited.log` | 3,414 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/model_vs_data.refined.log` | 3,493 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/molprobity.deposited.log` | 46,463 | phenix.molprobity with default settings. |
| `validation/release/molprobity.deposited.out` | 34,317 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.log` | 44,601 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.out` | 32,066 | phenix.molprobity with default settings. |
| `validation/release/rfree_indep.deposited.json` | 691 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.deposited.log` | 1,144 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.json` | 696 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.log` | 1,151 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/summary.json` | 2,651 | Release-time validation of the deposited and refined models (parsed from the logs beside it). |
