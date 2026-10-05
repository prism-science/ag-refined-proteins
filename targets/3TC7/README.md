# 3TC7 — Crystal Structure of Engineered Protein. Northeast Structural Genomics Consortium Target OR62.

**Status: improved.** This model has a lower R-free than the deposited file on the same free set.

| | |
|---|---|
| Resolution | 1.5 Å |
| Space group | P 31 2 1 |
| Data | amplitudes (FP,SIGFP), 41052 reflections |
| Free set | 2075 reflections (5.1 %), inherited unchanged from the deposition; select / report halves 1037 / 1038 |
| Deposited refinement program | PHENIX |
| Released | 2011-08-24 |
| Primary citation | Exploration of alternate catalytic mechanisms and optimization strategies for retroaldolase design. (J.Mol.Biol. 2014), DOI 10.1016/j.jmb.2013.10.012 |
| Thresholds version that judged the writing cycle | thresholds_v9 |
| Phenix | 2.1-6048 |

## R-free on the frozen flags

Both models scored at release time with the independent scorer (`scripts/indep_rfree.py`, cctbx fmodel on all reflections, no outlier rejection) and with `phenix.model_vs_data`. "Re-refined, no changes" is the mean of the campaign's ten noise-floor seeds: phenix.refine on the deposited file with nothing changed, under the campaign's protocol.

| Model | R-work | R-free full | select | report | model_vs_data R-work / R-free |
|---|---|---|---|---|---|
| Deposited, our flags | 0.1535 | 0.1916 | 0.1938 | 0.1893 | 0.1535 / 0.1914 |
| Re-refined, no changes (10 seeds) | — | 0.1885 ± 0.00204 | — | — | — |
| **This release** | **0.1350** | **0.1717** | 0.1755 | 0.1677 | 0.1350 / 0.1717 |

Δ full R-free vs deposited: **-0.0200**; beyond re-refinement alone: **-0.0168** (-8.2 × the floor's own spread).
Credit bar used by the campaign on this target (`ledger/noise_floor.csv`, protocol `noise_floor_h_wxu003`): σ_select 0.00008, σ_report 0.00027, σ_full 0.00015; a cycle is credited at ΔR-free-select ≤ -0.00017 (k = 2.0).
Campaign ledger for this model (`refinement/current.json`): R-work 0.1350, R-free full 0.1716, select 0.1755, report 0.1677.

## Geometry and composition (phenix.molprobity, release time, default settings)

| | Deposited | This release |
|---|---|---|
| Atoms (hydrogens) | 2220 (0) | 4804 (2274) |
| Waters | 180 | 236 |
| Altloc letters | A, B | A, B, C |
| Clashscore | 2.92 | 2.55 |
| Ramachandran outliers / favored (%) | 0.00 / 98.0 | 0.00 / 98.0 |
| Rotamer outliers (%) | 1.36 | 1.59 |
| Cβ deviations | 0 | 1 |
| RMS bonds (Å) / angles (°) | 0.0075 / 1.12 | 0.0066 / 1.04 |
| MolProbity score | 1.19 | 1.20 |

## What changed in the coordinates

From `validation/release/model_diff.json` (deposited vs released, by chain and residue number):

- Waters added (57): A 5001, A 5002, A 5003, A 5004, A 5005, A 5006, A 5007, A 5008, A 5009, A 5010, A 5011, A 5012, A 5013, A 5014, A 5015, A 5016, A 5017, A 5018, A 5019, A 5020, A 5021, A 5022, A 5023, A 5024, A 5025, A 5026, A 5027, A 5028, A 5029, A 5030, A 5031, A 5032, A 5033, A 5034, A 5035, A 5036, A 5037, A 5038, A 5039, A 5040 …
- Waters removed (1): A 782
- Residues whose alternate-conformation letters changed (29): A 107 ILE -→AB, A 11 ASP -→AB, A 129 THR -→AB, A 133 ILE -→AB, A 147 GLU -→AB, A 152 TYR -→AB, A 155 GLU -→AB, A 158 ILE -→AB, A 159 ILE -→AB, A 166 LEU -→AB, A 167 ASP -→AB, A 168 ILE -→AB, A 175 ARG -→AB, A 177 ILE -→AB, A 179 ILE -→AB, A 201 ILE -→AB, A 206 VAL -→AB, A 208 VAL -→ABC, A 250 SER -→ABC, A 30 ILE -→AB, A 34 ASN -→AB, A 40 PHE -→AB, A 46 THR -→AB, A 61 ASP -→AB, A 65 ASP -→AB, A 72 PHE -→AB, A 74 GLU -→AB, A 78 VAL -→AB, A 82 ILE -→AB
- Hydrogen atoms: +2274 (riding hydrogens added by the refinement protocol).

## What the campaign did

Refinement protocol of the released model: phenix.refine 2.1-6048, 5 macro-cycles, anisotropic ADPs, 2274 riding hydrogens, seed 1. ADP decision: n_refl/n_atoms(non-H)=16.23 >= 5.0 and d_min=1.5 <= 1.5. The verbatim command is `refinement/command.txt`.

The released model was written by cycle 913 (`graph`, run `3TC7.graph-weekend-20261002c`), verdict **accepted**, attributable ΔR-free-select -0.00101 against its paired null, ΔR-gap -0.00026; geometry flag: rota_outliers 1.59 > 1.5.

Cycles on record for this target: 74; credited: 13; changes proposed: 2053 (`ledger/cycles.csv`, `ledger/changes.csv`).

Credited cycles on record, all runs and experiment lines. A credit is relative to that cycle's own paired null; not every credit moved the standing model (promotion rules D484/D499/D508), and experiment-line cycles judged candidates against their own base.

| Cycle | Run | Attributable ΔR-free-select | R-free full after | ΔR-gap vs null | Geometry flag |
|---|---|---|---|---|---|
| 11 | `3TC7.run1` | -0.00460 | 0.1849 | — |  |
| 57 | `3TC7.E028b` | -0.00994 | 0.1728 | 0.00077 |  |
| 58 | `3TC7.E029` | -0.01041 | 0.1751 | -0.00926 |  |
| 64 | `3TC7.20260910v6` | -0.00084 | 0.1732 | 0.00026 |  |
| 68 | `3TC7.20260910v7` | -0.00149 | 0.1727 | -0.00113 |  |
| 912 | `3TC7.graph-weekend-20261002c` | -0.00164 | 0.1718 | -0.00155 | rota_outliers 1.58 > 1.5 |
| 913 | `3TC7.graph-weekend-20261002c` | -0.00101 | 0.1716 | -0.00026 | rota_outliers 1.59 > 1.5 |
| 915 | `3TC7.graph-weekend-20261002c` | -0.00172 | 0.1706 | -0.00015 | rota_outliers 1.62 > 1.5 |
| 917 | `3TC7.graph-weekend-20261002c` | -0.00047 | 0.1705 | -0.00014 |  |
| 919 | `3TC7.graph-weekend-20261002c` | -0.00051 | 0.1706 | -0.00024 |  |
| 957 | `3TC7.E042` | -0.00034 | 0.1709 | -0.00075 |  |
| 965 | `3TC7.E042` | -0.00043 | 0.1709 | -0.00064 |  |
| 966 | `3TC7.E042` | -0.00022 | 0.1710 | -0.00087 |  |

## Caveats

- The held-back report half did not improve with the 2026-10-03 promotions: ledger 0.16726 → 0.16769 (independent scorer 0.16730 → 0.16772, +1.6σ_report, D519). The full-set gain 0.17276 → 0.17161 is carried by the select half (0.17815 → 0.17545), the half the search consults. Each promotion passed the promotion rules; D519 proposes a cumulative report bound that would have refused the second one.
- Rotamer outliers 1.59 % at release time (campaign monitor 1.58 %) exceed the campaign's 1.5 % cap (D517); the previous released model had 0.8 %. Depositable by ordinary standards, not by the campaign's own bar.
- What the 2026-10-03 promotions added: qFit alternate conformers at A175, A250 and A30 in a credited batch (`3TC7.graph-weekend-20261002c` generation 2, D517), then a second credited batch (generation 3, node N3.0, D519).
- The largest single credited change on record is riding hydrogens on a model that never had any (no new parameters), −0.011 on every R-free set with the R-free − R-work gap unchanged (D488). Earlier credits added waters and alternate conformations.
- The refinement protocol uses a fixed ADP weight (wxu_scale 0.03) because Phenix's weight optimiser widens the R-gap on the hydrogen-bearing model (D491/D496); a re-refinement with default weights will not reproduce the R-gap. The credit bar (σ_select) quoted below is from the noise floor re-measured under that protocol.
- Campaign records after 2026-09-28 report a lower R-free on this target from manual Coot–refinement alternation (0.1583, D512). That model was never scored on the frozen flags and no copy of it was found (E039); plain Phenix water picking on these flags reaches 0.1702 and fails the R-gap gate. It is not in this release.

## Verify it yourself

```bash
# independent scorer (cctbx; needs Phenix)
phenix.python scripts/indep_rfree.py targets/3TC7/model/3TC7_refined.cif targets/3TC7/data/3TC7_data.mtz \
  targets/3TC7/data/3TC7_flags.mtz targets/3TC7/data/3TC7_split.mtz out.json
# standard tool
phenix.python scripts/merge_mtz.py targets/3TC7/data/3TC7_data.mtz targets/3TC7/data/3TC7_flags.mtz 3TC7_merged.mtz
phenix.model_vs_data targets/3TC7/model/3TC7_refined.cif 3TC7_merged.mtz
# look at it
coot targets/3TC7/model/3TC7_refined.pdb --auto targets/3TC7/maps/3TC7_refined_map_coeffs.mtz
```

## Provenance

- Campaign record `refinement/current.json`: cycle 913, stage `rerefine`, updated 2026-10-03T05:45:25+00:00.
- Model on the campaign pod: `/home/dev/runs/3TC7/graph/3TC7.graph-weekend-20261002c/g003/N2.0/combined/g003.N2.0.loo5/candidate_arm/refine_001.cif`.
- Data: `data.mtz` SHA-256 `999787e4c6ac7bf92b42aff1be61f56f14488d1b3b4f0bc77f6bb004ef2f2ead`, `flags.mtz` SHA-256 `411b1d1b86f0371724302b3513d1423aa380cb67812d20d3a36eed19b9ea36e3`; built from the deposited structure-factor file with SHA-256 `2f6c3f1a97718bcff16047b959f54eafc08a6f85e1df7855d4057eca0f47e236` (`data/prep.json`).
- Deposited header claim: R-work 0.158, R-free 0.193, 2075 free reflections.

## Files

| File | Size | What it is |
|---|---|---|
| `data/3TC7_data.mtz` | 823,680 | The frozen observed data (FP,SIGFP or IMEAN,SIGIMEAN) built from the deposited structure factors. |
| `data/3TC7_flags.mtz` | 659,392 | The frozen R-free flags, inherited unchanged from the deposited _refln.status ('f' = free; column R-free-flags, 0 = free). |
| `data/3TC7_split.mtz` | 659,392 | The select/report halves of the free set (column SPLIT: 1 = select, 2 = report, 0 = work). |
| `data/prep.json` | 3,874 | How data.mtz and flags.mtz were built: source file SHA-256, columns, counts, conventions, header claims. |
| `data/split.json` | 59,391 | The same split as a list of reflections, with the seed that made it. |
| `deposited/3TC7.cif` | 444,839 | The deposited coordinate file as fetched from RCSB (the starting point). |
| `deposited/3TC7.fasta` | 348 | The entry's sequence as fetched from RCSB. |
| `deposited/FETCHED` | 76 | When the raw files were fetched. |
| `deposited/fetch_manifest.sha256` | 756 | SHA-256 of the raw files at fetch time. |
| `deposited/rcsb_entry.json` | 13,974 | The RCSB entry record (title, citation, experimental details) as fetched. |
| `ledger/bisections.csv` | 246 | Bisection steps when a cycle regressed. |
| `ledger/changes.csv` | 6,025,594 | Every proposed change: type, selection, local density and geometry gates, ΔR-free-select, verdict. |
| `ledger/checks.csv` | 1,799 | Gate results G0–G8. |
| `ledger/cycles.csv` | 38,391 | Every paired cycle on this target: R-free on every set, verdict, attributable Δ, R-gap, geometry. |
| `ledger/defects.csv` | 118,347 | Values that could not be computed, with the reason (never a sentinel). |
| `ledger/deviations.csv` | 130,841 | Decision-log rows that name this target. |
| `ledger/noise_floor.csv` | 1,352 | The noise-floor row that set the credit bar: σ of R-free on every set. |
| `ledger/rfree_consultations.csv` | 228 | How many times R-free-select was consulted (PROTOCOL §3.6). |
| `ledger/runs/3TC7.20260908v5/DECISIONS.md` | 1,351 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/3TC7.20260908v5b/DECISIONS.md` | 18,282 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/3TC7.20260908v5b/run_summary.json` | 3,140 | The per-run summary (cycles, credits, stop reason). |
| `ledger/runs/3TC7.20260909corr/DECISIONS.md` | 1,324 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/3TC7.20260909corr_h/DECISIONS.md` | 1,335 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/3TC7.20260909corr_h2/DECISIONS.md` | 5,217 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/3TC7.20260909corr_h2/run_summary.json` | 2,642 | The per-run summary (cycles, credits, stop reason). |
| `ledger/runs/3TC7.20260910v6/DECISIONS.md` | 18,259 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/3TC7.20260910v7/DECISIONS.md` | 28,859 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/3TC7.20260910v7/run_summary.json` | 2,845 | The per-run summary (cycles, credits, stop reason). |
| `ledger/runs/3TC7.run1/DECISIONS.md` | 58,975 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/3TC7.run1/run_summary.json` | 4,174 | The per-run summary (cycles, credits, stop reason). |
| `ledger/runs/3TC7.run2/DECISIONS.md` | 62,516 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/3TC7.run2/run_summary.json` | 5,315 | The per-run summary (cycles, credits, stop reason). |
| `ledger/runs/3TC7.smoke1/DECISIONS.md` | 5,796 | The per-run human-readable decision log written by the driver. |
| `ledger/runs/3TC7.smoke1/run_summary.json` | 1,514 | The per-run summary (cycles, credits, stop reason). |
| `ledger/solvent_disagreements.csv` | 120 | Phenix/Coot disagreements on solvent sites. |
| `maps/3TC7_refined_map_coeffs.mtz` | 2,674,208 | Map coefficients from that run (2mFo−DFc and mFo−DFc; open with the model in Coot). |
| `model/3TC7_refined.cif` | 629,537 | The released model, mmCIF, as written by the phenix.refine run named in refinement/current.json. |
| `model/3TC7_refined.pdb` | 585,859 | The same model in PDB format, from the same run. |
| `refinement/command.txt` | 1,615 | The verbatim phenix.refine argv that wrote the model. |
| `refinement/current.json` | 519 | The campaign's standing-deliverable record: pod path of the model, R-free on every set, cycle index. |
| `refinement/experiment_paired_cycle.json` | 7,266 | Record of the experiment cycle that produced this model (paired null control, geometry of both arms). |
| `refinement/model_vs_data.campaign.log` | 2,101 | phenix.model_vs_data as run by the campaign on this model. |
| `refinement/refine_001.eff` | 42,818 | The effective parameters of that run. |
| `refinement/refine_001.log` | 73,146 | The phenix.refine log of that run. |
| `refinement/refine_decisions.json` | 2,108 | The harness's protocol decisions for that run (ADP model, TLS, restraints, data labels). |
| `refinement/refine_result.json` | 3,180 | The parsed result of that run (R factors, geometry, seed, wall clock). |
| `validation/campaign/checks/G3_3TC7.json` | 4,551 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/checks/fetch_3TC7.json` | 2,207 | Gate records: G3 (deposited R-free reproduced on the frozen flags) and the fetch check. |
| `validation/campaign/dossier.json` | 108,085 | The campaign dossier: xtriage, model audit, composition hypothesis, baselines. |
| `validation/campaign/noise_floor.json` | 7,472 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/noise_floor_h.json` | 7,664 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/noise_floor_h_fixedadp.json` | 7,984 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/noise_floor_h_input.json` | 7,834 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/noise_floor_h_wxu003.json` | 7,859 | A campaign noise floor: ten re-refinements of a model with different seeds (start_model says which model). |
| `validation/campaign/verify_20260907/3TC7_deposited.indep.json` | 530 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260907/3TC7_ours.indep.json` | 585 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260907/3TC7_pdbredo.indep.json` | 544 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260909/3TC7_e028b_candidate.indep.json` | 595 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20260909/3TC7_e028b_null.indep.json` | 587 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20261003/3TC7_N2.0.json` | 693 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20261003/3TC7_N3.0.json` | 693 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/campaign/verify_20261003/3TC7_start.json` | 660 | The campaign's independent verification runs (same scorer, earlier dates). |
| `validation/release/merge_mtz.log` | 395 | Log of the data+flags merge used by model_vs_data. |
| `validation/release/model_diff.json` | 3,207 | Coordinate-level diff, deposited vs released: waters added/removed, residues whose altloc set changed, hydrogens. |
| `validation/release/model_vs_data.deposited.log` | 3,316 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/model_vs_data.refined.log` | 2,293 | phenix.model_vs_data on the merged data+flags MTZ. |
| `validation/release/molprobity.deposited.log` | 16,206 | phenix.molprobity with default settings. |
| `validation/release/molprobity.deposited.out` | 3,899 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.log` | 24,270 | phenix.molprobity with default settings. |
| `validation/release/molprobity.refined.out` | 9,272 | phenix.molprobity with default settings. |
| `validation/release/rfree_indep.deposited.json` | 636 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.deposited.log` | 1,089 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.json` | 653 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/rfree_indep.refined.log` | 1,106 | Independent R-free scorer (scripts/indep_rfree.py): work/free/select/report, atom counts. |
| `validation/release/summary.json` | 2,553 | Release-time validation of the deposited and refined models (parsed from the logs beside it). |
