# 7KR0 — Crystal structure of SARS-CoV-2 NSP3 macrodomain (C2 crystal form, 100 K)

**Status: improved.** The released model is a six-copy ensemble with an R-free of 0.0726 on the deposited free set. The re-refined deposited model (S0001, the common recipe) scores 0.1095 and the deposited model as scored (S0000) 0.1175 on the same reflections.

| | |
|---|---|
| Resolution | 0.77 Å |
| Space group | C 1 2 1 |
| Data | amplitudes (FP,SIGFP); 174 924 reflections in the working files, 166 212 work and 8 712 free |
| Free set | the deposition's own flags, inherited unchanged (4.98 %); select / report halves 4 356 / 4 356 |
| Vault | 3 400 work reflections (2 %) removed from every working file at preprocessing; read one time, at S0011 |
| Deposited refinement program | PHENIX |
| Released by the PDB | 2020-12-09 |
| Primary citation | Fragment binding to the Nsp3 macrodomain of SARS-CoV-2 identified through crystallographic screening and computational docking (Sci Adv 2021), DOI 10.1126/sciadv.abf8711 |
| Harness | prism-science/autoresearch, branch `manzuoni/hierarchical_refinement` (the model: commit bd972d3; the card: bfed380, merged into `main` as 7d62e84) |
| Run | handle Tff1b3f, step S0053, 2026-10-18 23:06:47 UTC |
| Phenix | 2.1-6048 |
| Gate | ΔR-free ≤ −2σ against the control (σ = 0.00016 from three seeds), gap widened by at most 0.002, gap ≤ 0.0300 or not above the control's, clashscore ≤ 15, rotamer outliers ≤ 1.5 % or not above the control's |

## The three models on the same flags

All three are scored by the harness gate: a fresh cctbx fmodel on the working data with every reflection, no outlier
rejection. S0000 is the deposited model as anonymised at preprocessing; S0001 is that model after the common recipe
(phenix.refine, 10 macro-cycles, three seeds, the median), the baseline that every gain is measured against; the
release is the model in force. Geometry from phenix.clashscore (hydrogens kept), rotalyze and ramalyze; the
MolProbity score from those three.

| | Deposited as scored (S0000) | Re-refined (S0001) | This release (S0053) |
|---|---|---|---|
| R-free | 0.1175 | 0.1095 | **0.0726** |
| R-work | 0.1104 | 0.1005 | 0.0467 |
| Gap R-free − R-work | 0.0071 | 0.0089 | 0.0259 |
| R-free on the select / report halves | 0.1182 / 0.1168 | 0.1085 / 0.1104 | 0.0712 / 0.0740 |
| Clashscore (phenix.clashscore, hydrogens kept) | 4.3 | 5.3 | 7.7 |
| Rotamer outliers | 0.89 % | 1.33 % | 1.54 % |
| Ramachandran outliers / favoured | 0.0 % / 99.4 % | 0.0 % / 98.8 % | 0.0 % / 97.0 % |
| Bond RMSD / angle RMSD | 0.021 Å / 0.99° | 0.008 Å / 1.10° | 0.007 Å / 0.99° |
| MolProbity score | 1.21 | 1.38 | 1.74 |
| Copies | 1 (altlocs ABCD on some residues) | 1 (altlocs ABCD on some residues) | 6, altlocs ABCDEF |
| Atoms (of which H) | 4 300 (1 990) | 4 391 (1 990) | 17 372 (7 722) |
| Waters, occupancy sum | 316, 309 | 407, 298 | 1 958, 687 |
| ANISOU records | 2 310 | 2 269 | 9 173 |

The entry's own header reports R-free 0.1172 and R-work 0.1099 on its own flags.

## What the model is

Six complete copies of the protein (altlocs A to F), each at occupancy 1/6, refined together against the working data
with riding hydrogens, anisotropic ADPs on every protein atom and on most waters, restraint weights wc 0.3 / wu 0.25,
and individual water occupancies. Every water is one atom: a lettered water belongs to one copy (its occupancy is
refined; the mean is 0.30), a water with a blank altloc is shared by all six (mean 0.93). Ligands and ions are single.
The ensemble is the deliverable; it is not merged back into one model.

The model came from the deposited file in 54 recorded steps (S0000 to S0053), 15 of them accepted. The accepted levers,
in order: anisotropic water ADPs; the six-copy split (a representation change, scored and recorded but not judged);
water picks at 4, 3, 3, 2.5, 2.5, 2.5 and 2.5σ on work-only difference maps; anisotropic water ADPs again; restraint
weights 0.3 / 0.25; 20-cycle convergence steps; altloc occupancies; and, last, waters in own-copy clashes moved to a
copy they clear.

The gate judged every change against a control, the parent refined with the same command and seeds, and accepted a
change only when R-free fell by at least 2σ of the run's noise floor with the gap and the geometry inside their bounds.
`refinement/steps.md` lists every step with its verdict and `refinement/score_history.txt` is the hash-chained record
the gate wrote.

## Caveats

- **The vault was read once, at S0011** (R-vault 0.0769 against R-free 0.0809, no leak signature). The 42 steps after it used no held-out reflections of any kind in a decision, and every map that placed a water excluded the free set, but the gains since S0011 have not yet been checked against the vault. That read is the operator's.
- **The gap is 0.0259**, against 0.0089 for the re-refined model and 0.0071 for the deposited model as scored: the six copies and the free water occupancies fit the work set better than the free set. The run's cap is 0.030. A reference six-copy ensemble of this entry built earlier with maps that may have included the free reflections scores 0.0676 / 0.0507 on these flags; its advantage over this model is entirely in its solvent, and that comparison is in the harness plan, not in this release.
- **Clashscore 7.7** against 5.3 re-refined and 4.3 deposited; 40 waters sit in own-copy clashes that no other copy can take. Rotamer outliers 1.54 % are just above the gate's 1.5 % cap and passed because the control had the same.
- Three mmtbx sub-reports (C-beta deviations, omega, Rama-Z) fail on a six-copy model; the geometry numbers above come from phenix.clashscore, rotalyze and ramalyze.

## Files

| Path | Content |
|---|---|
| `model/7KR0_S0053.pdb` | the released model, PDB, occupancies at four decimals, as the gate wrote it |
| `model/7KR0_S0053.cif` | the same model as mmCIF (gemmi conversion) |
| `model/7KR0_S0001.pdb` | the re-refined deposited model (S0001, the common recipe, the median of three seeds): the baseline of every comparison |
| `maps/7KR0_S0053_map_coeffs.mtz` | phenix.maps coefficients from the work reflections only: `2FOFCWT/PH2FOFCWT` and `FOFCWT/PHFOFCWT` |
| `data/7KR0_data.mtz`, `7KR0_flags.mtz`, `7KR0_split.mtz` | the working data, the inherited flags, the select/report split; the vault is absent from all three |
| `data/prep.json`, `split.json` | how the files were built, with checksums and counts |
| `deposited/7KR0.cif`, `rcsb_entry.json` | the deposited model and the RCSB entry record, as fetched |
| `refinement/score_history.txt`, `score_history.jsonl`, `scorecard.csv` | every step: the facts line, the full metrics, the scorecard row |
| `refinement/steps.md` | the step table |
| `refinement/S0053/` | the released step: facts line, change record, score record |
| `refinement/S0001/`, `S0000/` | the baseline step and the deposited model as scored: facts lines and score records (`S0000/rescored.json`: the same model scored again by the current scorer at release, for the geometry fields the scorer of 2026-10-14 did not write) |
| `refinement/metaparams.yaml`, `run.json` | the metaparameters of the run and its state (noise floor, standing recipe, the sealed vault's checksums) |
| `refinement/chains/` | the chain scripts that scheduled the steps on the pod, as run, with their logs |
| `validation/` | phenix.clashscore, rotalyze and ramalyze logs of the released model (`*_S0053.*`) and of the re-refined baseline (`*_S0001.*`) |

## Reproduce

In the harness checkout on the pod (`docs/POD.md` there):

```
bash tools/preprocessing.sh 7KR0 --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/Tff1b3f 6
```

The second command runs the lever order that produced this model without an agent; the chain scripts under `refinement/chains/` are the hand-scheduled originals. Seeds are fixed; the same inputs give the same trajectory.
