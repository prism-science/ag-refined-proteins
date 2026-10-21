# 3QUE — Human p38 MAP Kinase in Complex with Skepinone-L

**Status: improved.** The released model is a single model with an R-free of 0.2642 on the deposited free set.
The deposited model scores 0.2901 on the same reflections.

| | |
|---|---|
| Resolution | 2.7 Å |
| Space group | P 21 21 21 |
| Data | amplitudes (FP,SIGFP); 10 593 reflections in the working files, 9 729 work and 864 free |
| Free set | the deposition's own flags, inherited unchanged (8.16 %); select / report halves 432 / 432 |
| Vault | 200 work reflections (2 %) removed from every working file at preprocessing and sealed; not read in this run (the read is the operator's) |
| Deposited refinement program | REFMAC |
| Released by the PDB | 2012-01-18 |
| Primary citation | Skepinone-L is a selective p38 mitogen-activated protein kinase inhibitor (Nat.Chem.Biol. 2012), DOI 10.1038/nchembio.761 |
| Harness | prism-science/autoresearch, branch `manzuoni/hierarchical_refinement`, commit bfed380 (merged into `main` as 7d62e84, 2026-10-21) |
| Run | handle T9884ae, step S0057, 2026-10-21 03:58:49 UTC |
| Phenix | 2.1-6048 |
| Gate | ΔR-free ≤ −2σ against the control (σ = 0.00080 from three seeds), gap widened by at most 0.002, gap ≤ 0.1008 or not above the control's, clashscore ≤ 15, rotamer outliers ≤ 1.5 % or not above the control's |

## The two models on the same flags

Both models are scored by the harness gate: a fresh cctbx fmodel on the working data with every reflection, no outlier
rejection. The deposited model is scored as anonymised at preprocessing (S0000).

| | Deposited, our flags (S0000) | This release (S0057) |
|---|---|---|
| R-free | 0.2901 | **0.2642** |
| R-work | 0.2231 | 0.2124 |
| Gap R-free − R-work | 0.0670 | 0.0518 |
| R-free on the select / report halves | 0.2919 / 0.2883 | 0.2702 / 0.2585 |
| Clashscore (phenix.clashscore, hydrogens kept) | 10.6 | 6.3 |
| Rotamer outliers | 7.59 % | 3.63 % |
| Ramachandran outliers / favoured | 0.3 % / 95.0 % | 0.3 % / 96.8 % |
| Bond RMSD / angle RMSD | 0.016 Å / 1.72° | 0.006 Å / 1.26° |
| MolProbity score | 2.56 | 1.98 |
| Copies | 1 | 1 |
| Atoms (of which H) | 2 849 (0) | 2 896 (0) |
| Waters, occupancy sum | 14, 14 | 61, 60 |
| ANISOU records | 0 | 2 764 |

The entry's own header reports R-free 0.3109 and R-work 0.2225 on its own flags.

## What the model is

A single model refined with restraint weights wc 2 / wu 2, TLS in three groups (phenix.find_tls_groups) over an
isotropic residual (the total ADP written as ANISOU records), secondary-structure and Ramachandran restraints, and
reference-model torsion restraints to PDB 3LFF, the same kinase at higher resolution (phenix reference_model, sigma 1.0,
limit 15, the sequences aligned by phenix; the file is `refinement/S0057/reference_model_3LFF.pdb`). No hydrogens;
61 isotropic waters.

The model came from the deposited file in 71 recorded steps (S0000 to S0070), 5 of them accepted and 1 build. The
lineage of S0057: TLS, three groups (S0027); restraint weights 2 / 2 (S0034); Coot auto-fit of the rotamer outliers
(S0041); secondary-structure and Ramachandran restraints (S0052); the reference-model restraints (S0057: R-free
0.2685 → 0.2642, R-work 0.1963 → 0.2124, rotamer outliers 8.2 → 3.6 %).

The gate judged every change against a control, the parent refined with the same command and seeds, and accepted a
change only when R-free fell by at least 2σ of the run's noise floor with the gap and the geometry inside their bounds.
`refinement/steps.md` lists every step with its verdict and `refinement/score_history.txt` is the hash-chained record
the gate wrote.

## Caveats

- **The vault has not been read in this run** (200 work reflections, sealed at preprocessing; `run.json` carries the checksums). No decision used held-out reflections of any kind, and every map that placed an atom excluded the free set, but the gains have not been checked against the vault. That read is the operator's.
- **The reference-model restraints pull the torsions toward 3LFF.** R-work rose by 0.016 while R-free fell by 0.004, so the gap closed from 0.072 to 0.052; the side-chain conformations of this model are not independent evidence. The restraint file and its options are in the step's record.
- **Rotamer outliers 3.6 %** (11 residues) are above the gate's 1.5 % cap; the step passed because the control had 25. One Ramachandran outlier (0.3 %, as in the deposited model), 96.8 % favoured against 95.0 %. Clashscore 6.3 against 10.6 deposited.
- At 2.7 Å the picks, the hydrogens, the mask and the weight re-tests were all refused after S0057. A six-copy fork of this run (T9884ae_six) was still converging at R-free 0.2834 when this snapshot was taken; it is not released.

## Files

| Path | Content |
|---|---|
| `model/3QUE_S0057.pdb` | the released model, PDB, occupancies at four decimals, as the gate wrote it |
| `model/3QUE_S0057.cif` | the same model as mmCIF (gemmi conversion) |
| `maps/3QUE_S0057_map_coeffs.mtz` | phenix.maps coefficients from the work reflections only: `2FOFCWT/PH2FOFCWT` and `FOFCWT/PHFOFCWT` |
| `data/3QUE_data.mtz`, `3QUE_flags.mtz`, `3QUE_split.mtz` | the working data, the inherited flags, the select/report split; the vault is absent from all three |
| `data/prep.json`, `split.json` | how the files were built, with checksums and counts |
| `deposited/3QUE.cif`, `rcsb_entry.json` | the deposited model and the RCSB entry record, as fetched |
| `refinement/score_history.txt`, `score_history.jsonl`, `scorecard.csv` | every step: the facts line, the full metrics, the scorecard row |
| `refinement/steps.md` | the step table |
| `refinement/S0057/` | the released step: facts line, change record, score record |
| `refinement/metaparams.yaml`, `run.json` | the metaparameters of the run and its state (noise floor, standing recipe, the sealed vault's checksums) |
| `refinement/chains/` | the chain scripts that scheduled the steps on the pod, as run, with their logs |
| `validation/` | phenix.clashscore, rotalyze and ramalyze logs of the released model |
| `refinement/S0057/reference_model_3LFF.pdb` | the reference model of the torsion restraints (PDB 3LFF as fetched) |

## Reproduce

In the harness checkout on the pod (`docs/POD.md` there):

```
bash tools/preprocessing.sh 3QUE --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/T9884ae 6
bash scripts/chain_lowres.sh /home/dev/runs/hr/T9884ae 6
bash scripts/chain_que2.sh /home/dev/runs/hr/T9884ae 6
bash scripts/chain_que3.sh /home/dev/runs/hr/T9884ae 6
```

The reference lever itself (`chain_reference_T9884ae.log`) and the levers whose logs have no script (`chain_after_mask`, `chain_after_tls`, `chain_occhet`, `chain_wref`) were scheduled from one-off scripts; every command line is in the step's `change.json` on the pod.
