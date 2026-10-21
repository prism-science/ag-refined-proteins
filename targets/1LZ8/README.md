# 1LZ8 — LYSOZYME PHASED ON ANOMALOUS SIGNAL OF SULFURS AND CHLORINES

**Status: improved.** The released model is a two-copy ensemble with an R-free of 0.2408 on the deposited free set.
The deposited model scores 0.2826 on the same reflections.

| | |
|---|---|
| Resolution | 1.53 Å |
| Space group | P 43 21 2 |
| Data | amplitudes (FP,SIGFP); 13 004 reflections in the working files, 12 348 work and 656 free |
| Free set | the deposition's own flags, inherited unchanged (5.04 %); select / report halves 328 / 328 |
| Vault | 260 work reflections (2 %) removed from every working file at preprocessing and sealed; not read in this run (the read is the operator's) |
| Deposited refinement program | REFMAC |
| Released by the PDB | 1999-05-26 |
| Primary citation | Can anomalous signal of sulfur become a tool for solving protein crystal structures? (J.Mol.Biol. 1999), DOI 10.1006/jmbi.1999.2743 |
| Harness | prism-science/autoresearch, branch `manzuoni/hierarchical_refinement`, commit bfed380 (merged into `main` as 7d62e84, 2026-10-21) |
| Run | handle Tee73c5, step S0073, 2026-10-20 07:22:22 UTC |
| Phenix | 2.1-6048 |
| Gate | ΔR-free ≤ −2σ against the control (σ = 0.00026 from three seeds), gap widened by at most 0.002, gap ≤ 0.0714 or not above the control's, clashscore ≤ 15, rotamer outliers ≤ 1.5 % or not above the control's |

## The two models on the same flags

Both models are scored by the harness gate: a fresh cctbx fmodel on the working data with every reflection, no outlier
rejection. The deposited model is scored as anonymised at preprocessing (S0000).

| | Deposited, our flags (S0000) | This release (S0073) |
|---|---|---|
| R-free | 0.2826 | **0.2408** |
| R-work | 0.2024 | 0.1662 |
| Gap R-free − R-work | 0.0802 | 0.0746 |
| R-free on the select / report halves | 0.2847 / 0.2803 | 0.2441 / 0.2375 |
| Clashscore (phenix.clashscore, hydrogens kept) | 5.1 | 1.3 |
| Rotamer outliers | 1.90 % | 0.48 % |
| Ramachandran outliers / favoured | 0.0 % / 96.9 % | 0.0 % / 93.7 % |
| Bond RMSD / angle RMSD | 0.026 Å / 3.58° | 0.005 Å / 0.75° |
| MolProbity score | 1.68 | 1.27 |
| Copies | 1 | 2, altlocs AB |
| Atoms (of which H) | 1 234 (0) | 4 346 (1 916) |
| Waters, occupancy sum | 224, 224 | 419, 257 |
| ANISOU records | 0 | 2 009 |

The entry's own header reports R-free 0.31 and R-work 0.22 on its own flags.

## What the model is

Two complete copies of the protein (altlocs A and B), each at occupancy 1/2, from a qFit split of the single
model (S0035), refined together with riding hydrogens, restraint weights wc 2 / wu 2, TLS (one group) over an isotropic
residual (the total ADP written as ANISOU records), optimised bulk-solvent mask radii and isotropic waters. Two chloride
ions placed at difference peaks (S0073) are single and at occupancy 1. A lettered water belongs to one copy, a blank one
to both.

The model came from the deposited file in 83 recorded steps (S0000 to S0082), 9 of them accepted and 3 builds. The
lineage of S0073: a convergence step (S0016); TLS, one group (S0020); a convergence step (S0032); the two-copy split
from qFit (S0035, a build); restraint weights 1 / 1 (S0053); the bulk-solvent mask radii optimised (S0060); a
convergence step (S0070); chloride ions at the two mFo−DFc peaks of 4σ and above that no atom explains, next to a
nitrogen (S0073; three waters removed). Restraint weights 2 / 2 were accepted on a sibling of the lineage (S0054) and
are in the standing recipe from there on.

The gate judged every change against a control, the parent refined with the same command and seeds, and accepted a
change only when R-free fell by at least 2σ of the run's noise floor with the gap and the geometry inside their bounds.
`refinement/steps.md` lists every step with its verdict and `refinement/score_history.txt` is the hash-chained record
the gate wrote.

## Caveats

- **The vault has not been read in this run** (260 work reflections, sealed at preprocessing; `run.json` carries the checksums). No decision used held-out reflections of any kind, and every map that placed an atom excluded the free set, but the gains have not been checked against the vault. That read is the operator's.
- **The gap is 0.0746**, above the run's cap of 0.0714; the step passed because the control's gap (0.0754) was higher. The gap was 0.0802 for the deposited model and 0.0864 at the split (S0035); it has narrowed since.
- Clashscore 1.3 against 5.1 deposited; rotamer outliers 0.48 % (one residue copy); no Ramachandran outlier; 93.7 % favoured against 96.9 % for the deposited model.
- A six-copy fork of this run (Tee73c5_six) reached R-free 0.2627 and did not beat the two-copy model; a three-copy build (S0079) and the levers after it did not beat S0073 either. Both stay in the record; neither is released.

## Files

| Path | Content |
|---|---|
| `model/1LZ8_S0073.pdb` | the released model, PDB, occupancies at four decimals, as the gate wrote it |
| `model/1LZ8_S0073.cif` | the same model as mmCIF (gemmi conversion) |
| `maps/1LZ8_S0073_map_coeffs.mtz` | phenix.maps coefficients from the work reflections only: `2FOFCWT/PH2FOFCWT` and `FOFCWT/PHFOFCWT` |
| `data/1LZ8_data.mtz`, `1LZ8_flags.mtz`, `1LZ8_split.mtz` | the working data, the inherited flags, the select/report split; the vault is absent from all three |
| `data/prep.json`, `split.json` | how the files were built, with checksums and counts |
| `deposited/1LZ8.cif`, `rcsb_entry.json` | the deposited model and the RCSB entry record, as fetched |
| `refinement/score_history.txt`, `score_history.jsonl`, `scorecard.csv` | every step: the facts line, the full metrics, the scorecard row |
| `refinement/steps.md` | the step table |
| `refinement/S0073/` | the released step: facts line, change record, score record |
| `refinement/metaparams.yaml`, `run.json` | the metaparameters of the run and its state (noise floor, standing recipe, the sealed vault's checksums) |
| `refinement/chains/` | the chain scripts that scheduled the steps on the pod, as run, with their logs |
| `validation/` | phenix.clashscore, rotalyze and ramalyze logs of the released model |

## Reproduce

In the harness checkout on the pod (`docs/POD.md` there):

```
bash tools/preprocessing.sh 1LZ8 --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/Tee73c5 6
```

The chain scripts under `refinement/chains/` (chain_target, chain_tight, chain_weights, chain_ens, chain_qfit, chain_more, chain_coot, chain_anneal, chain_ions, chain_lz2) are the hand-scheduled originals with their logs; the levers whose logs have no script (`chain_occhet`, `chain_qfit3`, `chain_reference`, `chain_six3`) were scheduled from one-off scripts, and every command line is in the step's `change.json` on the pod.
