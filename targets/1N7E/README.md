# 1N7E — Crystal structure of the sixth PDZ domain of GRIP1

**Status: improved.** This model has a lower R-free than the deposited file on the same free set.

| | |
|---|---|
| Resolution | 1.5 Å |
| Space group | P 65 2 2 |
| Data | amplitudes (FP,SIGFP), 17694 reflections |
| Free set | 1733 reflections (9.8 %), inherited unchanged from the deposition; select / report halves 866 / 867 |
| Deposited refinement program | CNS |
| Released | 2003-08-12 |
| Primary citation | Crystal structure of GRIP1 PDZ6-peptide complex reveals the structural basis for class II PDZ target recognition and PDZ domain-mediated multimerization (J.BIOL.CHEM. 2003), DOI 10.1074/jbc.M212263200 |
| Thresholds version that judged the writing cycle | thresholds_v8 |
| Phenix | 2.1-6048 |

## R-free on the frozen flags

Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, no outlier rejection) and with `phenix.model_vs_data`. "Re-refined, no changes" is the mean of the campaign's ten noise-floor seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.

| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |
|---|---|---|---|---|---|
| Deposited, our flags | 0.2491 | 0.2746 | 0.2882 | 0.2620 | 0.2491 / 0.2744 |
| Re-refined, no changes (10 seeds) | — | 0.2474 ± 0.00089 | — | — | — |
| **This release** | **0.2031** | **0.2447** | 0.2458 | 0.2437 | 0.2031 / 0.2448 |

Δ full R-free vs deposited: **-0.0299**; beyond re-refinement alone: **-0.0027** (-3.0 × the floor's own spread).
Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `noise_floor`): σ_select 0.00146, σ_report 0.00080, σ_full 0.00089; a cycle is credited at ΔR-free-select ≤ -0.00292 (k = 2.0).
Campaign ledger for this model (`refinement/current.json`): R-work 0.2031, R-free full 0.2446, select 0.2461, report 0.2433.

## Geometry and composition (phenix.molprobity, release time, default settings)

| | Deposited | This release |
|---|---|---|
| Atoms (hydrogens) | 841 (0) | 836 (0) |
| Waters | 141 | 136 |
| Altloc letters | none | none |
| Clashscore | 13.30 | 8.40 |
| Ramachandran outliers / favored (%) | 0.00 / 97.8 | 0.00 / 100.0 |
| Rotamer outliers (%) | 1.32 | 1.32 |
| Cβ deviations | 0 | 0 |
| RMS bonds (Å) / angles (°) | 0.0063 / 1.41 | 0.0147 / 1.45 |
| MolProbity score | 1.76 | 1.54 |

## What changed in the coordinates

From `validation/release/model_diff.json` (deposited vs released, by chain and residue number):

- Waters removed (5): A 141, A 66, A 70, A 73, A 84

## What the campaign did

Refinement protocol of the released model: phenix.refine 2.1-6048, 5 macro-cycles, isotropic ADPs with 7 TLS groups, no hydrogens in the model, seed 1. ADP decision: n_refl/n_atoms(non-H)=21.17 / d_min=1.5001: isotropic; TLS (d_min>=2.0 or chain>200 res). The verbatim command is `refinement/command.txt`.

The released model was written by cycle 1 (`rerefine`, run `1N7E.20260917T054928Z`), verdict **accepted**, attributable ΔR-free-select -0.00553 against its paired null, ΔR-gap -0.00086.
That run ended: converged (PROTOCOL §4.6): 3 quiet cycles; ΔR-free-select span 0.00290 within 2.0·σ.

Cycles on record for this target: 8; credited: 1; changes proposed: 67 (`ledger/cycles.csv`, `ledger/changes.csv`).

Credited cycles on record, all runs and experiment lines. A credit is relative to that cycle's own paired null; not every credit moved the standing model (promotion rules D484/D499/D508), and experiment-line cycles judged candidates against their own base.

| Cycle | Run | Attributable ΔR-free-select | R-free full after | ΔR-gap vs null | Geometry flag |
|---|---|---|---|---|---|
| 1 | `1N7E.20260917T054928Z` | -0.00553 | 0.2446 | -0.00086 |  |

## Caveats

- One credit: five waters removed. −0.003 beyond re-refinement at 3σ (D509).

## Verify it yourself

```bash
# independent scorer (cctbx; needs Phenix)
phenix.python scripts/indep_rfree.py targets/1N7E/model/1N7E_refined.cif targets/1N7E/data/1N7E_data.mtz \
  targets/1N7E/data/1N7E_flags.mtz targets/1N7E/data/1N7E_split.mtz out.json
# standard tool
phenix.python scripts/merge_mtz.py targets/1N7E/data/1N7E_data.mtz targets/1N7E/data/1N7E_flags.mtz 1N7E_merged.mtz
phenix.model_vs_data targets/1N7E/model/1N7E_refined.cif 1N7E_merged.mtz
# look at it
coot targets/1N7E/model/1N7E_refined.pdb --auto targets/1N7E/maps/1N7E_refined_map_coeffs.mtz
```

## Provenance

- Campaign record `refinement/current.json`: cycle 4, stage `rerefine`, updated 2026-09-17T08:10:00+00:00.
- Model on the campaign pod: `/home/dev/runs/1N7E/runs/1N7E.20260917T054928Z/cycles/c001/paired/candidate_arm/refine_001.cif`.
- Data: `data.mtz` SHA-256 `5b252b20c94b1cd8f3f43fb1e6401e9589c4a9425fd98dc8598e136d32cf1fad`, `flags.mtz` SHA-256 `e9f3fbbb5ba20bef3e586f4ded9a48ba18c7c6aaa059c2172d636d827995287f`; built from the deposited structure-factor file with SHA-256 `b794902abca70358cf773bb074cb449d7d42a591cf4f187e36797468f5f6c7cf` (`data/prep.json`).
- Deposited header claim: R-work 0.254, R-free 0.278, 1733 free reflections.

## Files

| File | Size | What it is |
|---|---|---|
| `data/1N7E_data.mtz` | 357,000 | The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors. |
| `data/1N7E_flags.mtz` | 286,144 | The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free). |
| `data/1N7E_split.mtz` | 286,144 | The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work). |
| `data/prep.json` | 3,022 | How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims. |
| `data/split.json` | 48,550 | The same split as a list of reflections, with the seed that made it. |
| `deposited/1N7E.cif` | 128,631 | The deposited coordinate file as fetched from RCSB (the starting point). |
| `deposited/1N7E.fasta` | 179 | The entry's sequence as fetched from RCSB. |
| `deposited/FETCHED` | 76 | When the raw files were fetched. |
| `deposited/fetch_manifest.sha256` | 756 | SHA-256 of the raw files at fetch time. |
| `deposited/rcsb_entry.json` | 12,385 | The RCSB entry record (title, citation, experimental details) as fetched. |
| `ledger/bisections.csv` | 246 | Bisection steps when a cycle regressed. |
| `ledger/changes.csv` | 262,561 | Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict. |
| `ledger/checks.csv` | 3,055 | Gate results G0–G8. |
| `ledger/cycles.csv` | 6,953 | Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry. |
| `ledger/defects.csv` | 97 | Values that could not be computed, with the reason (never a sentinel). |
| `ledger/deviations.csv` | 14,811 | Decision-log rows that name this target. |
| `ledger/noise_floor.csv` | 1,338 | The noise-floor row that set the credit bar: σ of R-free on every set. |
| `ledger/rfree_consultations.csv` | 226 | How many times R-free-select was consulted (PROTOCOL §3.6). |
| `ledger/runs/1N7E.20260917T054928Z/DECISIONS.md` | 33,355 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/1N7E.20260917T054928Z/run_summary.json` | 3,282 | The per-run summary (cycles, credits, stop reason). |
| `ledger/solvent_disagreements.csv` | 120 | Phenix/Coot disagreements on solvent sites. |
| `maps/1N7E_refined_map_coeffs.mtz` | 1,180,288 | Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot). |
| `model/1N7E_refined.cif` | 136,381 | The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json. |
| `model/1N7E_refined.pdb` | 134,371 | The same model in PDB format, from the same run. |
| `refinement/command.txt` | 2,077 | The verbatim phenix.refine argv that wrote the model. |
| `refinement/current.json` | 471 | The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index. |
| `refinement/experiment_paired_cycle.json` | 7,379 | Record of the experiment cycle that produced this model (paired null control, geometry of both arms). |
| `refinement/model_vs_data.campaign.log` | 3,290 | phenix.model_vs_data as run by the campaign on this model. |
| `refinement/refine_001.eff` | 43,139 | The effective parameters of that run. |
| `refinement/refine_001.log` | 175,955 | The phenix.refine log of that run. |
| `refinement/refine_decisions.json` | 2,774 | The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels). |
| `refinement/refine_result.json` | 4,039 | The parsed result of that run (R factors, geometry, seed, wall clock). |
| `validation/campaign/checks/G3_1N7E.json` | 4,614 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/fetch_1N7E.json` | 2,207 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/dossier.json` | 50,365 | The campaign dossier: xtriage, model audit, composition hypothesis, baselines. |
| `validation/campaign/noise_floor.json` | 7,491 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/verify_20260917/1N7E_baseline_rerefine.json` | 605 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/1N7E_current.json` | 575 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/1N7E_deposited.json` | 511 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/release/merge_mtz.log` | 395 | Log of the data+flags merge used by model_vs_data. |
| `validation/release/model_diff.json` | 500 | Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens. |
| `validation/release/model_vs_data.deposited.log` | 2,366 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/model_vs_data.refined.log` | 3,482 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/molprobity.deposited.log` | 14,428 | phenix.molprobity with default settings. |
| `validation/release/molprobity.deposited.out` | 3,588 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.log` | 15,315 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.out` | 3,759 | phenix.molprobity with default settings. |
| `validation/release/rfree_indep.deposited.json` | 617 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.deposited.log` | 1,077 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.json` | 623 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.log` | 1,085 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/summary.json` | 2,484 | Release-time validation of the deposited and refined models (parsed from the logs beside it). |
