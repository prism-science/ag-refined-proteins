# 8C5N — Sub-atomic resolution structure of the chitin-binding protein D (CbpD) from Pseudomonas aeruginosa

**Status: re-refined baseline, nothing credited.** See the caveats below.

| | |
|---|---|
| Resolution | 0.75 Å |
| Space group | P 1 21 1 |
| Data | amplitudes (FP,SIGFP), 198461 reflections |
| Free set | 9968 reflections (5.0 %), inherited unchanged from the deposition; select / report halves 4984 / 4984 |
| Deposited refinement program | PHENIX, SHELXL |
| Released | 2023-06-28 |
| Primary citation | Immunization with lytic polysaccharide monooxygenase CbpD induces protective immunity against Pseudomonas aeruginosa pneumonia. (Proc.Natl.Acad.Sci.USA 2023), DOI 10.1073/pnas.2301538120 |
| Thresholds version that judged the writing cycle | thresholds_v8 |
| Phenix | 2.1-6048 |

## R-free on the frozen flags

Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, no outlier rejection) and with `phenix.model_vs_data`. "Re-refined, no changes" is the mean of the campaign's ten noise-floor seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.

| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |
|---|---|---|---|---|---|
| Deposited, our flags | 0.1480 | 0.1570 | 0.1531 | 0.1608 | 0.1478 / 0.1571 |
| Re-refined, no changes (10 seeds) | — | 0.1533 ± 0.00013 | — | — | — |
| **This release** | **0.1471** | **0.1533** | 0.1490 | 0.1575 | 0.1468 / 0.1533 |

Δ full R-free vs deposited: **-0.0037**; beyond re-refinement alone: **-0.0000** (-0.1 × the floor's own spread).
Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `noise_floor`): σ_select 0.00019, σ_report 0.00011, σ_full 0.00013; a cycle is credited at ΔR-free-select ≤ -0.00038 (k = 2.0).
Campaign ledger for this model (`refinement/current.json`): R-work 0.1471, R-free full 0.1535, select 0.1491, report 0.1578.

## Geometry and composition (phenix.molprobity, release time, default settings)

| | Deposited | This release |
|---|---|---|
| Atoms (hydrogens) | 2433 (665) | 2433 (665) |
| Waters | 161 | 161 |
| Altloc letters | A, B, C | A, B, C |
| Clashscore | 6.33 | 5.69 |
| Ramachandran outliers / favored (%) | 0.00 / 99.5 | 0.00 / 99.5 |
| Rotamer outliers (%) | 2.34 | 2.34 |
| Cβ deviations | 0 | 0 |
| RMS bonds (Å) / angles (°) | 0.0150 / 2.02 | 0.0117 / 1.41 |
| MolProbity score | 1.63 | 1.59 |

## What changed in the coordinates

No residue added or removed and no alternate conformation changed: the released model is the deposited model re-refined (coordinates, ADPs and occupancies moved, nothing else). `validation/release/model_diff.json`.

## What the campaign did

Refinement protocol of the released model: phenix.refine 2.1-6048, 5 macro-cycles, anisotropic ADPs, 665 riding hydrogens, seed 1. ADP decision: n_refl/n_atoms(non-H)=112.25 >= 5.0 and d_min=0.7499 <= 1.5. The verbatim command is `refinement/command.txt`.

The released model is the cycle-0 baseline: one phenix.refine run on the deposited file with nothing changed (`baseline_rerefine`). The run that followed credited no change, so the standing record never moved (D484).

Cycles on record for this target: 4; credited: 0; changes proposed: 20 (`ledger/cycles.csv`, `ledger/changes.csv`).

## Caveats

- Refined and scored against the deposited amplitudes (F_meas_au), not the merged intensities: French–Wilson conversion of the intensities drops 44 of the 9 968 inherited free reflections (D540). The free set itself (status 'f') is unchanged.
- The released model is one Phenix re-refinement of the deposited file; nothing the agent proposed has been credited yet (E044). Rotamer outliers 2.3 % in both the deposited and the released model, above the campaign's 1.5 % cap (pre-existing).
- The deposited model carries 665 hydrogens, an incomplete riding set; the released model keeps the deposited hydrogens.
- Nothing was credited on this target; the released model is the single Phenix re-refinement of the deposited file (D484). For CNS/REFMAC/X-PLOR-era depositions the campaign's noise floor measures convergence variance rather than test-set noise, so its credit bar was effectively unreachable (D506). The gain over the deposited file is what phenix.refine does on its own.

## Verify it yourself

```bash
# independent scorer (cctbx; needs Phenix)
phenix.python scripts/indep_rfree.py targets/8C5N/model/8C5N_refined.cif targets/8C5N/data/8C5N_data.mtz \
  targets/8C5N/data/8C5N_flags.mtz targets/8C5N/data/8C5N_split.mtz out.json
# standard tool
phenix.python scripts/merge_mtz.py targets/8C5N/data/8C5N_data.mtz targets/8C5N/data/8C5N_flags.mtz 8C5N_merged.mtz
phenix.model_vs_data targets/8C5N/model/8C5N_refined.cif 8C5N_merged.mtz
# look at it
coot targets/8C5N/model/8C5N_refined.pdb --auto targets/8C5N/maps/8C5N_refined_map_coeffs.mtz
```

## Provenance

- Campaign record `refinement/current.json`: cycle 0, stage `baseline_rerefine`, updated 2026-10-05T05:48:44+00:00.
- Model on the campaign pod: `/home/dev/runs/8C5N/c000/baseline_rerefine/refine_001.cif`.
- Data: `data.mtz` SHA-256 `c8b5afe5ac57978cdd1668e88e51aa9efb14db53cf23506080576de12e6529e6`, `flags.mtz` SHA-256 `d42d38db669cc6f6f286bbe2075b52e07a110251664fadd2de15521913f722df`; built from the deposited structure-factor file with SHA-256 `cc11957c6dd43d76fdb111eac90d206921c4809df310923d9b70fc8c4f79d0ff` (`data/prep.json`).
- Deposited header claim: R-work 0.154, R-free 0.163, 9879 free reflections.

## Files

| File | Size | What it is |
|---|---|---|
| `data/8C5N_data.mtz` | 3,971,540 | The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors. |
| `data/8C5N_flags.mtz` | 3,177,616 | The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free). |
| `data/8C5N_split.mtz` | 3,177,616 | The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work). |
| `data/prep.json` | 4,931 | How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims. |
| `data/split.json` | 287,300 | The same split as a list of reflections, with the seed that made it. |
| `deposited/8C5N.cif` | 520,623 | The deposited coordinate file as fetched from RCSB (the starting point). |
| `deposited/8C5N.fasta` | 275 | The entry's sequence as fetched from RCSB. |
| `deposited/FETCHED` | 76 | When the raw files were fetched. |
| `deposited/fetch_manifest.sha256` | 756 | SHA-256 of the raw files at fetch time. |
| `deposited/rcsb_entry.json` | 17,900 | The RCSB entry record (title, citation, experimental details) as fetched. |
| `ledger/bisections.csv` | 246 | Bisection steps when a cycle regressed. |
| `ledger/changes.csv` | 66,077 | Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict. |
| `ledger/checks.csv` | 3,466 | Gate results G0–G8. |
| `ledger/cycles.csv` | 3,504 | Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry. |
| `ledger/defects.csv` | 3,157 | Values that could not be computed, with the reason (never a sentinel). |
| `ledger/deviations.csv` | 924 | Decision-log rows that name this target. |
| `ledger/noise_floor.csv` | 1,333 | The noise-floor row that set the credit bar: σ of R-free on every set. |
| `ledger/rfree_consultations.csv` | 226 | How many times R-free-select was consulted (PROTOCOL §3.6). |
| `ledger/solvent_disagreements.csv` | 120 | Phenix/Coot disagreements on solvent sites. |
| `maps/8C5N_refined_map_coeffs.mtz` | 13,112,672 | Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot). |
| `model/8C5N_refined.cif` | 358,972 | The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json. |
| `model/8C5N_refined.pdb` | 341,096 | The same model in PDB format, from the same run. |
| `refinement/command.txt` | 3,688 | The verbatim phenix.refine argv that wrote the model. |
| `refinement/current.json` | 351 | The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index. |
| `refinement/refine_001.eff` | 42,674 | The effective parameters of that run. |
| `refinement/refine_001.log` | 79,900 | The phenix.refine log of that run. |
| `refinement/refine_decisions.json` | 2,145 | The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels). |
| `refinement/refine_result.json` | 2,774 | The parsed result of that run (R factors, geometry, seed, wall clock). |
| `validation/campaign/checks/G3_8C5N.json` | 6,499 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/fetch_8C5N.json` | 2,207 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/clash_altloc.json` | 11,220 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/clashscore.json` | 37,238 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/cycle_row.json` | 1,267 | The campaign's per-cycle record for this model (PROTOCOL §7). |
| `validation/campaign/dossier.json` | 107,694 | The campaign dossier: xtriage, model audit, composition hypothesis, baselines. |
| `validation/campaign/molprobity.out` | 18,378 | The campaign's MolProbity run on this model. |
| `validation/campaign/molprobity_result.json` | 7,630 | The campaign's MolProbity run on this model. |
| `validation/campaign/noise_floor.json` | 7,564 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/release/merge_mtz.log` | 396 | Log of the data+flags merge used by model_vs_data. |
| `validation/release/model_diff.json` | 458 | Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens. |
| `validation/release/model_vs_data.deposited.log` | 2,454 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/model_vs_data.refined.log` | 3,646 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/molprobity.deposited.log` | 31,033 | phenix.molprobity with default settings. |
| `validation/release/molprobity.deposited.out` | 17,155 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.log` | 30,501 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.out` | 15,860 | phenix.molprobity with default settings. |
| `validation/release/rfree_indep.deposited.json` | 647 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.deposited.log` | 1,098 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.json` | 650 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.log` | 1,103 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/summary.json` | 2,565 | Release-time validation of the deposited and refined models (parsed from the logs beside it). |
