# 6CDX — High-resolution crystal structure of fluoropropylated cystine knot, binding to alpha-5 beta-6 integrin

**Status: improved.** This model has a lower R-free than the deposited file on the same free set.

| | |
|---|---|
| Resolution | 1.0 Å |
| Space group | P 21 21 21 |
| Data | amplitudes (FP,SIGFP), 27006 reflections |
| Free set | 1341 reflections (5.0 %), inherited unchanged from the deposition; select / report halves 670 / 671 |
| Deposited refinement program | REFMAC |
| Released | 2019-08-14 |
| Primary citation | Evaluation of integrin alpha v beta6cystine knot PET tracers to detect cancer and idiopathic pulmonary fibrosis. (Nat Commun 2019), DOI 10.1038/s41467-019-11863-w |
| Thresholds version that judged the writing cycle | thresholds_v8 |
| Phenix | 2.1-6048 |

## R-free on the frozen flags

Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, no outlier rejection) and with `phenix.model_vs_data`. "Re-refined, no changes" is the mean of the campaign's ten noise-floor seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.

| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |
|---|---|---|---|---|---|
| Deposited, our flags | 0.1997 | 0.2258 | 0.2284 | 0.2233 | 0.1996 / 0.2267 |
| Re-refined, no changes (10 seeds) | — | 0.1901 ± 0.00050 | — | — | — |
| **This release** | **0.1430** | **0.1716** | 0.1708 | 0.1725 | 0.1430 / 0.1722 |

Δ full R-free vs deposited: **-0.0542**; beyond re-refinement alone: **-0.0184** (-36.9 × the floor's own spread).
Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `noise_floor`): σ_select 0.00055, σ_report 0.00063, σ_full 0.00050; a cycle is credited at ΔR-free-select ≤ -0.00110 (k = 2.0).
Campaign ledger for this model (`refinement/current.json`): R-work 0.1430, R-free full 0.1720, select 0.1722, report 0.1718.

## Geometry and composition (phenix.molprobity, release time, default settings)

| | Deposited | This release |
|---|---|---|
| Atoms (hydrogens) | 589 (0) | 630 (0) |
| Waters | 52 | 57 |
| Altloc letters | A, B | A, B, C |
| Clashscore | 9.56 | 20.68 |
| Ramachandran outliers / favored (%) | 0.00 / 94.1 | 0.00 / 95.6 |
| Rotamer outliers (%) | 1.79 | 1.67 |
| Cβ deviations | 0 | 0 |
| RMS bonds (Å) / angles (°) | 0.0259 / 2.25 | 0.0129 / 1.53 |
| MolProbity score | 2.09 | 2.29 |

## What changed in the coordinates

From `validation/release/model_diff.json` (deposited vs released, by chain and residue number):

- Waters added (8): B 5001, B 5002, B 5003, B 5004, B 5005, B 5006, B 5007, B 5008
- Waters removed (3): A 122, B 101, B 126
- Residues whose alternate-conformation letters changed (3): A 34 TYR -→AB, A 5 ASN -→ABC, B 20 ASP -→AB

## What the campaign did

Refinement protocol of the released model: phenix.refine 2.1-6048, 5 macro-cycles, anisotropic ADPs, no hydrogens in the model, seed 1. ADP decision: n_refl/n_atoms(non-H)=42.87 >= 5.0 and d_min=1.0 <= 1.5. The verbatim command is `refinement/command.txt`.

The released model was written by cycle 7 (`rerefine`, run `6CDX.20260917T052744Z`), verdict **rejected**, attributable ΔR-free-select 0.00282 against its paired null, ΔR-gap 0.00058; geometry flag: rota_outliers 1.67 > 1.5; clashscore 20.6835 > 5.
It is the base kept from bisection step `6CDX.c007.d0.R.01` of that cycle (ΔR-free-select -0.00032, not regressed), which carried: `6CDX.c007.protein_altloc_add.B20`, `6CDX.c007.protein_altloc_add.A5`, `6CDX.c007.protein_altloc_add.A34`.
That run ended: max_cycles=8 reached.

Cycles on record for this target: 12; credited: 2; changes proposed: 207 (`ledger/cycles.csv`, `ledger/changes.csv`).

Credited cycles on record, all runs and experiment lines. A credit is relative to that cycle's own paired null; not every credit moved the standing model (promotion rules D484/D499/D508), and experiment-line cycles judged candidates against their own base.

| Cycle | Run | Attributable ΔR-free-select | R-free full after | ΔR-gap vs null | Geometry flag |
|---|---|---|---|---|---|
| 2 | `6CDX.20260917T052744Z` | -0.00226 | 0.1810 | 0.00055 | rota_outliers 1.79 > 1.5; clashscore 19.1022 > 5 |
| 3 | `6CDX.20260917T052744Z` | -0.00876 | 0.1739 | -0.00335 | rota_outliers 1.79 > 1.5; clashscore 19.1022 > 5 |

## Caveats

- The phase-2 result (D509): waters added and removed in two credited cycles, then alternate conformations at A5, A34 and B20 plus one water kept from the surviving half of a bisected cycle 7 (un-credited, within noise). The released model is that cycle-7 base, the best of the run. The whole-model geometry monitor flagged it (rotamer outliers and clashscore above the frozen caps); the release MolProbity numbers above show the clashscore.

## Verify it yourself

```bash
# independent scorer (cctbx; needs Phenix)
phenix.python scripts/indep_rfree.py targets/6CDX/model/6CDX_refined.cif targets/6CDX/data/6CDX_data.mtz \
  targets/6CDX/data/6CDX_flags.mtz targets/6CDX/data/6CDX_split.mtz out.json
# standard tool
phenix.python scripts/merge_mtz.py targets/6CDX/data/6CDX_data.mtz targets/6CDX/data/6CDX_flags.mtz 6CDX_merged.mtz
phenix.model_vs_data targets/6CDX/model/6CDX_refined.cif 6CDX_merged.mtz
# look at it
coot targets/6CDX/model/6CDX_refined.pdb --auto targets/6CDX/maps/6CDX_refined_map_coeffs.mtz
```

## Provenance

- Campaign record `refinement/current.json`: cycle 8, stage `rerefine`, updated 2026-09-17T12:48:17+00:00.
- Model on the campaign pod: `/home/dev/runs/6CDX/runs/6CDX.20260917T052744Z/cycles/c007/bisect/6CDX.c007.d0.R.01/refine/refine_001.cif`.
- Data: `data.mtz` SHA-256 `5f734473c345ac4b0698263406190dc04789df1cee03e3b6862d4cc13eb04b92`, `flags.mtz` SHA-256 `69d950d1c5b9a7f3e84e22f4dc8f9941918cb3b157ca63083a94346fdfd93e69`; built from the deposited structure-factor file with SHA-256 `48d9dc980cc3224cbfa4cf952cb00e17d404f4d692aa66f3c31a42d873dd0145` (`data/prep.json`).
- Deposited header claim: R-work 0.203, R-free 0.226, 1341 free reflections.

## Files

| File | Size | What it is |
|---|---|---|
| `data/6CDX_data.mtz` | 542,600 | The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors. |
| `data/6CDX_flags.mtz` | 434,496 | The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free). |
| `data/6CDX_split.mtz` | 434,496 | The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work). |
| `data/prep.json` | 3,019 | How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims. |
| `data/split.json` | 37,733 | The same split as a list of reflections, with the seed that made it. |
| `deposited/6CDX.cif` | 121,932 | The deposited coordinate file as fetched from RCSB (the starting point). |
| `deposited/6CDX.fasta` | 123 | The entry's sequence as fetched from RCSB. |
| `deposited/FETCHED` | 76 | When the raw files were fetched. |
| `deposited/fetch_manifest.sha256` | 756 | SHA-256 of the raw files at fetch time. |
| `deposited/rcsb_entry.json` | 17,094 | The RCSB entry record (title, citation, experimental details) as fetched. |
| `ledger/bisections.csv` | 5,558 | Bisection steps when a cycle regressed. |
| `ledger/changes.csv` | 727,122 | Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict. |
| `ledger/checks.csv` | 3,055 | Gate results G0–G8. |
| `ledger/cycles.csv` | 10,849 | Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry. |
| `ledger/defects.csv` | 18,954 | Values that could not be computed, with the reason (never a sentinel). |
| `ledger/deviations.csv` | 12,499 | Decision-log rows that name this target. |
| `ledger/noise_floor.csv` | 1,343 | The noise-floor row that set the credit bar: σ of R-free on every set. |
| `ledger/rfree_consultations.csv` | 226 | How many times R-free-select was consulted (PROTOCOL §3.6). |
| `ledger/runs/6CDX.20260917T052744Z/DECISIONS.md` | 91,624 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/6CDX.20260917T052744Z/run_summary.json` | 2,244 | The per-run summary (cycles, credits, stop reason). |
| `ledger/solvent_disagreements.csv` | 120 | Phenix/Coot disagreements on solvent sites. |
| `maps/6CDX_refined_map_coeffs.mtz` | 1,792,320 | Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot). |
| `model/6CDX_refined.cif` | 111,964 | The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json. |
| `model/6CDX_refined.pdb` | 106,069 | The same model in PDB format, from the same run. |
| `refinement/command.txt` | 1,625 | The verbatim phenix.refine argv that wrote the model. |
| `refinement/current.json` | 494 | The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index. |
| `refinement/refine_001.eff` | 42,950 | The effective parameters of that run. |
| `refinement/refine_001.log` | 70,202 | The phenix.refine log of that run. |
| `refinement/refine_decisions.json` | 2,103 | The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels). |
| `refinement/refine_result.json` | 3,135 | The parsed result of that run (R factors, geometry, seed, wall clock). |
| `validation/campaign/checks/G3_6CDX.json` | 4,665 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/fetch_6CDX.json` | 2,207 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/dossier.json` | 60,990 | The campaign dossier: xtriage, model audit, composition hypothesis, baselines. |
| `validation/campaign/noise_floor.json` | 7,493 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/verify_20260917/6CDX_baseline_rerefine.json` | 617 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/6CDX_current.json` | 670 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260917/6CDX_deposited.json` | 525 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/release/merge_mtz.log` | 395 | Log of the data+flags merge used by model_vs_data. |
| `validation/release/model_diff.json` | 788 | Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens. |
| `validation/release/model_vs_data.deposited.log` | 2,201 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/model_vs_data.refined.log` | 2,205 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/molprobity.deposited.log` | 18,889 | phenix.molprobity with default settings. |
| `validation/release/molprobity.deposited.out` | 5,303 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.log` | 19,048 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.out` | 4,077 | phenix.molprobity with default settings. |
| `validation/release/rfree_indep.deposited.json` | 631 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.deposited.log` | 1,084 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.json` | 642 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.log` | 1,095 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/summary.json` | 2,539 | Release-time validation of the deposited and refined models (parsed from the logs beside it). |
