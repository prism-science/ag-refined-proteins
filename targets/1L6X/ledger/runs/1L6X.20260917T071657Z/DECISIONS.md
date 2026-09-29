# 1L6X — run `1L6X.20260917T071657Z`

started 2026-09-17T07:16:57+00:00 on actl-ws-xraymemory-autoresearch-devspace-8597768cc8-lxfq5 pid 898496  
stages `['correction', 'solvent', 'protein_altloc']` · seed 1 · max cycles 8 · max/stage 20  
noise floor σ_select = 0.005481, k = 2.0: a cycle is credited at ≤ -0.010962, bisected above +0.010962  
published better model: none recorded in targets.yaml  
starting model: `/home/dev/runs/1L6X/c000/baseline_rerefine/refine_001.cif`

## cycle 0 — base

cycle 0: re-refined the starting model to obtain map coefficients (/home/dev/runs/1L6X/runs/1L6X.20260917T071657Z/base/rerefine/refine_001.cif)  
R-work 0.18973408173554593 · R-free full 0.23829283788476283 · report 0.23959164132761848 (select 0.2369934804136937)

TLS partition pinned for the rest of the run (D415): 6 group(s) from `/home/dev/runs/1L6X/runs/1L6X.20260917T071657Z/base/rerefine/refine_decisions.json`

## cycle 1 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 20, "attempted": 20, "accepted": 2, "reverted": 18, "not_attempted": []}, "solvent": {"proposed": 20, "attempted": 3, "accepted": 3, "reverted": 0, "not_attempted": ["1L6X.c001.water_remove.A667", "1L6X.c001.water_remove.A666", "1L6X.c001.water_remove.A603", "1L6X.c001.water_remove.A640", "1L6X.c001.water_remove.B95", "1L6X.c001.water_remove.B67", "1L6X.c001.water_remove.A555", "1L6X.c001.water_remove.B82", "1L6X.c001.water_remove.A641", "1L6X.c001.water_remove.A726", "1L6X.c001.water_remove.A670", "1L6X.c001.water_remove.A616", "1L6X.c001.water_remove.A716", "1L6X.c001.water_remove.A623", "1L6X.c001.water_remove.A665", "1L6X.c001.water_remove.B104", "1L6X.c001.water_remove.B100"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `1L6X.c001.rotamer_fix.A361` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: Coot rotamer_fix moved residue(s) outside the 3-residue window [('A', 360, ''), ('A', 361, ''), ('A', 362, '')]: [('A', 580, '')]
- `1L6X.c001.rotamer_fix.A326` **reverted** — rscc 0.844633→0.8064 (Δ -0.038233, rule mean_delta, worst neighbour drop 0.0391): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.038233 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.709.. moved -0.0391 (0.6744 -> 0.6353), allowed drop 0.02]; clash [1 new altloc-aware clash(es)]
- `1L6X.c001.rotamer_fix.A342` **accepted** — rscc 0.8694→0.880467 (Δ 0.011067, rule mean_delta, worst neighbour drop 0.0168): RSCC gate passed: RSCC gate passed under mean_delta (delta +0.0111 >= +0.01); worst untouched neighbour A.552.. moved -0.0168 (0.8982 -> 0.8814), allowed drop 0.02; local geometry bond_rmsd=0.00638 angle_rmsd=0.75781 over 22 bond(s)/32 angle(s) within the band for d_min=1.6471428767697989; no new al
- `1L6X.c001.rotamer_fix.A246` **reverted** — rscc 0.9145→0.9189 (Δ 0.0044, rule mean_delta, worst neighbour drop 0.0251): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.0044 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.676.. moved -0.0251 (0.6817 -> 0.6566), allowed drop 0.02]
- `1L6X.c001.rotamer_fix.A274` **reverted** — rscc 0.891567→0.8463 (Δ -0.045267, rule mean_delta, worst neighbour drop 0.0164): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.045267 < required +0.01]
- `1L6X.c001.rotamer_fix.A355` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: Coot rotamer_fix moved residue(s) outside the 3-residue window [('A', 354, ''), ('A', 355, ''), ('A', 356, '')]: [('A', 644, '')]
- `1L6X.c001.rotamer_fix.A311` **reverted** — rscc 0.922967→0.925633 (Δ 0.002666, rule mean_delta, worst neighbour drop 0.0035): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.002666 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `1L6X.c001.rotamer_fix.B38` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: Coot rotamer_fix moved residue(s) outside the 3-residue window [('B', 37, ''), ('B', 38, ''), ('B', 39, '')]: [('B', 84, ''), ('B', 111, '')]
- `1L6X.c001.rotamer_fix.A386` **accepted** — rscc 0.692467→0.708967 (Δ 0.0165, rule mean_delta, worst neighbour drop 0.02): RSCC gate passed: RSCC gate passed under mean_delta (delta +0.0165 >= +0.01); worst untouched neighbour A.690.. moved -0.0200 (0.7253 -> 0.7053), allowed drop 0.02; local geometry bond_rmsd=0.00498 angle_rmsd=0.83824 over 22 bond(s)/32 angle(s) within the band for d_min=1.6471428767697989; no new al
- `1L6X.c001.rotamer_fix.A296` **reverted** — rscc 0.759533→0.7546 (Δ -0.004933, rule mean_delta, worst neighbour drop 0.0133): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.004933 < required +0.01]
- `1L6X.c001.rotamer_fix.B39` **reverted** — rscc 0.52435→0.5668 (Δ 0.04245, rule mean_delta, worst neighbour drop 0.016): failed: geometry [angle_rmsd worsened by 0.3242 > rel_max 0.3 (prev 1.47696)]
- `1L6X.c001.rotamer_fix.A415` **reverted** — rscc 0.825933→0.854533 (Δ 0.0286, rule mean_delta, worst neighbour drop 0.0311): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.662.. moved -0.0311 (0.6525 -> 0.6214), allowed drop 0.02]; clash [1 new altloc-aware clash(es)]
- `1L6X.c001.peptide_flip.A384` **reverted** — rscc 0.776425→0.6563 (Δ -0.120125, rule mean_delta, worst neighbour drop 0.0125): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.120125 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `1L6X.c001.peptide_flip.A340` **reverted** — rscc 0.88995→0.751125 (Δ -0.138825, rule mean_delta, worst neighbour drop 0.0326): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.138825 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.680.. moved -0.0326 (0.7972 -> 0.7646), allowed drop 0.02]; clash [1 new altloc-aware clash(es)]
- `1L6X.c001.peptide_flip.A271` **reverted** — rscc 0.8628→0.810275 (Δ -0.052525, rule mean_delta, worst neighbour drop 0.0353): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.052525 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.614.. moved -0.0353 (0.8255 -> 0.7902), allowed drop 0.02]; clash [1 new altloc-aware clash(es)]
- `1L6X.c001.peptide_flip.A329` **reverted** — rscc 0.8464→0.72995 (Δ -0.11645, rule mean_delta, worst neighbour drop 0.066): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.11645 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.685.. moved -0.0660 (0.6894 -> 0.6234), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.3488 > rel_max 0.3 (prev 0.9156)]; cl
- `1L6X.c001.peptide_flip.A390` **reverted** — rscc 0.886975→0.64235 (Δ -0.244625, rule mean_delta, worst neighbour drop 0.1012): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.244625 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.700.. moved -0.1012 (0.7767 -> 0.6755), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.3639 > rel_max 0.3 (prev 0.96264)]; 
- `1L6X.c001.peptide_flip.A435` **reverted** — rscc 0.923375→0.732125 (Δ -0.19125, rule mean_delta, worst neighbour drop 0.0467): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.19125 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.514.. moved -0.0467 (0.701 -> 0.6543), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.3805 > rel_max 0.3 (prev 0.87253)]; cl
- `1L6X.c001.peptide_flip.A376` **reverted** — rscc 0.931975→0.527125 (Δ -0.40485, rule mean_delta, worst neighbour drop 0.0972): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.40485 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.719.. moved -0.0972 (0.8015 -> 0.7043), allowed drop 0.02]; geometry [bond_rmsd worsened by 0.00784 > rel_max 0.003 (prev 0.01074); 
- `1L6X.c001.peptide_flip.A434` **reverted** — rscc 0.931575→0.72745 (Δ -0.204125, rule mean_delta, worst neighbour drop 0.0365): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.204125 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.251.. moved -0.0365 (0.9354 -> 0.8989), allowed drop 0.02]; clash [4 new altloc-aware clash(es)]
- `1L6X.c001.water_remove.A669` **accepted** — rscc -0.0068→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0018): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.585.. moved -0.0018 (0.7454 -> 0.7436), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.6471428767697989; no new altloc-aware clash; site
- `1L6X.c001.water_remove.B71` **accepted** — rscc 0.1012→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0165): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour B.116.. moved -0.0165 (0.6592 -> 0.6427), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.6471428767697989; no new altloc-aware clash; site
- `1L6X.c001.water_remove.B89` **accepted** — rscc 0.2065→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0039): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour B.26.. moved -0.0039 (0.8774 -> 0.8735), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.6471428767697989; no new altloc-aware clash; site-

**paired cycle**: null arm R-free-select 0.23229985975391407 · treatment arm 0.23448899753039948 · attributable **+0.002189** vs credit ≤ -0.010962 / regression > +0.010962 → **no_change**  
attributable 0.002189 within (−0.010962, +0.010962]: of the raw -0.002504, -0.004694 is reproduced by re-refining the base with NO changes; the changes are not credited and are dropped: they made R-free-select worse, below the bar but worse (D411) || cross-check (phenix.model_vs_data, full set): null 0.2347 · treatment 0.2389 · Δ +0.0042 — agrees in sign || Metropolis (v8, D499): attributable +0.002189 = +0.40σ_select, T = 1σ = 0.005481, p_keep = exp(−Δ/T) = 0.671, u = 0.935 → dropped: base ← null arm

cross-check (phenix.model_vs_data, full test set): null 0.2347 · treatment 0.2389 · Δ +0.0042 → **agrees in sign** with the gate

5 change(s) dropped: within noise but attributable +0.002189 > 0 — base ← null arm (D411)

⚠ whole-model geometry outside the frozen caps: rota_outliers 3.11 > 1.5 (D479, monitor)

base after cycle: `/home/dev/runs/1L6X/runs/1L6X.20260917T071657Z/cycles/c001/paired/null_arm/refine_001.cif` · R-free full 0.23475540621352567 · report 0.2372099056617919 · Δselect vs before -0.004694 · 3440.4 s

## cycle 2 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 20, "attempted": 20, "accepted": 0, "reverted": 20, "not_attempted": []}, "solvent": {"proposed": 20, "attempted": 5, "accepted": 5, "reverted": 0, "not_attempted": ["1L6X.c002.water_remove.A666", "1L6X.c002.water_remove.A603", "1L6X.c002.water_remove.A667", "1L6X.c002.water_remove.A716", "1L6X.c002.water_remove.A555", "1L6X.c002.water_remove.B67", "1L6X.c002.water_remove.B82", "1L6X.c002.water_remove.A726", "1L6X.c002.water_remove.A559", "1L6X.c002.water_remove.A626", "1L6X.c002.water_remove.B95", "1L6X.c002.water_remove.A631", "1L6X.c002.water_remove.A640", "1L6X.c002.water_remove.A677", "1L6X.c002.water_remove.A670"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `1L6X.c002.rotamer_fix.A326` **reverted** — rscc 0.8427→0.8167 (Δ -0.026, rule mean_delta, worst neighbour drop 0.0249): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.026 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.709.. moved -0.0249 (0.7491 -> 0.7242), allowed drop 0.02]; clash [1 new altloc-aware clash(es)]
- `1L6X.c002.rotamer_fix.A361` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: Coot rotamer_fix moved residue(s) outside the 3-residue window [('A', 360, ''), ('A', 361, ''), ('A', 362, '')]: [('A', 580, '')]
- `1L6X.c002.rotamer_fix.A342` **reverted** — rscc 0.873767→0.88 (Δ 0.006233, rule mean_delta, worst neighbour drop 0.014): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.006233 < required +0.01]
- `1L6X.c002.rotamer_fix.A274` **reverted** — rscc 0.896533→0.864367 (Δ -0.032166, rule mean_delta, worst neighbour drop 0.0157): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.032166 < required +0.01]
- `1L6X.c002.rotamer_fix.A355` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: Coot rotamer_fix moved residue(s) outside the 3-residue window [('A', 354, ''), ('A', 355, ''), ('A', 356, '')]: [('A', 644, '')]
- `1L6X.c002.rotamer_fix.A320` **reverted** — rscc 0.930733→0.927567 (Δ -0.003166, rule mean_delta, worst neighbour drop 0.0098): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.003166 < required +0.01]
- `1L6X.c002.rotamer_fix.A311` **reverted** — rscc 0.9302→0.9337 (Δ 0.0035, rule mean_delta, worst neighbour drop 0.0153): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.0035 < required +0.01]
- `1L6X.c002.rotamer_fix.B38` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: Coot rotamer_fix moved residue(s) outside the 3-residue window [('B', 37, ''), ('B', 38, ''), ('B', 39, '')]: [('B', 84, ''), ('B', 111, '')]
- `1L6X.c002.rotamer_fix.A386` **reverted** — rscc 0.7132→0.721233 (Δ 0.008033, rule mean_delta, worst neighbour drop 0.0196): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.008033 < required +0.01]
- `1L6X.c002.rotamer_fix.A296` **reverted** — rscc 0.777933→0.7839 (Δ 0.005967, rule mean_delta, worst neighbour drop 0.0111): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.005967 < required +0.01]
- `1L6X.c002.rotamer_fix.B39` **reverted** — rscc 0.5908→0.6037 (Δ 0.0129, rule mean_delta, worst neighbour drop 0.0237): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour B.111.. moved -0.0237 (0.6028 -> 0.5791), allowed drop 0.02]
- `1L6X.c002.peptide_flip.A340` **reverted** — rscc 0.884675→0.756275 (Δ -0.1284, rule mean_delta, worst neighbour drop 0.0425): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.1284 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.680.. moved -0.0425 (0.7814 -> 0.7389), allowed drop 0.02]; clash [2 new altloc-aware clash(es)]
- `1L6X.c002.peptide_flip.A271` **reverted** — rscc 0.864025→0.8162 (Δ -0.047825, rule mean_delta, worst neighbour drop 0.0376): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.047825 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.614.. moved -0.0376 (0.842 -> 0.8044), allowed drop 0.02]; clash [1 new altloc-aware clash(es)]
- `1L6X.c002.peptide_flip.A390` **reverted** — rscc 0.8887→0.7396 (Δ -0.1491, rule mean_delta, worst neighbour drop 0.1717): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.1491 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.698.. moved -0.1717 (0.897 -> 0.7253), allowed drop 0.02]; clash [2 new altloc-aware clash(es)]
- `1L6X.c002.peptide_flip.A329` **reverted** — rscc 0.851525→0.74095 (Δ -0.110575, rule mean_delta, worst neighbour drop 0.0348): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.110575 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.709.. moved -0.0348 (0.7491 -> 0.7143), allowed drop 0.02]; clash [1 new altloc-aware clash(es)]
- `1L6X.c002.peptide_flip.A435` **reverted** — rscc 0.9231→0.7179 (Δ -0.2052, rule mean_delta, worst neighbour drop 0.0523): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.2052 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.528.. moved -0.0523 (0.8141 -> 0.7618), allowed drop 0.02]; clash [5 new altloc-aware clash(es)]
- `1L6X.c002.peptide_flip.A434` **reverted** — rscc 0.934225→0.7759 (Δ -0.158325, rule mean_delta, worst neighbour drop 0.0429): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.158325 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.460.. moved -0.0429 (0.8703 -> 0.8274), allowed drop 0.02]; clash [4 new altloc-aware clash(es)]
- `1L6X.c002.peptide_flip.A376` **reverted** — rscc 0.93655→0.52335 (Δ -0.4132, rule mean_delta, worst neighbour drop 0.0838): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.4132 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.524.. moved -0.0838 (0.8576 -> 0.7738), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.5978 > rel_max 0.3 (prev 1.16703)]; cl
- `1L6X.c002.zone_rsr.B36-39` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: CootError: chapi.refine_zone: no result file; exit=-11
tainer_t::make_restraints_ng(int, coot::protein_geometry const&, coot::restraint_usage_Flags, bool, bool, float, bool, bool, bool, bool, coot::pseudo_restraint_bond_type, bool, bool)
#4    Object "/home/dev/envs/
- `1L6X.c002.zone_rsr.A294-298` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: CootError: chapi.refine_zone: no result file; exit=-11
tainer_t::make_restraints_ng(int, coot::protein_geometry const&, coot::restraint_usage_Flags, bool, bool, float, bool, bool, bool, bool, coot::pseudo_restraint_bond_type, bool, bool)
#4    Object "/home/dev/envs/
- `1L6X.c002.water_remove.A669` **accepted** — rscc -0.0874→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.001): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.336.. moved -0.0010 (0.8039 -> 0.8029), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.6471428767697989; no new altloc-aware clash; site
- `1L6X.c002.water_remove.B89` **accepted** — rscc 0.1249→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0053): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour B.85.. moved -0.0053 (0.8255 -> 0.8202), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.6471428767697989; no new altloc-aware clash; site-
- `1L6X.c002.water_remove.B71` **accepted** — rscc 0.2301→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0125): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour B.116.. moved -0.0125 (0.6762 -> 0.6637), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.6471428767697989; no new altloc-aware clash; site
- `1L6X.c002.water_remove.A618` **accepted** — rscc 0.3695→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0048): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour C.6.. moved -0.0048 (0.5816 -> 0.5768), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.6471428767697989; no new altloc-aware clash; site-r
- `1L6X.c002.water_remove.A623` **accepted** — rscc 0.3816→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0069): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.480.. moved -0.0069 (0.6455 -> 0.6386), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.6471428767697989; no new altloc-aware clash; site

**paired cycle**: null arm R-free-select 0.22923797607308974 · treatment arm 0.22936698072758616 · attributable **+0.000129** vs credit ≤ -0.010962 / regression > +0.010962 → **no_change**  
attributable 0.000129 within (−0.010962, +0.010962]: of the raw -0.002933, -0.003062 is reproduced by re-refining the base with NO changes; the changes are not credited and are dropped: they made R-free-select worse, below the bar but worse (D411) || cross-check (phenix.model_vs_data, full set): null 0.231 · treatment 0.2313 · Δ +0.0003 — agrees in sign || Metropolis (v8, D499): attributable +0.000129 = +0.02σ_select, T = 1σ = 0.005481, p_keep = exp(−Δ/T) = 0.977, u = 0.674 → KEPT: the candidate arm carries on, un-credited (D499)

cross-check (phenix.model_vs_data, full test set): null 0.231 · treatment 0.2313 · Δ +0.0003 → **agrees in sign** with the gate

**Metropolis keep (v8, D499)**: attributable +0.000129 > 0 within noise; p_keep 0.977, u 0.674 — the candidate arm carries on un-credited

changes kept without credit; cumulative un-credited drift since the last credited base: +0.000129 (guard at > +0.010962)

⚠ whole-model geometry outside the frozen caps: rota_outliers 2.22 > 1.5 (D479, monitor)

base after cycle: `/home/dev/runs/1L6X/runs/1L6X.20260917T071657Z/cycles/c002/paired/candidate_arm/refine_001.cif` · R-free full 0.23128772640914497 · report 0.2332076531110782 · Δselect vs before -0.002933 · 3424.3 s

**stall detected** after cycle 2: 2 consecutive cycle(s) accepted changes locally but each moved R-free-select by < σ=0.005481: a minimum small edits cannot leave → next cycle takes an escape rung

## cycle 3 — stall escape rung `reweight_reseed`

different random seed, fresh xyz/adp weight optimisation, +3 macro-cycles: override `{'seed': 1001, 'optimize_xyz_weight': True, 'optimize_adp_weight': True, 'wxc_scale': None, 'wxu_scale': None, 'macro_cycles': 8}`  
null arm R-free-select 0.22807671384335249 · escape arm 0.2268897316656063 · attributable **-0.001187** → did not clear  
attributable -0.001187 within (−0.010962, +0.010962]: of the raw -0.002477, -0.001290 is reproduced by re-refining the base with NO changes; the changes are not credited and are not adopted (no local evidence of their own) || cross-check (phenix.model_vs_data, full set): null 0.2311 · treatment 0.2294 · Δ -0.0017 — agrees in sign  
ladder so far `{'reweight_reseed': 'failed'}`

## cycle 4 — stall escape rung `rescale_bulk_solvent`

bulk_solvent_and_scale.mode=slow — solvent and anisotropic scale re-fit from scratch: override `{'bulk_solvent_mode': 'slow'}`  
null arm R-free-select 0.22931309209314096 · escape arm 0.23179981314145853 · attributable **+0.002487** → did not clear  
attributable 0.002487 within (−0.010962, +0.010962]: of the raw 0.003723, 0.001236 is reproduced by re-refining the base with NO changes; the changes are not credited and are not adopted (no local evidence of their own) || cross-check (phenix.model_vs_data, full set): null 0.2316 · treatment 0.2337 · Δ +0.0021 — agrees in sign  
ladder so far `{'reweight_reseed': 'failed', 'rescale_bulk_solvent': 'failed'}`

## cycle 5 — stall escape rung `simulated_annealing`

simulated annealing (no altlocs present): override `{'simulated_annealing': True}`  
null arm R-free-select 0.22774229421606157 · escape arm 0.23188574423387326 · attributable **+0.004143** → did not clear  
attributable 0.004143 within (−0.010962, +0.010962]: of the raw 0.002573, -0.001571 is reproduced by re-refining the base with NO changes; the changes are not credited and are not adopted (no local evidence of their own) || cross-check (phenix.model_vs_data, full set): null 0.2303 · treatment 0.2344 · Δ +0.0041 — agrees in sign  
ladder so far `{'reweight_reseed': 'failed', 'rescale_bulk_solvent': 'failed', 'simulated_annealing': 'failed'}`

## cycle 6 — escape

escape ladder exhausted (reweight_reseed=failed, rescale_bulk_solvent=failed, simulated_annealing=failed): the model is converged at this minimum. **Converged at this minimum.**

## finished 2026-09-17T11:01:52+00:00

escape ladder exhausted (reweight_reseed=failed, rescale_bulk_solvent=failed, simulated_annealing=failed): the model is converged at this minimum  
R-free full 0.23829283788476283 → 0.23047879993542744 (Δ -0.007814) · report 0.23959164132761848 → 0.23321413884627148  
published better model: None · gap closed: None · reached: None  
credited changes (0): `[]`  
kept without credit: 5 · final model `/home/dev/runs/1L6X/runs/1L6X.20260917T071657Z/cycles/c005/escape/null_arm/refine_001.cif`  
best base of the run: cycle 5 · R-free full 0.23047879993542744 · report 0.23321413884627148 · `/home/dev/runs/1L6X/runs/1L6X.20260917T071657Z/cycles/c005/escape/null_arm/refine_001.cif`

