# 3TC7 — run `3TC7.20260908v5b`

started 2026-09-08T17:57:58+00:00 on actl-ws-xraymemory-autoresearch-devspace-54d7d7d896-4cxg2 pid 255469  
stages `['correction', 'solvent', 'protein_altloc']` · seed 1 · max cycles 3 · max/stage 20  
noise floor σ_select = 0.001811, k = 2.0: a cycle is credited at ≤ -0.003622, bisected above +0.003622  
published better model: {'r_work': 0.138, 'r_free': 0.163, 'method': 'qFit multiconformer model', 'source': 'https://dynamicpdb.com/entries/a937eeb3-1dfd-43a3-af1a-08675aad9807', 'fetched': '2026-08-27', 'comparable_to_our_flags': False, 'their_n_free': 1993, 'our_n_free': 2075, 'scored_on_our_flags': {'r_work': 0.139, 'r_free_full': 0.1439, 'r_free_gap': 0.0049, 'clashscore_altloc_aware': 15.39, 'model': 'https://files.dynamicpdb.com/a937eeb3-1dfd-43a3-af1a-08675aad9807/models/036b3d5e-c7e6-4f0e-ae39-37e76b3a7618/artifacts/2e719a59-01fd-4bd3-8ada-5bfdfc149940/3tc7_qFit_010.cif', 'sha256': '4dbee3272ff413a30db10dd5811c371c547a4804795792590592292e34e62a74', 'checked': '2026-08-29'}}  
starting model: `/home/dev/runs/3TC7/runs/3TC7.run2/cycles/c025/escape/null_arm/refine_001.cif`

## cycle 0 — base

current model already carries map coefficients; no cycle-0 refinement  
R-work 0.14679476884203055 · R-free full 0.18417302884819434 · report 0.17974181616365467 (select 0.1885086126445358)

## cycle 51 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 7, "attempted": 7, "accepted": 0, "reverted": 7, "not_attempted": []}, "solvent": {"proposed": 20, "attempted": 12, "accepted": 5, "reverted": 7, "not_attempted": ["3TC7.c051.water_add.A5058", "3TC7.c051.water_add.A5059", "3TC7.c051.water_add.A5060", "3TC7.c051.water_add.A5061", "3TC7.c051.water_add.A5062", "3TC7.c051.water_add.A5063", "3TC7.c051.water_add.A5064", "3TC7.c051.water_add.A5065"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `3TC7.c051.peptide_flip.A213` **reverted** — rscc 0.9615→0.933275 (Δ -0.028225, rule mean_delta, worst neighbour drop 0.0025): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.028225 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `3TC7.c051.peptide_flip.A76` **reverted** — rscc 0.97444→0.89824 (Δ -0.0762, rule mean_delta, worst neighbour drop 0.0271): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.0762 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.5029.. moved -0.0271 (0.8582 -> 0.8311), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.33 > rel_max 0.3 (prev 1.18821)]; cla
- `3TC7.c051.peptide_flip.A58` **reverted** — rscc 0.98385→0.843075 (Δ -0.140775, rule mean_delta, worst neighbour drop 0.0118): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.140775 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `3TC7.c051.zone_rsr.A211-215` **reverted** — rscc 0.96372→0.96132 (Δ -0.0024, rule mean_delta, worst neighbour drop 0.0014): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.0024 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `3TC7.c051.zone_rsr.A83-83` **reverted** — rscc 0.9677→0.9679 (Δ 0.0002, rule mean_delta, worst neighbour drop 0.0001): failed: rscc [mean RSCC over 1 changed residue(s) moved 0.0002 < required +0.01]
- `3TC7.c051.zone_rsr.A160-164` **reverted** — rscc 0.98052→0.97966 (Δ -0.00086, rule mean_delta, worst neighbour drop 0.0015): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.00086 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `3TC7.c051.zone_rsr.A56-60` **reverted** — rscc 0.98212→0.98146 (Δ -0.00066, rule mean_delta, worst neighbour drop 0.0005): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.00066 < required +0.01]
- `3TC7.c051.water_remove.A756` **reverted** — rscc 0.7934→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0016): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.756..=0.7934]
- `3TC7.c051.water_remove.A779` **reverted** — rscc 0.8488→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0004): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.779..=0.8488]
- `3TC7.c051.water_remove.A671` **reverted** — rscc 0.8783→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0001): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.671..=0.8783]
- `3TC7.c051.water_remove.A5015` **reverted** — rscc 0.8861→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0018): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.5015..=0.8861]
- `3TC7.c051.water_remove.A697` **reverted** — rscc 0.8884→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0014): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.697..=0.8884]
- `3TC7.c051.water_remove.A761` **reverted** — rscc 0.8887→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0031): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.761..=0.8887]
- `3TC7.c051.water_remove.A757` **reverted** — rscc 0.9466→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0003): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.757..=0.9466]
- `3TC7.c051.water_add.A5053` **accepted** — rscc None→0.909 (Δ None, rule new_residue_floor, worst neighbour drop 0.0009): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.656.. moved -0.0009 (0.9739 -> 0.973), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.4999525524595603; no new altloc-aware clash; site-rest
- `3TC7.c051.water_add.A5054` **accepted** — rscc None→0.841 (Δ None, rule new_residue_floor, worst neighbour drop 0.0122): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.740.. moved -0.0122 (0.9651 -> 0.9529), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.4999525524595603; no new altloc-aware clash; site-res
- `3TC7.c051.water_add.A5055` **accepted** — rscc None→0.8179 (Δ None, rule new_residue_floor, worst neighbour drop 0.0037): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.779.. moved -0.0037 (0.8596 -> 0.8559), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.4999525524595603; no new altloc-aware clash; site-res
- `3TC7.c051.water_add.A5056` **accepted** — rscc None→0.8626 (Δ None, rule new_residue_floor, worst neighbour drop 0.0015): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.736.. moved -0.0015 (0.9391 -> 0.9376), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.4999525524595603; no new altloc-aware clash; site-res
- `3TC7.c051.water_add.A5057` **accepted** — rscc None→0.7812 (Δ None, rule new_residue_floor, worst neighbour drop 0.0016): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.5049.. moved -0.0016 (0.9364 -> 0.9348), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.4999525524595603; no new altloc-aware clash; site-re

**paired cycle**: null arm R-free-select 0.18808956164296764 · treatment arm 0.18679365070052623 · attributable **-0.001296** vs credit ≤ -0.003622 / regression > +0.003622 → **no_change**  
attributable -0.001296 within (−0.003622, +0.003622]: of the raw -0.001715, -0.000419 is reproduced by re-refining the base with NO changes; the changes are not credited but stay (locally better, and not worse globally) || cross-check (phenix.model_vs_data, full set): null 0.184 · treatment 0.1835 · Δ -0.0005 — agrees in sign

cross-check (phenix.model_vs_data, full test set): null 0.184 · treatment 0.1835 · Δ -0.0005 → **agrees in sign** with the gate

changes kept without credit; cumulative un-credited drift since the last credited base: -0.001296 (guard at > +0.003622)

base after cycle: `/home/dev/runs/3TC7/runs/3TC7.20260908v5b/cycles/c051/paired/candidate_arm/refine_001.cif` · R-free full 0.183406263077054 · report 0.1799441606913849 · Δselect vs before -0.001715 · 3003.6 s

## cycle 52 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 9, "attempted": 9, "accepted": 0, "reverted": 9, "not_attempted": []}, "solvent": {"proposed": 16, "attempted": 12, "accepted": 5, "reverted": 7, "not_attempted": ["3TC7.c052.water_add.A5063", "3TC7.c052.water_add.A5064", "3TC7.c052.water_add.A5065", "3TC7.c052.water_add.A5066"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `3TC7.c052.peptide_flip.A27` **reverted** — rscc 0.9729→0.968075 (Δ -0.004825, rule mean_delta, worst neighbour drop 0.0023): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.004825 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `3TC7.c052.peptide_flip.A213` **reverted** — rscc 0.9621→0.93615 (Δ -0.02595, rule mean_delta, worst neighbour drop 0.0032): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.02595 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `3TC7.c052.peptide_flip.A76` **reverted** — rscc 0.97426→0.89766 (Δ -0.0766, rule mean_delta, worst neighbour drop 0.0276): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.0766 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.5029.. moved -0.0276 (0.8525 -> 0.8249), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.3309 > rel_max 0.3 (prev 1.19577)]; c
- `3TC7.c052.peptide_flip.A58` **reverted** — rscc 0.983925→0.807125 (Δ -0.1768, rule mean_delta, worst neighbour drop 0.0168): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.1768 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `3TC7.c052.zone_rsr.A211-215` **reverted** — rscc 0.96426→0.96218 (Δ -0.00208, rule mean_delta, worst neighbour drop 0.0011): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.00208 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `3TC7.c052.zone_rsr.A83-83` **reverted** — rscc 0.9674→0.9672 (Δ -0.0002, rule mean_delta, worst neighbour drop 0.0004): failed: rscc [mean RSCC over 1 changed residue(s) moved -0.0002 < required +0.01]
- `3TC7.c052.zone_rsr.A25-29` **reverted** — rscc 0.97604→0.97616 (Δ 0.00012, rule mean_delta, worst neighbour drop 0.0013): failed: rscc [mean RSCC over 5 changed residue(s) moved 0.00012 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `3TC7.c052.zone_rsr.A160-164` **reverted** — rscc 0.98068→0.97988 (Δ -0.0008, rule mean_delta, worst neighbour drop 0.0007): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.0008 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `3TC7.c052.zone_rsr.A56-60` **reverted** — rscc 0.98222→0.98134 (Δ -0.00088, rule mean_delta, worst neighbour drop 0.0007): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.00088 < required +0.01]
- `3TC7.c052.water_remove.A756` **reverted** — rscc 0.7904→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0014): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.756..=0.7904]
- `3TC7.c052.water_remove.A779` **reverted** — rscc 0.8486→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0002): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.779..=0.8486]
- `3TC7.c052.water_remove.A671` **reverted** — rscc 0.8775→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0001): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.671..=0.8775]
- `3TC7.c052.water_remove.A5015` **reverted** — rscc 0.8777→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0031): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.5015..=0.8777]
- `3TC7.c052.water_remove.A697` **reverted** — rscc 0.8875→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0019): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.697..=0.8875]
- `3TC7.c052.water_remove.A761` **reverted** — rscc 0.8875→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0025): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.761..=0.8875]
- `3TC7.c052.water_remove.A757` **reverted** — rscc 0.95→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0006): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.757..=0.95]
- `3TC7.c052.water_add.A5058` **accepted** — rscc None→0.8706 (Δ None, rule new_residue_floor, worst neighbour drop 0.0031): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.5020.. moved -0.0031 (0.9076 -> 0.9045), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.4999525524595603; no new altloc-aware clash; site-re
- `3TC7.c052.water_add.A5059` **accepted** — rscc None→0.8931 (Δ None, rule new_residue_floor, worst neighbour drop 0.0004): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.712.. moved -0.0004 (0.9721 -> 0.9717), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.4999525524595603; no new altloc-aware clash; site-res
- `3TC7.c052.water_add.A5060` **accepted** — rscc None→0.8741 (Δ None, rule new_residue_floor, worst neighbour drop 0.0001): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.701.. moved -0.0001 (0.98 -> 0.9799), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.4999525524595603; no new altloc-aware clash; site-restr
- `3TC7.c052.water_add.A5061` **accepted** — rscc None→0.7961 (Δ None, rule new_residue_floor, worst neighbour drop 0.0023): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.5016.. moved -0.0023 (0.7865 -> 0.7842), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.4999525524595603; no new altloc-aware clash; site-re
- `3TC7.c052.water_add.A5062` **accepted** — rscc None→0.8073 (Δ None, rule new_residue_floor, worst neighbour drop 0.0008): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.42.. moved -0.0008 (0.9595 -> 0.9587), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.4999525524595603; no new altloc-aware clash; site-rest

**paired cycle**: null arm R-free-select 0.1868649608461852 · treatment arm 0.18673137669735568 · attributable **-0.000134** vs credit ≤ -0.003622 / regression > +0.003622 → **no_change**  
attributable -0.000134 within (−0.003622, +0.003622]: of the raw -0.000062, 0.000071 is reproduced by re-refining the base with NO changes; the changes are not credited but stay (locally better, and not worse globally) || cross-check (phenix.model_vs_data, full set): null 0.1837 · treatment 0.1838 · Δ +0.0001 — DISAGREES in sign: treat this credit as provisional

cross-check (phenix.model_vs_data, full test set): null 0.1837 · treatment 0.1838 · Δ +0.0001 → **DISAGREES in sign** with the gate — credit provisional (D409)

changes kept without credit; cumulative un-credited drift since the last credited base: -0.001430 (guard at > +0.003622)

base after cycle: `/home/dev/runs/3TC7/runs/3TC7.20260908v5b/cycles/c052/paired/candidate_arm/refine_001.cif` · R-free full 0.18383426059422395 · report 0.18087324352528497 · Δselect vs before -0.000062 · 3036.0 s

**stall detected** after cycle 52: 2 consecutive cycle(s) accepted changes locally but each moved R-free-select by < σ=0.001811: a minimum small edits cannot leave → next cycle takes an escape rung

## cycle 53 — stall escape rung `reweight_reseed`

different random seed, fresh xyz/adp weight optimisation, +3 macro-cycles: override `{'seed': 1001, 'optimize_xyz_weight': True, 'optimize_adp_weight': True, 'wxc_scale': None, 'wxu_scale': None, 'macro_cycles': 8}`  
null arm R-free-select 0.18693266070808612 · escape arm 0.18696685984517059 · attributable **+0.000034** → did not clear  
attributable 0.000034 within (−0.003622, +0.003622]: of the raw 0.000235, 0.000201 is reproduced by re-refining the base with NO changes; the changes are not credited and are not adopted (no local evidence of their own) || cross-check (phenix.model_vs_data, full set): null 0.1839 · treatment 0.1839 · Δ +0.0000 — agrees in sign  
ladder so far `{'reweight_reseed': 'failed'}`

## finished 2026-09-08T20:04:35+00:00

max_cycles=3 reached  
R-free full 0.18417302884819434 → 0.18387697591124733 (Δ -0.000296) · report 0.17974181616365467 → 0.18075389263855599  
published better model: 0.163 · gap closed: None · reached: None  
credited changes (0): `[]`  
kept without credit: 10 · final model `/home/dev/runs/3TC7/runs/3TC7.20260908v5b/cycles/c053/escape/null_arm/refine_001.cif`  
best base of the run: cycle 52 · R-free full 0.18383426059422395 · report 0.18087324352528497 · `/home/dev/runs/3TC7/runs/3TC7.20260908v5b/cycles/c052/paired/candidate_arm/refine_001.cif`

