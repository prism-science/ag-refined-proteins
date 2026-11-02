# 1LZ8 — LYSOZYME PHASED ON ANOMALOUS SIGNAL OF SULFURS AND CHLORINES

> In development. Refined by an agent that was prompted to follow a procedure based on Passmore et al. (2026), with PDB 44PS as the reference model; see the [citation](../../README.md#citation).

**Status: lower R-free, not confirmed by the vault.** The released model is a two-conformer ensemble with an R-free of 0.2408 on the deposited free set. The re-refined deposited model (S0001, the common recipe) scores 0.2712 and the deposited model as scored (S0000) 0.2826 on the same reflections. The model is the release of 2026-10-21; the run has had no accepted step since. **The vault read of 2026-10-22 does not confirm the gain** (see Caveats).

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
| Harness | prism-science/agentic-refinement, branch `manzuoni/oct28-trials`, commit 25ec394 (pull request to `main` opened 2026-11-02); the models of 2026-10-21: branch `manzuoni/hierarchical_refinement`, commit bfed380 (merged into `main` as 7d62e84) |
| Run | handle Tee73c5, step S0073, 2026-10-20 07:22:22 UTC |
| Phenix | 2.1-6048 |
| Gate | ΔR-free ≤ −2σ against the control (σ = 0.00026 from three seeds), gap widened by at most 0.002, gap ≤ 0.0714 or not above the control's, clashscore ≤ 15, rotamer outliers ≤ 1.5 % or not above the control's |

## The three models on the same flags

All three are scored by the harness gate: a fresh cctbx fmodel on the working data with every reflection, no outlier
rejection. S0000 is the deposited model as anonymised at preprocessing; S0001 is that model after the common recipe
(phenix.refine, 10 macro-cycles, three seeds, the median), the baseline that every gain is measured against; the
release is the model in force. Geometry from phenix.clashscore (hydrogens kept), rotalyze and ramalyze; the
MolProbity score from those three.

| | Deposited as scored (S0000) | Re-refined (S0001) | This release (S0073) |
|---|---|---|---|
| R-free | 0.2826 | 0.2712 | **0.2408** |
| R-work | 0.2024 | 0.2048 | 0.1662 |
| Gap R-free − R-work | 0.0802 | 0.0664 | 0.0746 |
| R-free on the select / report halves | 0.2847 / 0.2803 | 0.2764 / 0.2659 | 0.2441 / 0.2375 |
| Clashscore (phenix.clashscore, hydrogens kept) | 5.1 | 4.1 | 1.3 |
| Rotamer outliers | 1.90 % | 1.90 % | 0.48 % |
| Ramachandran outliers / favoured | 0.0 % / 96.9 % | 0.0 % / 97.6 % | 0.0 % / 93.7 % |
| Bond RMSD / angle RMSD | 0.026 Å / 3.58° | 0.011 Å / 1.15° | 0.005 Å / 0.75° |
| MolProbity score | 1.68 | 1.48 | 1.27 |
| Conformers | 1 | 1 | 2, altlocs AB |
| Atoms (of which H) | 1 234 (0) | 1 221 (0) | 4 346 (1 916) |
| Waters, occupancy sum | 224, 224 | 211, 171 | 419, 257 |
| ANISOU records | 0 | 0 | 2 009 |

The entry's own header reports R-free 0.31 and R-work 0.22 on its own flags.

## What the model is

Two complete conformers of the protein (altlocs A and B), each at occupancy 1/2, from a qFit split of the single
model (S0035), refined together with riding hydrogens, restraint weights wc 2 / wu 2, TLS (one group) over an isotropic
residual (the total ADP written as ANISOU records), optimised bulk-solvent mask radii and isotropic waters. Two chloride
ions placed at difference peaks (S0073) are single and at occupancy 1. A lettered water belongs to one conformer, a blank one
to both.

The model came from the deposited file in 83 recorded steps (S0000 to S0082), 9 of them accepted and 3 builds. The
lineage of S0073: a convergence step (S0016); TLS, one group (S0020); a convergence step (S0032); the two-copy split
from qFit (S0035, a build); restraint weights 1 / 1 (S0053); the bulk-solvent mask radii optimised (S0060); a
convergence step (S0070); chloride ions at the two mFo−DFc peaks of 4σ and above that no atom explains, next to a
nitrogen (S0073; three waters removed). Restraint weights 2 / 2 were accepted on a sibling of the lineage (S0054) and
are in the standing recipe from there on.

The gate judged every change against a control, the parent refined with the same command and seeds, and accepted an
improving change only when R-free fell by at least 2σ of the run's noise floor with the gap and the geometry inside their
bounds. From 2026-10-27 the gate also holds the model checks of `docs/METHOD.md` (waters in protein density, conformer-B
outliers, residues in difference density, the tallest peak, Holton's wE) and accepts a repair: a change that lowers one
check with R-free not worse than 2σ against its control.
`refinement/steps.md` lists every step with its verdict and `refinement/score_history.txt` is the hash-chained record
the gate wrote.

## Caveats

- **The vault was read on 2026-10-22 at S0073** (the operator's read; 260 held-out work reflections): R-vault 0.2422 → 0.2517 from S0001 to that model, against R-free 0.2712 → 0.2408 on the deposited free set; the difference of the two changes is +2.5 σ of the sampling noise (σ 0.0158). **The vault does not confirm the gain: R-vault rose while R-free fell.** The free set is small, the gate's margin (two seed σ) is about 30 times smaller than the free set's own sampling noise of a paired change, and the run judged about 80 steps; the accepted gains are most likely fitted to the free set. The model is released as the record of the run, not as a confirmed improvement. No decision used held-out reflections of any kind, and every map that placed or moved an atom excluded the free set.
- **The gap is 0.0746**, above the run's cap of 0.0714; the step passed because the control's gap (0.0754) was higher. The gap was 0.0802 for the deposited model and 0.0864 at the split (S0035); it has narrowed since.
- Clashscore 1.3 against 5.1 deposited; rotamer outliers 0.48 % (one residue in one conformer); no Ramachandran outlier; 93.7 % favoured against 96.9 % for the deposited model.
- A six-conformer fork of this run (Tee73c5_six) reached R-free 0.2627 and did not beat the two-conformer model; a three-conformer build (S0079) and the levers after it did not beat S0073 either. Both stay in the record; neither is released.

## Files

| Path | Content |
|---|---|
| `model/1LZ8_S0073.pdb` | the released model, PDB, occupancies at four decimals, as the gate wrote it |
| `model/1LZ8_S0073.cif` | the same model as mmCIF (gemmi conversion) |
| `model/1LZ8_S0001.pdb` | the re-refined deposited model (S0001, the common recipe, the median of three seeds): the baseline of every comparison |
| `maps/1LZ8_S0073_map_coeffs.mtz` | phenix.maps coefficients from the work reflections only: `2FOFCWT/PH2FOFCWT` and `FOFCWT/PHFOFCWT` |
| `data/1LZ8_data.mtz`, `1LZ8_flags.mtz`, `1LZ8_split.mtz` | the working data, the inherited flags, the select/report split; the vault is absent from all three |
| `data/prep.json`, `split.json` | how the files were built, with checksums and counts |
| `deposited/1LZ8.cif`, `rcsb_entry.json` | the deposited model and the RCSB entry record, as fetched |
| `refinement/score_history.txt`, `score_history.jsonl`, `scorecard.csv` | every step: the facts line, the full metrics, the scorecard row |
| `refinement/steps.md` | the step table |
| `refinement/S0073/` | the released step: facts line, change record, score record |
| `refinement/S0001/`, `S0000/` | the baseline step and the deposited model as scored: facts lines and score records |
| `refinement/metaparams.yaml`, `run.json` | the metaparameters of the run and its state (noise floor, standing recipe, the sealed vault's checksums) |
| `refinement/chains/` | the chain scripts that scheduled the steps on the pod, as run, with their logs |
| `validation/` | phenix.clashscore, rotalyze and ramalyze logs of the released model (`*_S0073.*`) and of the re-refined baseline (`*_S0001.*`) |

## Reproduce

In the harness checkout on the pod (`docs/POD.md` there):

```
bash tools/preprocessing.sh 1LZ8 --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/Tee73c5 6
```

The chain scripts under `refinement/chains/` (chain_target, chain_tight, chain_weights, chain_ens, chain_qfit, chain_more, chain_coot, chain_anneal, chain_ions, chain_lz2) are the hand-scheduled originals with their logs; the levers whose logs have no script (`chain_occhet`, `chain_qfit3`, `chain_reference`, `chain_six3`) were scheduled from one-off scripts, and every command line is in the step's `change.json` on the pod.
