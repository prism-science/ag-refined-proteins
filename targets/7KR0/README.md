# 7KR0 — Crystal structure of SARS-CoV-2 NSP3 macrodomain (C2 crystal form, 100 K)

**Status: improved.** This model has a lower R-free than the deposited file on the same free set.

| | |
|---|---|
| Resolution | 0.77 Å |
| Space group | C 1 2 1 |
| Data | amplitudes (FP,SIGFP), 178324 reflections |
| Free set | 8712 reflections (4.9 %), inherited unchanged from the deposition; select / report halves 4356 / 4356 |
| Deposited refinement program | PHENIX |
| Released | 2020-12-09 |
| Primary citation | Fragment binding to the Nsp3 macrodomain of SARS-CoV-2 identified through crystallographic screening and computational docking. (Sci Adv 2021), DOI 10.1126/sciadv.abf8711 |
| Thresholds version that judged the writing cycle | thresholds_v5 |
| Phenix | 2.1-6048 |

## R-free on the frozen flags

Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, no outlier rejection) and with `phenix.model_vs_data`. "Re-refined, no changes" is the mean of the campaign's ten noise-floor seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.

| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |
|---|---|---|---|---|---|
| Deposited, our flags | 0.1103 | 0.1174 | 0.1159 | 0.1189 | 0.1102 / 0.1175 |
| Re-refined, no changes (10 seeds) | — | 0.1163 ± 0.00024 | — | — | — |
| **This release** | **0.1036** | **0.1125** | 0.1104 | 0.1147 | 0.1036 / 0.1125 |

Δ full R-free vs deposited: **-0.0048**; beyond re-refinement alone: **-0.0038** (-15.9 × the floor's own spread).
Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `noise_floor`): σ_select 0.00040, σ_report 0.00009, σ_full 0.00024; a cycle is credited at ΔR-free-select ≤ -0.00081 (k = 2.0).
Campaign ledger for this model (`refinement/current.json`): R-work 0.1036, R-free full 0.1126, select 0.1103, report 0.1148.

## Geometry and composition (phenix.molprobity, release time, default settings)

| | Deposited | This release |
|---|---|---|
| Atoms (hydrogens) | 4300 (1990) | 4298 (1990) |
| Waters | 312 | 310 |
| Altloc letters | A, B, C, D | A, B, C, D |
| Clashscore | 4.73 | 6.72 |
| Ramachandran outliers / favored (%) | 0.00 / 99.4 | 0.00 / 98.8 |
| Rotamer outliers (%) | 0.89 | 1.33 |
| Cβ deviations | 0 | 0 |
| RMS bonds (Å) / angles (°) | 0.0301 / 1.50 | 0.0126 / 1.61 |
| MolProbity score | 1.24 | 1.47 |

## What changed in the coordinates

From `validation/release/model_diff.json` (deposited vs released, by chain and residue number):

- Waters removed (2): A 246, A 381

## What the campaign did

Refinement protocol of the released model: phenix.refine 2.1-6048, 15 macro-cycles, anisotropic ADPs, 1990 riding hydrogens, seed 1. ADP decision: n_refl/n_atoms(non-H)=77.26 >= 5.0 and d_min=0.77 <= 1.5. The verbatim command is `refinement/command.txt`.

The released model was written by cycle 37 (`rerefine`, run `7KR0.E030c`), verdict **accepted**, attributable ΔR-free-select -0.00101 against its paired null, ΔR-gap -0.00039; geometry flag: clashscore 10.7098 > 5.

Cycles on record for this target: 32; credited: 6; changes proposed: 1009 (`ledger/cycles.csv`, `ledger/changes.csv`).

Credited cycles on record, all runs and experiment lines. A credit is relative to that cycle's own paired null; not every credit moved the standing model (promotion rules D484/D499/D508), and experiment-line cycles judged candidates against their own base.

| Cycle | Run | Attributable ΔR-free-select | R-free full after | ΔR-gap vs null | Geometry flag |
|---|---|---|---|---|---|
| 17 | `7KR0.exp_sw_distill` | -0.00672 | 0.2261 | — |  |
| 19 | `7KR0.exp_sw_distill` | -0.01784 | 0.1239 | — |  |
| 21 | `7KR0.exp_sw_distill` | -0.01490 | 0.1262 | — |  |
| 33 | `7KR0.E030` | -0.00085 | 0.1130 | -0.00024 | rota_outliers 1.78 > 1.5; clashscore 9.7136 > 5 |
| 35 | `7KR0.E030b` | -0.00082 | 0.1128 | -0.00025 | clashscore 10.2117 > 5 |
| 37 | `7KR0.E030c` | -0.00101 | 0.1126 | -0.00039 | clashscore 10.7098 > 5 |

## Caveats

- MolProbity rotamer outliers and the altloc-aware clashscore of this model exceed the campaign's own frozen caps (1.5 % and 5.0); the deposited multiconformer model already exceeds the clashscore cap by construction (D451, D474). Depositable by ordinary standards, not by the campaign's own bar.
- The changes carried by this model are two waters removed plus three 15-macro-cycle refinement passes credited at 2.1σ, 2.0σ and 2.5σ (D489, D493, D494): continued refinement, not remodelling. The deposited model was already near-optimal as a single-conformer representation.
- Three credited cycles on record (run `7KR0.exp_sw_distill`) belong to the ensemble-distillation line, which judged its candidates against its own base and was closed as a negative result (D463, D466); they are not in this model's lineage.
- Ensemble representations of the same data score far lower (44PS, the six-conformation model of Passmore et al. 2026 on this dataset, 0.0657 on these flags; the campaign's own six-copy models 0.088–0.092). They are a second representation, not a deliverable (PROTOCOL §18.1); the campaign's are released separately in `representations/7KR0/`.

## Verify it yourself

```bash
# independent scorer (cctbx; needs Phenix)
phenix.python scripts/indep_rfree.py targets/7KR0/model/7KR0_refined.cif targets/7KR0/data/7KR0_data.mtz \
  targets/7KR0/data/7KR0_flags.mtz targets/7KR0/data/7KR0_split.mtz out.json
# standard tool
phenix.python scripts/merge_mtz.py targets/7KR0/data/7KR0_data.mtz targets/7KR0/data/7KR0_flags.mtz 7KR0_merged.mtz
phenix.model_vs_data targets/7KR0/model/7KR0_refined.cif 7KR0_merged.mtz
# look at it
coot targets/7KR0/model/7KR0_refined.pdb --auto targets/7KR0/maps/7KR0_refined_map_coeffs.mtz
```

## Provenance

- Campaign record `refinement/current.json`: cycle 37, stage `rerefine`, updated 2026-09-09T19:41:05+00:00.
- Model on the campaign pod: `/home/dev/runs/7KR0/experiments/e030c_macro_cycles15/paired/candidate_arm/refine_001.cif`.
- Data: `data.mtz` SHA-256 `ae703738dc52b3e3597d4ca641d98bfb88f1793dee88ca8a24176d3d3fd378fe`, `flags.mtz` SHA-256 `31939295cafaf855a01545c567b5b6763ef8365a63246ae5a29639e7561b202f`; built from the deposited structure-factor file with SHA-256 `e243c56935c5c86a1bd79b7f3630ac16276eef3194d59c3c274f01b8afc06a54` (`data/prep.json`).
- Deposited header claim: R-work 0.110, R-free 0.117, 8711 free reflections.

## Files

| File | Size | What it is |
|---|---|---|
| `data/7KR0_data.mtz` | 3,568,960 | The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors. |
| `data/7KR0_flags.mtz` | 2,855,584 | The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free). |
| `data/7KR0_split.mtz` | 2,855,584 | The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work). |
| `data/prep.json` | 3,519 | How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims. |
| `data/split.json` | 253,981 | The same split as a list of reflections, with the seed that made it. |
| `deposited/7KR0.cif` | 668,616 | The deposited coordinate file as fetched from RCSB (the starting point). |
| `deposited/7KR0.fasta` | 273 | The entry's sequence as fetched from RCSB. |
| `deposited/FETCHED` | 154 | When the raw files were fetched. |
| `deposited/fetch_manifest.sha256` | 756 | SHA-256 of the raw files at fetch time. |
| `deposited/rcsb_entry.json` | 19,808 | The RCSB entry record (title, citation, experimental details) as fetched. |
| `ledger/bisections.csv` | 7,105 | Bisection steps when a cycle regressed. |
| `ledger/changes.csv` | 2,309,293 | Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict. |
| `ledger/checks.csv` | 3,596 | Gate results G0–G8. |
| `ledger/cycles.csv` | 17,604 | Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry. |
| `ledger/defects.csv` | 58,848 | Values that could not be computed, with the reason (never a sentinel). |
| `ledger/deviations.csv` | 93,320 | Decision-log rows that name this target. |
| `ledger/noise_floor.csv` | 1,350 | The noise-floor row that set the credit bar: σ of R-free on every set. |
| `ledger/rfree_consultations.csv` | 227 | How many times R-free-select was consulted (PROTOCOL §3.6). |
| `ledger/runs/7KR0.20260908v5/DECISIONS.md` | 696 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/7KR0.20260908v5b/DECISIONS.md` | 13,123 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/7KR0.20260908v5b/run_summary.json` | 2,154 | The per-run summary (cycles, credits, stop reason). |
| `ledger/runs/7KR0.20260910v6/DECISIONS.md` | 707 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/7KR0.20260910v7/DECISIONS.md` | 12,701 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/7KR0.20260910v7/run_summary.json` | 2,412 | The per-run summary (cycles, credits, stop reason). |
| `ledger/runs/7KR0.run1/DECISIONS.md` | 1,839 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/7KR0.run2/DECISIONS.md` | 51,346 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/7KR0.run2/run_summary.json` | 1,892 | The per-run summary (cycles, credits, stop reason). |
| `ledger/solvent_disagreements.csv` | 120 | Phenix/Coot disagreements on solvent sites. |
| `maps/7KR0_refined_map_coeffs.mtz` | 11,450,112 | Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot). |
| `model/7KR0_refined.cif` | 551,296 | The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json. |
| `model/7KR0_refined.pdb` | 529,555 | The same model in PDB format, from the same run. |
| `refinement/command.txt` | 1,527 | The verbatim phenix.refine argv that wrote the model. |
| `refinement/current.json` | 460 | The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index. |
| `refinement/experiment_header.json` | 458 | Record of the experiment cycle that produced this model (paired null control, geometry of both arms). |
| `refinement/experiment_paired_cycle.json` | 6,176 | Record of the experiment cycle that produced this model (paired null control, geometry of both arms). |
| `refinement/experiment_result.json` | 2,100 | Record of the experiment cycle that produced this model (paired null control, geometry of both arms). |
| `refinement/model_vs_data.campaign.log` | 2,261 | phenix.model_vs_data as run by the campaign on this model. |
| `refinement/refine_001.eff` | 42,787 | The effective parameters of that run. |
| `refinement/refine_001.log` | 144,413 | The phenix.refine log of that run. |
| `refinement/refine_decisions.json` | 2,089 | The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels). |
| `refinement/refine_result.json` | 4,215 | The parsed result of that run (R factors, geometry, seed, wall clock). |
| `validation/campaign/checks/G3_7KR0-6conf_flags.json` | 3,745 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/G3_7KR0.json` | 4,575 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/fetch_7KR0.json` | 2,207 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/dossier.json` | 164,515 | The campaign dossier: xtriage, model audit, composition hypothesis, baselines. |
| `validation/campaign/noise_floor.json` | 7,454 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/verify_20260907/7KR0_deposited.indep.json` | 551 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260907/7KR0_operator6conf.indep.json` | 654 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260907/7KR0_ours.indep.json` | 597 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260907/7KR0_pdbredo.indep.json` | 562 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260909/7KR0_e030_candidate.indep.json` | 606 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260909/7KR0_e030_null.indep.json` | 600 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260909/7KR0_e030b_candidate.indep.json` | 608 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260909/7KR0_e030b_null.indep.json` | 603 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260909/7KR0_e030c_candidate.indep.json` | 607 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260909/7KR0_e030c_null.indep.json` | 601 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/release/merge_mtz.log` | 396 | Log of the data+flags merge used by model_vs_data. |
| `validation/release/model_diff.json` | 483 | Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens. |
| `validation/release/model_vs_data.deposited.log` | 2,451 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/model_vs_data.refined.log` | 2,453 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/molprobity.deposited.log` | 19,545 | phenix.molprobity with default settings. |
| `validation/release/molprobity.deposited.out` | 5,528 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.log` | 20,375 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.out` | 6,040 | phenix.molprobity with default settings. |
| `validation/release/rfree_indep.deposited.json` | 657 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.deposited.log` | 1,106 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.json` | 661 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.log` | 1,112 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/summary.json` | 2,590 | Release-time validation of the deposited and refined models (parsed from the logs beside it). |
