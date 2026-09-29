# 3QUE — run `3QUE.20260909corr`

started 2026-09-09T16:46:27+00:00 on actl-ws-xraymemory-autoresearch-devspace-54d7d7d896-4cxg2 pid 470306  
stages `['correction']` · seed 1 · max cycles 3 · max/stage 20  
noise floor σ_select = 0.001440, k = 2.0: a cycle is credited at ≤ -0.002880, bisected above +0.002880  
published better model: {'r_work': 0.171, 'r_free': 0.25, 'method': 'ensemble refinement (different model representation — see SPEC_DPDB_RUNS §0)', 'comparable_to_our_flags': True, 'their_n_free': 864, 'our_n_free': 864, 'scored_on_our_flags': {'r_work': 0.1729, 'r_free_full': 0.2517, 'r_free_select': 0.2396, 'r_free_report': 0.2643, 'model': 'https://files.dynamicpdb.com/e1231493-23e9-4110-b815-da94a2c17184/models/22b2d460-38af-4dfd-8628-95a35c85a0a8/artifacts/99f81e84-d685-4072-b3b3-b67e66a1331c/3que_final_ensemble.pdb', 'sha256': '80e9a1f7fe2203f3d3f95109', 'checked': '2026-08-29'}, 'source': 'https://dynamicpdb.com/entries/e1231493-23e9-4110-b815-da94a2c17184', 'fetched': '2026-08-27'}  
starting model: `/home/dev/runs/3QUE/experiments/water_occupancy/candidate_arm/refine_001.cif`

## cycle 0 — base

current model already carries map coefficients; no cycle-0 refinement  
R-work 0.21131427444753276 · R-free full 0.25891058999407407 · report 0.26440837191730937 (select 0.2536515243015218)

## cycle 80 — real space (correction)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 20, "attempted": 20, "accepted": 0, "reverted": 20, "not_attempted": []}}`
- `3QUE.c080.rotamer_fix.A120` **reverted** — rscc 0.5195→0.483567 (Δ -0.035933, rule mean_delta, worst neighbour drop 0.0014): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.035933 < required +0.01]
- `3QUE.c080.rotamer_fix.A198` **reverted** — rscc 0.821533→0.8249 (Δ 0.003367, rule mean_delta, worst neighbour drop 0.0051): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.003367 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `3QUE.c080.rotamer_fix.A275` **reverted** — rscc 0.884067→0.887133 (Δ 0.003066, rule mean_delta, worst neighbour drop 0.0064): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.003066 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `3QUE.c080.rotamer_fix.A97` **reverted** — rscc 0.8961→0.898833 (Δ 0.002733, rule mean_delta, worst neighbour drop 0.0031): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.002733 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `3QUE.c080.rotamer_fix.A10` **reverted** — rscc 0.9246→0.8819 (Δ -0.0427, rule mean_delta, worst neighbour drop 0.0145): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.0427 < required +0.01]
- `3QUE.c080.rotamer_fix.A100` **reverted** — rscc 0.935867→0.934933 (Δ -0.000934, rule mean_delta, worst neighbour drop 0.0059): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.000934 < required +0.01]; geometry [angle_rmsd worsened by 0.5454 > rel_max 0.3 (prev 0.34866)]; clash [1 new altloc-aware clash(es)]
- `3QUE.c080.rotamer_fix.A81` **reverted** — rscc 0.9529→0.952767 (Δ -0.000133, rule mean_delta, worst neighbour drop 0.0065): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.000133 < required +0.01]
- `3QUE.c080.rotamer_fix.A109` **reverted** — rscc 0.9578→0.9582 (Δ 0.0004, rule mean_delta, worst neighbour drop 0.0021): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.0004 < required +0.01]
- `3QUE.c080.rotamer_fix.A197` **reverted** — rscc 0.848267→0.826833 (Δ -0.021434, rule mean_delta, worst neighbour drop 0.0031): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.021434 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `3QUE.c080.rotamer_fix.A204` **reverted** — rscc 0.964067→0.963667 (Δ -0.0004, rule mean_delta, worst neighbour drop 0.0051): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.0004 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `3QUE.c080.rotamer_fix.A52` **reverted** — rscc 0.962233→0.9694 (Δ 0.007167, rule mean_delta, worst neighbour drop 0.0009): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.007167 < required +0.01]
- `3QUE.c080.rotamer_fix.A284` **reverted** — rscc 0.957867→0.955167 (Δ -0.0027, rule mean_delta, worst neighbour drop 0.0026): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.0027 < required +0.01]
- `3QUE.c080.rotamer_fix.A119` **reverted** — rscc 0.4062→0.400067 (Δ -0.006133, rule mean_delta, worst neighbour drop 0.001): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.006133 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `3QUE.c080.rotamer_fix.A118` **reverted** — rscc 0.4992→0.507133 (Δ 0.007933, rule mean_delta, worst neighbour drop 0.0): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.007933 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `3QUE.c080.rotamer_fix.A176` **reverted** — rscc 0.66715→0.66955 (Δ 0.0024, rule mean_delta, worst neighbour drop 0.001): failed: rscc [mean RSCC over 2 changed residue(s) moved 0.0024 < required +0.01]
- `3QUE.c080.peptide_flip.A119` **reverted** — rscc 0.50805→0.468575 (Δ -0.039475, rule mean_delta, worst neighbour drop 0.0189): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.039475 < required +0.01]; geometry [angle_rmsd worsened by 0.8575 > rel_max 0.3 (prev 0.68419)]; clash [6 new altloc-aware clash(es)]
- `3QUE.c080.peptide_flip.A118` **reverted** — rscc 0.4983→0.594675 (Δ 0.096375, rule mean_delta, worst neighbour drop 0.0007): failed: geometry [angle_rmsd worsened by 0.5405 > rel_max 0.3 (prev 0.56715)]; clash [3 new altloc-aware clash(es)]
- `3QUE.c080.peptide_flip.A117` **reverted** — rscc 0.59405→0.59855 (Δ 0.0045, rule mean_delta, worst neighbour drop 0.0098): failed: rscc [mean RSCC over 4 changed residue(s) moved 0.0045 < required +0.01]; geometry [bond_rmsd worsened by 0.00315 > rel_max 0.003 (prev 0.00293)]
- `3QUE.c080.peptide_flip.A35` **reverted** — rscc 0.9059→0.905525 (Δ -0.000375, rule mean_delta, worst neighbour drop 0.0009): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.000375 < required +0.01]; geometry [angle_rmsd worsened by 0.6306 > rel_max 0.3 (prev 0.32677)]
- `3QUE.c080.peptide_flip.A149` **reverted** — rscc 0.944425→0.891325 (Δ -0.0531, rule mean_delta, worst neighbour drop 0.0087): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0531 < required +0.01]; clash [4 new altloc-aware clash(es)]

no change passed the RSCC gate → quiet cycle; base re-refined once: R-free-select 0.2536515243015218 → 0.25495751609329076 (Δ +0.001306)

⚠ whole-model geometry outside the frozen caps: rota_outliers 3.63 > 1.5 (D479, monitor)

base after cycle: `/home/dev/runs/3QUE/runs/3QUE.20260909corr/cycles/c080/rerefine/refine_001.cif` · R-free full 0.2618662759902022 · report 0.2690886340084723 · Δselect vs before +0.001306 · 1092.9 s

TLS partition pinned for the rest of the run (D415): 4 group(s) from `/home/dev/runs/3QUE/runs/3QUE.20260909corr/cycles/c080/rerefine/refine_decisions.json`

## cycle 81 — real space (correction)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 20, "attempted": 20, "accepted": 0, "reverted": 20, "not_attempted": []}}`
- `3QUE.c081.rotamer_fix.A120` **reverted** — rscc 0.525033→0.4614 (Δ -0.063633, rule mean_delta, worst neighbour drop 0.0021): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.063633 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `3QUE.c081.rotamer_fix.A275` **reverted** — rscc 0.884833→0.887867 (Δ 0.003034, rule mean_delta, worst neighbour drop 0.0087): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.003034 < required +0.01]; geometry [bond_rmsd worsened by 0.00309 > rel_max 0.003 (prev 0.00095)]; clash [1 new altloc-aware clash(es)]
- `3QUE.c081.rotamer_fix.A97` **reverted** — rscc 0.897567→0.899533 (Δ 0.001966, rule mean_delta, worst neighbour drop 0.0019): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.001966 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `3QUE.c081.rotamer_fix.A10` **reverted** — rscc 0.923567→0.8829 (Δ -0.040667, rule mean_delta, worst neighbour drop 0.018): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.040667 < required +0.01]
- `3QUE.c081.rotamer_fix.A100` **reverted** — rscc 0.932833→0.937133 (Δ 0.0043, rule mean_delta, worst neighbour drop 0.0075): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.0043 < required +0.01]; geometry [bond_rmsd worsened by 0.00308 > rel_max 0.003 (prev 0.00123); angle_rmsd worsened by 0.5658 > rel_max 0.3 (prev 0.33884)]; clash [1 new altloc-aware clash(es)]
- `3QUE.c081.rotamer_fix.A81` **reverted** — rscc 0.950467→0.951133 (Δ 0.000666, rule mean_delta, worst neighbour drop 0.0005): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.000666 < required +0.01]
- `3QUE.c081.rotamer_fix.A109` **reverted** — rscc 0.9554→0.955567 (Δ 0.000167, rule mean_delta, worst neighbour drop 0.0033): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.000167 < required +0.01]
- `3QUE.c081.rotamer_fix.A197` **reverted** — rscc 0.8424→0.825833 (Δ -0.016567, rule mean_delta, worst neighbour drop 0.0022): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.016567 < required +0.01]
- `3QUE.c081.rotamer_fix.A204` **reverted** — rscc 0.962133→0.964467 (Δ 0.002334, rule mean_delta, worst neighbour drop 0.0038): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.002334 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `3QUE.c081.rotamer_fix.A52` **reverted** — rscc 0.962→0.9702 (Δ 0.0082, rule mean_delta, worst neighbour drop 0.0018): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.0082 < required +0.01]
- `3QUE.c081.rotamer_fix.A284` **reverted** — rscc 0.955867→0.9547 (Δ -0.001167, rule mean_delta, worst neighbour drop 0.0028): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.001167 < required +0.01]
- `3QUE.c081.rotamer_fix.A119` **reverted** — rscc 0.412067→0.4024 (Δ -0.009667, rule mean_delta, worst neighbour drop 0.0038): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.009667 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `3QUE.c081.rotamer_fix.A118` **reverted** — rscc 0.502033→0.5165 (Δ 0.014467, rule mean_delta, worst neighbour drop -0.0006): failed: clash [2 new altloc-aware clash(es)]
- `3QUE.c081.rotamer_fix.A176` **reverted** — rscc 0.65755→0.65685 (Δ -0.0007, rule mean_delta, worst neighbour drop 0.0): failed: rscc [mean RSCC over 2 changed residue(s) moved -0.0007 < required +0.01]
- `3QUE.c081.peptide_flip.A119` **reverted** — rscc 0.509075→0.458975 (Δ -0.0501, rule mean_delta, worst neighbour drop 0.015): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0501 < required +0.01]; geometry [angle_rmsd worsened by 0.6041 > rel_max 0.3 (prev 0.64162)]; clash [5 new altloc-aware clash(es)]
- `3QUE.c081.peptide_flip.A118` **reverted** — rscc 0.50455→0.5737 (Δ 0.06915, rule mean_delta, worst neighbour drop 0.0013): failed: geometry [bond_rmsd worsened by 0.00318 > rel_max 0.003 (prev 0.00246); angle_rmsd worsened by 0.5702 > rel_max 0.3 (prev 0.55003)]; clash [3 new altloc-aware clash(es)]
- `3QUE.c081.peptide_flip.A117` **reverted** — rscc 0.5962→0.593075 (Δ -0.003125, rule mean_delta, worst neighbour drop 0.0037): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.003125 < required +0.01]; geometry [bond_rmsd worsened by 0.00378 > rel_max 0.003 (prev 0.00236)]
- `3QUE.c081.peptide_flip.A35` **reverted** — rscc 0.904125→0.90325 (Δ -0.000875, rule mean_delta, worst neighbour drop 0.0009): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.000875 < required +0.01]; geometry [angle_rmsd worsened by 0.6171 > rel_max 0.3 (prev 0.32091)]
- `3QUE.c081.peptide_flip.A149` **reverted** — rscc 0.942075→0.8907 (Δ -0.051375, rule mean_delta, worst neighbour drop 0.0064): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.051375 < required +0.01]; clash [4 new altloc-aware clash(es)]
- `3QUE.c081.peptide_flip.A57` **reverted** — rscc 0.935275→0.938025 (Δ 0.00275, rule mean_delta, worst neighbour drop 0.0012): failed: rscc [mean RSCC over 4 changed residue(s) moved 0.00275 < required +0.01]; clash [1 new altloc-aware clash(es)]

no change passed the RSCC gate → quiet cycle; base re-refined once: R-free-select 0.25495751609329076 → 0.25403521843182164 (Δ -0.000922)

⚠ whole-model geometry outside the frozen caps: rota_outliers 3.63 > 1.5 (D479, monitor)

base after cycle: `/home/dev/runs/3QUE/runs/3QUE.20260909corr/cycles/c081/rerefine/refine_001.cif` · R-free full 0.26329106028831184 · report 0.27296703754697027 · Δselect vs before -0.000922 · 1036.1 s

## cycle 82 — real space (correction)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 20, "attempted": 20, "accepted": 0, "reverted": 20, "not_attempted": []}}`
- `3QUE.c082.rotamer_fix.A120` **reverted** — rscc 0.5461→0.512533 (Δ -0.033567, rule mean_delta, worst neighbour drop 0.0062): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.033567 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `3QUE.c082.rotamer_fix.A275` **reverted** — rscc 0.8836→0.888333 (Δ 0.004733, rule mean_delta, worst neighbour drop 0.0096): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.004733 < required +0.01]; geometry [bond_rmsd worsened by 0.00325 > rel_max 0.003 (prev 0.00107)]; clash [1 new altloc-aware clash(es)]
- `3QUE.c082.rotamer_fix.A97` **reverted** — rscc 0.895633→0.900633 (Δ 0.005, rule mean_delta, worst neighbour drop 0.0018): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.005 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `3QUE.c082.rotamer_fix.A10` **reverted** — rscc 0.925333→0.879967 (Δ -0.045366, rule mean_delta, worst neighbour drop 0.0153): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.045366 < required +0.01]
- `3QUE.c082.rotamer_fix.A81` **reverted** — rscc 0.949233→0.948133 (Δ -0.0011, rule mean_delta, worst neighbour drop 0.0031): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.0011 < required +0.01]
- `3QUE.c082.rotamer_fix.A100` **reverted** — rscc 0.9372→0.9329 (Δ -0.0043, rule mean_delta, worst neighbour drop 0.0151): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.0043 < required +0.01]; geometry [angle_rmsd worsened by 0.4931 > rel_max 0.3 (prev 0.34606)]; clash [1 new altloc-aware clash(es)]
- `3QUE.c082.rotamer_fix.A109` **reverted** — rscc 0.955567→0.956133 (Δ 0.000566, rule mean_delta, worst neighbour drop 0.0025): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.000566 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `3QUE.c082.rotamer_fix.A197` **reverted** — rscc 0.848567→0.8297 (Δ -0.018867, rule mean_delta, worst neighbour drop 0.0027): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.018867 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `3QUE.c082.rotamer_fix.A204` **reverted** — rscc 0.9636→0.965367 (Δ 0.001767, rule mean_delta, worst neighbour drop 0.0039): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.001767 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `3QUE.c082.rotamer_fix.A52` **reverted** — rscc 0.962667→0.9703 (Δ 0.007633, rule mean_delta, worst neighbour drop 0.0012): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.007633 < required +0.01]
- `3QUE.c082.rotamer_fix.A284` **reverted** — rscc 0.955433→0.952733 (Δ -0.0027, rule mean_delta, worst neighbour drop 0.0025): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.0027 < required +0.01]
- `3QUE.c082.rotamer_fix.A119` **reverted** — rscc 0.4383→0.4126 (Δ -0.0257, rule mean_delta, worst neighbour drop 0.0031): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.0257 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `3QUE.c082.rotamer_fix.A176` **reverted** — rscc 0.64135→0.64425 (Δ 0.0029, rule mean_delta, worst neighbour drop 0.0007): failed: rscc [mean RSCC over 2 changed residue(s) moved 0.0029 < required +0.01]; geometry [angle_rmsd worsened by 0.3401 > rel_max 0.3 (prev 0.11331)]
- `3QUE.c082.rotamer_fix.A118` **reverted** — rscc 0.519433→0.523167 (Δ 0.003734, rule mean_delta, worst neighbour drop -0.0007): failed: rscc [mean RSCC over 3 changed residue(s) moved 0.003734 < required +0.01]; clash [2 new altloc-aware clash(es)]
- `3QUE.c082.peptide_flip.A119` **reverted** — rscc 0.5301→0.47385 (Δ -0.05625, rule mean_delta, worst neighbour drop 0.0168): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.05625 < required +0.01]; geometry [angle_rmsd worsened by 0.6369 > rel_max 0.3 (prev 0.60454)]; clash [5 new altloc-aware clash(es)]
- `3QUE.c082.peptide_flip.A118` **reverted** — rscc 0.527075→0.5772 (Δ 0.050125, rule mean_delta, worst neighbour drop 0.0015): failed: geometry [bond_rmsd worsened by 0.0032 > rel_max 0.003 (prev 0.00216); angle_rmsd worsened by 0.5578 > rel_max 0.3 (prev 0.53736)]; clash [3 new altloc-aware clash(es)]
- `3QUE.c082.peptide_flip.A117` **reverted** — rscc 0.609925→0.60735 (Δ -0.002575, rule mean_delta, worst neighbour drop 0.0027): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.002575 < required +0.01]
- `3QUE.c082.peptide_flip.A35` **reverted** — rscc 0.902375→0.9028 (Δ 0.000425, rule mean_delta, worst neighbour drop 0.0007): failed: rscc [mean RSCC over 4 changed residue(s) moved 0.000425 < required +0.01]; geometry [angle_rmsd worsened by 0.658 > rel_max 0.3 (prev 0.30191)]
- `3QUE.c082.peptide_flip.A149` **reverted** — rscc 0.94255→0.87615 (Δ -0.0664, rule mean_delta, worst neighbour drop 0.0072): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0664 < required +0.01]; clash [4 new altloc-aware clash(es)]
- `3QUE.c082.peptide_flip.A57` **reverted** — rscc 0.937275→0.94 (Δ 0.002725, rule mean_delta, worst neighbour drop 0.008): failed: rscc [mean RSCC over 4 changed residue(s) moved 0.002725 < required +0.01]; clash [2 new altloc-aware clash(es)]

no change passed the RSCC gate → quiet cycle; base re-refined once: R-free-select 0.25403521843182164 → 0.2518168946822915 (Δ -0.002218)

⚠ whole-model geometry outside the frozen caps: rota_outliers 3.96 > 1.5 (D479, monitor)

base after cycle: `/home/dev/runs/3QUE/runs/3QUE.20260909corr/cycles/c082/rerefine/refine_001.cif` · R-free full 0.2619517533883811 · report 0.27254664728137484 · Δselect vs before -0.002218 · 2726.9 s

## finished 2026-09-09T18:07:27+00:00

max_cycles=3 reached  
R-free full 0.25891058999407407 → 0.2619517533883811 (Δ 0.003041) · report 0.26440837191730937 → 0.27254664728137484  
published better model: 0.25 · gap closed: -0.3413 · reached: False  
credited changes (0): `[]`  
kept without credit: 0 · final model `/home/dev/runs/3QUE/runs/3QUE.20260909corr/cycles/c082/rerefine/refine_001.cif`  
best base of the run: cycle 82 · R-free full 0.2619517533883811 · report 0.27254664728137484 · `/home/dev/runs/3QUE/runs/3QUE.20260909corr/cycles/c082/rerefine/refine_001.cif`

