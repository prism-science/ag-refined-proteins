# 9D5Y — Nitrile hydratase S112T mutant

**Status: re-refined baseline, nothing credited.** See the caveats below.

| | |
|---|---|
| Resolution | 1.35 Å |
| Space group | P 32 2 1 |
| Data | intensities (IMEAN,SIGIMEAN), 102067 reflections |
| Free set | 2006 reflections (2.0 %), inherited unchanged from the deposition; select / report halves 1003 / 1003 |
| Deposited refinement program | PHENIX |
| Released | 2024-11-06 |
| Primary citation | Catalytic and post-translational maturation roles of a conserved active site serine residue in nitrile hydratases. (J.Inorg.Biochem. 2024), DOI 10.1016/j.jinorgbio.2024.112763 |
| Thresholds version that judged the writing cycle | thresholds_v8 |
| Phenix | 2.1-6048 |

## R-free on the frozen flags

Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, no outlier rejection) and with `phenix.model_vs_data`. "Re-refined, no changes" is the mean of the campaign's ten noise-floor seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.

| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |
|---|---|---|---|---|---|
| Deposited, our flags | 0.2528 | 0.2888 | 0.2840 | 0.2936 | 0.2531 / 0.2889 |
| Re-refined, no changes (10 seeds) | — | 0.2347 ± 0.00019 | — | — | — |
| **This release** | **0.2111** | **0.2342** | 0.2273 | 0.2412 | 0.2114 / 0.2346 |

Δ full R-free vs deposited: **-0.0546**; beyond re-refinement alone: **-0.0005** (-2.6 × the floor's own spread).
Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `noise_floor`): σ_select 0.00074, σ_report 0.00081, σ_full 0.00019; a cycle is credited at ΔR-free-select ≤ -0.00149 (k = 2.0).
Campaign ledger for this model (`refinement/current.json`): R-work 0.2111, R-free full 0.2344, select 0.2277, report 0.2412.

## Geometry and composition (phenix.molprobity, release time, default settings)

| | Deposited | This release |
|---|---|---|
| Atoms (hydrogens) | 3726 (8) | 3726 (8) |
| Waters | 242 | 242 |
| Altloc letters | A, B | A, B |
| Clashscore | 11.12 | 3.51 |
| Ramachandran outliers / favored (%) | 0.24 / 96.9 | 0.24 / 97.4 |
| Rotamer outliers (%) | 0.27 | 1.08 |
| Cβ deviations | 0 | 0 |
| RMS bonds (Å) / angles (°) | 0.0097 / 1.37 | 0.0074 / 0.94 |
| MolProbity score | 1.74 | 1.28 |

## What changed in the coordinates

No residue added or removed and no alternate conformation changed: the released model is the deposited model re-refined (coordinates, ADPs and occupancies moved, nothing else). `validation/release/model_diff.json`.

## What the campaign did

Refinement protocol of the released model: phenix.refine 2.1-6048, 5 macro-cycles, anisotropic ADPs, 8 riding hydrogens, seed 1. ADP decision: n_refl/n_atoms(non-H)=27.45 >= 5.0 and d_min=1.35 <= 1.5. The verbatim command is `refinement/command.txt`.

The released model is the cycle-0 baseline: one phenix.refine run on the deposited file with nothing changed (`baseline_rerefine`). The run that followed credited no change, so the standing record never moved (D484).

Cycles on record for this target: 7; credited: 0; changes proposed: 52 (`ledger/cycles.csv`, `ledger/changes.csv`).

## Caveats

- Nothing was credited on this target; the released model is the single Phenix re-refinement of the deposited file (D484). For CNS/REFMAC/X-PLOR-era depositions the campaign's noise floor measures convergence variance rather than test-set noise, so its credit bar was effectively unreachable (D506). The gain over the deposited file is what phenix.refine does on its own.

## Verify it yourself

```bash
# independent scorer (cctbx; needs Phenix)
phenix.python scripts/indep_rfree.py targets/9D5Y/model/9D5Y_refined.cif targets/9D5Y/data/9D5Y_data.mtz \
  targets/9D5Y/data/9D5Y_flags.mtz targets/9D5Y/data/9D5Y_split.mtz out.json
# standard tool
phenix.python scripts/merge_mtz.py targets/9D5Y/data/9D5Y_data.mtz targets/9D5Y/data/9D5Y_flags.mtz 9D5Y_merged.mtz
phenix.model_vs_data targets/9D5Y/model/9D5Y_refined.cif 9D5Y_merged.mtz
# look at it
coot targets/9D5Y/model/9D5Y_refined.pdb --auto targets/9D5Y/maps/9D5Y_refined_map_coeffs.mtz
```

## Provenance

- Campaign record `refinement/current.json`: cycle 0, stage `baseline_rerefine`, updated 2026-09-17T09:58:20+00:00.
- Model on the campaign pod: `/home/dev/runs/9D5Y/c000/baseline_rerefine/refine_001.cif`.
- Data: `data.mtz` SHA-256 `f1d9e5a41af0b028daec88c2eab0160683359ea6abc3e92c853882b02ba8c938`, `flags.mtz` SHA-256 `255ccbf4e14f535de4818ae21fe8d01f566f1439038522fadeb9e7ba9013f8e6`; built from the deposited structure-factor file with SHA-256 `41632145828344c92d762f6b3c9bd1b258618412faec9e58c1c420de76e96c46` (`data/prep.json`).
- Deposited header claim: R-work 0.231, R-free 0.266, 2017 free reflections.

## Files

| File | Size | What it is |
|---|---|---|
| `data/9D5Y_data.mtz` | 2,043,980 | The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors. |
| `data/9D5Y_flags.mtz` | 1,635,632 | The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free). |
| `data/9D5Y_split.mtz` | 1,635,632 | The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work). |
| `data/prep.json` | 3,391 | How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims. |
| `data/split.json` | 58,065 | The same split as a list of reflections, with the seed that made it. |
| `deposited/9D5Y.cif` | 753,817 | The deposited coordinate file as fetched from RCSB (the starting point). |
| `deposited/9D5Y.fasta` | 633 | The entry's sequence as fetched from RCSB. |
| `deposited/FETCHED` | 76 | When the raw files were fetched. |
| `deposited/fetch_manifest.sha256` | 756 | SHA-256 of the raw files at fetch time. |
| `deposited/rcsb_entry.json` | 11,199 | The RCSB entry record (title, citation, experimental details) as fetched. |
| `ledger/bisections.csv` | 2,473 | Bisection steps when a cycle regressed. |
| `ledger/changes.csv` | 216,585 | Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict. |
| `ledger/checks.csv` | 3,295 | Gate results G0–G8. |
| `ledger/cycles.csv` | 5,190 | Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry. |
| `ledger/defects.csv` | 1,054 | Values that could not be computed, with the reason (never a sentinel). |
| `ledger/deviations.csv` | 11,187 | Decision-log rows that name this target. |
| `ledger/noise_floor.csv` | 1,336 | The noise-floor row that set the credit bar: σ of R-free on every set. |
| `ledger/rfree_consultations.csv` | 226 | How many times R-free-select was consulted (PROTOCOL §3.6). |
| `ledger/runs/9D5Y.20260917T095827Z/DECISIONS.md` | 22,840 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/9D5Y.20260917T095827Z/run_summary.json` | 2,174 | The per-run summary (cycles, credits, stop reason). |
| `ledger/solvent_disagreements.csv` | 120 | Phenix/Coot disagreements on solvent sites. |
| `maps/9D5Y_refined_map_coeffs.mtz` | 6,646,624 | Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot). |
| `model/9D5Y_refined.cif` | 618,907 | The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json. |
| `model/9D5Y_refined.pdb` | 597,156 | The same model in PDB format, from the same run. |
| `refinement/command.txt` | 3,670 | The verbatim phenix.refine argv that wrote the model. |
| `refinement/current.json` | 347 | The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index. |
| `refinement/refine_001.eff` | 42,681 | The effective parameters of that run. |
| `refinement/refine_001.log` | 75,935 | The phenix.refine log of that run. |
| `refinement/refine_decisions.json` | 2,108 | The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels). |
| `refinement/refine_result.json` | 2,779 | The parsed result of that run (R factors, geometry, seed, wall clock). |
| `validation/campaign/checks/G3_9D5Y.json` | 6,366 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/fetch_9D5Y.json` | 2,207 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/clash_altloc.json` | 11,932 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/clashscore.json` | 49,817 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/cycle_row.json` | 1,263 | The campaign's per-cycle record for this model (PROTOCOL §7). |
| `validation/campaign/dossier.json` | 138,181 | The campaign dossier: xtriage, model audit, composition hypothesis, baselines. |
| `validation/campaign/molprobity.out` | 34,669 | The campaign's MolProbity run on this model. |
| `validation/campaign/molprobity_result.json` | 11,359 | The campaign's MolProbity run on this model. |
| `validation/campaign/noise_floor.json` | 7,462 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/verify_20260917/9D5Y_baseline_rerefine.json` | 682 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/9D5Y_current.json` | 682 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/9D5Y_deposited.json` | 651 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/release/merge_mtz.log` | 399 | Log of the data+flags merge used by model_vs_data. |
| `validation/release/model_diff.json` | 452 | Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens. |
| `validation/release/model_vs_data.deposited.log` | 3,409 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/model_vs_data.refined.log` | 3,488 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/molprobity.deposited.log` | 44,320 | phenix.molprobity with default settings. |
| `validation/release/molprobity.deposited.out` | 32,090 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.log` | 45,222 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.out` | 31,973 | phenix.molprobity with default settings. |
| `validation/release/rfree_indep.deposited.json` | 692 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.deposited.log` | 1,145 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.json` | 702 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.log` | 1,157 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/summary.json` | 2,660 | Release-time validation of the deposited and refined models (parsed from the logs beside it). |
