# 1LZ9 — ANOMALOUS SIGNAL OF SOLVENT BROMINES USED FOR PHASING OF LYSOZYME

**Status: re-refined baseline, nothing credited.** See the caveats below.

| | |
|---|---|
| Resolution | 1.7 Å |
| Space group | P 43 21 2 |
| Data | amplitudes (FP,SIGFP), 13308 reflections |
| Free set | 1318 reflections (9.9 %), inherited unchanged from the deposition; select / report halves 659 / 659 |
| Deposited refinement program | REFMAC |
| Released | 1999-05-26 |
| Primary citation | Anomalous signal of solvent bromides used for phasing of lysozyme. (J.Mol.Biol. 1999), DOI 10.1006/jmbi.1999.2744 |
| Thresholds version that judged the writing cycle | thresholds_v8 |
| Phenix | 2.1-6048 |

## R-free on the frozen flags

Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, no outlier rejection) and with `phenix.model_vs_data`. "Re-refined, no changes" is the mean of the campaign's ten noise-floor seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.

| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |
|---|---|---|---|---|---|
| Deposited, our flags | 0.2012 | 0.2738 | 0.2825 | 0.2649 | 0.2010 / 0.2740 |
| Re-refined, no changes (10 seeds) | — | 0.2758 ± 0.00557 | — | — | — |
| **This release** | **0.2318** | **0.2822** | 0.2950 | 0.2690 | 0.2320 / 0.2823 |

Δ full R-free vs deposited: **0.0084**; beyond re-refinement alone: **0.0064** (+1.2 × the floor's own spread).
Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `noise_floor`): σ_select 0.00590, σ_report 0.00532, σ_full 0.00557; a cycle is credited at ΔR-free-select ≤ -0.01179 (k = 2.0).
Campaign ledger for this model (`refinement/current.json`): R-work 0.2318, R-free full 0.2819, select 0.2941, report 0.2693.

## Geometry and composition (phenix.molprobity, release time, default settings)

| | Deposited | This release |
|---|---|---|
| Atoms (hydrogens) | 1214 (0) | 1214 (0) |
| Waters | 197 | 197 |
| Altloc letters | A, B | A, B |
| Clashscore | 7.57 | 3.54 |
| Ramachandran outliers / favored (%) | 0.00 / 96.1 | 0.00 / 98.4 |
| Rotamer outliers (%) | 2.78 | 1.85 |
| Cβ deviations | 21 | 0 |
| RMS bonds (Å) / angles (°) | 0.0623 / 4.41 | 0.0078 / 1.00 |
| MolProbity score | 2.02 | 1.35 |

## What changed in the coordinates

No residue added or removed and no alternate conformation changed: the released model is the deposited model re-refined (coordinates, ADPs and occupancies moved, nothing else). `validation/release/model_diff.json`.

## What the campaign did

Refinement protocol of the released model: phenix.refine 2.1-6048, 5 macro-cycles, isotropic ADPs with 9 TLS groups, no hydrogens in the model, seed 1. ADP decision: n_refl/n_atoms(non-H)=10.96 / d_min=1.7: isotropic; TLS (d_min>=2.0 or chain>200 res). The verbatim command is `refinement/command.txt`.

The released model is the cycle-0 baseline: one phenix.refine run on the deposited file with nothing changed (`baseline_rerefine`). The run that followed credited no change, so the standing record never moved (D484).

Cycles on record for this target: 8; credited: 0; changes proposed: 48 (`ledger/cycles.csv`, `ledger/changes.csv`).

## Caveats

- Nothing was credited on this target; the released model is the single Phenix re-refinement of the deposited file (D484). For CNS/REFMAC/X-PLOR-era depositions the campaign's noise floor measures convergence variance rather than test-set noise, so its credit bar was effectively unreachable (D506). The gain over the deposited file is what phenix.refine does on its own.

## Verify it yourself

```bash
# independent scorer (cctbx; needs Phenix)
phenix.python scripts/indep_rfree.py targets/1LZ9/model/1LZ9_refined.cif targets/1LZ9/data/1LZ9_data.mtz \
  targets/1LZ9/data/1LZ9_flags.mtz targets/1LZ9/data/1LZ9_split.mtz out.json
# standard tool
phenix.python scripts/merge_mtz.py targets/1LZ9/data/1LZ9_data.mtz targets/1LZ9/data/1LZ9_flags.mtz 1LZ9_merged.mtz
phenix.model_vs_data targets/1LZ9/model/1LZ9_refined.cif 1LZ9_merged.mtz
# look at it
coot targets/1LZ9/model/1LZ9_refined.pdb --auto targets/1LZ9/maps/1LZ9_refined_map_coeffs.mtz
```

## Provenance

- Campaign record `refinement/current.json`: cycle 0, stage `baseline_rerefine`, updated 2026-09-17T05:37:32+00:00.
- Model on the campaign pod: `/home/dev/runs/1LZ9/c000/baseline_rerefine/refine_001.cif`.
- Data: `data.mtz` SHA-256 `c2151e45223b21ceda3fbd0f92aef4cd57ec3294bad307835cc88ce08b0df187`, `flags.mtz` SHA-256 `fc985ebb6303f1aa29b0aa17162840ed5334a182459ef461ded73f7a17bc360a`; built from the deposited structure-factor file with SHA-256 `697dd89e8cc4ba5d5c153465fdfa3071a1f8c86535fb45999a6352f7b6a94abb` (`data/prep.json`).
- Deposited header claim: R-work 0.210, R-free 0.290, 1318 free reflections.

## Files

| File | Size | What it is |
|---|---|---|
| `data/1LZ9_data.mtz` | 268,960 | The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors. |
| `data/1LZ9_flags.mtz` | 215,648 | The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free). |
| `data/1LZ9_split.mtz` | 215,648 | The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work). |
| `data/prep.json` | 2,963 | How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims. |
| `data/split.json` | 37,180 | The same split as a list of reflections, with the seed that made it. |
| `deposited/1LZ9.cif` | 186,904 | The deposited coordinate file as fetched from RCSB (the starting point). |
| `deposited/1LZ9.fasta` | 186 | The entry's sequence as fetched from RCSB. |
| `deposited/FETCHED` | 76 | When the raw files were fetched. |
| `deposited/fetch_manifest.sha256` | 756 | SHA-256 of the raw files at fetch time. |
| `deposited/rcsb_entry.json` | 16,650 | The RCSB entry record (title, citation, experimental details) as fetched. |
| `ledger/bisections.csv` | 246 | Bisection steps when a cycle regressed. |
| `ledger/changes.csv` | 170,559 | Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict. |
| `ledger/checks.csv` | 3,052 | Gate results G0–G8. |
| `ledger/cycles.csv` | 6,019 | Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry. |
| `ledger/defects.csv` | 11,333 | Values that could not be computed, with the reason (never a sentinel). |
| `ledger/deviations.csv` | 9,729 | Decision-log rows that name this target. |
| `ledger/noise_floor.csv` | 1,335 | The noise-floor row that set the credit bar: σ of R-free on every set. |
| `ledger/rfree_consultations.csv` | 226 | How many times R-free-select was consulted (PROTOCOL §3.6). |
| `ledger/runs/1LZ9.20260917T053914Z/DECISIONS.md` | 25,852 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/1LZ9.20260917T053914Z/run_summary.json` | 3,116 | The per-run summary (cycles, credits, stop reason). |
| `ledger/solvent_disagreements.csv` | 120 | Phenix/Coot disagreements on solvent sites. |
| `maps/1LZ9_refined_map_coeffs.mtz` | 859,072 | Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot). |
| `model/1LZ9_refined.cif` | 197,477 | The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json. |
| `model/1LZ9_refined.pdb` | 191,495 | The same model in PDB format, from the same run. |
| `refinement/command.txt` | 4,360 | The verbatim phenix.refine argv that wrote the model. |
| `refinement/current.json` | 351 | The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index. |
| `refinement/refine_001.eff` | 43,120 | The effective parameters of that run. |
| `refinement/refine_001.log` | 195,026 | The phenix.refine log of that run. |
| `refinement/refine_decisions.json` | 2,546 | The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels). |
| `refinement/refine_result.json` | 3,849 | The parsed result of that run (R factors, geometry, seed, wall clock). |
| `validation/campaign/checks/G3_1LZ9.json` | 4,593 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/fetch_1LZ9.json` | 2,207 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/clash_altloc.json` | 4,627 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/clashscore.json` | 14,988 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/cycle_row.json` | 1,252 | The campaign's per-cycle record for this model (PROTOCOL §7). |
| `validation/campaign/dossier.json` | 69,381 | The campaign dossier: xtriage, model audit, composition hypothesis, baselines. |
| `validation/campaign/molprobity.out` | 13,668 | The campaign's MolProbity run on this model. |
| `validation/campaign/molprobity_result.json` | 6,922 | The campaign's MolProbity run on this model. |
| `validation/campaign/noise_floor.json` | 7,404 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/verify_20260917/1LZ9_baseline_rerefine.json` | 618 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/1LZ9_current.json` | 618 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/1LZ9_deposited.json` | 595 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/release/merge_mtz.log` | 395 | Log of the data+flags merge used by model_vs_data. |
| `validation/release/model_diff.json` | 452 | Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens. |
| `validation/release/model_vs_data.deposited.log` | 2,198 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/model_vs_data.refined.log` | 2,207 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/molprobity.deposited.log` | 37,303 | phenix.molprobity with default settings. |
| `validation/release/molprobity.deposited.out` | 25,298 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.log` | 16,446 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.out` | 3,943 | phenix.molprobity with default settings. |
| `validation/release/rfree_indep.deposited.json` | 636 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.deposited.log` | 1,089 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.json` | 638 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.log` | 1,093 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/summary.json` | 2,534 | Release-time validation of the deposited and refined models (parsed from the logs beside it). |
