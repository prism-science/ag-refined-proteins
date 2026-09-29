# 7DVR — run `7DVR.20260917T052749Z`

started 2026-09-17T05:27:49+00:00 on actl-ws-xraymemory-autoresearch-devspace-8597768cc8-lxfq5 pid 277308  
stages `['correction', 'solvent', 'protein_altloc']` · seed 1 · max cycles 8 · max/stage 20  
noise floor σ_select = 0.000960, k = 2.0: a cycle is credited at ≤ -0.001920, bisected above +0.001920  
published better model: none recorded in targets.yaml  
starting model: `/home/dev/runs/7DVR/c000/baseline_rerefine/refine_001.cif`

## cycle 0 — base

cycle 0: re-refined the starting model to obtain map coefficients (/home/dev/runs/7DVR/runs/7DVR.20260917T052749Z/base/rerefine/refine_001.cif)  
R-work 0.2544441969890793 · R-free full 0.28893069071988664 · report 0.2702698312576718 (select 0.3129434694023143)

## cycle 1 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 12, "attempted": 12, "accepted": 0, "reverted": 12, "not_attempted": []}, "solvent": {"proposed": 16, "attempted": 5, "accepted": 5, "reverted": 0, "not_attempted": ["7DVR.c001.water_remove.A334", "7DVR.c001.water_remove.A326", "7DVR.c001.water_remove.A325", "7DVR.c001.water_remove.A336", "7DVR.c001.water_remove.A308", "7DVR.c001.water_add.A5001", "7DVR.c001.water_add.A5002", "7DVR.c001.water_add.A5003", "7DVR.c001.water_add.A5004", "7DVR.c001.water_add.A5005", "7DVR.c001.water_add.A5006"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `7DVR.c001.peptide_flip.A142` **reverted** — rscc 0.8181→0.78735 (Δ -0.03075, rule mean_delta, worst neighbour drop 0.016): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.03075 < required +0.01]; geometry [angle_rmsd worsened by 0.4155 > rel_max 0.3 (prev 0.67336)]; clash [2 new altloc-aware clash(es)]
- `7DVR.c001.peptide_flip.A88` **reverted** — rscc 0.87805→0.85235 (Δ -0.0257, rule mean_delta, worst neighbour drop 0.0516): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0257 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.332.. moved -0.0516 (0.6388 -> 0.5872), allowed drop 0.02]; clash [4 new altloc-aware clash(es)]
- `7DVR.c001.peptide_flip.A89` **reverted** — rscc 0.8919→0.79355 (Δ -0.09835, rule mean_delta, worst neighbour drop 0.057): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.09835 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.332.. moved -0.0570 (0.6388 -> 0.5818), allowed drop 0.02]; clash [3 new altloc-aware clash(es)]
- `7DVR.c001.peptide_flip.A141` **reverted** — rscc 0.808825→0.786025 (Δ -0.0228, rule mean_delta, worst neighbour drop 0.0088): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0228 < required +0.01]; geometry [bond_rmsd worsened by 0.00422 > rel_max 0.003 (prev 0.00201)]; clash [2 new altloc-aware clash(es)]
- `7DVR.c001.peptide_flip.A145` **reverted** — rscc 0.82165→0.73685 (Δ -0.0848, rule mean_delta, worst neighbour drop 0.0107): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0848 < required +0.01]; geometry [angle_rmsd worsened by 0.4426 > rel_max 0.3 (prev 0.48788)]; clash [6 new altloc-aware clash(es)]
- `7DVR.c001.peptide_flip.A30` **reverted** — rscc 0.9126→0.8188 (Δ -0.0938, rule mean_delta, worst neighbour drop 0.1001): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0938 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.309.. moved -0.1001 (0.7804 -> 0.6803), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.6771 > rel_max 0.3 (prev 0.50296)]; cl
- `7DVR.c001.peptide_flip.A144` **reverted** — rscc 0.82→0.8023 (Δ -0.0177, rule mean_delta, worst neighbour drop 0.0167): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0177 < required +0.01]; clash [5 new altloc-aware clash(es)]
- `7DVR.c001.peptide_flip.A48` **reverted** — rscc 0.93866→0.79266 (Δ -0.146, rule mean_delta, worst neighbour drop 0.1375): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.146 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.335.. moved -0.1375 (0.7651 -> 0.6276), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.4048 > rel_max 0.3 (prev 0.47846)]; cla
- `7DVR.c001.peptide_flip.A28` **reverted** — rscc 0.92655→0.8318 (Δ -0.09475, rule mean_delta, worst neighbour drop 0.095): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.09475 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.305.. moved -0.0950 (0.732 -> 0.637), allowed drop 0.02]; geometry [bond_rmsd worsened by 0.00356 > rel_max 0.003 (prev 0.00136); an
- `7DVR.c001.zone_rsr.A139-147` **reverted** — rscc 0.831167→0.846178 (Δ 0.015011, rule mean_delta, worst neighbour drop 0.0092): failed: geometry [angle_rmsd worsened by 0.444 > rel_max 0.3 (prev 0.52396)]; clash [3 new altloc-aware clash(es)]
- `7DVR.c001.zone_rsr.A86-91` **reverted** — rscc 0.887033→0.89115 (Δ 0.004117, rule mean_delta, worst neighbour drop 0.0073): failed: rscc [mean RSCC over 6 changed residue(s) moved 0.004117 < required +0.01]
- `7DVR.c001.zone_rsr.A26-32` **reverted** — rscc 0.927914→0.931071 (Δ 0.003157, rule mean_delta, worst neighbour drop 0.0074): failed: rscc [mean RSCC over 7 changed residue(s) moved 0.003157 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `7DVR.c001.water_remove.A331` **accepted** — rscc 0.4567→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0036): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.61.. moved -0.0036 (0.9092 -> 0.9056), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7042752319993781; no new altloc-aware clash; site-
- `7DVR.c001.water_remove.A301` **accepted** — rscc 0.5882→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0048): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.16.. moved -0.0048 (0.9378 -> 0.933), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7042752319993781; no new altloc-aware clash; site-r
- `7DVR.c001.water_remove.A332` **accepted** — rscc 0.649→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0014): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.54.. moved -0.0014 (0.9418 -> 0.9404), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7042752319993781; no new altloc-aware clash; site-
- `7DVR.c001.water_remove.A312` **accepted** — rscc 0.6334→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0051): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.317.. moved -0.0051 (0.892 -> 0.8869), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7042752319993781; no new altloc-aware clash; site-
- `7DVR.c001.water_remove.A337` **accepted** — rscc 0.6894→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0017): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.134.. moved -0.0017 (0.8961 -> 0.8944), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7042752319993781; no new altloc-aware clash; site

**paired cycle**: null arm R-free-select 0.31302629365991697 · treatment arm 0.31514156268525834 · attributable **+0.002115** vs credit ≤ -0.001920 / regression > +0.001920 → **rejected** (REGRESSED)  
attributable 0.002115 > +0.001920: the changes made R-free-select WORSE than the identically refined base — regression, bisect (SPEC_LOOP_V2 §1.3) || cross-check (phenix.model_vs_data, full set): null 0.2897 · treatment 0.2917 · Δ +0.0020 — agrees in sign

cross-check (phenix.model_vs_data, full test set): null 0.2897 · treatment 0.2917 · Δ +0.0020 → **agrees in sign** with the gate

bisection: culprits `[]`, survivors `['7DVR.c001.water_remove.A331', '7DVR.c001.water_remove.A301', '7DVR.c001.water_remove.A332', '7DVR.c001.water_remove.A312', '7DVR.c001.water_remove.A337']` (2 refinement(s)); base ← best non-regressing subset 7DVR.c001.d0.L.00 at R-free-select 0.31284991956627173. no single change regresses on its own — the regression is an interaction between halves (7DVR.c001.water_remove.A331+7DVR.c001.water_remove.A301+7DVR.c001.water_remove.A332+7DVR.c001.water_remove.A312+7DVR.c001.water_remove.A337); nothing convicted

base after cycle: `/home/dev/runs/7DVR/runs/7DVR.20260917T052749Z/cycles/c001/bisect/7DVR.c001.d0.L.00/refine/refine_001.cif` · R-free full 0.2895627886522731 · report 0.27146584606135415 · Δselect vs before -0.000094 · 2600.8 s

## cycle 2 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 12, "attempted": 12, "accepted": 0, "reverted": 12, "not_attempted": []}, "solvent": {"proposed": 12, "attempted": 5, "accepted": 5, "reverted": 0, "not_attempted": ["7DVR.c002.water_remove.A329", "7DVR.c002.water_remove.A334", "7DVR.c002.water_remove.A337", "7DVR.c002.water_add.A5001", "7DVR.c002.water_add.A5002", "7DVR.c002.water_add.A5003", "7DVR.c002.water_add.A5004"]}, "protein_altloc": {"skipped": "max_changes_per_cycle=5 reached"}}`
- `7DVR.c002.peptide_flip.A142` **reverted** — rscc 0.814125→0.7837 (Δ -0.030425, rule mean_delta, worst neighbour drop 0.0073): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.030425 < required +0.01]; geometry [angle_rmsd worsened by 0.3337 > rel_max 0.3 (prev 0.6175)]; clash [1 new altloc-aware clash(es)]
- `7DVR.c002.peptide_flip.A88` **reverted** — rscc 0.880425→0.856675 (Δ -0.02375, rule mean_delta, worst neighbour drop 0.0334): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.02375 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.312.. moved -0.0334 (0.5537 -> 0.5203), allowed drop 0.02]; clash [5 new altloc-aware clash(es)]
- `7DVR.c002.peptide_flip.A141` **reverted** — rscc 0.802075→0.782925 (Δ -0.01915, rule mean_delta, worst neighbour drop 0.0051): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.01915 < required +0.01]; geometry [bond_rmsd worsened by 0.00488 > rel_max 0.003 (prev 0.00125)]
- `7DVR.c002.peptide_flip.A89` **reverted** — rscc 0.89305→0.796875 (Δ -0.096175, rule mean_delta, worst neighbour drop 0.0424): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.096175 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.332.. moved -0.0424 (0.6299 -> 0.5875), allowed drop 0.02]; clash [3 new altloc-aware clash(es)]
- `7DVR.c002.peptide_flip.A145` **reverted** — rscc 0.8313→0.738175 (Δ -0.093125, rule mean_delta, worst neighbour drop 0.0225): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.093125 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.142.. moved -0.0225 (0.7085 -> 0.686), allowed drop 0.02]; clash [6 new altloc-aware clash(es)]
- `7DVR.c002.peptide_flip.A30` **reverted** — rscc 0.91735→0.8229 (Δ -0.09445, rule mean_delta, worst neighbour drop 0.1045): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.09445 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.309.. moved -0.1045 (0.7579 -> 0.6534), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.7144 > rel_max 0.3 (prev 0.48246)]; c
- `7DVR.c002.peptide_flip.A144` **reverted** — rscc 0.829525→0.808225 (Δ -0.0213, rule mean_delta, worst neighbour drop 0.0243): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.0213 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.302.. moved -0.0243 (0.8872 -> 0.8629), allowed drop 0.02]; clash [5 new altloc-aware clash(es)]
- `7DVR.c002.peptide_flip.A48` **reverted** — rscc 0.94038→0.79142 (Δ -0.14896, rule mean_delta, worst neighbour drop 0.1293): failed: rscc [mean RSCC over 5 changed residue(s) moved -0.14896 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.335.. moved -0.1293 (0.7484 -> 0.6191), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.4732 > rel_max 0.3 (prev 0.39955)]; c
- `7DVR.c002.peptide_flip.A28` **reverted** — rscc 0.93135→0.831575 (Δ -0.099775, rule mean_delta, worst neighbour drop 0.0663): failed: rscc [mean RSCC over 4 changed residue(s) moved -0.099775 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.305.. moved -0.0663 (0.7641 -> 0.6978), allowed drop 0.02]; geometry [angle_rmsd worsened by 0.6415 > rel_max 0.3 (prev 0.53182)]; 
- `7DVR.c002.zone_rsr.A139-147` **reverted** — rscc 0.831889→0.846167 (Δ 0.014278, rule mean_delta, worst neighbour drop 0.0062): failed: geometry [angle_rmsd worsened by 0.481 > rel_max 0.3 (prev 0.545)]; clash [1 new altloc-aware clash(es)]
- `7DVR.c002.zone_rsr.A86-91` **reverted** — rscc 0.889767→0.893717 (Δ 0.00395, rule mean_delta, worst neighbour drop 0.0019): failed: rscc [mean RSCC over 6 changed residue(s) moved 0.00395 < required +0.01]
- `7DVR.c002.zone_rsr.A26-32` **reverted** — rscc 0.931171→0.928571 (Δ -0.0026, rule mean_delta, worst neighbour drop 0.0063): failed: rscc [mean RSCC over 7 changed residue(s) moved -0.0026 < required +0.01]; clash [1 new altloc-aware clash(es)]
- `7DVR.c002.water_remove.A312` **accepted** — rscc 0.5537→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0068): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.317.. moved -0.0068 (0.8705 -> 0.8637), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7042752319993781; no new altloc-aware clash; site
- `7DVR.c002.water_remove.A332` **accepted** — rscc 0.6334→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0015): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.333.. moved -0.0015 (0.9031 -> 0.9016), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7042752319993781; no new altloc-aware clash; site
- `7DVR.c002.water_remove.A326` **accepted** — rscc 0.689→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0033): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.121.. moved -0.0033 (0.9317 -> 0.9284), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7042752319993781; no new altloc-aware clash; site
- `7DVR.c002.water_remove.A336` **accepted** — rscc 0.6725→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0124): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.142.. moved -0.0124 (0.7223 -> 0.7099), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7042752319993781; no new altloc-aware clash; site
- `7DVR.c002.water_remove.A325` **accepted** — rscc 0.6623→None (Δ None, rule removed_residue_floor, worst neighbour drop 0.0009): RSCC gate passed: RSCC gate passed under removed_residue_floor; worst untouched neighbour A.122.. moved -0.0009 (0.9222 -> 0.9213), allowed drop 0.02; local geometry bond_rmsd=None angle_rmsd=None over 0 bond(s)/0 angle(s) within the band for d_min=1.7042752319993781; no new altloc-aware clash; site

**paired cycle**: null arm R-free-select 0.31791767192487647 · treatment arm 0.31608053582851803 · attributable **-0.001837** vs credit ≤ -0.001920 / regression > +0.001920 → **no_change**  
attributable -0.001837 within (−0.001920, +0.001920]: of the raw 0.003231, 0.005068 is reproduced by re-refining the base with NO changes; the changes are not credited but stay (locally better, and not worse globally) || cross-check (phenix.model_vs_data, full set): null 0.2911 · treatment 0.2932 · Δ +0.0021 — DISAGREES in sign: treat this credit as provisional

cross-check (phenix.model_vs_data, full test set): null 0.2911 · treatment 0.2932 · Δ +0.0021 → **DISAGREES in sign** with the gate — credit provisional (D409)

changes kept without credit; cumulative un-credited drift since the last credited base: -0.001837 (guard at > +0.001920)

**base guard (D418)**: the candidate arm refined to R-free-select +0.003231 worse than this cycle's base (> k·σ 0.001920) with no credited change — the base is kept as is

base after cycle: `/home/dev/runs/7DVR/runs/7DVR.20260917T052749Z/cycles/c001/bisect/7DVR.c001.d0.L.00/refine/refine_001.cif` · R-free full 0.2895627886522731 · report 0.27146584606135415 · Δselect vs before +0.000000 · 1587.5 s

**stall detected** after cycle 2: 2 consecutive cycle(s) accepted changes locally but each moved R-free-select by < σ=0.000960: a minimum small edits cannot leave → next cycle takes an escape rung

## cycle 3 — stall escape rung `reweight_reseed`

different random seed, fresh xyz/adp weight optimisation, +3 macro-cycles: override `{'seed': 1001, 'optimize_xyz_weight': True, 'optimize_adp_weight': True, 'wxc_scale': None, 'wxu_scale': None, 'macro_cycles': 8}`  
null arm R-free-select 0.31791767192487647 · escape arm 0.31913642178742363 · attributable **+0.001219** → did not clear  
attributable 0.001219 within (−0.001920, +0.001920]: of the raw 0.006287, 0.005068 is reproduced by re-refining the base with NO changes; the changes are not credited and are not adopted (no local evidence of their own) || cross-check (phenix.model_vs_data, full set): null 0.2911 · treatment 0.2923 · Δ +0.0012 — agrees in sign  
ladder so far `{'reweight_reseed': 'failed'}`

## cycle 4 — stall escape rung `rescale_bulk_solvent`

bulk_solvent_and_scale.mode=slow — solvent and anisotropic scale re-fit from scratch: override `{'bulk_solvent_mode': 'slow'}`  
null arm R-free-select 0.3184488115729717 · escape arm 0.32005359244912895 · attributable **+0.001605** → did not clear  
attributable 0.001605 within (−0.001920, +0.001920]: of the raw 0.002136, 0.000531 is reproduced by re-refining the base with NO changes; the changes are not credited and are not adopted (no local evidence of their own) || cross-check (phenix.model_vs_data, full set): null 0.293 · treatment 0.2952 · Δ +0.0022 — agrees in sign  
ladder so far `{'reweight_reseed': 'failed', 'rescale_bulk_solvent': 'failed'}`

## cycle 5 — escape

escape ladder exhausted (reweight_reseed=failed, rescale_bulk_solvent=failed, simulated_annealing=refused): the model is converged at this minimum. **Converged at this minimum.**

## finished 2026-09-17T07:06:15+00:00

escape ladder exhausted (reweight_reseed=failed, rescale_bulk_solvent=failed, simulated_annealing=refused): the model is converged at this minimum  
R-free full 0.28893069071988664 → 0.2928359508404325 (Δ 0.003905) · report 0.2702698312576718 → 0.27293163235750073  
published better model: None · gap closed: None · reached: None  
credited changes (0): `[]`  
kept without credit: 0 · final model `/home/dev/runs/7DVR/runs/7DVR.20260917T052749Z/cycles/c004/escape/null_arm/refine_001.cif`  
best base of the run: cycle 1 · R-free full 0.2895627886522731 · report 0.27146584606135415 · `/home/dev/runs/7DVR/runs/7DVR.20260917T052749Z/cycles/c001/bisect/7DVR.c001.d0.L.00/refine/refine_001.cif`

