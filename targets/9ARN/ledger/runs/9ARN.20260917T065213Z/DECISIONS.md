# 9ARN — run `9ARN.20260917T065213Z`

started 2026-09-17T06:52:13+00:00 on actl-ws-xraymemory-autoresearch-devspace-8597768cc8-lxfq5 pid 752030  
stages `['correction', 'solvent', 'protein_altloc']` · seed 1 · max cycles 8 · max/stage 20  
noise floor σ_select = 0.005437, k = 2.0: a cycle is credited at ≤ -0.010874, bisected above +0.010874  
published better model: none recorded in targets.yaml  
starting model: `/home/dev/runs/9ARN/c000/baseline_rerefine/refine_001.cif`

## cycle 0 — base

cycle 0: re-refined the starting model to obtain map coefficients (/home/dev/runs/9ARN/runs/9ARN.20260917T065213Z/base/rerefine/refine_001.cif)  
R-work 0.2580712690425478 · R-free full 0.2954925131671607 · report 0.2881466255752553 (select 0.30228396834967086)

## cycle 1 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 1, "attempted": 1, "accepted": 0, "reverted": 1, "not_attempted": []}, "solvent": {"proposed": 10, "attempted": 6, "accepted": 5, "reverted": 1, "not_attempted": ["9ARN.c001.water_add.A5003", "9ARN.c001.water_add.A5004", "9ARN.c001.water_add.A5005", "9ARN.c001.water_add.A5006"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `9ARN.c001.rotamer_fix.A62` **reverted** — rscc 0.922933→0.9132 (Δ -0.009733, rule mean_delta, worst neighbour drop 0.0118): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.009733 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `9ARN.c001.water_remove.A208` **accepted** — rscc 0.0275→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0005): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.8.. moved -0.0005 (0.8597 -> 0.8592), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.412727374567855; no new altloc-aware clash; site-re
- `9ARN.c001.water_remove.A221` **accepted** — rscc 0.5233→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0023): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.32.. moved -0.0023 (0.9571 -> 0.9548), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.412727374567855; no new altloc-aware clash; site-r
- `9ARN.c001.water_remove.A220` **accepted** — rscc 0.6505→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0033): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.9.. moved -0.0033 (0.8478 -> 0.8445), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.412727374567855; no new altloc-aware clash; site-re
- `9ARN.c001.water_remove.A232` **reverted** — rscc 0.7559→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0255): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.232..=0.7559]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.222.. moved -0.0255 (0.8317 -> 0.8062), allowed drop 0.02]
- `9ARN.c001.water_add.A5001` **accepted** — rscc None→0.9078 (Δ None, rule new_residue_floor, worst neighbour drop 0.0017): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.57.. moved -0.0017 (0.933 -> 0.9313), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.412727374567855; no new altloc-aware clash; site-restri
- `9ARN.c001.water_add.A5002` **accepted** — rscc None→0.7197 (Δ None, rule new_residue_floor, worst neighbour drop 0.0063): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.229.. moved -0.0063 (0.809 -> 0.8027), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.412727374567855; no new altloc-aware clash; site-restr

**paired cycle**: null arm R-free-select 0.31229501131205356 · treatment arm 0.31213682340485477 · attributable **-0.000158** vs credit ≤ -0.010874 / regression > +0.010874 → **no_change**  
attributable -0.000158 within (−0.010874, +0.010874]: of the raw 0.009853, 0.010011 is reproduced by re-refining the base with NO changes; the changes are not credited but stay (locally better, and not worse globally) || cross-check (phenix.model_vs_data, full set): null 0.3013 · treatment 0.3022 · Δ +0.0009 — DISAGREES in sign: treat this credit as provisional

cross-check (phenix.model_vs_data, full test set): null 0.3013 · treatment 0.3022 · Δ +0.0009 → **DISAGREES in sign** with the gate — credit provisional (D409)

changes kept without credit; cumulative un-credited drift since the last credited base: -0.000158 (guard at > +0.010874)

⚠ whole-model geometry outside the frozen caps: rota_outliers 3.03 > 1.5 (D479, monitor)

base after cycle: `/home/dev/runs/9ARN/runs/9ARN.20260917T065213Z/cycles/c001/paired/candidate_arm/refine_001.cif` · R-free full 0.3020029668430337 · report 0.29104181504638355 · Δselect vs before +0.009853 · 2545.6 s

## cycle 2 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 4, "attempted": 4, "accepted": 0, "reverted": 4, "not_attempted": []}, "solvent": {"proposed": 10, "attempted": 7, "accepted": 5, "reverted": 2, "not_attempted": ["9ARN.c002.water_add.A5009", "9ARN.c002.water_add.A5010", "9ARN.c002.water_add.A5011"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `9ARN.c002.rotamer_fix.A62` **reverted** — rscc 0.9112→0.902733 (Δ -0.008467, rule mean_delta, worst neighbour drop 0.0097): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.008467 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `9ARN.c002.rotamer_fix.A34` **reverted** — rscc 0.9434→0.912467 (Δ -0.030933, rule mean_delta, worst neighbour drop 0.0052): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.030933 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `9ARN.c002.rotamer_fix.A31` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: Coot rotamer_fix moved residue(s) outside the 2-residue window [('A', 31, ''), ('A', 32, '')]: [('A', 22, '')]
- `9ARN.c002.zone_rsr.A31-33` **reverted** — rscc 0.870433→0.8739 (Δ 0.003467, rule mean_delta, worst neighbour drop 0.0053): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.003467 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `9ARN.c002.water_remove.A232` **reverted** — rscc 0.7712→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0175): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.232..=0.7712]
- `9ARN.c002.water_add.A5003` **accepted** — rscc None→0.7982 (Δ None, rule new_residue_floor, worst neighbour drop 0.0101): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.222.. moved -0.0101 (0.8638 -> 0.8537), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.412727374567855; no new altloc-aware clash; site-rest
- `9ARN.c002.water_add.A5004` **accepted** — rscc None→0.8784 (Δ None, rule new_residue_floor, worst neighbour drop -0.0006): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.33.. moved +0.0006 (0.9539 -> 0.9545), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.412727374567855; no new altloc-aware clash; site-restr
- `9ARN.c002.water_add.A5005` **accepted** — rscc None→0.7125 (Δ None, rule new_residue_floor, worst neighbour drop 0.0082): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.31.. moved -0.0082 (0.7065 -> 0.6983), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.412727374567855; no new altloc-aware clash; site-restr
- `9ARN.c002.water_add.A5006` **reverted** — rscc None→0.6701 (Δ None, rule new_residue_floor, worst neighbour drop 0.0035): failed: rscc [added residue(s) below the frozen floor solvent.water_rscc_min=0.7: A.5006..=0.6701]
- `9ARN.c002.water_add.A5007` **accepted** — rscc None→0.8772 (Δ None, rule new_residue_floor, worst neighbour drop 0.0016): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.12.. moved -0.0016 (0.8604 -> 0.8588), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.412727374567855; no new altloc-aware clash; site-restr
- `9ARN.c002.water_add.A5008` **accepted** — rscc None→0.7954 (Δ None, rule new_residue_floor, worst neighbour drop 0.0146): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.228.. moved -0.0146 (0.9773 -> 0.9627), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.412727374567855; no new altloc-aware clash; site-rest

**paired cycle**: null arm R-free-select 0.3098292833218624 · treatment arm 0.3076459960979477 · attributable **-0.002183** vs credit ≤ -0.010874 / regression > +0.010874 → **no_change**  
attributable -0.002183 within (−0.010874, +0.010874]: of the raw -0.004491, -0.002308 is reproduced by re-refining the base with NO changes; the changes are not credited but stay (locally better, and not worse globally) || cross-check (phenix.model_vs_data, full set): null 0.3019 · treatment 0.3035 · Δ +0.0016 — DISAGREES in sign: treat this credit as provisional

cross-check (phenix.model_vs_data, full test set): null 0.3019 · treatment 0.3035 · Δ +0.0016 → **DISAGREES in sign** with the gate — credit provisional (D409)

changes kept without credit; cumulative un-credited drift since the last credited base: -0.002341 (guard at > +0.010874)

⚠ whole-model geometry outside the frozen caps: rota_outliers 3.03 > 1.5 (D479, monitor)

base after cycle: `/home/dev/runs/9ARN/runs/9ARN.20260917T065213Z/cycles/c002/paired/candidate_arm/refine_001.cif` · R-free full 0.30185229894591714 · report 0.2955856231192156 · Δselect vs before -0.004491 · 2642.5 s

## cycle 3 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 4, "attempted": 4, "accepted": 0, "reverted": 4, "not_attempted": []}, "solvent": {"proposed": 6, "attempted": 6, "accepted": 3, "reverted": 3, "not_attempted": []}, "protein_altloc": {"proposed": 20, "attempted": 9, "accepted": 2, "reverted": 7, "not_attempted": ["9ARN.c003.protein_altloc_add.A41", "9ARN.c003.protein_altloc_add.A61", "9ARN.c003.protein_altloc_add.A65", "9ARN.c003.protein_altloc_add.A17", "9ARN.c003.protein_altloc_add.A47", "9ARN.c003.protein_altloc_add.A42", "9ARN.c003.protein_altloc_add.A52", "9ARN.c003.protein_altloc_add.A18", "9ARN.c003.protein_altloc_add.A39", "9ARN.c003.protein_altloc_add.A56", "9ARN.c003.protein_altloc_add.A14"]}}`
- `9ARN.c003.rotamer_fix.A62` **reverted** — rscc 0.903967→0.8933 (Δ -0.010667, rule mean_delta, worst neighbour drop 0.0163): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.010667 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `9ARN.c003.rotamer_fix.A34` **reverted** — rscc 0.935833→0.8988 (Δ -0.037033, rule mean_delta, worst neighbour drop 0.0075): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.037033 < required +0.01]
- `9ARN.c003.rotamer_fix.A31` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: Coot rotamer_fix moved residue(s) outside the 2-residue window [('A', 31, ''), ('A', 32, '')]: [('A', 22, '')]
- `9ARN.c003.zone_rsr.A31-33` **reverted** — rscc 0.861867→0.862133 (Δ 0.000266, rule mean_delta, worst neighbour drop 0.0051): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.000266 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `9ARN.c003.water_remove.A232` **reverted** — rscc 0.8431→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0156): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.232..=0.8431]
- `9ARN.c003.water_add.A5009` **accepted** — rscc None→0.7041 (Δ None, rule new_residue_floor, worst neighbour drop 0.0042): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.2.. moved -0.0042 (0.8918 -> 0.8876), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.412727374567855; no new altloc-aware clash; site-restri
- `9ARN.c003.water_add.A5010` **reverted** — rscc None→0.6713 (Δ None, rule new_residue_floor, worst neighbour drop 0.0009): failed: rscc [added residue(s) below the frozen floor solvent.water_rscc_min=0.7: A.5010..=0.6713]
- `9ARN.c003.water_add.A5011` **accepted** — rscc None→0.8413 (Δ None, rule new_residue_floor, worst neighbour drop -0.0002): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.59.. moved +0.0002 (0.8381 -> 0.8383), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.412727374567855; no new altloc-aware clash; site-restr
- `9ARN.c003.water_add.A5012` **reverted** — rscc None→0.6734 (Δ None, rule new_residue_floor, worst neighbour drop 0.0014): failed: rscc [added residue(s) below the frozen floor solvent.water_rscc_min=0.7: A.5012..=0.6734]
- `9ARN.c003.water_add.A5013` **accepted** — rscc None→0.7477 (Δ None, rule new_residue_floor, worst neighbour drop 0.0023): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.20.. moved -0.0023 (0.9282 -> 0.9259), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.412727374567855; no new altloc-aware clash; site-restr
- `9ARN.c003.protein_altloc_add.A72` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 72, '') (conformers: ['single'])
- `9ARN.c003.protein_altloc_add.A77` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 77, '') (conformers: ['single'])
- `9ARN.c003.protein_altloc_add.A71` **accepted** — rscc 0.969→0.9614 (Δ -0.0076, rule split_residue, worst neighbour drop 0.0033): RSCC gate passed: split-residue rule passed: 2 new conformer(s) ≥ 0.7, residue RSCC 0.969 → 0.9614 (Δ -0.0076 within −0.01); worst untouched neighbour A.237.. moved -0.0033 (0.8745 -> 0.8712), allowed drop 0.02; local geometry bond_rmsd=0.00393 angle_rmsd=0.45341 over 16 bond(s)/26 angle(s) within t
- `9ARN.c003.protein_altloc_add.A69` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 69, '') (conformers: ['single'])
- `9ARN.c003.protein_altloc_add.A57` **reverted** — rscc 0.9488→0.94352 (Δ -0.00528, rule split_residue, worst neighbour drop 0.0272): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.5001.. moved -0.0272 (0.8952 -> 0.868), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.4745 > rel_max 0.3 (prev 0.38656)]
- `9ARN.c003.protein_altloc_add.A75` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 75, '') (conformers: ['single'])
- `9ARN.c003.protein_altloc_add.A50` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 50, '') (conformers: ['single'])
- `9ARN.c003.protein_altloc_add.A74` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 74, '') (conformers: ['single'])
- `9ARN.c003.protein_altloc_add.A58` **accepted** — rscc 0.9747→0.964849 (Δ -0.009851, rule split_residue, worst neighbour drop 0.0058): RSCC gate passed: split-residue rule passed: 2 new conformer(s) ≥ 0.7, residue RSCC 0.9747 → 0.964849 (Δ -0.0099 within −0.01); worst untouched neighbour A.219.. moved -0.0058 (0.8746 -> 0.8688), allowed drop 0.02; local geometry bond_rmsd=0.00286 angle_rmsd=0.26933 over 16 bond(s)/26 angle(s) withi

**paired cycle**: null arm R-free-select 0.3133898740420502 · treatment arm 0.32235023746595604 · attributable **+0.008960** vs credit ≤ -0.010874 / regression > +0.010874 → **no_change**  
attributable 0.008960 within (−0.010874, +0.010874]: of the raw 0.014704, 0.005744 is reproduced by re-refining the base with NO changes; the changes are not credited and are dropped: they made R-free-select worse, below the bar but worse (D411) || cross-check (phenix.model_vs_data, full set): null 0.3071 · treatment 0.3143 · Δ +0.0072 — agrees in sign || Metropolis (v8, D499): attributable +0.008960 = +1.65σ_select, T = 1σ = 0.005437, p_keep = exp(−Δ/T) = 0.192, u = 0.271 → dropped: base ← null arm

cross-check (phenix.model_vs_data, full test set): null 0.3071 · treatment 0.3143 · Δ +0.0072 → **agrees in sign** with the gate

5 change(s) dropped: within noise but attributable +0.008960 > 0 — base ← null arm (D411)

⚠ whole-model geometry outside the frozen caps: rota_outliers 1.52 > 1.5 (D479, monitor)

base after cycle: `/home/dev/runs/9ARN/runs/9ARN.20260917T065213Z/cycles/c003/paired/null_arm/refine_001.cif` · R-free full 0.30695621493423575 · report 0.2999973327299681 · Δselect vs before +0.005744 · 3672.2 s

## cycle 4 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 3, "attempted": 3, "accepted": 0, "reverted": 3, "not_attempted": []}, "solvent": {"proposed": 7, "attempted": 7, "accepted": 1, "reverted": 6, "not_attempted": []}, "protein_altloc": {"proposed": 20, "attempted": 20, "accepted": 0, "reverted": 20, "not_attempted": []}}`
- `9ARN.c004.rotamer_fix.A62` **reverted** — rscc 0.903933→0.8845 (Δ -0.019433, rule mean_delta, worst neighbour drop 0.0146): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.019433 < required +0.01]
- `9ARN.c004.rotamer_fix.A31` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: Coot rotamer_fix moved residue(s) outside the 2-residue window [('A', 31, ''), ('A', 32, '')]: [('A', 22, '')]
- `9ARN.c004.zone_rsr.A31-33` **reverted** — rscc 0.863267→0.8695 (Δ 0.006233, rule mean_delta, worst neighbour drop 0.0045): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.006233 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `9ARN.c004.water_remove.A226` **reverted** — rscc 0.8311→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0197): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.226..=0.8311]
- `9ARN.c004.water_remove.A232` **reverted** — rscc 0.8343→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0211): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.232..=0.8343]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.219.. moved -0.0211 (0.8379 -> 0.8168), allowed drop 0.02]
- `9ARN.c004.water_add.A5009` **reverted** — rscc None→0.6692 (Δ None, rule new_residue_floor, worst neighbour drop 0.0034): failed: rscc [added residue(s) below the frozen floor solvent.water_rscc_min=0.7: A.5009..=0.6692]
- `9ARN.c004.water_add.A5010` **reverted** — rscc None→0.6555 (Δ None, rule new_residue_floor, worst neighbour drop 0.0059): failed: rscc [added residue(s) below the frozen floor solvent.water_rscc_min=0.7: A.5010..=0.6555]
- `9ARN.c004.water_add.A5011` **accepted** — rscc None→0.8197 (Δ None, rule new_residue_floor, worst neighbour drop -0.0004): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.59.. moved +0.0004 (0.8433 -> 0.8437), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.412727374567855; no new altloc-aware clash; site-restr
- `9ARN.c004.water_add.A5012` **reverted** — rscc None→0.6645 (Δ None, rule new_residue_floor, worst neighbour drop 0.0012): failed: rscc [added residue(s) below the frozen floor solvent.water_rscc_min=0.7: A.5012..=0.6645]
- `9ARN.c004.water_add.A5013` **reverted** — rscc None→0.68 (Δ None, rule new_residue_floor, worst neighbour drop 0.0022): failed: rscc [added residue(s) below the frozen floor solvent.water_rscc_min=0.7: A.5013..=0.68]
- `9ARN.c004.protein_altloc_add.A72` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 72, '') (conformers: ['single'])
- `9ARN.c004.protein_altloc_add.A77` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 77, '') (conformers: ['single'])
- `9ARN.c004.protein_altloc_add.A71` **reverted** — rscc 0.9671→0.956145 (Δ -0.010955, rule split_residue, worst neighbour drop 0.0012): failed: rscc [the residue's occupancy-weighted RSCC fell -0.0110 (allowed −0.01)]; clash [2 new altloc-aware clash(es)]
- `9ARN.c004.protein_altloc_add.A69` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 69, '') (conformers: ['single'])
- `9ARN.c004.protein_altloc_add.A57` **reverted** — rscc 0.9486→0.93392 (Δ -0.01468, rule split_residue, worst neighbour drop 0.0313): failed: rscc [the residue's occupancy-weighted RSCC fell -0.0147 (allowed −0.01)]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.5001.. moved -0.0313 (0.9024 -> 0.8711), allowed drop 0.02]; clash [1 new altloc-aware clash(es)]
- `9ARN.c004.protein_altloc_add.A50` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 50, '') (conformers: ['single'])
- `9ARN.c004.protein_altloc_add.A75` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 75, '') (conformers: ['single'])
- `9ARN.c004.protein_altloc_add.A58` **reverted** — rscc 0.973→0.956971 (Δ -0.016029, rule split_residue, worst neighbour drop 0.0061): failed: rscc [the residue's occupancy-weighted RSCC fell -0.0160 (allowed −0.01)]
- `9ARN.c004.protein_altloc_add.A41` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 41, '') (conformers: ['single'])
- `9ARN.c004.protein_altloc_add.A61` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 61, '') (conformers: ['single'])
- `9ARN.c004.protein_altloc_add.A74` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 74, '') (conformers: ['single'])
- `9ARN.c004.protein_altloc_add.A17` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 17, '') (conformers: ['single'])
- `9ARN.c004.protein_altloc_add.A42` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 42, '') (conformers: ['single'])
- `9ARN.c004.protein_altloc_add.A47` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 47, '') (conformers: ['single'])
- `9ARN.c004.protein_altloc_add.A52` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 52, '') (conformers: ['single'])
- `9ARN.c004.protein_altloc_add.A65` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 65, '') (conformers: ['single'])
- `9ARN.c004.protein_altloc_add.A39` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 39, '') (conformers: ['single'])
- `9ARN.c004.protein_altloc_add.A18` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 18, '') (conformers: ['single'])
- `9ARN.c004.protein_altloc_add.A14` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 14, '') (conformers: ['single'])
- `9ARN.c004.protein_altloc_add.A7` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: qFit built no alternate conformer for ('A', 7, '') (conformers: ['single'])

**paired cycle**: null arm R-free-select 0.32168489081402907 · treatment arm 0.3171601581311995 · attributable **-0.004525** vs credit ≤ -0.010874 / regression > +0.010874 → **no_change**  
attributable -0.004525 within (−0.010874, +0.010874]: of the raw 0.003770, 0.008295 is reproduced by re-refining the base with NO changes; the changes are not credited but stay (locally better, and not worse globally) || cross-check (phenix.model_vs_data, full set): null 0.3125 · treatment 0.3099 · Δ -0.0026 — agrees in sign

cross-check (phenix.model_vs_data, full test set): null 0.3125 · treatment 0.3099 · Δ -0.0026 → **agrees in sign** with the gate

changes kept without credit; cumulative un-credited drift since the last credited base: -0.006866 (guard at > +0.010874)

⚠ whole-model geometry outside the frozen caps: rota_outliers 1.52 > 1.5 (D479, monitor)

base after cycle: `/home/dev/runs/9ARN/runs/9ARN.20260917T065213Z/cycles/c004/paired/candidate_arm/refine_001.cif` · R-free full 0.309708015378392 · report 0.3016475038223508 · Δselect vs before +0.003770 · 3803.2 s

**converged** after cycle 4: 3 quiet cycles; ΔR-free-select span 0.00502 within 2.0·σ

## finished 2026-09-17T10:40:52+00:00

converged (PROTOCOL §4.6): 3 quiet cycles; ΔR-free-select span 0.00502 within 2.0·σ  
R-free full 0.2954925131671607 → 0.309708015378392 (Δ 0.014216) · report 0.2881466255752553 → 0.3016475038223508  
published better model: None · gap closed: None · reached: None  
credited changes (0): `[]`  
kept without credit: 11 · final model `/home/dev/runs/9ARN/runs/9ARN.20260917T065213Z/cycles/c004/paired/candidate_arm/refine_001.cif`  
best base of the run: cycle 0 · R-free full 0.2954925131671607 · report 0.2881466255752553 · `/home/dev/runs/9ARN/runs/9ARN.20260917T065213Z/base/rerefine/refine_001.cif`

