# 4QO4 — co-crystal structure of MDM2 (17-111) with compound 16, {(3R,5R,6S)-5-(3-CHLOROPHENYL)-6-(4-CHLOROPHENYL)-1-[(1S)-1-(6-CYCLOPROPYLPYRIDIN-2-YL)PROPYL]-3-METHYL-2-OXOPIPERIDIN-3-YL}ACETIC ACID

> In development. Refined by an agent that was prompted to follow a procedure based on Passmore et al. (2026), with PDB 44PS as the reference model; see the [citation](../../README.md#citation).

**Status: improved.** The released model is a single model with an R-free of 0.2747 on the deposited free set. The re-refined deposited model (S0001, the common recipe) scores 0.3097 and the deposited model as scored (S0000) 0.3133 on the same reflections.

| | |
|---|---|
| Resolution | 1.7 Å |
| Space group | P 61 2 2 |
| Data | intensities (IMEAN,SIGIMEAN); 10 811 reflections in the working files, 10 283 work and 528 free |
| Free set | the deposition's own flags, inherited unchanged (4.88 %); select / report halves 264 / 264 |
| Vault | 200 work reflections (2 %) removed from every working file at preprocessing and sealed; not read in this run (the read is the operator's) |
| Deposited refinement program | CNS |
| Released by the PDB | 2014-07-16 |
| Primary citation | Discovery of Potent and Simplified Piperidinone-Based Inhibitors of the MDM2-p53 Interaction (ACS Med Chem Lett 2014), DOI 10.1021/ml500142b |
| Harness | prism-science/agentic-refinement, branch `manzuoni/hierarchical_refinement`, commit bfed380 (merged into `main` as 7d62e84, 2026-10-21) |
| Run | handle T40560e, step S0064, 2026-10-20 08:38:01 UTC |
| Phenix | 2.1-6048 |
| Gate | ΔR-free ≤ −2σ against the control (σ = 0.00056 from three seeds), gap widened by at most 0.002, gap ≤ 0.0704 or not above the control's, clashscore ≤ 15, rotamer outliers ≤ 1.5 % or not above the control's |

## The three models on the same flags

All three are scored by the harness gate: a fresh cctbx fmodel on the working data with every reflection, no outlier
rejection. S0000 is the deposited model as anonymised at preprocessing; S0001 is that model after the common recipe
(phenix.refine, 10 macro-cycles, three seeds, the median), the baseline that every gain is measured against; the
release is the model in force. Geometry from phenix.clashscore (hydrogens kept), rotalyze and ramalyze; the
MolProbity score from those three.

| | Deposited as scored (S0000) | Re-refined (S0001) | This release (S0064) |
|---|---|---|---|
| R-free | 0.3133 | 0.3097 | **0.2747** |
| R-work | 0.2631 | 0.2443 | 0.2229 |
| Gap R-free − R-work | 0.0502 | 0.0654 | 0.0518 |
| R-free on the select / report halves | 0.3368 / 0.2909 | 0.3591 / 0.2625 | 0.2874 / 0.2625 |
| Clashscore (phenix.clashscore, hydrogens kept) | 16.0 | 2.6 | 7.3 |
| Rotamer outliers | 6.02 % | 2.41 % | 3.53 % |
| Ramachandran outliers / favoured | 0.0 % / 97.6 % | 0.0 % / 98.8 % | 0.0 % / 95.6 % |
| Bond RMSD / angle RMSD | 0.011 Å / 1.62° | 0.011 Å / 1.30° | 0.016 Å / 1.63° |
| MolProbity score | 2.38 | 1.33 | 2.13 |
| Copies | 1 | 1 | 1 |
| Atoms (of which H) | 845 (0) | 844 (0) | 892 (0) |
| Waters, occupancy sum | 78, 78 | 77, 64 | 77, 65 |
| ANISOU records | 0 | 0 | 0 |

The entry's own header reports R-free 0.302 and R-work 0.264 on its own flags.

## What the model is

A single model, as deposited, refined with restraint weights wc 0.3 / wu 0.25 and individual isotropic ADPs,
without hydrogens, with sulfate ions placed at difference peaks (S0050) and the loop 69 to 72 of chain A built (S0064),
which the deposited model lacks.

The model came from the deposited file in 80 recorded steps (S0000 to S0079), 5 of them accepted and 2 builds. The
lineage of S0064: restraint weights 0.3 / 0.25 (S0009); a convergence step (S0017); sulfate ions at the mFo−DFc peaks
of 5σ and above that no atom explains, next to a nitrogen (S0050, −0.014); a convergence step (S0052); residues 69 to
72 of chain A built by phenix.fit_loops into the work-only 2mFo−DFc map, their rotamers fitted by Coot, one side chain
with a map correlation under 0.3 cut to CB (S0064, −0.009).

The gate judged every change against a control, the parent refined with the same command and seeds, and accepted a
change only when R-free fell by at least 2σ of the run's noise floor with the gap and the geometry inside their bounds.
`refinement/steps.md` lists every step with its verdict and `refinement/score_history.txt` is the hash-chained record
the gate wrote.

## Caveats

- **The vault has not been read in this run** (200 work reflections, sealed at preprocessing; `run.json` carries the checksums). No decision used held-out reflections of any kind, and every map that placed an atom excluded the free set, but the gains have not been checked against the vault. That read is the operator's.
- **Rotamer outliers 3.5 %** (three residues) are above the gate's 1.5 % cap; the step passed because the control had the same three. The deposited model has 6.0 %. Clashscore 7.3 against 16.0 deposited; no Ramachandran outlier, 95.6 % favoured.
- **The gain since the baseline is on the select half only.** R-free on the select / report halves is 0.3592 / 0.2625 at S0001 and 0.2874 / 0.2625 at S0064, with 264 reflections in each half; the re-refinement had moved them the other way (0.3368 / 0.2909 at S0000). Halves this small are noisy, and the vault read is the check.
- The gap is 0.0518 against 0.0654 for the re-refined model and 0.0502 for the deposited model as scored (the run's cap 0.0704).
- The model has no hydrogens: riding hydrogens were refused in this run. Reference-model restraints (S0075 and the later re-test) were refused; a two-copy qFit build (S0069) and a six-copy fork (T40560e_six, R-free 0.3042) did not beat the single model. None of these is released.

## Files

| Path | Content |
|---|---|
| `model/4QO4_S0064.pdb` | the released model, PDB, occupancies at four decimals, as the gate wrote it |
| `model/4QO4_S0064.cif` | the same model as mmCIF (gemmi conversion) |
| `model/4QO4_S0001.pdb` | the re-refined deposited model (S0001, the common recipe, the median of three seeds): the baseline of every comparison |
| `maps/4QO4_S0064_map_coeffs.mtz` | phenix.maps coefficients from the work reflections only: `2FOFCWT/PH2FOFCWT` and `FOFCWT/PHFOFCWT` |
| `data/4QO4_data.mtz`, `4QO4_flags.mtz`, `4QO4_split.mtz` | the working data, the inherited flags, the select/report split; the vault is absent from all three |
| `data/prep.json`, `split.json` | how the files were built, with checksums and counts |
| `deposited/4QO4.cif`, `rcsb_entry.json` | the deposited model and the RCSB entry record, as fetched |
| `refinement/score_history.txt`, `score_history.jsonl`, `scorecard.csv` | every step: the facts line, the full metrics, the scorecard row |
| `refinement/steps.md` | the step table |
| `refinement/S0064/` | the released step: facts line, change record, score record |
| `refinement/S0001/`, `S0000/` | the baseline step and the deposited model as scored: facts lines and score records |
| `refinement/metaparams.yaml`, `run.json` | the metaparameters of the run and its state (noise floor, standing recipe, the sealed vault's checksums) |
| `refinement/chains/` | the chain scripts that scheduled the steps on the pod, as run, with their logs |
| `validation/` | phenix.clashscore, rotalyze and ramalyze logs of the released model (`*_S0064.*`) and of the re-refined baseline (`*_S0001.*`) |

## Reproduce

In the harness checkout on the pod (`docs/POD.md` there):

```
bash tools/preprocessing.sh 4QO4 --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/T40560e 6
bash scripts/chain_ions.sh /home/dev/runs/hr/T40560e 6
bash scripts/chain_loop.sh /home/dev/runs/hr/T40560e 6
```

The levers whose logs have no script in `refinement/chains/` (`chain_loop2`, `chain_loop3`, `chain_occhet`, `chain_qfit2`, `chain_reference*`, `chain_zones`) were scheduled from one-off scripts; every command line is in the step's `change.json` on the pod.
