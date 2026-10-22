# 7R2H — 0.79A resolution structure of DMSO bound Cyclophilin D

> In development. Refined by an agent that was prompted to follow a procedure based on Passmore et al. (2026), with PDB 44PS as the reference model; see the [citation](../../README.md#citation).

**Status: improved.** The released model is a six-copy ensemble with an R-free of 0.0993 on the deposited free set. The re-refined deposited model (S0001, the common recipe) scores 0.1355 and the deposited model as scored (S0000) 0.1551 on the same reflections. The run continues; this is the model in force on 2026-10-21.

| | |
|---|---|
| Resolution | 0.79 Å |
| Space group | P 41 21 2 |
| Data | amplitudes (FP,SIGFP); 147 186 reflections in the working files, 139 648 work and 7 538 free |
| Free set | the deposition's own flags, inherited unchanged (5.12 %); select / report halves 3 769 / 3 769 |
| Vault | 2 000 work reflections (1 %) removed from every working file at preprocessing and sealed; not read in this run (the read is the operator's) |
| Deposited refinement program | PHENIX |
| Released by the PDB | 2023-02-15 |
| Primary citation | Structure-based design of pyrazole derivatives targeting the human Cyclophilin D binding site (Int.J.Biol.Macromol. 2026), DOI 10.1016/j.ijbiomac.2026.151496 |
| Harness | prism-science/agentic-refinement, branch `manzuoni/hierarchical_refinement`, commit bfed380 (merged into `main` as 7d62e84, 2026-10-21) |
| Run | handle Ta4f3f9, step S0019, 2026-10-21 04:20:51 UTC |
| Phenix | 2.1-6048 |
| Gate | ΔR-free ≤ −2σ against the control (σ = 0.00016 from three seeds), gap widened by at most 0.002, gap ≤ 0.0300 or not above the control's, clashscore ≤ 15, rotamer outliers ≤ 1.5 % or not above the control's |

## The three models on the same flags

All three are scored by the harness gate: a fresh cctbx fmodel on the working data with every reflection, no outlier
rejection. S0000 is the deposited model as anonymised at preprocessing; S0001 is that model after the common recipe
(phenix.refine, 10 macro-cycles, three seeds, the median), the baseline that every gain is measured against; the
release is the model in force. Geometry from phenix.clashscore (hydrogens kept), rotalyze and ramalyze; the
MolProbity score from those three.

| | Deposited as scored (S0000) | Re-refined (S0001) | This release (S0019) |
|---|---|---|---|
| R-free | 0.1551 | 0.1355 | **0.0993** |
| R-work | 0.1445 | 0.1243 | 0.0693 |
| Gap R-free − R-work | 0.0106 | 0.0112 | 0.0300 |
| R-free on the select / report halves | 0.1513 / 0.1589 | 0.1345 / 0.1365 | 0.0985 / 0.1001 |
| Clashscore (phenix.clashscore, hydrogens kept) | 0.0 | 4.3 | 7.8 |
| Rotamer outliers | 0.00 % | 0.00 % | 0.99 % |
| Ramachandran outliers / favoured | 0.0 % / 96.3 % | 0.0 % / 96.9 % | 0.0 % / 93.8 % |
| Bond RMSD / angle RMSD | 0.006 Å / 0.76° | 0.008 Å / 1.07° | 0.009 Å / 1.10° |
| MolProbity score | 0.75 | 1.40 | 1.84 |
| Copies | 1 (altlocs AB on some residues) | 1 (altlocs AB on some residues) | 6, altlocs ABCDEF |
| Atoms (of which H) | 2 850 (1 253) | 2 975 (1 253) | 16 461 (7 380) |
| Waters, occupancy sum | 335, 334 | 460, 324 | 1 637, 524 |
| ANISOU records | 1 258 | 1 258 | 8 890 |

The entry's own header reports R-free 0.1549 and R-work 0.1434 on its own flags.

## What the model is

Six complete copies of the protein (altlocs A to F), each at occupancy 1/6, refined together against the working
data with riding hydrogens, anisotropic ADPs on every protein atom and on most waters (191 of 1 637 isotropic),
restraint weights wc 0.3 / wu 0.25 and individual water occupancies. A lettered water belongs to one copy, a water with
a blank altloc to all six. The ligand is single. The ensemble is the deliverable; it is not merged back into one model.

The model came from the deposited file in 26 recorded steps (S0000 to S0025), 6 of them accepted and 1 build. The
lineage of S0019: restraint weights 0.3 / 0.25 (S0008); anisotropic water ADPs (S0012, −0.011); the six-copy split from
shake (S0014, a build, −0.010); water picks at 4σ three times (S0015, S0016, S0017) and at 2.5σ (S0019) on work-only
difference maps. The run continues: the water re-letter, the copy votes and a convergence step were running when this
snapshot was taken, with a fork under looser gap bounds queued after them.

The gate judged every change against a control, the parent refined with the same command and seeds, and accepted a
change only when R-free fell by at least 2σ of the run's noise floor with the gap and the geometry inside their bounds.
`refinement/steps.md` lists every step with its verdict and `refinement/score_history.txt` is the hash-chained record
the gate wrote.

## Caveats

- **The vault has not been read in this run** (2 000 work reflections, sealed at preprocessing; `run.json` carries the checksums). No decision used held-out reflections of any kind, and every map that placed an atom excluded the free set, but the gains have not been checked against the vault. That read is the operator's.
- **The gap is 0.0300**, at the run's cap of 0.030, against 0.0106 for the deposited model. The two picks after S0019 were refused on the gap rule (S0020, S0024); the queued fork loosens the bound for the operator to judge with the vault.
- Clashscore 7.8 against 0.0 for the deposited file (which carries its own hydrogens); rotamer outliers 1.0 % (deposited 0.0 %); no Ramachandran outlier, 93.8 % favoured.
- Six copies at 0.79 Å: 16 461 atoms against 2 850 deposited. The deposited model scores 0.1551 on our flags and 0.1355 after the common recipe (S0001); the header reports 0.1549 on its own flags.

## Files

| Path | Content |
|---|---|
| `model/7R2H_S0019.pdb` | the released model, PDB, occupancies at four decimals, as the gate wrote it |
| `model/7R2H_S0019.cif` | the same model as mmCIF (gemmi conversion) |
| `model/7R2H_S0001.pdb` | the re-refined deposited model (S0001, the common recipe, the median of three seeds): the baseline of every comparison |
| `maps/7R2H_S0019_map_coeffs.mtz` | phenix.maps coefficients from the work reflections only: `2FOFCWT/PH2FOFCWT` and `FOFCWT/PHFOFCWT` |
| `data/7R2H_data.mtz`, `7R2H_flags.mtz`, `7R2H_split.mtz` | the working data, the inherited flags, the select/report split; the vault is absent from all three |
| `data/prep.json`, `split.json` | how the files were built, with checksums and counts |
| `deposited/7R2H.cif`, `rcsb_entry.json` | the deposited model and the RCSB entry record, as fetched |
| `refinement/score_history.txt`, `score_history.jsonl`, `scorecard.csv` | every step: the facts line, the full metrics, the scorecard row |
| `refinement/steps.md` | the step table |
| `refinement/S0019/` | the released step: facts line, change record, score record |
| `refinement/S0001/`, `S0000/` | the baseline step and the deposited model as scored: facts lines and score records |
| `refinement/metaparams.yaml`, `run.json` | the metaparameters of the run and its state (noise floor, standing recipe, the sealed vault's checksums) |
| `refinement/chains/` | the chain scripts that scheduled the steps on the pod, as run, with their logs |
| `validation/` | phenix.clashscore, rotalyze and ramalyze logs of the released model (`*_S0019.*`) and of the re-refined baseline (`*_S0001.*`) |

## Reproduce

In the harness checkout on the pod (`docs/POD.md` there):

```
bash tools/preprocessing.sh 7R2H --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/Ta4f3f9 6
```

`chain_target.sh` is the one chain of this run; its log is `refinement/chains/chain_target_Ta4f3f9.log`.
