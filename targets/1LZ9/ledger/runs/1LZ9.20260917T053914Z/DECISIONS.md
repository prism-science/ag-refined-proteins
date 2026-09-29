# 1LZ9 — run `1LZ9.20260917T053914Z`

started 2026-09-17T05:39:14+00:00 on actl-ws-xraymemory-autoresearch-devspace-8597768cc8-lxfq5 pid 327360  
stages `['correction', 'solvent', 'protein_altloc']` · seed 1 · max cycles 8 · max/stage 20  
noise floor σ_select = 0.005895, k = 2.0: a cycle is credited at ≤ -0.011790, bisected above +0.011790  
published better model: none recorded in targets.yaml  
starting model: `/home/dev/runs/1LZ9/c000/baseline_rerefine/refine_001.cif`

## cycle 0 — base

cycle 0: re-refined the starting model to obtain map coefficients (/home/dev/runs/1LZ9/runs/1LZ9.20260917T053914Z/base/rerefine/refine_001.cif)  
R-work 0.22017143454064844 · R-free full 0.26823129906531984 · report 0.2571987108525899 (select 0.27892559130331473)

TLS partition pinned for the rest of the run (D415): 9 group(s) from `/home/dev/runs/1LZ9/runs/1LZ9.20260917T053914Z/base/rerefine/refine_decisions.json`

## cycle 1 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 18, "attempted": 18, "accepted": 0, "reverted": 18, "not_attempted": []}, "solvent": {"proposed": 20, "attempted": 5, "accepted": 5, "reverted": 0, "not_attempted": ["1LZ9.c001.water_remove.A361", "1LZ9.c001.water_remove.A353", "1LZ9.c001.water_remove.A369", "1LZ9.c001.water_remove.A401", "1LZ9.c001.water_remove.A399", "1LZ9.c001.water_remove.A351", "1LZ9.c001.water_remove.A397", "1LZ9.c001.water_remove.A373", "1LZ9.c001.water_remove.A356", "1LZ9.c001.water_remove.A301", "1LZ9.c001.water_remove.A323", "1LZ9.c001.water_remove.A384", "1LZ9.c001.water_remove.A359", "1LZ9.c001.water_remove.A365", "1LZ9.c001.water_remove.A345"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `1LZ9.c001.rotamer_fix.A14` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: Coot rotamer_fix moved residue(s) outside the 3-residue window [('A', 13, ''), ('A', 14, ''), ('A', 15, '')]: [('A', 304, '')]
- `1LZ9.c001.rotamer_fix.A18` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: Coot rotamer_fix moved residue(s) outside the 3-residue window [('A', 17, ''), ('A', 18, ''), ('A', 19, '')]: [('A', 245, '')]
- `1LZ9.c001.peptide_flip.A101` **reverted** — rscc 0.907275→0.81445 (Δ -0.092825, rule mean_delta, worst neighbour drop 0.0394): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.092825 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.368.. moved -0.0394 (0.7302 -> 0.6908), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.321 > rel_max 0.3 (prev 0.85011)]; c
- `1LZ9.c001.peptide_flip.A62` **reverted** — rscc 0.91645→0.7678 (Δ -0.14865, rule mean_delta, worst neighbour drop 0.0826): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.14865 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.399.. moved -0.0826 (0.4827 -> 0.4001), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.5651 > rel_max 0.3 (prev 0.88589)]; c
- `1LZ9.c001.peptide_flip.A103` **reverted** — rscc 0.942425→0.79885 (Δ -0.143575, rule mean_delta, worst neighbour drop 0.028): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.143575 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.235.. moved -0.0280 (0.8832 -> 0.8552), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.4099 > rel_max 0.3 (prev 1.10718)]; 
- `1LZ9.c001.peptide_flip.A74` **reverted** — rscc 0.930325→0.848125 (Δ -0.0822, rule mean_delta, worst neighbour drop 0.0186): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0822 < required +0.01]; clash [3 new altloc-aware clash(es)]
- `1LZ9.c001.peptide_flip.A55` **reverted** — rscc 0.963325→0.87815 (Δ -0.085175, rule mean_delta, worst neighbour drop 0.0086): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.085175 < required +0.01]; clash [3 new altloc-aware clash(es)]
- `1LZ9.c001.peptide_flip.A20` **reverted** — rscc 0.934825→0.870325 (Δ -0.0645, rule mean_delta, worst neighbour drop 0.0434): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0645 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.374.. moved -0.0434 (0.5633 -> 0.5199), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.3377 > rel_max 0.3 (prev 1.09111)]; cl
- `1LZ9.c001.peptide_flip.A37` **reverted** — rscc 0.9679→0.862325 (Δ -0.105575, rule mean_delta, worst neighbour drop 0.0906): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.105575 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.396.. moved -0.0906 (0.6132 -> 0.5226), allowed drop 0.02]; clash [3 new altloc-aware clash(es)]
- `1LZ9.c001.peptide_flip.A66` **reverted** — rscc 0.9409→0.837575 (Δ -0.103325, rule mean_delta, worst neighbour drop 0.0364): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.103325 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.343.. moved -0.0364 (0.8157 -> 0.7793), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.3114 > rel_max 0.3 (prev 1.42799)]; 
- `1LZ9.c001.peptide_flip.A115` **reverted** — rscc 0.9493→0.875475 (Δ -0.073825, rule mean_delta, worst neighbour drop 0.0246): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.073825 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.282.. moved -0.0246 (0.8803 -> 0.8557), allowed drop 0.02]; clash [2 new altloc-aware clash(es)]
- `1LZ9.c001.zone_rsr.A18-22` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: CootError: chapi.refine_zone: no result file; exit=-11
tainer_t::make_restraints_ng(int, coot::protein_geometry const&, coot::restraint_usage_Flags, bool, bool, float, bool, bool, bool, bool, coot::pseudo_restraint_bond_type, bool, bool)
#4    Object "/home/dev/envs/
- `1LZ9.c001.zone_rsr.A99-105` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: CootError: chapi.refine_zone: no result file; exit=-11
tainer_t::make_restraints_ng(int, coot::protein_geometry const&, coot::restraint_usage_Flags, bool, bool, float, bool, bool, bool, bool, coot::pseudo_restraint_bond_type, bool, bool)
#4    Object "/home/dev/envs/
- `1LZ9.c001.zone_rsr.A72-76` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: CootError: chapi.refine_zone: no result file; exit=-11
tainer_t::make_restraints_ng(int, coot::protein_geometry const&, coot::restraint_usage_Flags, bool, bool, float, bool, bool, bool, bool, coot::pseudo_restraint_bond_type, bool, bool)
#4    Object "/home/dev/envs/
- `1LZ9.c001.zone_rsr.A60-68` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: CootError: chapi.refine_zone: no result file; exit=-11
tainer_t::make_restraints_ng(int, coot::protein_geometry const&, coot::restraint_usage_Flags, bool, bool, float, bool, bool, bool, bool, coot::pseudo_restraint_bond_type, bool, bool)
#4    Object "/home/dev/envs/
- `1LZ9.c001.zone_rsr.A113-117` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: CootError: chapi.refine_zone: no result file; exit=-11
tainer_t::make_restraints_ng(int, coot::protein_geometry const&, coot::restraint_usage_Flags, bool, bool, float, bool, bool, bool, bool, coot::pseudo_restraint_bond_type, bool, bool)
#4    Object "/home/dev/envs/
- `1LZ9.c001.zone_rsr.A53-57` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: CootError: chapi.refine_zone: no result file; exit=-11
tainer_t::make_restraints_ng(int, coot::protein_geometry const&, coot::restraint_usage_Flags, bool, bool, float, bool, bool, bool, bool, coot::pseudo_restraint_bond_type, bool, bool)
#4    Object "/home/dev/envs/
- `1LZ9.c001.zone_rsr.A35-39` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: CootError: chapi.refine_zone: no result file; exit=-11
tainer_t::make_restraints_ng(int, coot::protein_geometry const&, coot::restraint_usage_Flags, bool, bool, float, bool, bool, bool, bool, coot::pseudo_restraint_bond_type, bool, bool)
#4    Object "/home/dev/envs/
- `1LZ9.c001.water_remove.A362` **accepted** — rscc 0.1535→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0027): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.125.. moved -0.0027 (0.9248 -> 0.9221), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7000371181531966; no new altloc-aware clash; site
- `1LZ9.c001.water_remove.A393` **accepted** — rscc 0.4→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0005): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.221.. moved -0.0005 (0.9663 -> 0.9658), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7000371181531966; no new altloc-aware clash; site
- `1LZ9.c001.water_remove.A387` **accepted** — rscc 0.4355→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0048): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.365.. moved -0.0048 (0.5454 -> 0.5406), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7000371181531966; no new altloc-aware clash; site
- `1LZ9.c001.water_remove.A243` **accepted** — rscc 0.4352→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.103.. moved -0.0000 (0.918 -> 0.918), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7000371181531966; no new altloc-aware clash; site-r
- `1LZ9.c001.water_remove.A376` **accepted** — rscc 0.4371→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0097): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.398.. moved -0.0097 (0.7531 -> 0.7434), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7000371181531966; no new altloc-aware clash; site

**paired cycle**: null arm R-free-select 0.27693159101184145 · treatment arm 0.2795734096766197 · attributable **+0.002642** vs credit ≤ -0.011790 / regression > +0.011790 → **no_change**  
attributable 0.002642 within (−0.011790, +0.011790]: of the raw 0.000648, -0.001994 is reproduced by re-refining the base with NO changes; the changes are not credited and are dropped: they made R-free-select worse, below the bar but worse (D411) || cross-check (phenix.model_vs_data, full set): null 0.2671 · treatment 0.269 · Δ +0.0019 — agrees in sign || Metropolis (v8, D499): attributable +0.002642 = +0.45σ_select, T = 1σ = 0.005895, p_keep = exp(−Δ/T) = 0.639, u = 0.623 → KEPT: the candidate arm carries on, un-credited (D499)

cross-check (phenix.model_vs_data, full test set): null 0.2671 · treatment 0.269 · Δ +0.0019 → **agrees in sign** with the gate

**Metropolis keep (v8, D499)**: attributable +0.002642 > 0 within noise; p_keep 0.639, u 0.623 — the candidate arm carries on un-credited

changes kept without credit; cumulative un-credited drift since the last credited base: +0.002642 (guard at > +0.011790)

⚠ whole-model geometry outside the frozen caps: rota_outliers 1.85 > 1.5 (D479, monitor)

base after cycle: `/home/dev/runs/1LZ9/runs/1LZ9.20260917T053914Z/cycles/c001/paired/candidate_arm/refine_001.cif` · R-free full 0.2688363652371388 · report 0.25775967242882775 · Δselect vs before +0.000648 · 1697.1 s

## cycle 2 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 17, "attempted": 17, "accepted": 0, "reverted": 17, "not_attempted": []}, "solvent": {"proposed": 20, "attempted": 6, "accepted": 5, "reverted": 1, "not_attempted": ["1LZ9.c002.water_remove.A401", "1LZ9.c002.water_remove.A397", "1LZ9.c002.water_remove.A373", "1LZ9.c002.water_remove.A359", "1LZ9.c002.water_remove.A384", "1LZ9.c002.water_remove.A323", "1LZ9.c002.water_remove.A356", "1LZ9.c002.water_remove.A385", "1LZ9.c002.water_remove.A365", "1LZ9.c002.water_remove.A403", "1LZ9.c002.water_remove.A394", "1LZ9.c002.water_remove.A345", "1LZ9.c002.water_remove.A374", "1LZ9.c002.water_remove.A382"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `1LZ9.c002.rotamer_fix.A14` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: Coot rotamer_fix moved residue(s) outside the 3-residue window [('A', 13, ''), ('A', 14, ''), ('A', 15, '')]: [('A', 304, '')]
- `1LZ9.c002.rotamer_fix.A18` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: Coot rotamer_fix moved residue(s) outside the 3-residue window [('A', 17, ''), ('A', 18, ''), ('A', 19, '')]: [('A', 245, '')]
- `1LZ9.c002.peptide_flip.A101` **reverted** — rscc 0.90635→0.813525 (Δ -0.092825, rule mean_delta, worst neighbour drop 0.0446): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.092825 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.368.. moved -0.0446 (0.7194 -> 0.6748), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.3185 > rel_max 0.3 (prev 0.83706)]; 
- `1LZ9.c002.peptide_flip.A103` **reverted** — rscc 0.94165→0.799525 (Δ -0.142125, rule mean_delta, worst neighbour drop 0.0268): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.142125 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.235.. moved -0.0268 (0.88 -> 0.8532), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.4018 > rel_max 0.3 (prev 1.09851)]; cl
- `1LZ9.c002.peptide_flip.A74` **reverted** — rscc 0.928625→0.8459 (Δ -0.082725, rule mean_delta, worst neighbour drop 0.018): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.082725 < required +0.01]; clash [3 new altloc-aware clash(es)]
- `1LZ9.c002.peptide_flip.A55` **reverted** — rscc 0.96295→0.878125 (Δ -0.084825, rule mean_delta, worst neighbour drop 0.0109): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.084825 < required +0.01]; clash [3 new altloc-aware clash(es)]
- `1LZ9.c002.peptide_flip.A20` **reverted** — rscc 0.934→0.869025 (Δ -0.064975, rule mean_delta, worst neighbour drop 0.051): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.064975 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.349.. moved -0.0510 (0.6414 -> 0.5904), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.3115 > rel_max 0.3 (prev 1.09511)]; 
- `1LZ9.c002.peptide_flip.A37` **reverted** — rscc 0.9665→0.8634 (Δ -0.1031, rule mean_delta, worst neighbour drop 0.0848): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.1031 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.396.. moved -0.0848 (0.5823 -> 0.4975), allowed drop 0.02]; clash [3 new altloc-aware clash(es)]
- `1LZ9.c002.peptide_flip.A66` **reverted** — rscc 0.938525→0.8373 (Δ -0.101225, rule mean_delta, worst neighbour drop 0.0358): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.101225 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.343.. moved -0.0358 (0.8018 -> 0.766), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.3379 > rel_max 0.3 (prev 1.40614)]
- `1LZ9.c002.peptide_flip.A115` **reverted** — rscc 0.949275→0.874725 (Δ -0.07455, rule mean_delta, worst neighbour drop 0.0288): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.07455 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.282.. moved -0.0288 (0.8736 -> 0.8448), allowed drop 0.02]; clash [5 new altloc-aware clash(es)]
- `1LZ9.c002.zone_rsr.A18-22` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: CootError: chapi.refine_zone: no result file; exit=-11
tainer_t::make_restraints_ng(int, coot::protein_geometry const&, coot::restraint_usage_Flags, bool, bool, float, bool, bool, bool, bool, coot::pseudo_restraint_bond_type, bool, bool)
#4    Object "/home/dev/envs/
- `1LZ9.c002.zone_rsr.A72-76` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: CootError: chapi.refine_zone: no result file; exit=-11
tainer_t::make_restraints_ng(int, coot::protein_geometry const&, coot::restraint_usage_Flags, bool, bool, float, bool, bool, bool, bool, coot::pseudo_restraint_bond_type, bool, bool)
#4    Object "/home/dev/envs/
- `1LZ9.c002.zone_rsr.A99-105` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: CootError: chapi.refine_zone: no result file; exit=-11
tainer_t::make_restraints_ng(int, coot::protein_geometry const&, coot::restraint_usage_Flags, bool, bool, float, bool, bool, bool, bool, coot::pseudo_restraint_bond_type, bool, bool)
#4    Object "/home/dev/envs/
- `1LZ9.c002.zone_rsr.A64-68` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: CootError: chapi.refine_zone: no result file; exit=-11
tainer_t::make_restraints_ng(int, coot::protein_geometry const&, coot::restraint_usage_Flags, bool, bool, float, bool, bool, bool, bool, coot::pseudo_restraint_bond_type, bool, bool)
#4    Object "/home/dev/envs/
- `1LZ9.c002.zone_rsr.A113-117` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: CootError: chapi.refine_zone: no result file; exit=-11
tainer_t::make_restraints_ng(int, coot::protein_geometry const&, coot::restraint_usage_Flags, bool, bool, float, bool, bool, bool, bool, coot::pseudo_restraint_bond_type, bool, bool)
#4    Object "/home/dev/envs/
- `1LZ9.c002.zone_rsr.A53-57` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: CootError: chapi.refine_zone: no result file; exit=-11
tainer_t::make_restraints_ng(int, coot::protein_geometry const&, coot::restraint_usage_Flags, bool, bool, float, bool, bool, bool, bool, coot::pseudo_restraint_bond_type, bool, bool)
#4    Object "/home/dev/envs/
- `1LZ9.c002.zone_rsr.A35-39` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: CootError: chapi.refine_zone: no result file; exit=-11
tainer_t::make_restraints_ng(int, coot::protein_geometry const&, coot::restraint_usage_Flags, bool, bool, float, bool, bool, bool, bool, coot::pseudo_restraint_bond_type, bool, bool)
#4    Object "/home/dev/envs/
- `1LZ9.c002.water_remove.A369` **accepted** — rscc 0.4094→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0031): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.293.. moved -0.0031 (0.7951 -> 0.792), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7000371181531966; no new altloc-aware clash; site-
- `1LZ9.c002.water_remove.A361` **accepted** — rscc 0.4108→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0069): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.406.. moved -0.0069 (0.7333 -> 0.7264), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7000371181531966; no new altloc-aware clash; site
- `1LZ9.c002.water_remove.A353` **accepted** — rscc 0.4515→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0131): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.313.. moved -0.0131 (0.6759 -> 0.6628), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7000371181531966; no new altloc-aware clash; site
- `1LZ9.c002.water_remove.A351` **accepted** — rscc 0.4648→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0037): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.384.. moved -0.0037 (0.5157 -> 0.512), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7000371181531966; no new altloc-aware clash; site-
- `1LZ9.c002.water_remove.A301` **reverted** — rscc 0.4642→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0273): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.379.. moved -0.0273 (0.6251 -> 0.5978), allowed drop 0.02]
- `1LZ9.c002.water_remove.A399` **accepted** — rscc 0.4801→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0046): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.62.. moved -0.0046 (0.8762 -> 0.8716), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7000371181531966; no new altloc-aware clash; site-

**paired cycle**: null arm R-free-select 0.2758200413505892 · treatment arm 0.2737351236018988 · attributable **-0.002085** vs credit ≤ -0.011790 / regression > +0.011790 → **no_change**  
attributable -0.002085 within (−0.011790, +0.011790]: of the raw -0.005838, -0.003753 is reproduced by re-refining the base with NO changes; the changes are not credited but stay (locally better, and not worse globally) || cross-check (phenix.model_vs_data, full set): null 0.2653 · treatment 0.2629 · Δ -0.0024 — agrees in sign

cross-check (phenix.model_vs_data, full test set): null 0.2653 · treatment 0.2629 · Δ -0.0024 → **agrees in sign** with the gate

changes kept without credit; cumulative un-credited drift since the last credited base: +0.000557 (guard at > +0.011790)

⚠ whole-model geometry outside the frozen caps: rota_outliers 2.78 > 1.5 (D479, monitor)

base after cycle: `/home/dev/runs/1LZ9/runs/1LZ9.20260917T053914Z/cycles/c002/paired/candidate_arm/refine_001.cif` · R-free full 0.2628606655261614 · report 0.2516422122319867 · Δselect vs before -0.005838 · 1577.4 s

**stall detected** after cycle 2: 2 consecutive cycle(s) accepted changes locally but each moved R-free-select by < σ=0.005895: a minimum small edits cannot leave → next cycle takes an escape rung

## cycle 3 — stall escape rung `reweight_reseed`

different random seed, fresh xyz/adp weight optimisation, +3 macro-cycles: override `{'seed': 1001, 'optimize_xyz_weight': True, 'optimize_adp_weight': True, 'wxc_scale': None, 'wxu_scale': None, 'macro_cycles': 8}`  
null arm R-free-select 0.28920394494821156 · escape arm 0.2869557176831563 · attributable **-0.002248** → did not clear  
attributable -0.002248 within (−0.011790, +0.011790]: of the raw 0.013221, 0.015469 is reproduced by re-refining the base with NO changes; the changes are not credited and are not adopted (no local evidence of their own) || cross-check (phenix.model_vs_data, full set): null 0.2782 · treatment 0.2751 · Δ -0.0031 — agrees in sign  
ladder so far `{'reweight_reseed': 'failed'}`

## cycle 4 — stall escape rung `rescale_bulk_solvent`

bulk_solvent_and_scale.mode=slow — solvent and anisotropic scale re-fit from scratch: override `{'bulk_solvent_mode': 'slow'}`  
null arm R-free-select 0.2738860270548344 · escape arm 0.30121311938670764 · attributable **+0.027327** → did not clear  
attributable 0.027327 > +0.011790: the changes made R-free-select WORSE than the identically refined base — regression, bisect (SPEC_LOOP_V2 §1.3) || cross-check (phenix.model_vs_data, full set): null 0.264 · treatment 0.2949 · Δ +0.0309 — agrees in sign  
ladder so far `{'reweight_reseed': 'failed', 'rescale_bulk_solvent': 'failed'}`

## cycle 5 — escape

escape ladder exhausted (reweight_reseed=failed, rescale_bulk_solvent=failed, simulated_annealing=refused): the model is converged at this minimum. **Converged at this minimum.**

## finished 2026-09-17T07:04:56+00:00

escape ladder exhausted (reweight_reseed=failed, rescale_bulk_solvent=failed, simulated_annealing=refused): the model is converged at this minimum  
R-free full 0.26823129906531984 → 0.26365443021353363 (Δ -0.004577) · report 0.2571987108525899 → 0.2530991739893119  
published better model: None · gap closed: None · reached: None  
credited changes (0): `[]`  
kept without credit: 10 · final model `/home/dev/runs/1LZ9/runs/1LZ9.20260917T053914Z/cycles/c004/escape/null_arm/refine_001.cif`  
best base of the run: cycle 2 · R-free full 0.2628606655261614 · report 0.2516422122319867 · `/home/dev/runs/1LZ9/runs/1LZ9.20260917T053914Z/cycles/c002/paired/candidate_arm/refine_001.cif`

