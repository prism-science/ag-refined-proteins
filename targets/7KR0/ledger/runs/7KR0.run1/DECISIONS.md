# 7KR0 — run `7KR0.run1`

started 2026-09-03T22:38:24+00:00 on actl-ws-xraymemory-autoresearch-devspace-76dc76b9fd-l6vsd pid 721185  
stages `['correction', 'solvent', 'protein_altloc']` · seed 1 · max cycles 6 · max/stage 20  
noise floor σ_select = 0.000405, k = 2.0: a cycle is credited at ≤ -0.000810, bisected above +0.000810  
published better model: none recorded in targets.yaml  
starting model: `/home/dev/runs/7KR0/c000/noise_floor/seed1/nf_001.cif`

## cycle 0 — base

current model already carries map coefficients; no cycle-0 refinement  
R-work 0.10802639946578843 · R-free full 0.11618223726481212 · report 0.11804804062130884 (select 0.11433690725244183)

## cycle 1 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 4, "attempted": 1, "accepted": 0, "reverted": 1, "not_attempted": ["7KR0.c001.peptide_flip.A47", "7KR0.c001.peptide_flip.A89", "7KR0.c001.peptide_flip.A45"]}}`
- `7KR0.c001.peptide_flip.A90` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): occupancy sums do not hold on the applied model — this is a bug in the proposer, not a property of the density: [{'type': 'polymer_group_sum', 'chain': 'A', 'resseq': 75, 'icode': '', 'resnames': ['LEU'], 'kind': 'polymer', 'letters': ['A', 'B', 'C'], 'letter_occ': {'A': 0.416, 'B': 0.108, 'C': 0.37

**occupancy sums violated during stage correction (PROTOCOL §12): cycle stopped here**

no change passed the RSCC gate → quiet cycle; base re-refined once: R-free-select 0.11433690725244183 → 0.11432609898595034 (Δ -0.000011)

base after cycle: `/home/dev/runs/7KR0/runs/7KR0.run1/cycles/c001/rerefine/refine_001.cif` · R-free full 0.11605231376150789 · report 0.11779768033587068 · Δselect vs before -0.000011 · 1859.4 s

