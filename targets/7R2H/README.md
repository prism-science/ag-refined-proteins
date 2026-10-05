# 7R2H — 0.79A resolution structure of DMSO bound Cyclophilin D

**Status: re-refined baseline, nothing credited.** See the caveats below.

| | |
|---|---|
| Resolution | 0.79 Å |
| Space group | P 41 21 2 |
| Data | amplitudes (FP,SIGFP), 149186 reflections |
| Free set | 7538 reflections (5.1 %), inherited unchanged from the deposition; select / report halves 3769 / 3769 |
| Deposited refinement program | PHENIX |
| Released | 2023-02-15 |
| Primary citation | Structure-based design of pyrazole derivatives targeting the human Cyclophilin D binding site (Int.J.Biol.Macromol. 2026), DOI 10.1016/j.ijbiomac.2026.151496 |
| Thresholds version that judged the writing cycle | thresholds_v8 |
| Phenix | 2.1-6048 |

## R-free on the frozen flags

Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, no outlier rejection) and with `phenix.model_vs_data`. "Re-refined, no changes" is the mean of the campaign's ten noise-floor seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.

| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |
|---|---|---|---|---|---|
| Deposited, our flags | 0.1440 | 0.1546 | 0.1527 | 0.1565 | 0.1437 / 0.1545 |
| Re-refined, no changes (10 seeds) | — | 0.1289 ± 0.00013 | — | — | — |
| **This release** | **0.1146** | **0.1290** | 0.1287 | 0.1294 | 0.1143 / 0.1289 |

Δ full R-free vs deposited: **-0.0256**; beyond re-refinement alone: **0.0001** (+0.9 × the floor's own spread).
Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `noise_floor`): σ_select 0.00021, σ_report 0.00019, σ_full 0.00013; a cycle is credited at ΔR-free-select ≤ -0.00042 (k = 2.0).
Campaign ledger for this model (`refinement/current.json`): R-work 0.1146, R-free full 0.1290, select 0.1287, report 0.1293.

## Geometry and composition (phenix.molprobity, release time, default settings)

| | Deposited | This release |
|---|---|---|
| Atoms (hydrogens) | 2850 (1253) | 2850 (1253) |
| Waters | 335 | 335 |
| Altloc letters | A, B | A, B |
| Clashscore | 0.80 | 1.20 |
| Ramachandran outliers / favored (%) | 0.00 / 96.9 | 0.00 / 96.9 |
| Rotamer outliers (%) | 0.00 | 0.73 |
| Cβ deviations | 0 | 0 |
| RMS bonds (Å) / angles (°) | 0.0054 / 0.91 | 0.0106 / 1.29 |
| MolProbity score | 0.93 | 1.02 |

## What changed in the coordinates

No residue added or removed and no alternate conformation changed: the released model is the deposited model re-refined (coordinates, ADPs and occupancies moved, nothing else). `validation/release/model_diff.json`.

## What the campaign did

Refinement protocol of the released model: phenix.refine 2.1-6048, 5 macro-cycles, anisotropic ADPs, 1253 riding hydrogens, seed 1. ADP decision: n_refl/n_atoms(non-H)=93.42 >= 5.0 and d_min=0.7892 <= 1.5. The verbatim command is `refinement/command.txt`.

The released model is the cycle-0 baseline: one phenix.refine run on the deposited file with nothing changed (`baseline_rerefine`). The run that followed credited no change, so the standing record never moved (D484).

Cycles on record for this target: 4; credited: 0; changes proposed: 0 (`ledger/cycles.csv`, `ledger/changes.csv`).

## Caveats

- The released model is one Phenix re-refinement of the deposited file; nothing the agent proposed has been credited yet (E044). The −0.026 over the deposited file is the campaign's re-refinement protocol on its own, and it is mostly an ADP-model change: the deposited file carries ANISOU on 1 258 of its 1 597 non-hydrogen atoms (the isotropic ones are the 335 waters and the DMSO), the campaign's protocol refines every non-hydrogen atom anisotropically. R-work falls further than R-free, so the R-free − R-work gap widens from 0.011 to 0.014.
- Rotamer outliers rise from 0.00 % to 0.73 % (one residue) and clashscore from 0.8 to 1.2 on re-refinement.
- Nothing was credited on this target; the released model is the single Phenix re-refinement of the deposited file (D484). For CNS/REFMAC/X-PLOR-era depositions the campaign's noise floor measures convergence variance rather than test-set noise, so its credit bar was effectively unreachable (D506). The gain over the deposited file is what phenix.refine does on its own.

## Verify it yourself

```bash
# independent scorer (cctbx; needs Phenix)
phenix.python scripts/indep_rfree.py targets/7R2H/model/7R2H_refined.cif targets/7R2H/data/7R2H_data.mtz \
  targets/7R2H/data/7R2H_flags.mtz targets/7R2H/data/7R2H_split.mtz out.json
# standard tool
phenix.python scripts/merge_mtz.py targets/7R2H/data/7R2H_data.mtz targets/7R2H/data/7R2H_flags.mtz 7R2H_merged.mtz
phenix.model_vs_data targets/7R2H/model/7R2H_refined.cif 7R2H_merged.mtz
# look at it
coot targets/7R2H/model/7R2H_refined.pdb --auto targets/7R2H/maps/7R2H_refined_map_coeffs.mtz
```

## Provenance

- Campaign record `refinement/current.json`: cycle 0, stage `baseline_rerefine`, updated 2026-10-05T07:38:38+00:00.
- Model on the campaign pod: `/home/dev/runs/7R2H/c000/baseline_rerefine/refine_001.cif`.
- Data: `data.mtz` SHA-256 `5871418b32ac4d56b3fd5d7ae0274f1f178c6efbecfb74e29343883c26f3e854`, `flags.mtz` SHA-256 `88357d540ed5245a7901c89b387ba53290f1965535ed9b2eaf60a17bae067c07`; built from the deposited structure-factor file with SHA-256 `15f9cf6c1c2ad9585e0f0d80e7a138ecdaec6b02b0b70a7ef02a3ceb3c42ab70` (`data/prep.json`).
- Deposited header claim: R-work 0.143, R-free 0.155, 7538 free reflections.

## Files

| File | Size | What it is |
|---|---|---|
| `data/7R2H_data.mtz` | 2,986,520 | The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors. |
| `data/7R2H_flags.mtz` | 2,389,696 | The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free). |
| `data/7R2H_split.mtz` | 2,389,696 | The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work). |
| `data/prep.json` | 3,740 | How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims. |
| `data/split.json` | 215,394 | The same split as a list of reflections, with the seed that made it. |
| `deposited/7R2H.cif` | 495,732 | The deposited coordinate file as fetched from RCSB (the starting point). |
| `deposited/7R2H.fasta` | 255 | The entry's sequence as fetched from RCSB. |
| `deposited/FETCHED` | 37 | When the raw files were fetched. |
| `deposited/fetch_manifest.sha256` | 756 | SHA-256 of the raw files at fetch time. |
| `deposited/rcsb_entry.json` | 12,086 | The RCSB entry record (title, citation, experimental details) as fetched. |
| `ledger/bisections.csv` | 246 | Bisection steps when a cycle regressed. |
| `ledger/changes.csv` | 510 | Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict. |
| `ledger/checks.csv` | 3,061 | Gate results G0–G8. |
| `ledger/cycles.csv` | 3,466 | Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry. |
| `ledger/defects.csv` | 97 | Values that could not be computed, with the reason (never a sentinel). |
| `ledger/deviations.csv` | 126 | Decision-log rows that name this target. |
| `ledger/noise_floor.csv` | 1,335 | The noise-floor row that set the credit bar: σ of R-free on every set. |
| `ledger/rfree_consultations.csv` | 77 | How many times R-free-select was consulted (PROTOCOL §3.6). |
| `ledger/solvent_disagreements.csv` | 120 | Phenix/Coot disagreements on solvent sites. |
| `maps/7R2H_refined_map_coeffs.mtz` | 10,232,640 | Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot). |
| `model/7R2H_refined.cif` | 380,401 | The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json. |
| `model/7R2H_refined.pdb` | 359,913 | The same model in PDB format, from the same run. |
| `refinement/command.txt` | 3,688 | The verbatim phenix.refine argv that wrote the model. |
| `refinement/current.json` | 352 | The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index. |
| `refinement/refine_001.eff` | 42,674 | The effective parameters of that run. |
| `refinement/refine_001.log` | 76,676 | The phenix.refine log of that run. |
| `refinement/refine_decisions.json` | 2,135 | The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels). |
| `refinement/refine_result.json` | 2,775 | The parsed result of that run (R factors, geometry, seed, wall clock). |
| `validation/campaign/checks/G3_7R2H.json` | 4,667 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/fetch_7R2H.json` | 2,207 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/clash_altloc.json` | 4,311 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/clashscore.json` | 6,728 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/cycle_row.json` | 1,266 | The campaign's per-cycle record for this model (PROTOCOL §7). |
| `validation/campaign/dossier.json` | 147,106 | The campaign dossier: xtriage, model audit, composition hypothesis, baselines. |
| `validation/campaign/molprobity.out` | 34,626 | The campaign's MolProbity run on this model. |
| `validation/campaign/molprobity_result.json` | 9,083 | The campaign's MolProbity run on this model. |
| `validation/campaign/noise_floor.json` | 7,498 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/release/merge_mtz.log` | 396 | Log of the data+flags merge used by model_vs_data. |
| `validation/release/model_diff.json` | 458 | Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens. |
| `validation/release/model_vs_data.deposited.log` | 2,535 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/model_vs_data.refined.log` | 2,538 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/molprobity.deposited.log` | 49,735 | phenix.molprobity with default settings. |
| `validation/release/molprobity.deposited.out` | 37,271 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.log` | 44,921 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.out` | 31,828 | phenix.molprobity with default settings. |
| `validation/release/rfree_indep.deposited.json` | 643 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.deposited.log` | 1,096 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.json` | 647 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.log` | 1,102 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/summary.json` | 2,550 | Release-time validation of the deposited and refined models (parsed from the logs beside it). |
