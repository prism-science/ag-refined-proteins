# 3TC7 — run `3TC7.20260909corr_h2`

started 2026-09-09T18:15:29+00:00 on actl-ws-xraymemory-autoresearch-devspace-54d7d7d896-4cxg2 pid 620023  
stages `['correction']` · seed 1 · max cycles 1 · max/stage 20  
noise floor σ_select = 0.000457, k = 2.0: a cycle is credited at ≤ -0.000914, bisected above +0.000914  
published better model: {'r_work': 0.138, 'r_free': 0.163, 'method': 'qFit multiconformer model', 'source': 'https://dynamicpdb.com/entries/a937eeb3-1dfd-43a3-af1a-08675aad9807', 'fetched': '2026-08-27', 'comparable_to_our_flags': False, 'their_n_free': 1993, 'our_n_free': 2075, 'scored_on_our_flags': {'r_work': 0.139, 'r_free_full': 0.1439, 'r_free_gap': 0.0049, 'clashscore_altloc_aware': 15.39, 'model': 'https://files.dynamicpdb.com/a937eeb3-1dfd-43a3-af1a-08675aad9807/models/036b3d5e-c7e6-4f0e-ae39-37e76b3a7618/artifacts/2e719a59-01fd-4bd3-8ada-5bfdfc149940/3tc7_qFit_010.cif', 'sha256': '4dbee3272ff413a30db10dd5811c371c547a4804795792590592292e34e62a74', 'checked': '2026-08-29'}}  
starting model: `/home/dev/runs/3TC7/experiments/e028b_riding_h_pre/paired/candidate_arm/refine_001.cif`

## cycle 0 — base

current model already carries map coefficients; no cycle-0 refinement  
R-work 0.1351496281935661 · R-free full 0.17276394500804818 · report 0.16726042463813334 (select 0.17814869528687724)

## cycle 62 — real space (correction)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 9, "attempted": 9, "accepted": 0, "reverted": 9, "not_attempted": []}}`
- `3TC7.c062.rotamer_fix.A15` **reverted** — rscc 0.970067→0.950433 (Δ -0.019634, rule mean_delta, worst neighbour drop 0.0292): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.019634 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.5052.. moved -0.0292 (0.751 -> 0.7218), allowed drop 0.02]
- `3TC7.c062.rotamer_fix.A17` **reverted** — rscc 0.955733→0.949033 (Δ -0.0067, rule mean_delta, worst neighbour drop 0.0008): failed: rscc [mean RSCC over 3 changed residue(s) moved -0.0067 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `3TC7.c062.peptide_flip.A27` **reverted** — rscc 0.974825→0.917175 (Δ -0.05765, rule mean_delta, worst neighbour drop 0.0199): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.05765 < required +0.01]
- `3TC7.c062.peptide_flip.A213` **reverted** — rscc 0.9639→0.7352 (Δ -0.2287, rule mean_delta, worst neighbour drop 0.0205): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.2287 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.696.. moved -0.0205 (0.9832 -> 0.9627), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.3785 > rel_max 0.3 (prev 1.34543)]; cl
- `3TC7.c062.peptide_flip.A76` **reverted** — rscc 0.98098→0.87666 (Δ -0.10432, rule mean_delta, worst neighbour drop 0.0272): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.10432 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.5029.. moved -0.0272 (0.8236 -> 0.7964), allowed drop 0.02]; clash [6 new altloc-aware clash(es)]
- `3TC7.c062.peptide_flip.A58` **reverted** — rscc 0.9826→0.665425 (Δ -0.317175, rule mean_delta, worst neighbour drop 0.0578): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.317175 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.5013.. moved -0.0578 (0.9749 -> 0.9171), allowed drop 0.02]; clash [6 new altloc-aware clash(es)]
- `3TC7.c062.zone_rsr.A211-215` **reverted** — rscc 0.96656→0.95512 (Δ -0.01144, rule mean_delta, worst neighbour drop 0.0127): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.01144 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `3TC7.c062.zone_rsr.A25-29` **reverted** — rscc 0.9773→0.97268 (Δ -0.00462, rule mean_delta, worst neighbour drop 0.0049): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.00462 < required +0.01]
- `3TC7.c062.zone_rsr.A56-60` **reverted** — rscc 0.98166→0.97208 (Δ -0.00958, rule mean_delta, worst neighbour drop 0.002): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.00958 < required +0.01]

no change passed the RSCC gate → quiet cycle; base re-refined once: R-free-select 0.17814869528687724 → 0.1764409192329584 (Δ -0.001708)

base after cycle: `/home/dev/runs/3TC7/runs/3TC7.20260909corr_h2/cycles/c062/rerefine/refine_001.cif` · R-free full 0.17234217576095642 · report 0.16815302732859555 · Δselect vs before -0.001708 · 1351.2 s

## finished 2026-09-09T18:38:03+00:00

max_cycles=1 reached  
R-free full 0.17276394500804818 → 0.17234217576095642 (Δ -0.000422) · report 0.16726042463813334 → 0.16815302732859555  
published better model: 0.163 · gap closed: None · reached: None  
credited changes (0): `[]`  
kept without credit: 0 · final model `/home/dev/runs/3TC7/runs/3TC7.20260909corr_h2/cycles/c062/rerefine/refine_001.cif`  
best base of the run: cycle 62 · R-free full 0.17234217576095642 · report 0.16815302732859555 · `/home/dev/runs/3TC7/runs/3TC7.20260909corr_h2/cycles/c062/rerefine/refine_001.cif`

