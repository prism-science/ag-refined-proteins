# 4QO4 — run `4QO4.20260917T052656Z`

started 2026-09-17T05:26:56+00:00 on actl-ws-xraymemory-autoresearch-devspace-8597768cc8-lxfq5 pid 272061  
stages `['correction', 'solvent', 'protein_altloc']` · seed 1 · max cycles 8 · max/stage 20  
noise floor σ_select = 0.001872, k = 2.0: a cycle is credited at ≤ -0.003744, bisected above +0.003744  
published better model: none recorded in targets.yaml  
starting model: `/home/dev/runs/4QO4/c000/baseline_rerefine/refine_001.cif`

## cycle 0 — base

cycle 0: re-refined the starting model to obtain map coefficients (/home/dev/runs/4QO4/runs/4QO4.20260917T052656Z/base/rerefine/refine_001.cif)  
R-work 0.28717316643233076 · R-free full 0.36190468754175514 · report 0.38475677251927276 (select 0.3414751997278627)

## cycle 1 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 5, "attempted": 5, "accepted": 0, "reverted": 5, "not_attempted": []}, "solvent": {"proposed": 20, "attempted": 7, "accepted": 5, "reverted": 2, "not_attempted": ["4QO4.c001.water_remove.A365", "4QO4.c001.water_remove.A317", "4QO4.c001.water_remove.A376", "4QO4.c001.water_remove.A373", "4QO4.c001.water_remove.A354", "4QO4.c001.water_remove.A329", "4QO4.c001.water_remove.A371", "4QO4.c001.water_remove.A308", "4QO4.c001.water_remove.A357", "4QO4.c001.water_remove.A339", "4QO4.c001.water_remove.A318", "4QO4.c001.water_remove.A356", "4QO4.c001.water_remove.A349"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `4QO4.c001.rotamer_fix.A24` **reverted** — rscc 0.892633→0.905467 (Δ 0.012834, rule mean_delta, worst neighbour drop 0.0261): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.338.. moved -0.0261 (0.7117 -> 0.6856), allowed drop 0.02]
- `4QO4.c001.rotamer_fix.A18` **reverted** — rscc 0.8889→0.8935 (Δ 0.0046, rule mean_delta, worst neighbour drop 0.0015): failed: rscc [mean RSCC over 2 changed residue(s) moved 0.0046 < required +0.01]
- `4QO4.c001.rotamer_fix.A36` **reverted** — rscc 0.910467→0.9105 (Δ 3.3e-05, rule mean_delta, worst neighbour drop 0.0054): failed: rscc [mean RSCC over 3 changed residue(s) moved 3.3e-05 < required +0.01]
- `4QO4.c001.peptide_flip.A79` **reverted** — rscc 0.8548→0.86215 (Δ 0.00735, rule mean_delta, worst neighbour drop 0.0041): failed: rscc [mean RSCC over 4 changed residue(s) moved 0.00735 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `4QO4.c001.zone_rsr.A77-81` **reverted** — rscc 0.87156→0.8758 (Δ 0.00424, rule mean_delta, worst neighbour drop 0.0066): failed: rscc [mean RSCC over 5 changed residue(s) moved 0.00424 < required +0.01]
- `4QO4.c001.water_remove.A346` **accepted** — rscc 0.2352→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0013): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.350.. moved -0.0013 (0.7967 -> 0.7954), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-
- `4QO4.c001.water_remove.A352` **reverted** — rscc 0.2449→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0232): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.326.. moved -0.0232 (0.7169 -> 0.6937), allowed drop 0.02]
- `4QO4.c001.water_remove.A364` **accepted** — rscc 0.332→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0019): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.67.. moved -0.0019 (0.8924 -> 0.8905), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-r
- `4QO4.c001.water_remove.A341` **reverted** — rscc 0.4244→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0248): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.308.. moved -0.0248 (0.6638 -> 0.639), allowed drop 0.02]
- `4QO4.c001.water_remove.A309` **accepted** — rscc 0.4332→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0006): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.85.. moved -0.0006 (0.9208 -> 0.9202), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-r
- `4QO4.c001.water_remove.A340` **accepted** — rscc 0.4332→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0147): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.310.. moved -0.0147 (0.4438 -> 0.4291), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-
- `4QO4.c001.water_remove.A310` **accepted** — rscc 0.4291→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0037): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.368.. moved -0.0037 (0.7335 -> 0.7298), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-

**paired cycle**: null arm R-free-select 0.34514295768402065 · treatment arm 0.33676778220105136 · attributable **-0.008375** vs credit ≤ -0.003744 / regression > +0.003744 → **accepted**  
attributable -0.008375 ≤ -0.003744; the null arm moved 0.003668 on its own and is not credited || cross-check (phenix.model_vs_data, full set): null 0.3642 · treatment 0.3602 · Δ -0.0040 — agrees in sign

cross-check (phenix.model_vs_data, full test set): null 0.3642 · treatment 0.3602 · Δ -0.0040 → **agrees in sign** with the gate

⚠ whole-model geometry outside the frozen caps: rota_outliers 2.41 > 1.5 (D479, monitor)

base after cycle: `/home/dev/runs/4QO4/runs/4QO4.20260917T052656Z/cycles/c001/paired/candidate_arm/refine_001.cif` · R-free full 0.3595680617453874 · report 0.3850720748858448 · Δselect vs before -0.004707 · 1353.0 s

## cycle 2 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 4, "attempted": 4, "accepted": 0, "reverted": 4, "not_attempted": []}, "solvent": {"proposed": 20, "attempted": 8, "accepted": 5, "reverted": 3, "not_attempted": ["4QO4.c002.water_remove.A371", "4QO4.c002.water_remove.A367", "4QO4.c002.water_remove.A329", "4QO4.c002.water_remove.A338", "4QO4.c002.water_remove.A363", "4QO4.c002.water_remove.A308", "4QO4.c002.water_remove.A325", "4QO4.c002.water_remove.A339", "4QO4.c002.water_remove.A356", "4QO4.c002.water_remove.A372", "4QO4.c002.water_remove.A342", "4QO4.c002.water_remove.A301"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `4QO4.c002.rotamer_fix.A24` **reverted** — rscc 0.893533→0.908733 (Δ 0.0152, rule mean_delta, worst neighbour drop 0.021): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.338.. moved -0.0210 (0.6758 -> 0.6548), allowed drop 0.02]
- `4QO4.c002.rotamer_fix.A18` **reverted** — rscc 0.88245→0.88965 (Δ 0.0072, rule mean_delta, worst neighbour drop 0.0022): failed: rscc [mean RSCC over 2 changed residue(s) moved 0.0072 < required +0.01]
- `4QO4.c002.peptide_flip.A79` **reverted** — rscc 0.85555→0.863775 (Δ 0.008225, rule mean_delta, worst neighbour drop 0.0064): failed: rscc [mean RSCC over 4 changed residue(s) moved 0.008225 < required +0.01]; clash [4 new altloc-aware clash(es)]
- `4QO4.c002.zone_rsr.A77-81` **reverted** — rscc 0.87156→0.87738 (Δ 0.00582, rule mean_delta, worst neighbour drop 0.0045): failed: rscc [mean RSCC over 5 changed residue(s) moved 0.00582 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `4QO4.c002.water_remove.A352` **reverted** — rscc 0.4188→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0213): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.326.. moved -0.0213 (0.713 -> 0.6917), allowed drop 0.02]
- `4QO4.c002.water_remove.A317` **accepted** — rscc 0.4606→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0011): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.24.. moved -0.0011 (0.847 -> 0.8459), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-re
- `4QO4.c002.water_remove.A365` **reverted** — rscc 0.4783→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0215): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.354.. moved -0.0215 (0.5245 -> 0.503), allowed drop 0.02]
- `4QO4.c002.water_remove.A354` **accepted** — rscc 0.5245→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0163): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.335.. moved -0.0163 (0.7588 -> 0.7425), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-
- `4QO4.c002.water_remove.A341` **accepted** — rscc 0.5467→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0169): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.308.. moved -0.0169 (0.6683 -> 0.6514), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-
- `4QO4.c002.water_remove.A349` **accepted** — rscc 0.553→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0147): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.318.. moved -0.0147 (0.7498 -> 0.7351), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-
- `4QO4.c002.water_remove.A376` **reverted** — rscc 0.5823→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0478): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.367.. moved -0.0478 (0.656 -> 0.6082), allowed drop 0.02]
- `4QO4.c002.water_remove.A373` **accepted** — rscc 0.6206→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0053): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.110.. moved -0.0053 (0.8837 -> 0.8784), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-

**paired cycle**: null arm R-free-select 0.34360713904358714 · treatment arm 0.34043198253278506 · attributable **-0.003175** vs credit ≤ -0.003744 / regression > +0.003744 → **no_change**  
attributable -0.003175 within (−0.003744, +0.003744]: of the raw 0.003664, 0.006839 is reproduced by re-refining the base with NO changes; the changes are not credited but stay (locally better, and not worse globally) || cross-check (phenix.model_vs_data, full set): null 0.3609 · treatment 0.3509 · Δ -0.0100 — agrees in sign

cross-check (phenix.model_vs_data, full test set): null 0.3609 · treatment 0.3509 · Δ -0.0100 → **agrees in sign** with the gate

changes kept without credit; cumulative un-credited drift since the last credited base: -0.003175 (guard at > +0.003744)

⚠ whole-model geometry outside the frozen caps: rota_outliers 2.41 > 1.5 (D479, monitor)

base after cycle: `/home/dev/runs/4QO4/runs/4QO4.20260917T052656Z/cycles/c002/paired/candidate_arm/refine_001.cif` · R-free full 0.3590997528086618 · report 0.37998120987558764 · Δselect vs before +0.003664 · 1503.8 s

## cycle 3 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 4, "attempted": 4, "accepted": 1, "reverted": 3, "not_attempted": []}, "solvent": {"proposed": 20, "attempted": 5, "accepted": 4, "reverted": 1, "not_attempted": ["4QO4.c003.water_remove.A339", "4QO4.c003.water_remove.A325", "4QO4.c003.water_remove.A329", "4QO4.c003.water_remove.A368", "4QO4.c003.water_remove.A356", "4QO4.c003.water_remove.A370", "4QO4.c003.water_remove.A378", "4QO4.c003.water_remove.A342", "4QO4.c003.water_remove.A301", "4QO4.c003.water_remove.A304", "4QO4.c003.water_remove.A362", "4QO4.c003.water_add.A5001", "4QO4.c003.water_add.A5002", "4QO4.c003.water_add.A5003", "4QO4.c003.water_add.A5004"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `4QO4.c003.rotamer_fix.A18` **accepted** — rscc 0.8821→0.89285 (Δ 0.01075, rule mean_delta, worst neighbour drop 0.0047): RSCC gate passed: RSCC gate passed under mean_delta (delta +0.0107 >= +0.01); worst untouched neighbour A.305.. moved -0.0047 (0.887 -> 0.8823), allowed drop 0.02; local geometry bond_rmsd=0.00492 angle_rmsd=0.61055 over 17 bond(s)/24 angle(s) within the band for d_min=1.700359054039257; no new altl
- `4QO4.c003.rotamer_fix.A24` **reverted** — rscc 0.9012→0.914667 (Δ 0.013467, rule mean_delta, worst neighbour drop 0.0295): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.338.. moved -0.0295 (0.6509 -> 0.6214), allowed drop 0.02]
- `4QO4.c003.peptide_flip.A79` **reverted** — rscc 0.86295→0.86505 (Δ 0.0021, rule mean_delta, worst neighbour drop 0.0052): failed: rscc [mean RSCC over 4 changed residue(s) moved 0.0021 < required +0.01]; clash [3 new altloc-aware clash(es)]
- `4QO4.c003.zone_rsr.A77-81` **reverted** — rscc 0.87874→0.87924 (Δ 0.0005, rule mean_delta, worst neighbour drop 0.0023): failed: rscc [mean RSCC over 5 changed residue(s) moved 0.0005 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `4QO4.c003.water_remove.A352` **accepted** — rscc 0.3982→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0171): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.325.. moved -0.0171 (0.6711 -> 0.654), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-r
- `4QO4.c003.water_remove.A365` **reverted** — rscc 0.4167→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.003): failed: site-restricted reciprocal: attributable ΔR-free-select +0.008054 > +0.003744 (2.0σ_select) — the change makes R-free worse beyond noise and is dropped before the batch
- `4QO4.c003.water_remove.A363` **accepted** — rscc 0.6266→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0046): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.315.. moved -0.0046 (0.9252 -> 0.9206), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-
- `4QO4.c003.water_remove.A372` **accepted** — rscc 0.6427→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0048): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.376.. moved -0.0048 (0.7109 -> 0.7061), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-
- `4QO4.c003.water_remove.A338` **accepted** — rscc 0.6396→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0026): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.44.. moved -0.0026 (0.8415 -> 0.8389), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-r

**paired cycle**: null arm R-free-select 0.33765736040122274 · treatment arm 0.33854245184263493 · attributable **+0.000885** vs credit ≤ -0.003744 / regression > +0.003744 → **no_change**  
attributable 0.000885 within (−0.003744, +0.003744]: of the raw -0.001890, -0.002775 is reproduced by re-refining the base with NO changes; the changes are not credited and are dropped: they made R-free-select worse, below the bar but worse (D411) || cross-check (phenix.model_vs_data, full set): null 0.3554 · treatment 0.3539 · Δ -0.0015 — DISAGREES in sign: treat this credit as provisional || Metropolis (v8, D499): attributable +0.000885 = +0.47σ_select, T = 1σ = 0.001872, p_keep = exp(−Δ/T) = 0.623, u = 0.126 → KEPT: the candidate arm carries on, un-credited (D499)

cross-check (phenix.model_vs_data, full test set): null 0.3554 · treatment 0.3539 · Δ -0.0015 → **DISAGREES in sign** with the gate — credit provisional (D409)

**Metropolis keep (v8, D499)**: attributable +0.000885 > 0 within noise; p_keep 0.623, u 0.126 — the candidate arm carries on un-credited

changes kept without credit; cumulative un-credited drift since the last credited base: -0.002290 (guard at > +0.003744)

⚠ whole-model geometry outside the frozen caps: rota_outliers 2.41 > 1.5 (D479, monitor)

base after cycle: `/home/dev/runs/4QO4/runs/4QO4.20260917T052656Z/cycles/c003/paired/candidate_arm/refine_001.cif` · R-free full 0.3542453171644818 · report 0.3718102809068115 · Δselect vs before -0.001890 · 1317.3 s

## cycle 4 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 4, "attempted": 4, "accepted": 0, "reverted": 4, "not_attempted": []}, "solvent": {"proposed": 18, "attempted": 5, "accepted": 5, "reverted": 0, "not_attempted": ["4QO4.c004.water_remove.A371", "4QO4.c004.water_remove.A370", "4QO4.c004.water_remove.A356", "4QO4.c004.water_remove.A378", "4QO4.c004.water_remove.A342", "4QO4.c004.water_remove.A301", "4QO4.c004.water_remove.A362", "4QO4.c004.water_remove.A304", "4QO4.c004.water_add.A5001", "4QO4.c004.water_add.A5002", "4QO4.c004.water_add.A5003", "4QO4.c004.water_add.A5004", "4QO4.c004.water_add.A5005"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `4QO4.c004.rotamer_fix.A18` **reverted** — rscc 0.8812→0.88875 (Δ 0.00755, rule mean_delta, worst neighbour drop 0.004): failed: rscc [mean RSCC over 2 changed residue(s) moved 0.00755 < required +0.01]
- `4QO4.c004.rotamer_fix.A24` **reverted** — rscc 0.902833→0.9163 (Δ 0.013467, rule mean_delta, worst neighbour drop 0.0217): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.305.. moved -0.0217 (0.8712 -> 0.8495), allowed drop 0.02]
- `4QO4.c004.peptide_flip.A79` **reverted** — rscc 0.862875→0.864275 (Δ 0.0014, rule mean_delta, worst neighbour drop 0.007): failed: rscc [mean RSCC over 4 changed residue(s) moved 0.0014 < required +0.01]; clash [4 new altloc-aware clash(es)]
- `4QO4.c004.zone_rsr.A77-81` **reverted** — rscc 0.87924→0.87994 (Δ 0.0007, rule mean_delta, worst neighbour drop 0.0044): failed: rscc [mean RSCC over 5 changed residue(s) moved 0.0007 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `4QO4.c004.water_remove.A365` **accepted** — rscc 0.3749→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0015): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.31.. moved -0.0015 (0.935 -> 0.9335), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-re
- `4QO4.c004.water_remove.A325` **accepted** — rscc 0.6265→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0147): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.318.. moved -0.0147 (0.7537 -> 0.739), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-r
- `4QO4.c004.water_remove.A339` **accepted** — rscc 0.665→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0064): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.336.. moved -0.0064 (0.7273 -> 0.7209), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-
- `4QO4.c004.water_remove.A329` **accepted** — rscc 0.6486→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0037): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.105.. moved -0.0037 (0.7424 -> 0.7387), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-
- `4QO4.c004.water_remove.A353` **accepted** — rscc 0.6995→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.008): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.350.. moved -0.0080 (0.8164 -> 0.8084), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-

**paired cycle**: null arm R-free-select 0.33918685919328423 · treatment arm 0.33201687214604014 · attributable **-0.007170** vs credit ≤ -0.003744 / regression > +0.003744 → **accepted**  
attributable -0.007170 ≤ -0.003744; the null arm moved 0.000644 on its own and is not credited || cross-check (phenix.model_vs_data, full set): null 0.3533 · treatment 0.3443 · Δ -0.0090 — agrees in sign

cross-check (phenix.model_vs_data, full test set): null 0.3533 · treatment 0.3443 · Δ -0.0090 → **agrees in sign** with the gate

⚠ whole-model geometry outside the frozen caps: rota_outliers 2.41 > 1.5 (D479, monitor)

base after cycle: `/home/dev/runs/4QO4/runs/4QO4.20260917T052656Z/cycles/c004/paired/candidate_arm/refine_001.cif` · R-free full 0.3443905478751905 · report 0.35823153556037973 · Δselect vs before -0.006526 · 1361.6 s

## cycle 5 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 4, "attempted": 4, "accepted": 1, "reverted": 3, "not_attempted": []}, "solvent": {"proposed": 11, "attempted": 11, "accepted": 4, "reverted": 7, "not_attempted": []}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `4QO4.c005.rotamer_fix.A18` **accepted** — rscc 0.8822→0.8927 (Δ 0.0105, rule mean_delta, worst neighbour drop 0.0097): RSCC gate passed: RSCC gate passed under mean_delta (delta +0.0105 >= +0.01); worst untouched neighbour A.342.. moved -0.0097 (0.8275 -> 0.8178), allowed drop 0.02; local geometry bond_rmsd=0.00763 angle_rmsd=0.62754 over 17 bond(s)/24 angle(s) within the band for d_min=1.700359054039257; no new alt
- `4QO4.c005.rotamer_fix.A24` **reverted** — rscc 0.904133→0.9179 (Δ 0.013767, rule mean_delta, worst neighbour drop 0.0262): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.324.. moved -0.0262 (0.809 -> 0.7828), allowed drop 0.02]; clash [1 new altloc-aware clash(es)]
- `4QO4.c005.peptide_flip.A79` **reverted** — rscc 0.8681→0.864675 (Δ -0.003425, rule mean_delta, worst neighbour drop 0.0091): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.003425 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `4QO4.c005.zone_rsr.A77-81` **reverted** — rscc 0.88472→0.88146 (Δ -0.00326, rule mean_delta, worst neighbour drop 0.0039): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.00326 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `4QO4.c005.water_remove.A370` **reverted** — rscc 0.6481→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0018): failed: site-restricted reciprocal: attributable ΔR-free-select +0.004635 > +0.003744 (2.0σ_select) — the change makes R-free worse beyond noise and is dropped before the batch
- `4QO4.c005.water_remove.A356` **reverted** — rscc 0.7245→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0041): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.356..=0.7245]
- `4QO4.c005.water_remove.A378` **reverted** — rscc 0.7868→None (Δ None, rule removed_residue_floor, worst neighbour drop -0.0005): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.378..=0.7868]
- `4QO4.c005.water_remove.A342` **reverted** — rscc 0.8178→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0024): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.342..=0.8178]
- `4QO4.c005.water_remove.A301` **reverted** — rscc 0.9005→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0032): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.301..=0.9005]
- `4QO4.c005.water_remove.A362` **reverted** — rscc 0.95→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0018): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.362..=0.95]
- `4QO4.c005.water_remove.A304` **reverted** — rscc 0.9502→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0067): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.304..=0.9502]
- `4QO4.c005.water_add.A5001` **accepted** — rscc None→0.9038 (Δ None, rule new_residue_floor, worst neighbour drop 0.0022): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.79.. moved -0.0022 (0.8442 -> 0.842), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-restri
- `4QO4.c005.water_add.A5002` **accepted** — rscc None→0.911 (Δ None, rule new_residue_floor, worst neighbour drop 0.002): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.35.. moved -0.0020 (0.9258 -> 0.9238), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-restr
- `4QO4.c005.water_add.A5003` **accepted** — rscc None→0.8836 (Δ None, rule new_residue_floor, worst neighbour drop 0.0096): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.332.. moved -0.0096 (0.8737 -> 0.8641), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-rest
- `4QO4.c005.water_add.A5004` **accepted** — rscc None→0.8038 (Δ None, rule new_residue_floor, worst neighbour drop 0.0014): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.94.. moved -0.0014 (0.9186 -> 0.9172), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-restr

**paired cycle**: null arm R-free-select 0.3308535190063403 · treatment arm 0.3370352167403544 · attributable **+0.006182** vs credit ≤ -0.003744 / regression > +0.003744 → **rejected** (REGRESSED)  
attributable 0.006182 > +0.003744: the changes made R-free-select WORSE than the identically refined base — regression, bisect (SPEC_LOOP_V2 §1.3) || cross-check (phenix.model_vs_data, full set): null 0.3446 · treatment 0.3534 · Δ +0.0088 — agrees in sign

cross-check (phenix.model_vs_data, full test set): null 0.3446 · treatment 0.3534 · Δ +0.0088 → **agrees in sign** with the gate

bisection: culprits `[]` (2 refinement(s)); no subset beat the null arm — base ← null arm. no single change regresses on its own — the regression is an interaction between halves (4QO4.c005.rotamer_fix.A18+4QO4.c005.water_add.A5001+4QO4.c005.water_add.A5002+4QO4.c005.water_add.A5003+4QO4.c005.water_add.A5004); nothing convicted

⚠ whole-model geometry outside the frozen caps: rota_outliers 2.41 > 1.5 (D479, monitor)

base after cycle: `/home/dev/runs/4QO4/runs/4QO4.20260917T052656Z/cycles/c005/paired/null_arm/refine_001.cif` · R-free full 0.3446706364302604 · report 0.36012623396614446 · Δselect vs before -0.001163 · 2055.3 s

## cycle 6 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 4, "attempted": 4, "accepted": 1, "reverted": 3, "not_attempted": []}, "solvent": {"proposed": 14, "attempted": 11, "accepted": 4, "reverted": 7, "not_attempted": ["4QO4.c006.water_add.A5003", "4QO4.c006.water_add.A5004", "4QO4.c006.water_add.A5005"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `4QO4.c006.rotamer_fix.A18` **accepted** — rscc 0.87675→0.8895 (Δ 0.01275, rule mean_delta, worst neighbour drop 0.0053): RSCC gate passed: RSCC gate passed under mean_delta (delta +0.0127 >= +0.01); worst untouched neighbour A.342.. moved -0.0053 (0.8334 -> 0.8281), allowed drop 0.02; local geometry bond_rmsd=0.00471 angle_rmsd=0.56825 over 17 bond(s)/24 angle(s) within the band for d_min=1.700359054039257; no new alt
- `4QO4.c006.rotamer_fix.A24` **reverted** — rscc 0.903767→0.919167 (Δ 0.0154, rule mean_delta, worst neighbour drop 0.0218): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.324.. moved -0.0218 (0.7929 -> 0.7711), allowed drop 0.02]; clash [1 new altloc-aware clash(es)]
- `4QO4.c006.peptide_flip.A79` **reverted** — rscc 0.8645→0.8643 (Δ -0.0002, rule mean_delta, worst neighbour drop 0.0039): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0002 < required +0.01]; clash [4 new altloc-aware clash(es)]
- `4QO4.c006.zone_rsr.A77-81` **reverted** — rscc 0.88174→0.87996 (Δ -0.00178, rule mean_delta, worst neighbour drop 0.0016): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.00178 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `4QO4.c006.water_remove.A370` **accepted** — rscc 0.6643→None (Δ None, rule removed_residue_floor, worst neighbour drop -0.0006): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.79.. moved +0.0006 (0.8421 -> 0.8427), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-r
- `4QO4.c006.water_remove.A371` **accepted** — rscc 0.6918→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.011): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.375.. moved -0.0110 (0.8326 -> 0.8216), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-
- `4QO4.c006.water_remove.A326` **reverted** — rscc 0.7145→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0196): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.326..=0.7145]
- `4QO4.c006.water_remove.A356` **reverted** — rscc 0.7679→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0037): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.356..=0.7679]
- `4QO4.c006.water_remove.A378` **reverted** — rscc 0.7977→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0001): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.378..=0.7977]
- `4QO4.c006.water_remove.A342` **reverted** — rscc 0.8318→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0017): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.342..=0.8318]
- `4QO4.c006.water_remove.A301` **reverted** — rscc 0.8974→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0056): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.301..=0.8974]
- `4QO4.c006.water_remove.A304` **reverted** — rscc 0.9416→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0079): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.304..=0.9416]
- `4QO4.c006.water_remove.A362` **reverted** — rscc 0.9559→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.002): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.362..=0.9559]
- `4QO4.c006.water_add.A5001` **accepted** — rscc None→0.9113 (Δ None, rule new_residue_floor, worst neighbour drop 0.0026): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.79.. moved -0.0026 (0.842 -> 0.8394), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-restri
- `4QO4.c006.water_add.A5002` **accepted** — rscc None→0.8482 (Δ None, rule new_residue_floor, worst neighbour drop 0.0025): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.324.. moved -0.0025 (0.7887 -> 0.7862), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.700359054039257; no new altloc-aware clash; site-rest

**paired cycle**: null arm R-free-select 0.33062819294006046 · treatment arm 0.33084427445829445 · attributable **+0.000216** vs credit ≤ -0.003744 / regression > +0.003744 → **no_change**  
attributable 0.000216 within (−0.003744, +0.003744]: of the raw -0.000009, -0.000225 is reproduced by re-refining the base with NO changes; the changes are not credited and are dropped: they made R-free-select worse, below the bar but worse (D411) || cross-check (phenix.model_vs_data, full set): null 0.344 · treatment 0.3437 · Δ -0.0003 — DISAGREES in sign: treat this credit as provisional || Metropolis (v8, D499): attributable +0.000216 = +0.12σ_select, T = 1σ = 0.001872, p_keep = exp(−Δ/T) = 0.891, u = 0.050 → KEPT: the candidate arm carries on, un-credited (D499)

cross-check (phenix.model_vs_data, full test set): null 0.344 · treatment 0.3437 · Δ -0.0003 → **DISAGREES in sign** with the gate — credit provisional (D409)

**Metropolis keep (v8, D499)**: attributable +0.000216 > 0 within noise; p_keep 0.891, u 0.050 — the candidate arm carries on un-credited

changes kept without credit; cumulative un-credited drift since the last credited base: +0.000216 (guard at > +0.003744)

⚠ whole-model geometry outside the frozen caps: rota_outliers 2.41 > 1.5 (D479, monitor)

base after cycle: `/home/dev/runs/4QO4/runs/4QO4.20260917T052656Z/cycles/c006/paired/candidate_arm/refine_001.cif` · R-free full 0.34346780864564974 · report 0.3575882838427747 · Δselect vs before -0.000009 · 1149.4 s

**stall detected** after cycle 6: 2 consecutive cycle(s) accepted changes locally but each moved R-free-select by < σ=0.001872: a minimum small edits cannot leave → next cycle takes an escape rung

## cycle 7 — stall escape rung `reweight_reseed`

different random seed, fresh xyz/adp weight optimisation, +3 macro-cycles: override `{'seed': 1001, 'optimize_xyz_weight': True, 'optimize_adp_weight': True, 'wxc_scale': None, 'wxu_scale': None, 'macro_cycles': 8}`  
null arm R-free-select 0.33181610427514646 · escape arm 0.3335813033450641 · attributable **+0.001765** → did not clear  
attributable 0.001765 within (−0.003744, +0.003744]: of the raw 0.002737, 0.000972 is reproduced by re-refining the base with NO changes; the changes are not credited and are not adopted (no local evidence of their own) || cross-check (phenix.model_vs_data, full set): null 0.3463 · treatment 0.3474 · Δ +0.0011 — agrees in sign  
ladder so far `{'reweight_reseed': 'failed'}`

## cycle 8 — stall escape rung `rescale_bulk_solvent`

bulk_solvent_and_scale.mode=slow — solvent and anisotropic scale re-fit from scratch: override `{'bulk_solvent_mode': 'slow'}`  
null arm R-free-select 0.3314094888341326 · escape arm 0.3187102950887748 · attributable **-0.012699** → **cleared**  
attributable -0.012699 ≤ -0.003744; the null arm moved -0.000407 on its own and is not credited || cross-check (phenix.model_vs_data, full set): null 0.3468 · treatment 0.3248 · Δ -0.0220 — agrees in sign  
ladder so far `{'reweight_reseed': 'failed', 'rescale_bulk_solvent': 'cleared'}`

## finished 2026-09-17T08:16:13+00:00

max_cycles=8 reached  
R-free full 0.36190468754175514 → 0.32495401078949043 (Δ -0.036951) · report 0.38475677251927276 → 0.3319381272327418  
published better model: None · gap closed: None · reached: None  
credited changes (11): `['4QO4.c001.water_remove.A346', '4QO4.c001.water_remove.A364', '4QO4.c001.water_remove.A309', '4QO4.c001.water_remove.A340', '4QO4.c001.water_remove.A310', '4QO4.c004.water_remove.A365', '4QO4.c004.water_remove.A325', '4QO4.c004.water_remove.A339', '4QO4.c004.water_remove.A329', '4QO4.c004.water_remove.A353', '4QO4.c008.weight_change.rescale_bulk_solvent']`  
kept without credit: 5 · final model `/home/dev/runs/4QO4/runs/4QO4.20260917T052656Z/cycles/c008/escape/candidate_arm/refine_001.cif`  
best base of the run: cycle 8 · R-free full 0.32495401078949043 · report 0.3319381272327418 · `/home/dev/runs/4QO4/runs/4QO4.20260917T052656Z/cycles/c008/escape/candidate_arm/refine_001.cif`

