# 7KR0 — run `7KR0.20260910v7`

started 2026-09-10T03:50:56+00:00 on actl-ws-xraymemory-autoresearch-devspace-54d7d7d896-4cxg2 pid 836490  
stages `['correction', 'solvent']` · seed 1 · max cycles 2 · max/stage 20  
noise floor σ_select = 0.000405, k = 2.0: a cycle is credited at ≤ -0.000810, bisected above +0.000810  
published better model: none recorded in targets.yaml  
starting model: `/home/dev/runs/7KR0/experiments/e030c_macro_cycles15/paired/candidate_arm/refine_001.cif`

## cycle 0 — base

current model already carries map coefficients; no cycle-0 refinement  
R-work 0.10360832962303718 · R-free full 0.1125685619303301 · report 0.11482593627366146 (select 0.11033595761519327)

## cycle 45 — real space (correction, solvent)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 5, "attempted": 5, "accepted": 0, "reverted": 5, "not_attempted": []}, "solvent": {"proposed": 20, "attempted": 5, "accepted": 5, "reverted": 0, "not_attempted": ["7KR0.c045.water_remove.A376", "7KR0.c045.water_remove.A371", "7KR0.c045.water_remove.A269", "7KR0.c045.water_remove.A403", "7KR0.c045.water_remove.A505", "7KR0.c045.water_remove.A475", "7KR0.c045.water_remove.A208", "7KR0.c045.water_remove.A219", "7KR0.c045.water_remove.A206", "7KR0.c045.water_remove.A404", "7KR0.c045.water_remove.A430", "7KR0.c045.water_remove.A290", "7KR0.c045.water_remove.A411", "7KR0.c045.water_remove.A222", "7KR0.c045.water_remove.A487"]}}`
- `7KR0.c045.peptide_flip.A90` **reverted** — rscc 0.9913→0.866975 (Δ -0.124325, rule mean_delta, worst neighbour drop 0.0162): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.124325 < required +0.01]; geometry [angle_rmsd worsened by 0.3656 > rel_max 0.3 (prev 1.10923)]; clash [8 new altloc-aware clash(es)]
- `7KR0.c045.peptide_flip.A47` **reverted** — rscc 0.99225→0.819525 (Δ -0.172725, rule mean_delta, worst neighbour drop 0.0208): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.172725 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.269.. moved -0.0208 (0.6626 -> 0.6418), allowed drop 0.02]
- `7KR0.c045.peptide_flip.A89` **reverted** — rscc 0.9887→0.80502 (Δ -0.18368, rule mean_delta, worst neighbour drop 0.0339): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.18368 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.464.. moved -0.0339 (0.8217 -> 0.7878), allowed drop 0.02]; clash [5 new altloc-aware clash(es)]
- `7KR0.c045.peptide_flip.A45` **reverted** — rscc 0.99214→0.8543 (Δ -0.13784, rule mean_delta, worst neighbour drop 0.0194): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.13784 < required +0.01]; clash [3 new altloc-aware clash(es)]
- `7KR0.c045.zone_rsr.A90-92` **reverted** — rscc 0.990433→0.989667 (Δ -0.000766, rule mean_delta, worst neighbour drop 0.0037): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.000766 < required +0.01]
- `7KR0.c045.water_remove.A509` **accepted** — rscc 0.1915→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0073): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.506.. moved -0.0073 (0.8839 -> 0.8766), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site
- `7KR0.c045.water_remove.A214` **accepted** — rscc 0.3808→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0042): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.469.. moved -0.0042 (0.7176 -> 0.7134), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site
- `7KR0.c045.water_remove.A209` **accepted** — rscc 0.5249→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0068): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.500.. moved -0.0068 (0.943 -> 0.9362), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site-
- `7KR0.c045.water_remove.A374` **accepted** — rscc 0.5371→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.005): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.269.. moved -0.0050 (0.6626 -> 0.6576), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site
- `7KR0.c045.water_remove.A493` **accepted** — rscc 0.5253→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0008): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.242.. moved -0.0008 (0.8653 -> 0.8645), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site

**paired cycle**: null arm R-free-select 0.11079524991044302 · treatment arm 0.11035539186775042 · attributable **-0.000440** vs credit ≤ -0.000810 / regression > +0.000810 → **no_change**  
attributable -0.000440 within (−0.000810, +0.000810]: of the raw 0.000019, 0.000459 is reproduced by re-refining the base with NO changes; the changes are not credited but stay (locally better, and not worse globally) || cross-check (phenix.model_vs_data, full set): null 0.113 · treatment 0.1127 · Δ -0.0003 — agrees in sign

cross-check (phenix.model_vs_data, full test set): null 0.113 · treatment 0.1127 · Δ -0.0003 → **agrees in sign** with the gate

changes kept without credit; cumulative un-credited drift since the last credited base: -0.000440 (guard at > +0.000810)

⚠ whole-model geometry outside the frozen caps: rota_outliers 1.78 > 1.5; clashscore 10.0025 > 5 (D479, monitor)

base after cycle: `/home/dev/runs/7KR0/runs/7KR0.20260910v7/cycles/c045/paired/candidate_arm/refine_001.cif` · R-free full 0.11279409470451703 · report 0.1152598541664168 · Δselect vs before +0.000019 · 9628.6 s

## cycle 46 — real space (correction, solvent)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 5, "attempted": 5, "accepted": 0, "reverted": 5, "not_attempted": []}, "solvent": {"proposed": 20, "attempted": 6, "accepted": 5, "reverted": 1, "not_attempted": ["7KR0.c046.water_remove.A249", "7KR0.c046.water_remove.A233", "7KR0.c046.water_remove.A475", "7KR0.c046.water_remove.A444", "7KR0.c046.water_remove.A404", "7KR0.c046.water_remove.A411", "7KR0.c046.water_remove.A222", "7KR0.c046.water_remove.A208", "7KR0.c046.water_remove.A430", "7KR0.c046.water_remove.A206", "7KR0.c046.water_remove.A290", "7KR0.c046.water_remove.A207", "7KR0.c046.water_remove.A219", "7KR0.c046.water_remove.A487"]}}`
- `7KR0.c046.peptide_flip.A90` **reverted** — rscc 0.991225→0.8559 (Δ -0.135325, rule mean_delta, worst neighbour drop 0.0179): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.135325 < required +0.01]; clash [7 new altloc-aware clash(es)]
- `7KR0.c046.peptide_flip.A47` **reverted** — rscc 0.992→0.811225 (Δ -0.180775, rule mean_delta, worst neighbour drop 0.0193): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.180775 < required +0.01]
- `7KR0.c046.peptide_flip.A89` **reverted** — rscc 0.98864→0.80526 (Δ -0.18338, rule mean_delta, worst neighbour drop 0.039): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.18338 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.464.. moved -0.0390 (0.7749 -> 0.7359), allowed drop 0.02]; clash [5 new altloc-aware clash(es)]
- `7KR0.c046.peptide_flip.A45` **reverted** — rscc 0.99196→0.8553 (Δ -0.13666, rule mean_delta, worst neighbour drop 0.0223): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.13666 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.269.. moved -0.0223 (0.6516 -> 0.6293), allowed drop 0.02]; clash [3 new altloc-aware clash(es)]
- `7KR0.c046.zone_rsr.A90-92` **reverted** — rscc 0.9903→0.9893 (Δ -0.001, rule mean_delta, worst neighbour drop 0.0039): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.001 < required +0.01]
- `7KR0.c046.water_remove.A403` **accepted** — rscc 0.5462→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0024): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.351.. moved -0.0024 (0.9103 -> 0.9079), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site
- `7KR0.c046.water_remove.A376` **accepted** — rscc 0.5717→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0019): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.500.. moved -0.0019 (0.9433 -> 0.9414), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site
- `7KR0.c046.water_remove.A371` **accepted** — rscc 0.6264→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.006): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.474.. moved -0.0060 (0.7827 -> 0.7767), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site
- `7KR0.c046.water_remove.A269` **reverted** — rscc 0.6563→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0832): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.450.. moved -0.0832 (0.8745 -> 0.7913), allowed drop 0.02]
- `7KR0.c046.water_remove.A505` **accepted** — rscc 0.6578→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.009): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.221.. moved -0.0090 (0.816 -> 0.807), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site-r
- `7KR0.c046.water_remove.A469` **accepted** — rscc 0.6584→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0027): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.244.. moved -0.0027 (0.8848 -> 0.8821), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site

**paired cycle**: null arm R-free-select 0.11044613490184875 · treatment arm 0.10984305258267618 · attributable **-0.000603** vs credit ≤ -0.000810 / regression > +0.000810 → **no_change**  
attributable -0.000603 within (−0.000810, +0.000810]: of the raw -0.000512, 0.000091 is reproduced by re-refining the base with NO changes; the changes are not credited but stay (locally better, and not worse globally) || cross-check (phenix.model_vs_data, full set): null 0.1127 · treatment 0.1123 · Δ -0.0004 — agrees in sign

cross-check (phenix.model_vs_data, full test set): null 0.1127 · treatment 0.1123 · Δ -0.0004 → **agrees in sign** with the gate

changes kept without credit; cumulative un-credited drift since the last credited base: -0.001043 (guard at > +0.000810)

⚠ whole-model geometry outside the frozen caps: clashscore 10.9589 > 5 (D479, monitor)

base after cycle: `/home/dev/runs/7KR0/runs/7KR0.20260910v7/cycles/c046/paired/candidate_arm/refine_001.cif` · R-free full 0.11237070374638494 · report 0.11492639838835916 · Δselect vs before -0.000512 · 9614.8 s

## finished 2026-09-10T09:11:46+00:00

max_cycles=2 reached  
R-free full 0.1125685619303301 → 0.11237070374638494 (Δ -0.000198) · report 0.11482593627366146 → 0.11492639838835916  
published better model: None · gap closed: None · reached: None  
credited changes (0): `[]`  
kept without credit: 10 · final model `/home/dev/runs/7KR0/runs/7KR0.20260910v7/cycles/c046/paired/candidate_arm/refine_001.cif`  
best base of the run: cycle 46 · R-free full 0.11237070374638494 · report 0.11492639838835916 · `/home/dev/runs/7KR0/runs/7KR0.20260910v7/cycles/c046/paired/candidate_arm/refine_001.cif`

