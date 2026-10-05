# 3QUE — Human p38 MAP Kinase in Complex with Skepinone-L

**Status: improved.** This model has a lower R-free than the deposited file on the same free set.

| | |
|---|---|
| Resolution | 2.7 Å |
| Space group | P 21 21 21 |
| Data | amplitudes (FP,SIGFP), 10793 reflections |
| Free set | 864 reflections (8.0 %), inherited unchanged from the deposition; select / report halves 432 / 432 |
| Deposited refinement program | REFMAC |
| Released | 2012-01-18 |
| Primary citation | Skepinone-L is a selective p38 mitogen-activated protein kinase inhibitor. (Nat.Chem.Biol. 2012), DOI 10.1038/nchembio.761 |
| Thresholds version that judged the writing cycle | thresholds_v9 |
| Phenix | 2.1-6048 |

## R-free on the frozen flags

Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, no outlier rejection) and with `phenix.model_vs_data`. "Re-refined, no changes" is the mean of the campaign's ten noise-floor seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.

| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |
|---|---|---|---|---|---|
| Deposited, our flags | 0.2151 | 0.2879 | 0.2858 | 0.2901 | 0.2132 / 0.2856 |
| Re-refined, no changes (10 seeds) | — | 0.2668 ± 0.00168 | — | — | — |
| **This release** | **0.2104** | **0.2533** | 0.2429 | 0.2642 | 0.2103 / 0.2525 |

Δ full R-free vs deposited: **-0.0346**; beyond re-refinement alone: **-0.0135** (-8.0 × the floor's own spread).
Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `noise_floor_e043_wxc01`): σ_select 0.00205, σ_report 0.00352, σ_full 0.00273; a cycle is credited at ΔR-free-select ≤ -0.00410 (k = 2.0).
Campaign ledger for this model (`refinement/current.json`): R-work 0.2104, R-free full 0.2525, select 0.2420, report 0.2633.

## Geometry and composition (phenix.molprobity, release time, default settings)

| | Deposited | This release |
|---|---|---|
| Atoms (hydrogens) | 2849 (0) | 2881 (0) |
| Waters | 14 | 46 |
| Altloc letters | none | none |
| Clashscore | 10.58 | 2.82 |
| Ramachandran outliers / favored (%) | 0.29 / 95.0 | 0.00 / 98.5 |
| Rotamer outliers (%) | 7.59 | 4.29 |
| Cβ deviations | 2 | 0 |
| RMS bonds (Å) / angles (°) | 0.0156 / 1.66 | 0.0039 / 0.62 |
| MolProbity score | 2.56 | 1.55 |

## What changed in the coordinates

From `validation/release/model_diff.json` (deposited vs released, by chain and residue number):

- Waters added (34): A 5001, A 5007, A 5008, A 5139, A 5140, A 5141, A 5159, A 5167, A 5172, A 5177, A 5185, A 5187, A 5188, A 5192, A 5195, A 5201, A 5204, A 5210, A 5217, A 5224, A 5226, A 5253, A 5255, A 5258, A 5260, A 5307, A 5322, A 5323, A 5326, A 5331, A 5340, A 5354, A 5356, A 5357
- Waters removed (2): A 365, A 376

## What the campaign did

Refinement protocol of the released model: phenix.refine 2.1-6048, 5 macro-cycles, isotropic ADPs with 4 TLS groups, no hydrogens in the model, seed 1. ADP decision: n_refl/n_atoms(non-H)=3.75 / d_min=2.7002: isotropic; TLS (d_min>=2.0 or chain>200 res). The verbatim command is `refinement/command.txt`.

The released model was written by cycle 921 (`graph`, run `3QUE.graph-weekend-20261002d`), verdict **accepted**, attributable ΔR-free-select -0.00869 against its paired null, ΔR-gap -0.00059; geometry flag: rota_outliers 4.29 > 1.5.

Cycles on record for this target: 68; credited: 9; changes proposed: 2855 (`ledger/cycles.csv`, `ledger/changes.csv`).

Credited cycles on record, all runs and experiment lines. A credit is relative to that cycle's own paired null; not every credit moved the standing model (promotion rules D484/D499/D508), and experiment-line cycles judged candidates against their own base.

| Cycle | Run | Attributable ΔR-free-select | R-free full after | ΔR-gap vs null | Geometry flag |
|---|---|---|---|---|---|
| 31 | `3QUE.run3` | -0.00727 | 0.2599 | — |  |
| 41 | `3QUE.exp_water_occ` | -0.00557 | 0.2589 | — |  |
| 912 | `3QUE.E040` | -0.00378 | 0.2615 | -0.00414 |  |
| 913 | `3QUE.E040` | -0.00376 | 0.2622 | -0.00458 |  |
| 915 | `3QUE.graph-weekend-20261002d` | -0.00661 | 0.2571 | -0.00724 | rota_outliers 3.96 > 1.5 |
| 916 | `3QUE.graph-weekend-20261002d` | -0.00514 | 0.2565 | -0.01013 | rota_outliers 3.96 > 1.5 |
| 917 | `3QUE.graph-weekend-20261002d` | -0.00479 | 0.2528 | 0.00546 | rota_outliers 3.96 > 1.5 |
| 921 | `3QUE.graph-weekend-20261002d` | -0.00869 | 0.2525 | -0.00059 | rota_outliers 4.29 > 1.5 |
| 922 | `3QUE.graph-weekend-20261002d` | -0.00438 | 0.2584 | 0.00384 | rota_outliers 3.96 > 1.5 |

## Caveats

- The held-back report half, the unbiased estimate (PROTOCOL §3.6), improved much less than the full set. Ledger values, previous record (2026-08-28) → this model: full 0.25891 → 0.25246, report 0.26441 → 0.26334, select 0.25365 → 0.24205 (independent scorer: full 0.25968 → 0.25330, report 0.26517 → 0.26420). Most of the full-set gain sits on the select half, the half the search consults (D519).
- This model is the graph search's third 3QUE promotion on 2026-10-03 (`3QUE.graph-weekend-20261002d`, generation 6). The one before it (generation 4, D520) had report 0.25983, better on both halves than the 2026-08-28 record; this promotion lowered full by 0.0004 and raised report by 0.0035. It passed the promotion rules (report inside 2σ_report of the record it replaced); no decision row covers it yet. The first promotion (generation 2, D518) had made report worse (0.26725).
- The gain is water sites transferred from 9MHB, the 1.65 Å isomorphous p38α entry, combined in credited batches against matched null arms (D518, D520). Waters 15 → 46 against the previous release (deposited 14).
- Rotamer outliers are above the campaign's 1.5 % cap: 4.29 % at release time (phenix.molprobity; previous released model 3.96 %, deposited 7.59 %). The campaign records 3.96 % for both records and calls it pre-existing (D518, D520).
- The deposited header R-free (0.311) is a REFMAC number; Phenix recomputes the same model at 0.287 on these flags (D008). Only the recomputed value is comparable.
- Most of the gain over the deposited file is Phenix re-refinement of a REFMAC-refined model (TLS, weight optimisation); the campaign's own credited changes are water edits: three added, two removed, water occupancies refined (D421/D485), then the 9MHB transfer waters.
- The model carries no riding hydrogens: adding them was tested and rejected at 2.7 Å (D490).

## Verify it yourself

```bash
# independent scorer (cctbx; needs Phenix)
phenix.python scripts/indep_rfree.py targets/3QUE/model/3QUE_refined.cif targets/3QUE/data/3QUE_data.mtz \
  targets/3QUE/data/3QUE_flags.mtz targets/3QUE/data/3QUE_split.mtz out.json
# standard tool
phenix.python scripts/merge_mtz.py targets/3QUE/data/3QUE_data.mtz targets/3QUE/data/3QUE_flags.mtz 3QUE_merged.mtz
phenix.model_vs_data targets/3QUE/model/3QUE_refined.cif 3QUE_merged.mtz
# look at it
coot targets/3QUE/model/3QUE_refined.pdb --auto targets/3QUE/maps/3QUE_refined_map_coeffs.mtz
```

## Provenance

- Campaign record `refinement/current.json`: cycle 922, stage `rerefine`, updated 2026-10-03T09:13:23+00:00.
- Model on the campaign pod: `/home/dev/runs/3QUE/graph/3QUE.graph-weekend-20261002d/g006/N5.0/combined/g006.N5.0.loo3/candidate_arm/refine_001.cif`.
- Data: `data.mtz` SHA-256 `46e775eaef62e9ea6ba161189332747b22e18d456bb52f6eff759fdf3bb7d3c9`, `flags.mtz` SHA-256 `389672087b3a3ca53fea456853e5df57ae38c009636c80fd5685679361721bd2`; built from the deposited structure-factor file with SHA-256 `7dca2e602c18bdef3c708cd5d41354cda0ea63daddb6f0089bdb4081c84314cf` (`data/prep.json`).
- Deposited header claim: R-work 0.223, R-free 0.311, 863 free reflections.

## Files

| File | Size | What it is |
|---|---|---|
| `data/3QUE_data.mtz` | 218,340 | The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors. |
| `data/3QUE_flags.mtz` | 175,088 | The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free). |
| `data/3QUE_split.mtz` | 175,088 | The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work). |
| `data/prep.json` | 2,805 | How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims. |
| `data/split.json` | 24,274 | The same split as a list of reflections, with the seed that made it. |
| `deposited/3QUE.cif` | 350,945 | The deposited coordinate file as fetched from RCSB (the starting point). |
| `deposited/3QUE.fasta` | 433 | The entry's sequence as fetched from RCSB. |
| `deposited/FETCHED` | 76 | When the raw files were fetched. |
| `deposited/fetch_manifest.sha256` | 935 | SHA-256 of the raw files at fetch time. |
| `deposited/rcsb_entry.json` | 18,418 | The RCSB entry record (title, citation, experimental details) as fetched. |
| `ledger/bisections.csv` | 1,268 | Bisection steps when a cycle regressed. |
| `ledger/changes.csv` | 8,717,661 | Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict. |
| `ledger/checks.csv` | 1,693 | Gate results G0–G8. |
| `ledger/cycles.csv` | 36,822 | Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry. |
| `ledger/defects.csv` | 120,938 | Values that could not be computed, with the reason (never a sentinel). |
| `ledger/deviations.csv` | 121,458 | Decision-log rows that name this target. |
| `ledger/noise_floor.csv` | 1,346 | The noise-floor row that set the credit bar: σ of R-free on every set. |
| `ledger/rfree_consultations.csv` | 228 | How many times R-free-select was consulted (PROTOCOL §3.6). |
| `ledger/runs/3QUE.20260908v5/DECISIONS.md` | 1,361 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/3QUE.20260908v5b/DECISIONS.md` | 31,862 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/3QUE.20260908v5b/run_summary.json` | 2,855 | The per-run summary (cycles, credits, stop reason). |
| `ledger/runs/3QUE.20260909corr/DECISIONS.md` | 19,318 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/3QUE.20260909corr/run_summary.json` | 2,934 | The per-run summary (cycles, credits, stop reason). |
| `ledger/runs/3QUE.run1/DECISIONS.md` | 901 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/3QUE.run2/DECISIONS.md` | 901 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/3QUE.run3/DECISIONS.md` | 82,973 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/3QUE.run3/run_summary.json` | 2,630 | The per-run summary (cycles, credits, stop reason). |
| `ledger/runs/3QUE.run5/DECISIONS.md` | 3,329 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/3QUE.run5/run_summary.json` | 2,298 | The per-run summary (cycles, credits, stop reason). |
| `ledger/solvent_disagreements.csv` | 120 | Phenix/Coot disagreements on solvent sites. |
| `maps/3QUE_refined_map_coeffs.mtz` | 697,408 | Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot). |
| `model/3QUE_refined.cif` | 510,111 | The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json. |
| `model/3QUE_refined.pdb` | 457,646 | The same model in PDB format, from the same run. |
| `refinement/command.txt` | 1,933 | The verbatim phenix.refine argv that wrote the model. |
| `refinement/current.json` | 520 | The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index. |
| `refinement/experiment_paired_cycle.json` | 7,428 | Record of the experiment cycle that produced this model (paired null control, geometry of both arms). |
| `refinement/model_vs_data.campaign.log` | 2,809 | phenix.model_vs_data as run by the campaign on this model. |
| `refinement/refine_001.eff` | 52,224 | The effective parameters of that run. |
| `refinement/refine_001.log` | 152,624 | The phenix.refine log of that run. |
| `refinement/refine_decisions.json` | 2,350 | The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels). |
| `refinement/refine_result.json` | 3,662 | The parsed result of that run (R factors, geometry, seed, wall clock). |
| `validation/campaign/checks/G3_3QUE.json` | 6,300 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/fetch_3QUE.json` | 2,400 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/dossier.json` | 108,647 | The campaign dossier: xtriage, model audit, composition hypothesis, baselines. |
| `validation/campaign/noise_floor.json` | 7,468 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/noise_floor_e043_wxc01.json` | 8,041 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/verify_20260907/3QUE_deposited.indep.json` | 509 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260907/3QUE_ours.indep.json` | 555 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260907/3QUE_pdbredo.indep.json` | 525 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20261003/3QUE_d_g002.json` | 661 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20261003/3QUE_now.json` | 658 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20261003/3QUE_old.json` | 620 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/release/merge_mtz.log` | 394 | Log of the data+flags merge used by model_vs_data. |
| `validation/release/model_diff.json` | 882 | Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens. |
| `validation/release/model_vs_data.deposited.log` | 2,996 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/model_vs_data.refined.log` | 3,001 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/molprobity.deposited.log` | 16,072 | phenix.molprobity with default settings. |
| `validation/release/molprobity.deposited.out` | 4,766 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.log` | 15,055 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.out` | 3,732 | phenix.molprobity with default settings. |
| `validation/release/rfree_indep.deposited.json` | 615 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.deposited.log` | 1,075 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.json` | 621 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.log` | 1,083 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/summary.json` | 2,483 | Release-time validation of the deposited and refined models (parsed from the logs beside it). |
