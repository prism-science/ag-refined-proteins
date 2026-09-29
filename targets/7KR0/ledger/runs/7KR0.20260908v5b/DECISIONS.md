# 7KR0 — run `7KR0.20260908v5b`

started 2026-09-08T17:57:58+00:00 on actl-ws-xraymemory-autoresearch-devspace-54d7d7d896-4cxg2 pid 255477  
stages `['correction', 'solvent']` · seed 1 · max cycles 2 · max/stage 20  
noise floor σ_select = 0.000405, k = 2.0: a cycle is credited at ≤ -0.000810, bisected above +0.000810  
published better model: none recorded in targets.yaml  
starting model: `/home/dev/runs/7KR0/runs/7KR0.run2/cycles/c003/paired/null_arm/refine_001.cif`

## cycle 0 — base

current model already carries map coefficients; no cycle-0 refinement  
R-work 0.10503058524074757 · R-free full 0.11368992018885889 · report 0.11565148513284632 (select 0.1117498793749345)

## cycle 31 — real space (correction, solvent)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 5, "attempted": 5, "accepted": 0, "reverted": 5, "not_attempted": []}, "solvent": {"proposed": 20, "attempted": 5, "accepted": 5, "reverted": 0, "not_attempted": ["7KR0.c031.water_remove.A374", "7KR0.c031.water_remove.A376", "7KR0.c031.water_remove.A464", "7KR0.c031.water_remove.A269", "7KR0.c031.water_remove.A233", "7KR0.c031.water_remove.A371", "7KR0.c031.water_remove.A469", "7KR0.c031.water_remove.A505", "7KR0.c031.water_remove.A206", "7KR0.c031.water_remove.A475", "7KR0.c031.water_remove.A430", "7KR0.c031.water_remove.A222", "7KR0.c031.water_remove.A487", "7KR0.c031.water_remove.A404", "7KR0.c031.water_remove.A219"]}}`
- `7KR0.c031.peptide_flip.A90` **reverted** — rscc 0.9912→0.866375 (Δ -0.124825, rule mean_delta, worst neighbour drop 0.0198): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.124825 < required +0.01]; geometry [angle_rmsd worsened by 0.3448 > rel_max 0.3 (prev 1.1325)]; clash [7 new altloc-aware clash(es)]
- `7KR0.c031.peptide_flip.A47` **reverted** — rscc 0.99195→0.778825 (Δ -0.213125, rule mean_delta, worst neighbour drop 0.0229): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.213125 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.450.. moved -0.0229 (0.8704 -> 0.8475), allowed drop 0.02]
- `7KR0.c031.peptide_flip.A89` **reverted** — rscc 0.98864→0.80386 (Δ -0.18478, rule mean_delta, worst neighbour drop 0.0245): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.18478 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.464.. moved -0.0245 (0.584 -> 0.5595), allowed drop 0.02]; clash [4 new altloc-aware clash(es)]
- `7KR0.c031.peptide_flip.A45` **reverted** — rscc 0.99214→0.85484 (Δ -0.1373, rule mean_delta, worst neighbour drop 0.0266): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.1373 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.269.. moved -0.0266 (0.6004 -> 0.5738), allowed drop 0.02]; clash [3 new altloc-aware clash(es)]
- `7KR0.c031.zone_rsr.A90-92` **reverted** — rscc 0.990433→0.989667 (Δ -0.000766, rule mean_delta, worst neighbour drop 0.0047): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.000766 < required +0.01]
- `7KR0.c031.water_remove.A509` **accepted** — rscc 0.2102→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0081): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.506.. moved -0.0081 (0.7566 -> 0.7485), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site
- `7KR0.c031.water_remove.A214` **accepted** — rscc 0.3534→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0058): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.469.. moved -0.0058 (0.6769 -> 0.6711), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site
- `7KR0.c031.water_remove.A209` **accepted** — rscc 0.485→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0064): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.500.. moved -0.0064 (0.9498 -> 0.9434), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site
- `7KR0.c031.water_remove.A493` **accepted** — rscc 0.5046→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0035): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.242.. moved -0.0035 (0.7857 -> 0.7822), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site
- `7KR0.c031.water_remove.A403` **accepted** — rscc 0.5227→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0022): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.351.. moved -0.0022 (0.9153 -> 0.9131), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site

**paired cycle**: null arm R-free-select 0.11146937550294304 · treatment arm 0.11142235812194572 · attributable **-0.000047** vs credit ≤ -0.000810 / regression > +0.000810 → **no_change**  
attributable -0.000047 within (−0.000810, +0.000810]: of the raw -0.000328, -0.000281 is reproduced by re-refining the base with NO changes; the changes are not credited but stay (locally better, and not worse globally) || cross-check (phenix.model_vs_data, full set): null 0.1136 · treatment 0.1134 · Δ -0.0002 — agrees in sign

cross-check (phenix.model_vs_data, full test set): null 0.1136 · treatment 0.1134 · Δ -0.0002 → **agrees in sign** with the gate

changes kept without credit; cumulative un-credited drift since the last credited base: -0.000047 (guard at > +0.000810)

⚠ whole-model geometry outside the frozen caps: rota_outliers 2.22 > 1.5; clashscore 9.7136 > 5 (D479, monitor)

base after cycle: `/home/dev/runs/7KR0/runs/7KR0.20260908v5b/cycles/c031/paired/candidate_arm/refine_001.cif` · R-free full 0.1134811207388861 · report 0.11556272466618411 · Δselect vs before -0.000328 · 9621.0 s

## cycle 32 — real space (correction, solvent)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 5, "attempted": 5, "accepted": 0, "reverted": 5, "not_attempted": []}, "solvent": {"proposed": 20, "attempted": 6, "accepted": 5, "reverted": 1, "not_attempted": ["7KR0.c032.water_remove.A505", "7KR0.c032.water_remove.A464", "7KR0.c032.water_remove.A506", "7KR0.c032.water_remove.A475", "7KR0.c032.water_remove.A430", "7KR0.c032.water_remove.A206", "7KR0.c032.water_remove.A404", "7KR0.c032.water_remove.A222", "7KR0.c032.water_remove.A487", "7KR0.c032.water_remove.A411", "7KR0.c032.water_remove.A208", "7KR0.c032.water_remove.A219", "7KR0.c032.water_remove.A207", "7KR0.c032.water_remove.A202"]}}`
- `7KR0.c032.peptide_flip.A90` **reverted** — rscc 0.9913→0.8665 (Δ -0.1248, rule mean_delta, worst neighbour drop 0.0191): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.1248 < required +0.01]; geometry [angle_rmsd worsened by 0.3455 > rel_max 0.3 (prev 1.13511)]; clash [7 new altloc-aware clash(es)]
- `7KR0.c032.peptide_flip.A47` **reverted** — rscc 0.9918→0.8104 (Δ -0.1814, rule mean_delta, worst neighbour drop 0.0194): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.1814 < required +0.01]
- `7KR0.c032.peptide_flip.A89` **reverted** — rscc 0.98854→0.8045 (Δ -0.18404, rule mean_delta, worst neighbour drop 0.0351): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.18404 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.464.. moved -0.0351 (0.6886 -> 0.6535), allowed drop 0.02]; clash [4 new altloc-aware clash(es)]
- `7KR0.c032.peptide_flip.A45` **reverted** — rscc 0.99202→0.83542 (Δ -0.1566, rule mean_delta, worst neighbour drop 0.041): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.1566 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.374.. moved -0.0410 (0.5413 -> 0.5003), allowed drop 0.02]; clash [2 new altloc-aware clash(es)]
- `7KR0.c032.zone_rsr.A90-92` **reverted** — rscc 0.990567→0.989733 (Δ -0.000834, rule mean_delta, worst neighbour drop 0.0038): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.000834 < required +0.01]
- `7KR0.c032.water_remove.A374` **accepted** — rscc 0.5413→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0068): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.269.. moved -0.0068 (0.621 -> 0.6142), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site-
- `7KR0.c032.water_remove.A376` **accepted** — rscc 0.5481→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0018): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.351.. moved -0.0018 (0.9243 -> 0.9225), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site
- `7KR0.c032.water_remove.A269` **reverted** — rscc 0.6148→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0839): failed: neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.450.. moved -0.0839 (0.8845 -> 0.8006), allowed drop 0.02]
- `7KR0.c032.water_remove.A233` **accepted** — rscc 0.6429→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0023): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.442.. moved -0.0023 (0.9334 -> 0.9311), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site
- `7KR0.c032.water_remove.A371` **accepted** — rscc 0.6555→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0052): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.474.. moved -0.0052 (0.765 -> 0.7598), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site-
- `7KR0.c032.water_remove.A469` **accepted** — rscc 0.6881→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0046): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.244.. moved -0.0046 (0.87 -> 0.8654), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=0.7700003403620237; no new altloc-aware clash; site-r

**paired cycle**: null arm R-free-select 0.11123417629346787 · treatment arm 0.11147602436338756 · attributable **+0.000242** vs credit ≤ -0.000810 / regression > +0.000810 → **no_change**  
attributable 0.000242 within (−0.000810, +0.000810]: of the raw 0.000054, -0.000188 is reproduced by re-refining the base with NO changes; the changes are not credited and are dropped: they made R-free-select worse, below the bar but worse (D411) || cross-check (phenix.model_vs_data, full set): null 0.1134 · treatment 0.1135 · Δ +0.0001 — agrees in sign

cross-check (phenix.model_vs_data, full test set): null 0.1134 · treatment 0.1135 · Δ +0.0001 → **agrees in sign** with the gate

5 change(s) dropped: within noise but attributable +0.000242 > 0 — base ← null arm (D411)

⚠ whole-model geometry outside the frozen caps: rota_outliers 1.78 > 1.5; clashscore 10.2117 > 5 (D479, monitor)

base after cycle: `/home/dev/runs/7KR0/runs/7KR0.20260908v5b/cycles/c032/paired/null_arm/refine_001.cif` · R-free full 0.11343035762600034 · report 0.11565090488542817 · Δselect vs before -0.000188 · 9286.4 s

**stall detected** after cycle 32: 2 consecutive cycle(s) accepted changes locally but each moved R-free-select by < σ=0.000405: a minimum small edits cannot leave → next cycle takes an escape rung

## finished 2026-09-08T23:13:12+00:00

max_cycles=2 reached  
R-free full 0.11368992018885889 → 0.11343035762600034 (Δ -0.00026) · report 0.11565148513284632 → 0.11565090488542817  
published better model: None · gap closed: None · reached: None  
credited changes (0): `[]`  
kept without credit: 5 · final model `/home/dev/runs/7KR0/runs/7KR0.20260908v5b/cycles/c032/paired/null_arm/refine_001.cif`  
best base of the run: cycle 32 · R-free full 0.11343035762600034 · report 0.11565090488542817 · `/home/dev/runs/7KR0/runs/7KR0.20260908v5b/cycles/c032/paired/null_arm/refine_001.cif`

