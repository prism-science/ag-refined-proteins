# 9D5Y — run `9D5Y.20260917T095827Z`

started 2026-09-17T09:58:27+00:00 on actl-ws-xraymemory-autoresearch-devspace-8597768cc8-lxfq5 pid 1578991  
stages `['correction', 'solvent', 'protein_altloc']` · seed 1 · max cycles 8 · max/stage 20  
noise floor σ_select = 0.000743, k = 2.0: a cycle is credited at ≤ -0.001486, bisected above +0.001486  
published better model: none recorded in targets.yaml  
starting model: `/home/dev/runs/9D5Y/c000/baseline_rerefine/refine_001.cif`

## cycle 0 — base

cycle 0: re-refined the starting model to obtain map coefficients (/home/dev/runs/9D5Y/runs/9D5Y.20260917T095827Z/base/rerefine/refine_001.cif)  
R-work 0.2114453195130788 · R-free full 0.23359709497704842 · report 0.2404834227995269 (select 0.2267560047837419)

## cycle 1 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 20, "attempted": 20, "accepted": 0, "reverted": 20, "not_attempted": []}, "solvent": {"proposed": 20, "attempted": 5, "accepted": 5, "reverted": 0, "not_attempted": ["9D5Y.c001.water_add.B5002", "9D5Y.c001.water_add.B5003", "9D5Y.c001.water_add.B5004", "9D5Y.c001.water_add.B5005", "9D5Y.c001.water_add.B5006", "9D5Y.c001.water_add.B5007", "9D5Y.c001.water_add.B5008", "9D5Y.c001.water_add.B5009", "9D5Y.c001.water_add.B5010", "9D5Y.c001.water_add.B5011", "9D5Y.c001.water_add.B5012", "9D5Y.c001.water_add.B5013", "9D5Y.c001.water_add.B5014", "9D5Y.c001.water_add.B5015", "9D5Y.c001.water_add.B5016"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `9D5Y.c001.rotamer_fix.B228` **reverted** — rscc 0.83225→0.8253 (Δ -0.00695, rule mean_delta, worst neighbour drop 0.0019): failed: rscc [mean RSCC over 2 changed residue(s) moved -0.00695 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `9D5Y.c001.rotamer_fix.B1` **reverted** — rscc 0.89505→0.8922 (Δ -0.00285, rule mean_delta, worst neighbour drop 0.0018): failed: rscc [mean RSCC over 2 changed residue(s) moved -0.00285 < required +0.01]
- `9D5Y.c001.rotamer_fix.B211` **reverted** — rscc 0.933233→0.927267 (Δ -0.005966, rule mean_delta, worst neighbour drop 0.0054): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.005966 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `9D5Y.c001.rotamer_fix.B46` **reverted** — rscc 0.951067→0.932333 (Δ -0.018734, rule mean_delta, worst neighbour drop 0.0095): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.018734 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `9D5Y.c001.rotamer_fix.A204` **reverted** — rscc 0.79345→0.7763 (Δ -0.01715, rule mean_delta, worst neighbour drop 0.0023): failed: rscc [mean RSCC over 2 changed residue(s) moved -0.01715 < required +0.01]
- `9D5Y.c001.peptide_flip.B206` **reverted** — rscc 0.873925→0.790725 (Δ -0.0832, rule mean_delta, worst neighbour drop 0.006): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0832 < required +0.01]; geometry [angle_rmsd worsened by 0.5984 > rel_max 0.3 (prev 1.0794)]; clash [4 new altloc-aware clash(es)]
- `9D5Y.c001.peptide_flip.B226` **reverted** — rscc 0.8668→0.796075 (Δ -0.070725, rule mean_delta, worst neighbour drop 0.0052): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.070725 < required +0.01]; geometry [angle_rmsd worsened by 0.3435 > rel_max 0.3 (prev 0.54584)]; clash [2 new altloc-aware clash(es)]
- `9D5Y.c001.peptide_flip.B225` **reverted** — rscc 0.89815→0.5877 (Δ -0.31045, rule mean_delta, worst neighbour drop 0.0431): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.31045 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour B.228.. moved -0.0431 (0.7903 -> 0.7472), allowed drop 0.02]; clash [6 new altloc-aware clash(es)]
- `9D5Y.c001.peptide_flip.A178` **reverted** — rscc 0.935975→0.85215 (Δ -0.083825, rule mean_delta, worst neighbour drop 0.0038): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.083825 < required +0.01]; geometry [angle_rmsd worsened by 0.3893 > rel_max 0.3 (prev 0.56783)]; clash [4 new altloc-aware clash(es)]
- `9D5Y.c001.peptide_flip.A111` **reverted** — rscc 0.9484→0.749 (Δ -0.1994, rule mean_delta, worst neighbour drop 0.0132): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.1994 < required +0.01]; clash [3 new altloc-aware clash(es)]
- `9D5Y.c001.peptide_flip.B127` **reverted** — rscc 0.961175→0.9544 (Δ -0.006775, rule mean_delta, worst neighbour drop 0.0015): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.006775 < required +0.01]
- `9D5Y.c001.peptide_flip.B45` **reverted** — rscc 0.954875→0.90075 (Δ -0.054125, rule mean_delta, worst neighbour drop 0.0026): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.054125 < required +0.01]; geometry [angle_rmsd worsened by 0.3655 > rel_max 0.3 (prev 1.17397)]; clash [1 new altloc-aware clash(es)]
- `9D5Y.c001.peptide_flip.A50` **reverted** — rscc 0.9696→0.8645 (Δ -0.1051, rule mean_delta, worst neighbour drop 0.006): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.1051 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `9D5Y.c001.peptide_flip.B155` **reverted** — rscc 0.96135→0.917225 (Δ -0.044125, rule mean_delta, worst neighbour drop 0.0183): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.044125 < required +0.01]; clash [3 new altloc-aware clash(es)]
- `9D5Y.c001.peptide_flip.A196` **reverted** — rscc 0.967525→0.848 (Δ -0.119525, rule mean_delta, worst neighbour drop 0.0038): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.119525 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `9D5Y.c001.peptide_flip.A88` **reverted** — rscc 0.96915→0.8577 (Δ -0.11145, rule mean_delta, worst neighbour drop 0.0154): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.11145 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `9D5Y.c001.peptide_flip.A121` **reverted** — rscc 0.972625→0.970275 (Δ -0.00235, rule mean_delta, worst neighbour drop 0.0013): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.00235 < required +0.01]
- `9D5Y.c001.peptide_flip.A85` **reverted** — rscc 0.967325→0.767625 (Δ -0.1997, rule mean_delta, worst neighbour drop 0.0081): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.1997 < required +0.01]; geometry [angle_rmsd worsened by 0.9449 > rel_max 0.3 (prev 0.47074)]; clash [3 new altloc-aware clash(es)]
- `9D5Y.c001.peptide_flip.A164` **reverted** — rscc 0.95635→0.84435 (Δ -0.112, rule mean_delta, worst neighbour drop 0.0061): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.112 < required +0.01]; geometry [angle_rmsd worsened by 0.5686 > rel_max 0.3 (prev 1.08443)]; clash [6 new altloc-aware clash(es)]
- `9D5Y.c001.peptide_flip.A165` **reverted** — rscc 0.953975→0.952125 (Δ -0.00185, rule mean_delta, worst neighbour drop 0.0018): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.00185 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `9D5Y.c001.water_remove.A490` **accepted** — rscc 0.309→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0005): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.47.. moved -0.0005 (0.9446 -> 0.9441), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3499998698895317; no new altloc-aware clash; site-
- `9D5Y.c001.water_remove.A478` **accepted** — rscc 0.4817→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0005): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.48.. moved -0.0005 (0.9429 -> 0.9424), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3499998698895317; no new altloc-aware clash; site-
- `9D5Y.c001.water_remove.B418` **accepted** — rscc 0.5606→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0013): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour B.135.. moved -0.0013 (0.8963 -> 0.895), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3499998698895317; no new altloc-aware clash; site-
- `9D5Y.c001.water_remove.A474` **accepted** — rscc 0.6326→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0004): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.402.. moved -0.0004 (0.9806 -> 0.9802), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3499998698895317; no new altloc-aware clash; site
- `9D5Y.c001.water_add.B5001` **accepted** — rscc None→0.9419 (Δ None, rule new_residue_floor, worst neighbour drop 0.0027): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour B.1.. moved -0.0027 (0.8433 -> 0.8406), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3499998698895317; no new altloc-aware clash; site-restr

**paired cycle**: null arm R-free-select 0.22716973858434275 · treatment arm 0.22867102304129963 · attributable **+0.001501** vs credit ≤ -0.001486 / regression > +0.001486 → **rejected** (REGRESSED)  
attributable 0.001501 > +0.001486: the changes made R-free-select WORSE than the identically refined base — regression, bisect (SPEC_LOOP_V2 §1.3) || cross-check (phenix.model_vs_data, full set): null 0.234 · treatment 0.2341 · Δ +0.0001 — agrees in sign

cross-check (phenix.model_vs_data, full test set): null 0.234 · treatment 0.2341 · Δ +0.0001 → **agrees in sign** with the gate

bisection: culprits `[]` (2 refinement(s)); no subset beat the null arm — base ← null arm. no single change regresses on its own — the regression is an interaction between halves (9D5Y.c001.water_remove.A490+9D5Y.c001.water_remove.A478+9D5Y.c001.water_remove.B418+9D5Y.c001.water_remove.A474+9D5Y.c001.water_add.B5001); nothing convicted

base after cycle: `/home/dev/runs/9D5Y/runs/9D5Y.20260917T095827Z/cycles/c001/paired/null_arm/refine_001.cif` · R-free full 0.233676786049079 · report 0.24022686224050813 · Δselect vs before +0.000414 · 14386.3 s

## cycle 2 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 20, "attempted": 20, "accepted": 0, "reverted": 20, "not_attempted": []}, "solvent": {"proposed": 20, "attempted": 5, "accepted": 5, "reverted": 0, "not_attempted": ["9D5Y.c002.water_add.B5003", "9D5Y.c002.water_add.B5004", "9D5Y.c002.water_add.B5005", "9D5Y.c002.water_add.B5006", "9D5Y.c002.water_add.B5007", "9D5Y.c002.water_add.B5008", "9D5Y.c002.water_add.B5009", "9D5Y.c002.water_add.B5010", "9D5Y.c002.water_add.B5011", "9D5Y.c002.water_add.B5012", "9D5Y.c002.water_add.B5013", "9D5Y.c002.water_add.B5014", "9D5Y.c002.water_add.B5015", "9D5Y.c002.water_add.B5016", "9D5Y.c002.water_add.B5017"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `9D5Y.c002.rotamer_fix.B228` **reverted** — rscc 0.82785→0.82935 (Δ 0.0015, rule mean_delta, worst neighbour drop 0.0008): failed: rscc [mean RSCC over 2 changed residue(s) moved 0.0015 < required +0.01]; geometry [angle_rmsd worsened by 0.3146 > rel_max 0.3 (prev 0.50795)]; clash [1 new altloc-aware clash(es)]
- `9D5Y.c002.rotamer_fix.B1` **reverted** — rscc 0.89385→0.89075 (Δ -0.0031, rule mean_delta, worst neighbour drop 0.0013): failed: rscc [mean RSCC over 2 changed residue(s) moved -0.0031 < required +0.01]
- `9D5Y.c002.rotamer_fix.B211` **reverted** — rscc 0.934933→0.929233 (Δ -0.0057, rule mean_delta, worst neighbour drop 0.0062): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.0057 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `9D5Y.c002.rotamer_fix.B224` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: Coot rotamer_fix moved residue(s) outside the 3-residue window [('B', 223, ''), ('B', 224, ''), ('B', 225, '')]: [('B', 391, '')]
- `9D5Y.c002.rotamer_fix.B46` **reverted** — rscc 0.951667→0.930533 (Δ -0.021134, rule mean_delta, worst neighbour drop 0.0103): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.021134 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `9D5Y.c002.rotamer_fix.A204` **reverted** — rscc 0.7906→0.7819 (Δ -0.0087, rule mean_delta, worst neighbour drop 0.0008): failed: rscc [mean RSCC over 2 changed residue(s) moved -0.0087 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `9D5Y.c002.peptide_flip.B206` **reverted** — rscc 0.87465→0.79615 (Δ -0.0785, rule mean_delta, worst neighbour drop 0.005): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0785 < required +0.01]; geometry [angle_rmsd worsened by 0.7258 > rel_max 0.3 (prev 1.13579)]; clash [3 new altloc-aware clash(es)]
- `9D5Y.c002.peptide_flip.B226` **reverted** — rscc 0.865275→0.79865 (Δ -0.066625, rule mean_delta, worst neighbour drop 0.0056): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.066625 < required +0.01]; clash [4 new altloc-aware clash(es)]
- `9D5Y.c002.peptide_flip.B225` **reverted** — rscc 0.899225→0.5912 (Δ -0.308025, rule mean_delta, worst neighbour drop 0.0439): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.308025 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour B.228.. moved -0.0439 (0.7802 -> 0.7363), allowed drop 0.02]; clash [5 new altloc-aware clash(es)]
- `9D5Y.c002.peptide_flip.A178` **reverted** — rscc 0.9353→0.85115 (Δ -0.08415, rule mean_delta, worst neighbour drop 0.0038): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.08415 < required +0.01]; geometry [angle_rmsd worsened by 0.4963 > rel_max 0.3 (prev 0.50733)]; clash [3 new altloc-aware clash(es)]
- `9D5Y.c002.peptide_flip.A111` **reverted** — rscc 0.949767→0.748367 (Δ -0.2014, rule mean_delta, worst neighbour drop 0.0115): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.2014 < required +0.01]; clash [3 new altloc-aware clash(es)]
- `9D5Y.c002.peptide_flip.B127` **reverted** — rscc 0.96135→0.954175 (Δ -0.007175, rule mean_delta, worst neighbour drop 0.0017): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.007175 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `9D5Y.c002.peptide_flip.B45` **reverted** — rscc 0.955475→0.901075 (Δ -0.0544, rule mean_delta, worst neighbour drop 0.0024): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0544 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `9D5Y.c002.peptide_flip.A50` **reverted** — rscc 0.969525→0.863475 (Δ -0.10605, rule mean_delta, worst neighbour drop 0.0064): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.10605 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `9D5Y.c002.peptide_flip.B155` **reverted** — rscc 0.96215→0.917725 (Δ -0.044425, rule mean_delta, worst neighbour drop 0.0176): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.044425 < required +0.01]; clash [4 new altloc-aware clash(es)]
- `9D5Y.c002.peptide_flip.A196` **reverted** — rscc 0.96745→0.847 (Δ -0.12045, rule mean_delta, worst neighbour drop 0.0039): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.12045 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `9D5Y.c002.peptide_flip.A88` **reverted** — rscc 0.969→0.84975 (Δ -0.11925, rule mean_delta, worst neighbour drop 0.0135): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.11925 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `9D5Y.c002.peptide_flip.A121` **reverted** — rscc 0.972925→0.971075 (Δ -0.00185, rule mean_delta, worst neighbour drop 0.0024): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.00185 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `9D5Y.c002.peptide_flip.A85` **reverted** — rscc 0.967075→0.770925 (Δ -0.19615, rule mean_delta, worst neighbour drop 0.0068): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.19615 < required +0.01]; geometry [angle_rmsd worsened by 1.033 > rel_max 0.3 (prev 0.51136)]; clash [3 new altloc-aware clash(es)]
- `9D5Y.c002.peptide_flip.A164` **reverted** — rscc 0.95675→0.84455 (Δ -0.1122, rule mean_delta, worst neighbour drop 0.0087): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.1122 < required +0.01]; geometry [angle_rmsd worsened by 0.471 > rel_max 0.3 (prev 1.18572)]; clash [6 new altloc-aware clash(es)]
- `9D5Y.c002.water_remove.A490` **accepted** — rscc 0.3402→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0004): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.47.. moved -0.0004 (0.9448 -> 0.9444), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3499998698895317; no new altloc-aware clash; site-
- `9D5Y.c002.water_remove.B418` **accepted** — rscc 0.6025→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0011): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour B.135.. moved -0.0011 (0.8964 -> 0.8953), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3499998698895317; no new altloc-aware clash; site
- `9D5Y.c002.water_remove.A478` **accepted** — rscc 0.6439→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0004): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.48.. moved -0.0004 (0.9432 -> 0.9428), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3499998698895317; no new altloc-aware clash; site-
- `9D5Y.c002.water_add.B5001` **accepted** — rscc None→0.9375 (Δ None, rule new_residue_floor, worst neighbour drop 0.0003): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour B.183.. moved -0.0003 (0.9708 -> 0.9705), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3499998698895317; no new altloc-aware clash; site-res
- `9D5Y.c002.water_add.B5002` **accepted** — rscc None→0.9394 (Δ None, rule new_residue_floor, worst neighbour drop 0.0026): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour B.1.. moved -0.0026 (0.8438 -> 0.8412), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3499998698895317; no new altloc-aware clash; site-restr

**paired cycle**: null arm R-free-select 0.22666230919375946 · treatment arm 0.228567761059109 · attributable **+0.001905** vs credit ≤ -0.001486 / regression > +0.001486 → **rejected** (REGRESSED)  
attributable 0.001905 > +0.001486: the changes made R-free-select WORSE than the identically refined base — regression, bisect (SPEC_LOOP_V2 §1.3) || cross-check (phenix.model_vs_data, full set): null 0.2333 · treatment 0.2337 · Δ +0.0004 — agrees in sign

cross-check (phenix.model_vs_data, full test set): null 0.2333 · treatment 0.2337 · Δ +0.0004 → **agrees in sign** with the gate

bisection: culprits `[]` (2 refinement(s)); no subset beat the null arm — base ← null arm. no single change regresses on its own — the regression is an interaction between halves (9D5Y.c002.water_remove.A490+9D5Y.c002.water_remove.B418+9D5Y.c002.water_remove.A478+9D5Y.c002.water_add.B5001+9D5Y.c002.water_add.B5002); nothing convicted

base after cycle: `/home/dev/runs/9D5Y/runs/9D5Y.20260917T095827Z/cycles/c002/paired/null_arm/refine_001.cif` · R-free full 0.23331033135846468 · report 0.24000231446403084 · Δselect vs before -0.000507 · 14508.5 s

**stall detected** after cycle 2: 2 consecutive cycle(s) accepted changes locally but each moved R-free-select by < σ=0.000743: a minimum small edits cannot leave → next cycle takes an escape rung

## cycle 3 — stall escape rung `reweight_reseed`

different random seed, fresh xyz/adp weight optimisation, +3 macro-cycles: override `{'seed': 1001, 'optimize_xyz_weight': True, 'optimize_adp_weight': True, 'wxc_scale': None, 'wxu_scale': None, 'macro_cycles': 8}`  
null arm R-free-select 0.2264470578116706 · escape arm 0.22632128381707947 · attributable **-0.000126** → did not clear  
attributable -0.000126 within (−0.001486, +0.001486]: of the raw -0.000341, -0.000215 is reproduced by re-refining the base with NO changes; the changes are not credited and are not adopted (no local evidence of their own) || cross-check (phenix.model_vs_data, full set): null 0.2335 · treatment 0.2336 · Δ +0.0001 — DISAGREES in sign: treat this credit as provisional  
ladder so far `{'reweight_reseed': 'failed'}`

## cycle 4 — stall escape rung `rescale_bulk_solvent`

bulk_solvent_and_scale.mode=slow — solvent and anisotropic scale re-fit from scratch: override `{'bulk_solvent_mode': 'slow'}`  
null arm R-free-select 0.22669081562534324 · escape arm 0.22715215304382574 · attributable **+0.000461** → did not clear  
attributable 0.000461 within (−0.001486, +0.001486]: of the raw 0.000705, 0.000244 is reproduced by re-refining the base with NO changes; the changes are not credited and are not adopted (no local evidence of their own) || cross-check (phenix.model_vs_data, full set): null 0.2337 · treatment 0.2337 · Δ +0.0000 — agrees in sign  
ladder so far `{'reweight_reseed': 'failed', 'rescale_bulk_solvent': 'failed'}`

## cycle 5 — escape

escape ladder exhausted (reweight_reseed=failed, rescale_bulk_solvent=failed, simulated_annealing=refused): the model is converged at this minimum. **Converged at this minimum.**

## finished 2026-09-17T21:07:21+00:00

escape ladder exhausted (reweight_reseed=failed, rescale_bulk_solvent=failed, simulated_annealing=refused): the model is converged at this minimum  
R-free full 0.23359709497704842 → 0.23340040659130262 (Δ -0.000197) · report 0.2404834227995269 → 0.24015436563010356  
published better model: None · gap closed: None · reached: None  
credited changes (0): `[]`  
kept without credit: 0 · final model `/home/dev/runs/9D5Y/runs/9D5Y.20260917T095827Z/cycles/c004/escape/null_arm/refine_001.cif`  
best base of the run: cycle 3 · R-free full 0.23315949529026464 · report 0.23991631966464783 · `/home/dev/runs/9D5Y/runs/9D5Y.20260917T095827Z/cycles/c003/escape/null_arm/refine_001.cif`

