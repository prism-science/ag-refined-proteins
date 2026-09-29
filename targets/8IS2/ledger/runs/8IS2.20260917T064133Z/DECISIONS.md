# 8IS2 — run `8IS2.20260917T064133Z`

started 2026-09-17T06:41:33+00:00 on actl-ws-xraymemory-autoresearch-devspace-8597768cc8-lxfq5 pid 668676  
stages `['correction', 'solvent', 'protein_altloc']` · seed 1 · max cycles 8 · max/stage 20  
noise floor σ_select = 0.001002, k = 2.0: a cycle is credited at ≤ -0.002004, bisected above +0.002004  
published better model: none recorded in targets.yaml  
starting model: `/home/dev/runs/8IS2/c000/baseline_rerefine/refine_001.cif`

## cycle 0 — base

cycle 0: re-refined the starting model to obtain map coefficients (/home/dev/runs/8IS2/runs/8IS2.20260917T064133Z/base/rerefine/refine_001.cif)  
R-work 0.22411924136785685 · R-free full 0.2648328460442745 · report 0.27948476541684597 (select 0.24956050430223833)

## cycle 1 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 20, "attempted": 20, "accepted": 0, "reverted": 20, "not_attempted": []}, "solvent": {"proposed": 20, "attempted": 6, "accepted": 5, "reverted": 1, "not_attempted": ["8IS2.c001.water_remove.A208", "8IS2.c001.water_remove.B216", "8IS2.c001.water_remove.A222", "8IS2.c001.water_remove.B268", "8IS2.c001.water_remove.A284", "8IS2.c001.water_remove.A265", "8IS2.c001.water_remove.B251", "8IS2.c001.water_add.A5001", "8IS2.c001.water_add.A5002", "8IS2.c001.water_add.A5003", "8IS2.c001.water_add.A5004", "8IS2.c001.water_add.A5005", "8IS2.c001.water_add.A5006", "8IS2.c001.water_add.A5007"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `8IS2.c001.rotamer_fix.B68` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: Coot rotamer_fix moved residue(s) outside the 2-residue window [('B', 68, ''), ('B', 69, '')]: [('B', 55, '')]
- `8IS2.c001.rotamer_fix.A87` **reverted** — rscc 0.798→0.7444 (Δ -0.0536, rule mean_delta, worst neighbour drop 0.0112): failed: rscc [mean RSCC over 2 changed residue(s) moved -0.0536 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `8IS2.c001.peptide_flip.A14` **reverted** — rscc 0.926125→0.8196 (Δ -0.106525, rule mean_delta, worst neighbour drop 0.0397): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.106525 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.212.. moved -0.0397 (0.7722 -> 0.7325), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.4799 > rel_max 0.3 (prev 1.04402)]; 
- `8IS2.c001.peptide_flip.B14` **reverted** — rscc 0.8601→0.856125 (Δ -0.003975, rule mean_delta, worst neighbour drop 0.0082): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.003975 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `8IS2.c001.peptide_flip.B108` **reverted** — rscc 0.9311→0.90725 (Δ -0.02385, rule mean_delta, worst neighbour drop 0.0182): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.02385 < required +0.01]
- `8IS2.c001.peptide_flip.B107` **reverted** — rscc 0.92225→0.9096 (Δ -0.01265, rule mean_delta, worst neighbour drop 0.0062): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.01265 < required +0.01]
- `8IS2.c001.peptide_flip.B111` **reverted** — rscc 0.941575→0.9389 (Δ -0.002675, rule mean_delta, worst neighbour drop 0.0113): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.002675 < required +0.01]
- `8IS2.c001.peptide_flip.B109` **reverted** — rscc 0.93455→0.858825 (Δ -0.075725, rule mean_delta, worst neighbour drop 0.026): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.075725 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour B.253.. moved -0.0260 (0.8328 -> 0.8068), allowed drop 0.02]; clash [3 new altloc-aware clash(es)]
- `8IS2.c001.peptide_flip.B110` **reverted** — rscc 0.9412→0.87835 (Δ -0.06285, rule mean_delta, worst neighbour drop 0.0261): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.06285 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.277.. moved -0.0261 (0.8346 -> 0.8085), allowed drop 0.02]; clash [3 new altloc-aware clash(es)]
- `8IS2.c001.peptide_flip.A108` **reverted** — rscc 0.9427→0.881575 (Δ -0.061125, rule mean_delta, worst neighbour drop 0.0243): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.061125 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.210.. moved -0.0243 (0.8623 -> 0.838), allowed drop 0.02]
- `8IS2.c001.peptide_flip.B92` **reverted** — rscc 0.947375→0.85935 (Δ -0.088025, rule mean_delta, worst neighbour drop 0.0238): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.088025 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.252.. moved -0.0238 (0.8032 -> 0.7794), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.5764 > rel_max 0.3 (prev 1.30534)]; 
- `8IS2.c001.peptide_flip.B90` **reverted** — rscc 0.95825→0.86305 (Δ -0.0952, rule mean_delta, worst neighbour drop 0.0161): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0952 < required +0.01]; clash [6 new altloc-aware clash(es)]
- `8IS2.c001.peptide_flip.A47` **reverted** — rscc 0.954→0.8684 (Δ -0.0856, rule mean_delta, worst neighbour drop 0.0184): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0856 < required +0.01]; clash [5 new altloc-aware clash(es)]
- `8IS2.c001.peptide_flip.B91` **reverted** — rscc 0.952925→0.84245 (Δ -0.110475, rule mean_delta, worst neighbour drop 0.0113): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.110475 < required +0.01]; geometry [angle_rmsd worsened by 0.3281 > rel_max 0.3 (prev 1.2099)]; clash [1 new altloc-aware clash(es)]
- `8IS2.c001.zone_rsr.A85-87` **reverted** — rscc 0.8436→0.840433 (Δ -0.003167, rule mean_delta, worst neighbour drop 0.0008): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.003167 < required +0.01]
- `8IS2.c001.zone_rsr.B12-16` **reverted** — rscc 0.8699→0.87404 (Δ 0.00414, rule mean_delta, worst neighbour drop 0.0049): failed: rscc [mean RSCC over 5 changed residue(s) moved 0.00414 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `8IS2.c001.zone_rsr.A12-16` **reverted** — rscc 0.92608→0.9293 (Δ 0.00322, rule mean_delta, worst neighbour drop 0.0011): failed: rscc [mean RSCC over 5 changed residue(s) moved 0.00322 < required +0.01]
- `8IS2.c001.zone_rsr.B105-113` **reverted** — rscc 0.928589→0.929922 (Δ 0.001333, rule mean_delta, worst neighbour drop 0.0044): failed: rscc [mean RSCC over 9 changed residue(s) moved 0.001333 < required +0.01]
- `8IS2.c001.zone_rsr.A106-110` **reverted** — rscc 0.94282→0.94762 (Δ 0.0048, rule mean_delta, worst neighbour drop 0.006): failed: rscc [mean RSCC over 5 changed residue(s) moved 0.0048 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `8IS2.c001.zone_rsr.B88-94` **reverted** — rscc 0.951229→0.952586 (Δ 0.001357, rule mean_delta, worst neighbour drop 0.0018): failed: rscc [mean RSCC over 7 changed residue(s) moved 0.001357 < required +0.01]
- `8IS2.c001.water_remove.A262` **accepted** — rscc 0.4159→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0015): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.60.. moved -0.0015 (0.9034 -> 0.9019), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3218055758019736; no new altloc-aware clash; site-
- `8IS2.c001.water_remove.A267` **reverted** — rscc 0.5034→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0229): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.260.. moved -0.0229 (0.7977 -> 0.7748), allowed drop 0.02]
- `8IS2.c001.water_remove.B258` **accepted** — rscc 0.5371→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0003): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour B.103.. moved -0.0003 (0.9631 -> 0.9628), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3218055758019736; no new altloc-aware clash; site
- `8IS2.c001.water_remove.B212` **accepted** — rscc 0.6463→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.017): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour B.245.. moved -0.0170 (0.7148 -> 0.6978), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3218055758019736; no new altloc-aware clash; site
- `8IS2.c001.water_remove.A204` **accepted** — rscc 0.6339→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0007): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.81.. moved -0.0007 (0.945 -> 0.9443), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3218055758019736; no new altloc-aware clash; site-r
- `8IS2.c001.water_remove.B208` **accepted** — rscc 0.6888→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.006): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour B.99.. moved -0.0060 (0.9119 -> 0.9059), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3218055758019736; no new altloc-aware clash; site-

**paired cycle**: null arm R-free-select 0.24796928521733774 · treatment arm 0.24783538807334832 · attributable **-0.000134** vs credit ≤ -0.002004 / regression > +0.002004 → **no_change**  
attributable -0.000134 within (−0.002004, +0.002004]: of the raw -0.001725, -0.001591 is reproduced by re-refining the base with NO changes; the changes are not credited but stay (locally better, and not worse globally) || cross-check (phenix.model_vs_data, full set): null 0.2637 · treatment 0.2628 · Δ -0.0009 — agrees in sign

cross-check (phenix.model_vs_data, full test set): null 0.2637 · treatment 0.2628 · Δ -0.0009 → **agrees in sign** with the gate

changes kept without credit; cumulative un-credited drift since the last credited base: -0.000134 (guard at > +0.002004)

base after cycle: `/home/dev/runs/8IS2/runs/8IS2.20260917T064133Z/cycles/c001/paired/candidate_arm/refine_001.cif` · R-free full 0.262838793835424 · report 0.2772327024614257 · Δselect vs before -0.001725 · 3443.3 s

## cycle 2 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 19, "attempted": 19, "accepted": 0, "reverted": 19, "not_attempted": []}, "solvent": {"proposed": 17, "attempted": 11, "accepted": 5, "reverted": 6, "not_attempted": ["8IS2.c002.water_add.A5004", "8IS2.c002.water_add.A5005", "8IS2.c002.water_add.A5006", "8IS2.c002.water_add.A5007", "8IS2.c002.water_add.A5008", "8IS2.c002.water_add.A5009"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `8IS2.c002.rotamer_fix.B68` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: Coot rotamer_fix moved residue(s) outside the 2-residue window [('B', 68, ''), ('B', 69, '')]: [('B', 55, '')]
- `8IS2.c002.rotamer_fix.A87` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: Coot rotamer_fix moved residue(s) outside the 2-residue window [('A', 86, ''), ('A', 87, '')]: [('A', 95, '')]
- `8IS2.c002.peptide_flip.A14` **reverted** — rscc 0.92685→0.82185 (Δ -0.105, rule mean_delta, worst neighbour drop 0.0244): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.105 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.203.. moved -0.0244 (0.7459 -> 0.7215), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.5618 > rel_max 0.3 (prev 0.99186)]; cla
- `8IS2.c002.peptide_flip.B14` **reverted** — rscc 0.857875→0.85075 (Δ -0.007125, rule mean_delta, worst neighbour drop 0.0145): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.007125 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `8IS2.c002.peptide_flip.B108` **reverted** — rscc 0.9291→0.8614 (Δ -0.0677, rule mean_delta, worst neighbour drop 0.008): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0677 < required +0.01]; geometry [angle_rmsd worsened by 0.4063 > rel_max 0.3 (prev 1.25537)]; clash [3 new altloc-aware clash(es)]
- `8IS2.c002.peptide_flip.B107` **reverted** — rscc 0.920075→0.909325 (Δ -0.01075, rule mean_delta, worst neighbour drop 0.0036): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.01075 < required +0.01]
- `8IS2.c002.peptide_flip.B111` **reverted** — rscc 0.94235→0.9393 (Δ -0.00305, rule mean_delta, worst neighbour drop 0.0046): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.00305 < required +0.01]
- `8IS2.c002.peptide_flip.B109` **reverted** — rscc 0.93355→0.857525 (Δ -0.076025, rule mean_delta, worst neighbour drop 0.0166): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.076025 < required +0.01]; clash [3 new altloc-aware clash(es)]
- `8IS2.c002.peptide_flip.B110` **reverted** — rscc 0.941525→0.879825 (Δ -0.0617, rule mean_delta, worst neighbour drop 0.0163): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0617 < required +0.01]; clash [3 new altloc-aware clash(es)]
- `8IS2.c002.peptide_flip.B92` **reverted** — rscc 0.948375→0.85965 (Δ -0.088725, rule mean_delta, worst neighbour drop 0.0177): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.088725 < required +0.01]; geometry [angle_rmsd worsened by 0.6268 > rel_max 0.3 (prev 1.26665)]; clash [1 new altloc-aware clash(es)]
- `8IS2.c002.peptide_flip.A108` **reverted** — rscc 0.94195→0.883125 (Δ -0.058825, rule mean_delta, worst neighbour drop 0.0169): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.058825 < required +0.01]
- `8IS2.c002.peptide_flip.B90` **reverted** — rscc 0.956125→0.847325 (Δ -0.1088, rule mean_delta, worst neighbour drop 0.0184): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.1088 < required +0.01]; clash [6 new altloc-aware clash(es)]
- `8IS2.c002.peptide_flip.B91` **reverted** — rscc 0.951775→0.844725 (Δ -0.10705, rule mean_delta, worst neighbour drop 0.0138): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.10705 < required +0.01]; geometry [angle_rmsd worsened by 0.4108 > rel_max 0.3 (prev 1.14264)]; clash [1 new altloc-aware clash(es)]
- `8IS2.c002.zone_rsr.A85-87` **reverted** — rscc 0.843567→0.842933 (Δ -0.000634, rule mean_delta, worst neighbour drop 0.0042): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.000634 < required +0.01]
- `8IS2.c002.zone_rsr.B12-16` **reverted** — rscc 0.86924→0.87238 (Δ 0.00314, rule mean_delta, worst neighbour drop 0.0072): failed: rscc [mean RSCC over 5 changed residue(s) moved 0.00314 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `8IS2.c002.zone_rsr.A12-16` **reverted** — rscc 0.92538→0.92882 (Δ 0.00344, rule mean_delta, worst neighbour drop 0.0017): failed: rscc [mean RSCC over 5 changed residue(s) moved 0.00344 < required +0.01]
- `8IS2.c002.zone_rsr.B105-113` **reverted** — rscc 0.928→0.928789 (Δ 0.000789, rule mean_delta, worst neighbour drop 0.0039): failed: rscc [mean RSCC over 9 changed residue(s) moved 0.000789 < required +0.01]
- `8IS2.c002.zone_rsr.A106-110` **reverted** — rscc 0.9418→0.94702 (Δ 0.00522, rule mean_delta, worst neighbour drop 0.0049): failed: rscc [mean RSCC over 5 changed residue(s) moved 0.00522 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `8IS2.c002.zone_rsr.B88-94` **reverted** — rscc 0.951671→0.953114 (Δ 0.001443, rule mean_delta, worst neighbour drop 0.0056): failed: rscc [mean RSCC over 7 changed residue(s) moved 0.001443 < required +0.01]
- `8IS2.c002.water_remove.A267` **accepted** — rscc 0.5758→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0162): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.260.. moved -0.0162 (0.7885 -> 0.7723), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3218055758019736; no new altloc-aware clash; site
- `8IS2.c002.water_remove.A208` **accepted** — rscc 0.6712→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0058): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.211.. moved -0.0058 (0.8214 -> 0.8156), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3218055758019736; no new altloc-aware clash; site
- `8IS2.c002.water_remove.B245` **reverted** — rscc 0.7009→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.002): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: B.245..=0.7009]
- `8IS2.c002.water_remove.B268` **reverted** — rscc 0.7622→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0031): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: B.268..=0.7622]
- `8IS2.c002.water_remove.A222` **reverted** — rscc 0.7563→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0103): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.222..=0.7563]
- `8IS2.c002.water_remove.A284` **reverted** — rscc 0.824→None (Δ None, rule removed_residue_floor, worst neighbour drop None): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.284..=0.824]
- `8IS2.c002.water_remove.A265` **reverted** — rscc 0.8672→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0021): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.265..=0.8672]
- `8IS2.c002.water_remove.B251` **reverted** — rscc 0.9103→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0025): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: B.251..=0.9103]
- `8IS2.c002.water_add.A5001` **accepted** — rscc None→0.9132 (Δ None, rule new_residue_floor, worst neighbour drop 0.0074): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.271.. moved -0.0074 (0.8087 -> 0.8013), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3218055758019736; no new altloc-aware clash; site-res
- `8IS2.c002.water_add.A5002` **accepted** — rscc None→0.9079 (Δ None, rule new_residue_floor, worst neighbour drop 0.0005): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.79.. moved -0.0005 (0.9573 -> 0.9568), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3218055758019736; no new altloc-aware clash; site-rest
- `8IS2.c002.water_add.A5003` **accepted** — rscc None→0.9263 (Δ None, rule new_residue_floor, worst neighbour drop 0.0011): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour B.32.. moved -0.0011 (0.9438 -> 0.9427), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3218055758019736; no new altloc-aware clash; site-rest

**paired cycle**: null arm R-free-select 0.24704289460810888 · treatment arm 0.24748670026973987 · attributable **+0.000444** vs credit ≤ -0.002004 / regression > +0.002004 → **no_change**  
attributable 0.000444 within (−0.002004, +0.002004]: of the raw -0.000349, -0.000792 is reproduced by re-refining the base with NO changes; the changes are not credited and are dropped: they made R-free-select worse, below the bar but worse (D411) || cross-check (phenix.model_vs_data, full set): null 0.2619 · treatment 0.2623 · Δ +0.0004 — agrees in sign || Metropolis (v8, D499): attributable +0.000444 = +0.44σ_select, T = 1σ = 0.001002, p_keep = exp(−Δ/T) = 0.642, u = 0.015 → KEPT: the candidate arm carries on, un-credited (D499)

cross-check (phenix.model_vs_data, full test set): null 0.2619 · treatment 0.2623 · Δ +0.0004 → **agrees in sign** with the gate

**Metropolis keep (v8, D499)**: attributable +0.000444 > 0 within noise; p_keep 0.642, u 0.015 — the candidate arm carries on un-credited

changes kept without credit; cumulative un-credited drift since the last credited base: +0.000310 (guard at > +0.002004)

base after cycle: `/home/dev/runs/8IS2/runs/8IS2.20260917T064133Z/cycles/c002/paired/candidate_arm/refine_001.cif` · R-free full 0.2623782439631469 · report 0.2766648347960602 · Δselect vs before -0.000349 · 3591.3 s

## cycle 3 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 18, "attempted": 18, "accepted": 0, "reverted": 18, "not_attempted": []}, "solvent": {"proposed": 16, "attempted": 12, "accepted": 5, "reverted": 7, "not_attempted": ["8IS2.c003.water_add.A5007", "8IS2.c003.water_add.A5008", "8IS2.c003.water_add.A5009", "8IS2.c003.water_add.A5010"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `8IS2.c003.rotamer_fix.A87` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: Coot rotamer_fix moved residue(s) outside the 2-residue window [('A', 86, ''), ('A', 87, '')]: [('A', 95, '')]
- `8IS2.c003.peptide_flip.A14` **reverted** — rscc 0.928125→0.793975 (Δ -0.13415, rule mean_delta, worst neighbour drop 0.0275): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.13415 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.212.. moved -0.0275 (0.8164 -> 0.7889), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.5462 > rel_max 0.3 (prev 0.79599)]; c
- `8IS2.c003.peptide_flip.B14` **reverted** — rscc 0.86275→0.78195 (Δ -0.0808, rule mean_delta, worst neighbour drop 0.0511): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0808 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour B.203.. moved -0.0511 (0.8339 -> 0.7828), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.7754 > rel_max 0.3 (prev 0.62227)]; cl
- `8IS2.c003.peptide_flip.B108` **reverted** — rscc 0.932625→0.848125 (Δ -0.0845, rule mean_delta, worst neighbour drop 0.0197): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0845 < required +0.01]; geometry [angle_rmsd worsened by 0.3294 > rel_max 0.3 (prev 1.13695)]; clash [3 new altloc-aware clash(es)]
- `8IS2.c003.peptide_flip.B107` **reverted** — rscc 0.924775→0.912975 (Δ -0.0118, rule mean_delta, worst neighbour drop 0.0042): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0118 < required +0.01]
- `8IS2.c003.peptide_flip.B111` **reverted** — rscc 0.9426→0.9391 (Δ -0.0035, rule mean_delta, worst neighbour drop 0.0088): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0035 < required +0.01]
- `8IS2.c003.peptide_flip.B109` **reverted** — rscc 0.935575→0.86135 (Δ -0.074225, rule mean_delta, worst neighbour drop 0.02): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.074225 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `8IS2.c003.peptide_flip.B92` **reverted** — rscc 0.94795→0.85785 (Δ -0.0901, rule mean_delta, worst neighbour drop 0.0242): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0901 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.280.. moved -0.0242 (0.8506 -> 0.8264), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.6301 > rel_max 0.3 (prev 1.25598)]; cl
- `8IS2.c003.peptide_flip.B110` **reverted** — rscc 0.94205→0.8322 (Δ -0.10985, rule mean_delta, worst neighbour drop 0.0149): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.10985 < required +0.01]; clash [5 new altloc-aware clash(es)]
- `8IS2.c003.peptide_flip.A108` **reverted** — rscc 0.94395→0.87275 (Δ -0.0712, rule mean_delta, worst neighbour drop 0.0284): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0712 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.210.. moved -0.0284 (0.864 -> 0.8356), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.3666 > rel_max 0.3 (prev 0.82152)]; cla
- `8IS2.c003.peptide_flip.B90` **reverted** — rscc 0.955325→0.842 (Δ -0.113325, rule mean_delta, worst neighbour drop 0.0253): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.113325 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.227.. moved -0.0253 (0.78 -> 0.7547), allowed drop 0.02]; clash [5 new altloc-aware clash(es)]
- `8IS2.c003.peptide_flip.B91` **reverted** — rscc 0.95185→0.822 (Δ -0.12985, rule mean_delta, worst neighbour drop 0.0176): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.12985 < required +0.01]; geometry [angle_rmsd worsened by 0.3325 > rel_max 0.3 (prev 1.10143)]; clash [1 new altloc-aware clash(es)]
- `8IS2.c003.zone_rsr.A85-87` **reverted** — rscc 0.842→0.841733 (Δ -0.000267, rule mean_delta, worst neighbour drop 0.0036): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.000267 < required +0.01]
- `8IS2.c003.zone_rsr.B12-16` **reverted** — rscc 0.87418→0.87568 (Δ 0.0015, rule mean_delta, worst neighbour drop 0.0036): failed: rscc [mean RSCC over 5 changed residue(s) moved 0.0015 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `8IS2.c003.zone_rsr.A12-16` **reverted** — rscc 0.92758→0.93102 (Δ 0.00344, rule mean_delta, worst neighbour drop 0.0016): failed: rscc [mean RSCC over 5 changed residue(s) moved 0.00344 < required +0.01]
- `8IS2.c003.zone_rsr.B105-113` **reverted** — rscc 0.9304→0.929756 (Δ -0.000644, rule mean_delta, worst neighbour drop 0.0044): failed: rscc [mean RSCC over 9 changed residue(s) moved -0.000644 < required +0.01]
- `8IS2.c003.zone_rsr.A106-110` **reverted** — rscc 0.94422→0.94844 (Δ 0.00422, rule mean_delta, worst neighbour drop 0.0033): failed: rscc [mean RSCC over 5 changed residue(s) moved 0.00422 < required +0.01]
- `8IS2.c003.zone_rsr.B88-94` **reverted** — rscc 0.950957→0.9528 (Δ 0.001843, rule mean_delta, worst neighbour drop 0.0025): failed: rscc [mean RSCC over 7 changed residue(s) moved 0.001843 < required +0.01]
- `8IS2.c003.water_remove.A207` **accepted** — rscc 0.6878→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0025): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.5002.. moved -0.0025 (0.9483 -> 0.9458), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3218055758019736; no new altloc-aware clash; sit
- `8IS2.c003.water_remove.B201` **reverted** — rscc 0.6868→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0202): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour B.216.. moved -0.0202 (0.7067 -> 0.6865), allowed drop 0.02]
- `8IS2.c003.water_remove.B245` **accepted** — rscc 0.6987→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0004): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour B.13.. moved -0.0004 (0.8664 -> 0.866), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3218055758019736; no new altloc-aware clash; site-r
- `8IS2.c003.water_remove.A275` **reverted** — rscc 0.7211→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0004): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.275..=0.7211]
- `8IS2.c003.water_remove.B268` **reverted** — rscc 0.7329→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0043): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: B.268..=0.7329]
- `8IS2.c003.water_remove.A222` **reverted** — rscc 0.7573→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0089): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.222..=0.7573]
- `8IS2.c003.water_remove.A284` **reverted** — rscc 0.8121→None (Δ None, rule removed_residue_floor, worst neighbour drop None): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.284..=0.8121]
- `8IS2.c003.water_remove.A265` **reverted** — rscc 0.835→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0018): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: A.265..=0.835]
- `8IS2.c003.water_remove.B251` **reverted** — rscc 0.9022→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0059): failed: rscc [removed residue(s) that were fitting their density at or above solvent.water_rscc_min=0.7: B.251..=0.9022]
- `8IS2.c003.water_add.A5004` **accepted** — rscc None→0.8019 (Δ None, rule new_residue_floor, worst neighbour drop -0.0005): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour B.38.. moved +0.0005 (0.9238 -> 0.9243), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3218055758019736; no new altloc-aware clash; site-rest
- `8IS2.c003.water_add.A5005` **accepted** — rscc None→0.908 (Δ None, rule new_residue_floor, worst neighbour drop 0.0021): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.59.. moved -0.0021 (0.8376 -> 0.8355), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3218055758019736; no new altloc-aware clash; site-rest
- `8IS2.c003.water_add.A5006` **accepted** — rscc None→0.903 (Δ None, rule new_residue_floor, worst neighbour drop 0.0037): RSCC gate passed: RSCC gate passed under new_residue_floor; worst untouched neighbour A.264.. moved -0.0037 (0.8721 -> 0.8684), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.3218055758019736; no new altloc-aware clash; site-res

**paired cycle**: null arm R-free-select 0.24810089316032385 · treatment arm 0.24825291505152186 · attributable **+0.000152** vs credit ≤ -0.002004 / regression > +0.002004 → **no_change**  
attributable 0.000152 within (−0.002004, +0.002004]: of the raw 0.000766, 0.000614 is reproduced by re-refining the base with NO changes; the changes are not credited and are dropped: they made R-free-select worse, below the bar but worse (D411) || cross-check (phenix.model_vs_data, full set): null 0.262 · treatment 0.262 · Δ +0.0000 — agrees in sign || Metropolis (v8, D499): attributable +0.000152 = +0.15σ_select, T = 1σ = 0.001002, p_keep = exp(−Δ/T) = 0.859, u = 0.470 → KEPT: the candidate arm carries on, un-credited (D499)

cross-check (phenix.model_vs_data, full test set): null 0.262 · treatment 0.262 · Δ +0.0000 → **agrees in sign** with the gate

**Metropolis keep (v8, D499)**: attributable +0.000152 > 0 within noise; p_keep 0.859, u 0.470 — the candidate arm carries on un-credited

changes kept without credit; cumulative un-credited drift since the last credited base: +0.000462 (guard at > +0.002004)

base after cycle: `/home/dev/runs/8IS2/runs/8IS2.20260917T064133Z/cycles/c003/paired/candidate_arm/refine_001.cif` · R-free full 0.2622507423735067 · report 0.27567992309622125 · Δselect vs before +0.000766 · 3593.1 s

**stall detected** after cycle 3: 2 consecutive cycle(s) accepted changes locally but each moved R-free-select by < σ=0.001002: a minimum small edits cannot leave → next cycle takes an escape rung

## cycle 4 — stall escape rung `reweight_reseed`

different random seed, fresh xyz/adp weight optimisation, +3 macro-cycles: override `{'seed': 1001, 'optimize_xyz_weight': True, 'optimize_adp_weight': True, 'wxc_scale': None, 'wxu_scale': None, 'macro_cycles': 8}`  
null arm R-free-select 0.24915086871424375 · escape arm 0.2480632542501447 · attributable **-0.001088** → did not clear  
attributable -0.001088 within (−0.002004, +0.002004]: of the raw -0.000190, 0.000898 is reproduced by re-refining the base with NO changes; the changes are not credited and are not adopted (no local evidence of their own) || cross-check (phenix.model_vs_data, full set): null 0.2628 · treatment 0.2623 · Δ -0.0005 — agrees in sign  
ladder so far `{'reweight_reseed': 'failed'}`

## cycle 5 — stall escape rung `rescale_bulk_solvent`

bulk_solvent_and_scale.mode=slow — solvent and anisotropic scale re-fit from scratch: override `{'bulk_solvent_mode': 'slow'}`  
null arm R-free-select 0.2493424220899396 · escape arm 0.2486724055753783 · attributable **-0.000670** → did not clear  
attributable -0.000670 within (−0.002004, +0.002004]: of the raw -0.000478, 0.000192 is reproduced by re-refining the base with NO changes; the changes are not credited and are not adopted (no local evidence of their own) || cross-check (phenix.model_vs_data, full set): null 0.2628 · treatment 0.2631 · Δ +0.0003 — DISAGREES in sign: treat this credit as provisional  
ladder so far `{'reweight_reseed': 'failed', 'rescale_bulk_solvent': 'failed'}`

## cycle 6 — stall escape rung `simulated_annealing`

simulated annealing (no altlocs present): override `{'simulated_annealing': True}`  
null arm R-free-select 0.25052653457875057 · escape arm 0.2613795246524598 · attributable **+0.010853** → did not clear  
attributable 0.010853 > +0.002004: the changes made R-free-select WORSE than the identically refined base — regression, bisect (SPEC_LOOP_V2 §1.3) || cross-check (phenix.model_vs_data, full set): null 0.2634 · treatment 0.2678 · Δ +0.0044 — agrees in sign  
ladder so far `{'reweight_reseed': 'failed', 'rescale_bulk_solvent': 'failed', 'simulated_annealing': 'failed'}`

## cycle 7 — escape

escape ladder exhausted (reweight_reseed=failed, rescale_bulk_solvent=failed, simulated_annealing=failed): the model is converged at this minimum. **Converged at this minimum.**

## finished 2026-09-17T11:08:50+00:00

escape ladder exhausted (reweight_reseed=failed, rescale_bulk_solvent=failed, simulated_annealing=failed): the model is converged at this minimum  
R-free full 0.2648328460442745 → 0.2637038369559452 (Δ -0.001129) · report 0.27948476541684597 → 0.2763458256725295  
published better model: None · gap closed: None · reached: None  
credited changes (0): `[]`  
kept without credit: 15 · final model `/home/dev/runs/8IS2/runs/8IS2.20260917T064133Z/cycles/c006/escape/null_arm/refine_001.cif`  
best base of the run: cycle 2 · R-free full 0.2623782439631469 · report 0.2766648347960602 · `/home/dev/runs/8IS2/runs/8IS2.20260917T064133Z/cycles/c002/paired/candidate_arm/refine_001.cif`

