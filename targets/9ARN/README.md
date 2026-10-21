# 9ARN — Structure and interactions of HIV-1 gp41 CHR-NHR reverse hairpin constructs reveal molecular determinants of antiviral activity

**Status: improved.** The released model is a single model with an R-free of 0.2769 on the deposited free set. The re-refined deposited model (S0001, the common recipe) scores 0.2970 and the deposited model as scored (S0000) 0.2944 on the same reflections.

| | |
|---|---|
| Resolution | 1.41 Å |
| Space group | H 3 2 |
| Data | intensities (IMEAN,SIGIMEAN); 15 310 reflections in the working files, 14 538 work and 772 free |
| Free set | the deposition's own flags, inherited unchanged (5.01 %); select / report halves 384 / 388 |
| Vault | 360 work reflections (2 %) removed from every working file at preprocessing and sealed; not read in this run (the read is the operator's) |
| Deposited refinement program | PHENIX |
| Released by the PDB | 2025-03-05 |
| Primary citation | Structure and Interactions of HIV-1 gp41 CHR-NHR Reverse Hairpin Constructs Reveal Molecular Determinants of Antiviral Activity (J.Mol.Biol. 2024), DOI 10.1016/j.jmb.2024.168650 |
| Harness | prism-science/autoresearch, branch `manzuoni/hierarchical_refinement`, commit bfed380 (merged into `main` as 7d62e84, 2026-10-21) |
| Run | handle Tba97f6, step S0062, 2026-10-20 02:10:55 UTC |
| Phenix | 2.1-6048 |
| Gate | ΔR-free ≤ −2σ against the control (σ = 0.00093 from three seeds), gap widened by at most 0.002, gap ≤ 0.0674 or not above the control's, clashscore ≤ 15, rotamer outliers ≤ 1.5 % or not above the control's |

## The three models on the same flags

All three are scored by the harness gate: a fresh cctbx fmodel on the working data with every reflection, no outlier
rejection. S0000 is the deposited model as anonymised at preprocessing; S0001 is that model after the common recipe
(phenix.refine, 10 macro-cycles, three seeds, the median), the baseline that every gain is measured against; the
release is the model in force. Geometry from phenix.clashscore (hydrogens kept), rotalyze and ramalyze; the
MolProbity score from those three.

| | Deposited as scored (S0000) | Re-refined (S0001) | This release (S0062) |
|---|---|---|---|
| R-free | 0.2944 | 0.2970 | **0.2769** |
| R-work | 0.2542 | 0.2346 | 0.2389 |
| Gap R-free − R-work | 0.0402 | 0.0624 | 0.0380 |
| R-free on the select / report halves | 0.2947 / 0.2941 | 0.2777 / 0.3157 | 0.2680 / 0.2856 |
| Clashscore (phenix.clashscore, hydrogens kept) | 1.6 | 3.2 | 1.6 |
| Rotamer outliers | 0.00 % | 3.03 % | 0.00 % |
| Ramachandran outliers / favoured | 0.0 % / 100.0 % | 0.0 % / 100.0 % | 0.0 % / 100.0 % |
| Bond RMSD / angle RMSD | 0.006 Å / 0.73° | 0.010 Å / 1.03° | 0.004 Å / 0.52° |
| MolProbity score | 0.91 | 1.48 | 0.91 |
| Copies | 1 (altlocs AB on some residues) | 1 (altlocs AB on some residues) | 1 (altlocs AB on some residues) |
| Atoms (of which H) | 654 (0) | 673 (0) | 654 (0) |
| Waters, occupancy sum | 38, 36 | 57, 51 | 38, 36 |
| ANISOU records | 611 | 611 | 649 |

The entry's own header reports R-free 0.2912 and R-work 0.2555 on its own flags.

## What the model is

A single model with the deposited alternate conformations (altlocs A and B on some residues), refined with
restraint weights wc 2 / wu 2, secondary-structure and Ramachandran restraints, anisotropic ADPs on the protein and the
waters, and TLS in two groups (phenix.find_tls_groups). No hydrogens; 38 waters.

The model came from the deposited file in 75 recorded steps (S0000 to S0074), 9 of them accepted and 2 builds. The
re-refinement with the common recipe (S0001) scored above the deposited model (0.2970 against 0.2944), so the levers
were applied to S0000. The lineage of S0062: secondary-structure and Ramachandran restraints (S0056); anisotropic water
ADPs (S0060); TLS, two groups (S0062, −0.010). Restraint weights 2 / 2 (S0049) were accepted on another branch and are
in the standing recipe.

The gate judged every change against a control, the parent refined with the same command and seeds, and accepted a
change only when R-free fell by at least 2σ of the run's noise floor with the gap and the geometry inside their bounds.
`refinement/steps.md` lists every step with its verdict and `refinement/score_history.txt` is the hash-chained record
the gate wrote.

## Caveats

- **The vault has not been read in this run** (360 work reflections, sealed at preprocessing; `run.json` carries the checksums). No decision used held-out reflections of any kind, and every map that placed an atom excluded the free set, but the gains have not been checked against the vault. That read is the operator's.
- The gap is 0.0380 against 0.0402 for the deposited model. Clashscore 1.6 (deposited 1.6), no rotamer outlier, no Ramachandran outlier, 100 % favoured.
- A run of the same entry with the data cut at 1.85 Å (handle Tf7cc84, `d_min_cut` 1.85) reached R-free 0.2598 at its S0002 with the same TLS lever. Its numbers are on a different reflection set and are not comparable with this card; it is not released. The entry's header reports 1.41 Å.
- A six-copy fork of this run (Tba97f6_six, R-free 0.2853) did not beat the single model and is not released. The sulfate pick (S0071), the mask, annealing, isotropic protein ADPs and the water picks were refused after S0062.

## Files

| Path | Content |
|---|---|
| `model/9ARN_S0062.pdb` | the released model, PDB, occupancies at four decimals, as the gate wrote it |
| `model/9ARN_S0062.cif` | the same model as mmCIF (gemmi conversion) |
| `model/9ARN_S0001.pdb` | the re-refined deposited model (S0001, the common recipe, the median of three seeds): the baseline of every comparison |
| `maps/9ARN_S0062_map_coeffs.mtz` | phenix.maps coefficients from the work reflections only: `2FOFCWT/PH2FOFCWT` and `FOFCWT/PHFOFCWT` |
| `data/9ARN_data.mtz`, `9ARN_flags.mtz`, `9ARN_split.mtz` | the working data, the inherited flags, the select/report split; the vault is absent from all three |
| `data/prep.json`, `split.json` | how the files were built, with checksums and counts |
| `deposited/9ARN.cif`, `rcsb_entry.json` | the deposited model and the RCSB entry record, as fetched |
| `refinement/score_history.txt`, `score_history.jsonl`, `scorecard.csv` | every step: the facts line, the full metrics, the scorecard row |
| `refinement/steps.md` | the step table |
| `refinement/S0062/` | the released step: facts line, change record, score record |
| `refinement/S0001/`, `S0000/` | the baseline step and the deposited model as scored: facts lines and score records |
| `refinement/metaparams.yaml`, `run.json` | the metaparameters of the run and its state (noise floor, standing recipe, the sealed vault's checksums) |
| `refinement/chains/` | the chain scripts that scheduled the steps on the pod, as run, with their logs |
| `validation/` | phenix.clashscore, rotalyze and ramalyze logs of the released model (`*_S0062.*`) and of the re-refined baseline (`*_S0001.*`) |

## Reproduce

In the harness checkout on the pod (`docs/POD.md` there):

```
bash tools/preprocessing.sh 9ARN --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/Tba97f6 6
bash scripts/chain_tls.sh /home/dev/runs/hr/Tba97f6 6
```

The chain scripts under `refinement/chains/` (chain_target, chain_tls, chain_arn2, chain_arn3, chain_coot, chain_ions, chain_more, chain_noise, chain_qfit) are the hand-scheduled originals with their logs; `chain_after_rota` and `followup` were one-off scripts, and every command line is in the step's `change.json` on the pod.
