# 9ARN — Structure and interactions of HIV-1 gp41 CHR-NHR reverse hairpin constructs reveal molecular determinants of antiviral activity

**Status: re-refined baseline, nothing credited.** See the caveats below.

| | |
|---|---|
| Resolution | 1.41 Å |
| Space group | H 3 2 |
| Data | amplitudes (FP,SIGFP), 15576 reflections |
| Free set | 771 reflections (4.9 %), inherited unchanged from the deposition; select / report halves 385 / 386 |
| Deposited refinement program | PHENIX |
| Released | 2025-03-05 |
| Primary citation | Structure and Interactions of HIV-1 gp41 CHR-NHR Reverse Hairpin Constructs Reveal Molecular Determinants of Antiviral Activity. (J.Mol.Biol. 2024), DOI 10.1016/j.jmb.2024.168650 |
| Thresholds version that judged the writing cycle | thresholds_v8 |
| Phenix | 2.1-6048 |

## R-free on the frozen flags

Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, no outlier rejection) and with `phenix.model_vs_data`. "Re-refined, no changes" is the mean of the campaign's ten noise-floor seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.

| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |
|---|---|---|---|---|---|
| Deposited, our flags | 0.2555 | 0.2952 | 0.3023 | 0.2875 | 0.2554 / 0.2949 |
| Re-refined, no changes (10 seeds) | — | 0.2983 ± 0.00363 | — | — | — |
| **This release** | **0.2562** | **0.2962** | 0.3012 | 0.2908 | 0.2562 / 0.2962 |

Δ full R-free vs deposited: **0.0010**; beyond re-refinement alone: **-0.0021** (-0.6 × the floor's own spread).
Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `noise_floor`): σ_select 0.00544, σ_report 0.00237, σ_full 0.00363; a cycle is credited at ΔR-free-select ≤ -0.01087 (k = 2.0).
Campaign ledger for this model (`refinement/current.json`): R-work 0.2562, R-free full 0.2963, select 0.3012, report 0.2909.

## Geometry and composition (phenix.molprobity, release time, default settings)

| | Deposited | This release |
|---|---|---|
| Atoms (hydrogens) | 654 (0) | 654 (0) |
| Waters | 38 | 38 |
| Altloc letters | A, B | A, B |
| Clashscore | 1.59 | 1.59 |
| Ramachandran outliers / favored (%) | 0.00 / 100.0 | 0.00 / 100.0 |
| Rotamer outliers (%) | 0.00 | 1.52 |
| Cβ deviations | 0 | 0 |
| RMS bonds (Å) / angles (°) | 0.0062 / 0.73 | 0.0060 / 0.70 |
| MolProbity score | 0.91 | 1.04 |

## What changed in the coordinates

No residue added or removed and no alternate conformation changed: the released model is the deposited model re-refined (coordinates, ADPs and occupancies moved, nothing else). `validation/release/model_diff.json`.

## What the campaign did

Refinement protocol of the released model: phenix.refine 2.1-6048, 5 macro-cycles, anisotropic ADPs, no hydrogens in the model, seed 1. ADP decision: n_refl/n_atoms(non-H)=23.82 >= 5.0 and d_min=1.4127 <= 1.5. The verbatim command is `refinement/command.txt`.

The released model is the cycle-0 baseline: one phenix.refine run on the deposited file with nothing changed (`baseline_rerefine`). The run that followed credited no change, so the standing record never moved (D484).

Cycles on record for this target: 8; credited: 0; changes proposed: 67 (`ledger/cycles.csv`, `ledger/changes.csv`).

## Caveats

- Nothing was credited on this target; the released model is the single Phenix re-refinement of the deposited file (D484). For CNS/REFMAC/X-PLOR-era depositions the campaign's noise floor measures convergence variance rather than test-set noise, so its credit bar was effectively unreachable (D506). The gain over the deposited file is what phenix.refine does on its own.

## Verify it yourself

```bash
# independent scorer (cctbx; needs Phenix)
phenix.python scripts/indep_rfree.py targets/9ARN/model/9ARN_refined.cif targets/9ARN/data/9ARN_data.mtz \
  targets/9ARN/data/9ARN_flags.mtz targets/9ARN/data/9ARN_split.mtz out.json
# standard tool
phenix.python scripts/merge_mtz.py targets/9ARN/data/9ARN_data.mtz targets/9ARN/data/9ARN_flags.mtz 9ARN_merged.mtz
phenix.model_vs_data targets/9ARN/model/9ARN_refined.cif 9ARN_merged.mtz
# look at it
coot targets/9ARN/model/9ARN_refined.pdb --auto targets/9ARN/maps/9ARN_refined_map_coeffs.mtz
```

## Provenance

- Campaign record `refinement/current.json`: cycle 0, stage `baseline_rerefine`, updated 2026-09-17T06:51:16+00:00.
- Model on the campaign pod: `/home/dev/runs/9ARN/c000/baseline_rerefine/refine_001.cif`.
- Data: `data.mtz` SHA-256 `49252437f6e3ee3b80f4bde7d2f8a5d278832c16fa512ba6ce251d1203c68abf`, `flags.mtz` SHA-256 `01abef3973eb9a308d9151af85bf49d8af7b9f59b026893d82c45a224d7b6b72`; built from the deposited structure-factor file with SHA-256 `07d93a472fc9bb7e03b56b48833bf8892153865ecc31e0e6c88ffb3e2846c4db` (`data/prep.json`).
- Deposited header claim: R-work 0.256, R-free 0.291, 771 free reflections.

## Files

| File | Size | What it is |
|---|---|---|
| `data/9ARN_data.mtz` | 315,120 | The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors. |
| `data/9ARN_flags.mtz` | 252,736 | The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free). |
| `data/9ARN_split.mtz` | 252,736 | The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work). |
| `data/prep.json` | 4,641 | How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims. |
| `data/split.json` | 22,437 | The same split as a list of reflections, with the seed that made it. |
| `deposited/9ARN.cif` | 192,510 | The deposited coordinate file as fetched from RCSB (the starting point). |
| `deposited/9ARN.fasta` | 164 | The entry's sequence as fetched from RCSB. |
| `deposited/FETCHED` | 76 | When the raw files were fetched. |
| `deposited/fetch_manifest.sha256` | 756 | SHA-256 of the raw files at fetch time. |
| `deposited/rcsb_entry.json` | 11,762 | The RCSB entry record (title, citation, experimental details) as fetched. |
| `ledger/bisections.csv` | 246 | Bisection steps when a cycle regressed. |
| `ledger/changes.csv` | 203,089 | Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict. |
| `ledger/checks.csv` | 3,283 | Gate results G0–G8. |
| `ledger/cycles.csv` | 7,030 | Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry. |
| `ledger/defects.csv` | 8,291 | Values that could not be computed, with the reason (never a sentinel). |
| `ledger/deviations.csv` | 17,709 | Decision-log rows that name this target. |
| `ledger/noise_floor.csv` | 1,330 | The noise-floor row that set the credit bar: σ of R-free on every set. |
| `ledger/rfree_consultations.csv` | 226 | How many times R-free-select was consulted (PROTOCOL §3.6). |
| `ledger/runs/9ARN.20260917T065213Z/DECISIONS.md` | 28,443 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/9ARN.20260917T065213Z/run_summary.json` | 2,504 | The per-run summary (cycles, credits, stop reason). |
| `ledger/solvent_disagreements.csv` | 120 | Phenix/Coot disagreements on solvent sites. |
| `maps/9ARN_refined_map_coeffs.mtz` | 1,088,672 | Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot). |
| `model/9ARN_refined.cif` | 111,928 | The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json. |
| `model/9ARN_refined.pdb` | 109,160 | The same model in PDB format, from the same run. |
| `refinement/command.txt` | 3,656 | The verbatim phenix.refine argv that wrote the model. |
| `refinement/current.json` | 349 | The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index. |
| `refinement/refine_001.eff` | 42,756 | The effective parameters of that run. |
| `refinement/refine_001.log` | 68,875 | The phenix.refine log of that run. |
| `refinement/refine_decisions.json` | 2,098 | The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels). |
| `refinement/refine_result.json` | 2,769 | The parsed result of that run (R factors, geometry, seed, wall clock). |
| `validation/campaign/checks/G3_9ARN.json` | 4,633 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/fetch_9ARN.json` | 2,207 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/clash_altloc.json` | 2,398 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/clashscore.json` | 4,663 | The campaign's clashscore runs (standard and altloc-aware). |
| `validation/campaign/cycle_row.json` | 1,262 | The campaign's per-cycle record for this model (PROTOCOL §7). |
| `validation/campaign/dossier.json` | 56,806 | The campaign dossier: xtriage, model audit, composition hypothesis, baselines. |
| `validation/campaign/molprobity.out` | 6,402 | The campaign's MolProbity run on this model. |
| `validation/campaign/molprobity_result.json` | 4,992 | The campaign's MolProbity run on this model. |
| `validation/campaign/noise_floor.json` | 7,522 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/verify_20260917/9ARN_baseline_rerefine.json` | 612 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/9ARN_current.json` | 612 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/9ARN_deposited.json` | 588 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/release/merge_mtz.log` | 394 | Log of the data+flags merge used by model_vs_data. |
| `validation/release/model_diff.json` | 446 | Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens. |
| `validation/release/model_vs_data.deposited.log` | 3,161 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/model_vs_data.refined.log` | 3,164 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/molprobity.deposited.log` | 15,078 | phenix.molprobity with default settings. |
| `validation/release/molprobity.deposited.out` | 3,631 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.log` | 15,474 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.out` | 3,631 | phenix.molprobity with default settings. |
| `validation/release/rfree_indep.deposited.json` | 629 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.deposited.log` | 1,082 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.json` | 632 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.log` | 1,087 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/summary.json` | 2,521 | Release-time validation of the deposited and refined models (parsed from the logs beside it). |
