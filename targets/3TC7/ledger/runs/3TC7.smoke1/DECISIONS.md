# 3TC7 — run `3TC7.smoke1`

started 2026-08-27T16:21:24+00:00 on actl-ws-xraymemory-autoresearch-devspace-76dc76b9fd-l6vsd pid 138288  
stages `['correction', 'solvent', 'protein_altloc']` · seed 1 · max cycles 1 · max/stage 3  
noise floor σ_select = 0.001811, k = 2.0: a cycle is credited at ≤ -0.003622, bisected above +0.003622  
published better model: {'r_work': 0.138, 'r_free': 0.163, 'method': 'qFit multiconformer model', 'source': 'https://dynamicpdb.com/entries/a937eeb3-1dfd-43a3-af1a-08675aad9807', 'fetched': '2026-08-27'}  
starting model: `/home/dev/runs/3TC7/c000/noise_floor/seed1/nf_001.cif`

## cycle 0 — base

current model already carries map coefficients; no cycle-0 refinement  
R-work 0.15328839080604148 · R-free full 0.1917118596921645 · report 0.1866390497449829 (select 0.1966751946017364)

## cycle 1 — real space (correction, solvent, protein_altloc)

proposed/attempted/accepted/reverted per stage: `{"correction": {"proposed": 3, "attempted": 3, "accepted": 0, "reverted": 3, "not_attempted": []}, "solvent": {"proposed": 3, "attempted": 3, "accepted": 0, "reverted": 3, "not_attempted": []}, "protein_altloc": {"proposed": 3, "attempted": 3, "accepted": 0, "reverted": 3, "not_attempted": []}}`
- `3TC7.c001.peptide_flip.A27` **reverted** — rscc 0.955→0.84205 (Δ -0.11295, rule mean_delta, worst neighbour drop 0.0258): failed: rscc [mean RSCC over 2 changed residue(s) moved -0.11295 < required +0.01]; neighbours [density stolen from an untouched neighbour: worst untouched neighbour A.782.. moved -0.0258 (0.4444 -> 0.4186), allowed drop 0.02]; geometry [bond_rmsd=0.04094 > abs_max 0.02; bond_rmsd worsened by 0.0209
- `3TC7.c001.peptide_flip.A213` **reverted** — rscc 0.95765→0.7935 (Δ -0.16415, rule mean_delta, worst neighbour drop 0.013): failed: rscc [mean RSCC over 2 changed residue(s) moved -0.16415 < required +0.01]; geometry [bond_rmsd=0.04444 > abs_max 0.02; bond_rmsd worsened by 0.03428 > rel_max 0.003 (prev 0.01016); angle_rmsd=5.51426 > abs_max 2.0; angle_rmsd worsened by 4.268 > rel_max 0.3 (prev 1.24651)]; clash [3 new alt
- `3TC7.c001.peptide_flip.A76` **reverted** — rscc 0.9777→0.8117 (Δ -0.166, rule mean_delta, worst neighbour drop 0.0135): failed: rscc [mean RSCC over 2 changed residue(s) moved -0.166 < required +0.01]; geometry [bond_rmsd=0.03878 > abs_max 0.02; bond_rmsd worsened by 0.03101 > rel_max 0.003 (prev 0.00777); angle_rmsd=3.06801 > abs_max 2.0; angle_rmsd worsened by 1.931 > rel_max 0.3 (prev 1.13672)]; clash [3 new altlo
- `3TC7.c001.water_remove.A782` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): local real-space refinement of 'chain A and resseq 782' failed, so the change cannot be measured: RealSpaceError: phenix.real_space_refine produced no refined model (exit 1); log /home/dev/runs/3TC7/runs/3TC7.smoke1/cycles/c001/discrete/3TC7.c001.water_remove.A782/rsr/real_space_refine.stdout.log
d 
- `3TC7.c001.water_remove.A671` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): RSCC could not be measured for this change: RsccError: phenix.real_space_correlation produced no table (exit 1)
Starting phenix.real_space_correlation
on Thu Aug 27 16:27:48 2026 by root
===============================================================================

Processing files:
--------------
- `3TC7.c001.water_remove.A756` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): RSCC could not be measured for this change: RsccError: phenix.real_space_correlation produced no table (exit 1)
Starting phenix.real_space_correlation
on Thu Aug 27 16:27:52 2026 by root
===============================================================================

Processing files:
--------------
- `3TC7.c001.protein_altloc_add.A111` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: QfitError: qfit_protein produced no multiconformer_model2.pdb (exit 0); log /home/dev/runs/3TC7/runs/3TC7.smoke1/cycles/c001/discrete/3TC7.c001.protein_altloc_add.A111/apply/qfit/qfit_protein.stdout.log

Sampling residues:   0%|          | 0.00/1.00 [00:00<?, ?residu
- `3TC7.c001.protein_altloc_add.A121` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: QfitError: qfit_protein produced no multiconformer_model2.pdb (exit 0); log /home/dev/runs/3TC7/runs/3TC7.smoke1/cycles/c001/discrete/3TC7.c001.protein_altloc_add.A121/apply/qfit/qfit_protein.stdout.log

Sampling residues:   0%|          | 0.00/1.00 [00:00<?, ?residu
- `3TC7.c001.protein_altloc_add.A85` **reverted** — rscc None→None (Δ None, rule None, worst neighbour drop None): the change could not be applied: QfitError: qfit_protein produced no multiconformer_model2.pdb (exit 0); log /home/dev/runs/3TC7/runs/3TC7.smoke1/cycles/c001/discrete/3TC7.c001.protein_altloc_add.A85/apply/qfit/qfit_protein.stdout.log

Sampling residues:   0%|          | 0.00/1.00 [00:00<?, ?residue

no change passed the RSCC gate → quiet cycle; base re-refined once: R-free-select 0.1966751946017364 → 0.19505044923657153 (Δ -0.001625)

base after cycle: `/home/dev/runs/3TC7/runs/3TC7.smoke1/cycles/c001/rerefine/refine_001.cif` · R-free full 0.1909527593528231 · report 0.18676468774744748 · Δselect vs before -0.001625 · 1494.7 s

## finished 2026-08-27T16:46:22+00:00

max_cycles=1 reached  
R-free full 0.1917118596921645 → 0.1909527593528231 (Δ -0.000759) · report 0.1866390497449829 → 0.18676468774744748  
published better model: 0.163 · gap closed: 0.0264 · reached: False  
credited changes (0): `[]`  
kept without credit: 0 · final model `/home/dev/runs/3TC7/runs/3TC7.smoke1/cycles/c001/rerefine/refine_001.cif`

