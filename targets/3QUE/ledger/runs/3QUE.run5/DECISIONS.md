# 3QUE — run `3QUE.run5`

started 2026-08-28T15:44:01+00:00 on actl-ws-xraymemory-autoresearch-devspace-76dc76b9fd-l6vsd pid 633393  
stages `['gaps']` · seed 1 · max cycles 2 · max/stage 4  
noise floor σ_select = 0.001440, k = 2.0: a cycle is credited at ≤ -0.002880, bisected above +0.002880  
published better model: {'r_work': 0.171, 'r_free': 0.25, 'method': 'ensemble refinement (different model representation — see SPEC_DPDB_RUNS §0)', 'source': 'https://dynamicpdb.com/entries/e1231493-23e9-4110-b815-da94a2c17184', 'fetched': '2026-08-27'}  
starting model: `/home/dev/runs/3QUE/experiments/water_occupancy/candidate_arm/refine_001.cif`

## cycle 0 — base

current model already carries map coefficients; no cycle-0 refinement  
R-work 0.21131427444753276 · R-free full 0.25891058999407407 · report 0.26440837191730937 (select 0.2536515243015218)

## cycle 61 — real space (gaps)

proposed/attempted/accepted/reverted per stage: `{"gaps": {"proposed": 1, "attempted": 1, "accepted": 0, "reverted": 1, "not_attempted": []}}`
- `3QUE.c061.loop_build.A177-182` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: phenix.fit_loops wrote no model (exit 0); log /home/dev/runs/3QUE/runs/3QUE.run5/cycles/c061/discrete/3QUE.c061.loop_build.A177-182/apply/fit_loops/phenix.fit_loops.stdout.log

no change passed the RSCC gate → quiet cycle; base re-refined once: R-free-select 0.2536515243015218 → 0.25495751609329076 (Δ +0.001306)

base after cycle: `/home/dev/runs/3QUE/runs/3QUE.run5/cycles/c061/rerefine/refine_001.cif` · R-free full 0.2618662759902022 · report 0.2690886340084723 · Δselect vs before +0.001306 · 604.6 s

TLS partition pinned for the rest of the run (D415): 4 group(s) from `/home/dev/runs/3QUE/runs/3QUE.run5/cycles/c061/rerefine/refine_decisions.json`

## cycle 62 — real space (gaps)

proposed/attempted/accepted/reverted per stage: `{"gaps": {"proposed": 1, "attempted": 1, "accepted": 0, "reverted": 1, "not_attempted": []}}`
- `3QUE.c062.loop_build.A177-182` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: DiscreteError: phenix.fit_loops wrote no model (exit 0); log /home/dev/runs/3QUE/runs/3QUE.run5/cycles/c062/discrete/3QUE.c062.loop_build.A177-182/apply/fit_loops/phenix.fit_loops.stdout.log

no change passed the RSCC gate → quiet cycle; base re-refined once: R-free-select 0.25495751609329076 → 0.25403521843182164 (Δ -0.000922)

base after cycle: `/home/dev/runs/3QUE/runs/3QUE.run5/cycles/c062/rerefine/refine_001.cif` · R-free full 0.26329106028831184 · report 0.27296703754697027 · Δselect vs before -0.000922 · 594.6 s

## finished 2026-08-28T17:25:01+00:00

max_cycles=2 reached  
R-free full 0.25891058999407407 → 0.26329106028831184 (Δ 0.00438) · report 0.26440837191730937 → 0.27296703754697027  
published better model: 0.25 · gap closed: -0.4916 · reached: False  
credited changes (0): `[]`  
kept without credit: 0 · final model `/home/dev/runs/3QUE/runs/3QUE.run5/cycles/c062/rerefine/refine_001.cif`  
best base of the run: cycle 60 · R-free full 0.25891058999407407 · report 0.26440837191730937 · `/home/dev/runs/3QUE/experiments/water_occupancy/candidate_arm/refine_001.cif`

