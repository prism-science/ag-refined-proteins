# 6UDY — X-ray co-crystal structure of compound 5 with Mcl-1

**Status: improved.** This model has a lower R-free than the deposited file on the same free set.

| | |
|---|---|
| Resolution | 1.7 Å |
| Space group | P 21 21 21 |
| Data | intensities (IMEAN,SIGIMEAN), 35508 reflections |
| Free set | 1778 reflections (5.0 %), inherited unchanged from the deposition; select / report halves 889 / 889 |
| Deposited refinement program | CNS |
| Released | 2019-12-11 |
| Primary citation | Discovery and in Vivo Evaluation of Macrocyclic Mcl-1 Inhibitors Featuring an alpha-Hydroxy Phenylacetic Acid Pharmacophore or Bioisostere. (J.Med.Chem. 2019), DOI 10.1021/acs.jmedchem.9b01310 |
| Thresholds version that judged the writing cycle | thresholds_v8 |
| Phenix | 2.1-6048 |

## R-free on the frozen flags

Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, no outlier rejection) and with `phenix.model_vs_data`. "Re-refined, no changes" is the mean of the campaign's ten noise-floor seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.

| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |
|---|---|---|---|---|---|
| Deposited, our flags | 0.2279 | 0.2592 | 0.2525 | 0.2655 | 0.2283 / 0.2594 |
| Re-refined, no changes (10 seeds) | — | 0.2567 ± 0.00772 | — | — | — |
| **This release** | **0.1983** | **0.2479** | 0.2397 | 0.2555 | 0.1981 / 0.2479 |

Δ full R-free vs deposited: **-0.0113**; beyond re-refinement alone: **-0.0088** (-1.1 × the floor's own spread).
Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `noise_floor`): σ_select 0.00872, σ_report 0.00690, σ_full 0.00772; a cycle is credited at ΔR-free-select ≤ -0.01743 (k = 2.0).
Campaign ledger for this model (`refinement/current.json`): R-work 0.1983, R-free full 0.2479, select 0.2397, report 0.2556.

## Geometry and composition (phenix.molprobity, release time, default settings)

| | Deposited | This release |
|---|---|---|
| Atoms (hydrogens) | 2890 (0) | 2885 (0) |
| Waters | 417 | 412 |
| Altloc letters | none | none |
| Clashscore | 12.92 | 4.24 |
| Ramachandran outliers / favored (%) | 0.00 / 98.3 | 0.00 / 98.6 |
| Rotamer outliers (%) | 1.15 | 0.77 |
| Cβ deviations | 0 | 0 |
| RMS bonds (Å) / angles (°) | 0.0109 / 1.27 | 0.0080 / 0.92 |
| MolProbity score | 1.67 | 1.21 |

## What changed in the coordinates

From `validation/release/model_diff.json` (deposited vs released, by chain and residue number):

- Waters removed (5): A 506, A 612, A 634, A 676, B 675

## What the campaign did

Refinement protocol of the released model: phenix.refine 2.1-6048, 5 macro-cycles, isotropic ADPs with 10 TLS groups, no hydrogens in the model, seed 1. ADP decision: n_refl/n_atoms(non-H)=12.31 / d_min=1.6999: isotropic; TLS (d_min>=2.0 or chain>200 res). The verbatim command is `refinement/command.txt`.

The released model was written by cycle 3 (`rerefine`, run `6UDY.20260917T061820Z`), verdict **no_change**, attributable ΔR-free-select 0.00330 against its paired null, ΔR-gap 0.00038.
That run ended: escape ladder exhausted (reweight_reseed=failed, rescale_bulk_solvent=failed, simulated_annealing=failed): the model is converged at this minimum.

Cycles on record for this target: 11; credited: 1; changes proposed: 111 (`ledger/cycles.csv`, `ledger/changes.csv`).

Credited cycles on record, all runs and experiment lines. A credit is relative to that cycle's own paired null; not every credit moved the standing model (promotion rules D484/D499/D508), and experiment-line cycles judged candidates against their own base.

| Cycle | Run | Attributable ΔR-free-select | R-free full after | ΔR-gap vs null | Geometry flag |
|---|---|---|---|---|---|
| 2 | `6UDY.20260917T061820Z` | -0.01973 | 0.2485 | -0.00279 |  |

## Caveats

- The single credit recovered cycle-0 drift on an unconverged CNS-era model (D506). The model beats the re-refined baseline on the consulted half only; on the full and report sets the difference is within its wide noise floor (σ_full 0.0077), and the report half is worse than the baseline's (D508).

## Verify it yourself

```bash
# independent scorer (cctbx; needs Phenix)
phenix.python scripts/indep_rfree.py targets/6UDY/model/6UDY_refined.cif targets/6UDY/data/6UDY_data.mtz \
  targets/6UDY/data/6UDY_flags.mtz targets/6UDY/data/6UDY_split.mtz out.json
# standard tool
phenix.python scripts/merge_mtz.py targets/6UDY/data/6UDY_data.mtz targets/6UDY/data/6UDY_flags.mtz 6UDY_merged.mtz
phenix.model_vs_data targets/6UDY/model/6UDY_refined.cif 6UDY_merged.mtz
# look at it
coot targets/6UDY/model/6UDY_refined.pdb --auto targets/6UDY/maps/6UDY_refined_map_coeffs.mtz
```

## Provenance

- Campaign record `refinement/current.json`: cycle 5, stage `rerefine`, updated 2026-09-17T10:09:37+00:00.
- Model on the campaign pod: `/home/dev/runs/6UDY/runs/6UDY.20260917T061820Z/cycles/c003/paired/null_arm/refine_001.cif`.
- Data: `data.mtz` SHA-256 `b6588a9c04d28559daf6f4011ce097684441a94440ec870f432bd7131a322485`, `flags.mtz` SHA-256 `3ea0316878ecbaf18fcac2247446befe76ee9280b97a98b6bf27f88eb61bda23`; built from the deposited structure-factor file with SHA-256 `824e20d33848573b55383b70d0b0946bcf88926f4f3a463465f88f32732baaec` (`data/prep.json`).
- Deposited header claim: R-work 0.250, R-free 0.285, 1778 free reflections.

## Files

| File | Size | What it is |
|---|---|---|
| `data/6UDY_data.mtz` | 712,640 | The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors. |
| `data/6UDY_flags.mtz` | 570,528 | The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free). |
| `data/6UDY_split.mtz` | 570,528 | The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work). |
| `data/prep.json` | 4,108 | How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims. |
| `data/split.json` | 50,180 | The same split as a list of reflections, with the seed that made it. |
| `deposited/6UDY.cif` | 354,184 | The deposited coordinate file as fetched from RCSB (the starting point). |
| `deposited/6UDY.fasta` | 258 | The entry's sequence as fetched from RCSB. |
| `deposited/FETCHED` | 76 | When the raw files were fetched. |
| `deposited/fetch_manifest.sha256` | 756 | SHA-256 of the raw files at fetch time. |
| `deposited/rcsb_entry.json` | 11,736 | The RCSB entry record (title, citation, experimental details) as fetched. |
| `ledger/bisections.csv` | 246 | Bisection steps when a cycle regressed. |
| `ledger/changes.csv` | 455,567 | Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict. |
| `ledger/checks.csv` | 3,119 | Gate results G0–G8. |
| `ledger/cycles.csv` | 8,156 | Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry. |
| `ledger/defects.csv` | 442 | Values that could not be computed, with the reason (never a sentinel). |
| `ledger/deviations.csv` | 23,500 | Decision-log rows that name this target. |
| `ledger/noise_floor.csv` | 1,333 | The noise-floor row that set the credit bar: σ of R-free on every set. |
| `ledger/rfree_consultations.csv` | 226 | How many times R-free-select was consulted (PROTOCOL §3.6). |
| `ledger/runs/6UDY.20260917T061820Z/DECISIONS.md` | 49,201 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/6UDY.20260917T061820Z/run_summary.json` | 3,098 | The per-run summary (cycles, credits, stop reason). |
| `ledger/solvent_disagreements.csv` | 120 | Phenix/Coot disagreements on solvent sites. |
| `maps/6UDY_refined_map_coeffs.mtz` | 2,400,576 | Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot). |
| `model/6UDY_refined.cif` | 463,645 | The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json. |
| `model/6UDY_refined.pdb` | 434,898 | The same model in PDB format, from the same run. |
| `refinement/command.txt` | 2,321 | The verbatim phenix.refine argv that wrote the model. |
| `refinement/current.json` | 459 | The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index. |
| `refinement/experiment_paired_cycle.json` | 8,607 | Record of the experiment cycle that produced this model (paired null control, geometry of both arms). |
| `refinement/model_vs_data.campaign.log` | 3,138 | phenix.model_vs_data as run by the campaign on this model. |
| `refinement/refine_001.eff` | 43,316 | The effective parameters of that run. |
| `refinement/refine_001.log` | 208,401 | The phenix.refine log of that run. |
| `refinement/refine_decisions.json` | 3,077 | The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels). |
| `refinement/refine_result.json` | 4,392 | The parsed result of that run (R factors, geometry, seed, wall clock). |
| `validation/campaign/checks/G3_6UDY.json` | 6,296 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/fetch_6UDY.json` | 2,207 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/dossier.json` | 110,231 | The campaign dossier: xtriage, model audit, composition hypothesis, baselines. |
| `validation/campaign/noise_floor.json` | 7,532 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/verify_20260917/6UDY_baseline_rerefine.json` | 660 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/6UDY_current.json` | 691 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/6UDY_deposited.json` | 635 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/release/merge_mtz.log` | 398 | Log of the data+flags merge used by model_vs_data. |
| `validation/release/model_diff.json` | 508 | Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens. |
| `validation/release/model_vs_data.deposited.log` | 2,294 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/model_vs_data.refined.log` | 3,330 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/molprobity.deposited.log` | 17,013 | phenix.molprobity with default settings. |
| `validation/release/molprobity.deposited.out` | 4,013 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.log` | 16,495 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.out` | 3,669 | phenix.molprobity with default settings. |
| `validation/release/rfree_indep.deposited.json` | 676 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.deposited.log` | 1,136 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.json` | 679 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.log` | 1,141 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/summary.json` | 2,600 | Release-time validation of the deposited and refined models (parsed from the logs beside it). |
