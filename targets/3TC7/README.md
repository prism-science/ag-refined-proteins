# 3TC7 — Crystal Structure of Engineered Protein. Northeast Structural Genomics Consortium Target OR62

**Status: improved.** The released model is a six-copy ensemble with an R-free of 0.1475 on the deposited free set.
The deposited model scores 0.1918 on the same reflections.

| | |
|---|---|
| Resolution | 1.5 Å |
| Space group | P 31 2 1 |
| Data | amplitudes (FP,SIGFP); 40 272 reflections in the working files, 38 197 work and 2 075 free |
| Free set | the deposition's own flags, inherited unchanged (5.15 %); select / report halves 1 038 / 1 037 |
| Vault | 780 work reflections (2 %) removed from every working file at preprocessing and sealed; not read in this run (the read is the operator's) |
| Deposited refinement program | PHENIX |
| Released by the PDB | 2011-08-24 |
| Primary citation | Exploration of alternate catalytic mechanisms and optimization strategies for retroaldolase design (J.Mol.Biol. 2014), DOI 10.1016/j.jmb.2013.10.012 |
| Harness | prism-science/autoresearch, branch `manzuoni/hierarchical_refinement`, commit bfed380 (merged into `main` as 7d62e84, 2026-10-21) |
| Run | handle T431c8e_gap, step S0061, 2026-10-21 01:52:30 UTC |
| Phenix | 2.1-6048 |
| Gate | ΔR-free ≤ −2σ against the control (σ = 0.00027 from three seeds), gap widened by at most 0.01, gap ≤ 0.1200 or not above the control's, clashscore ≤ 15, rotamer outliers ≤ 1.5 % or not above the control's |

## The two models on the same flags

Both models are scored by the harness gate: a fresh cctbx fmodel on the working data with every reflection, no outlier
rejection. The deposited model is scored as anonymised at preprocessing (S0000).

| | Deposited, our flags (S0000) | This release (S0061) |
|---|---|---|
| R-free | 0.1918 | **0.1475** |
| R-work | 0.1536 | 0.0806 |
| Gap R-free − R-work | 0.0382 | 0.0668 |
| R-free on the select / report halves | 0.1904 / 0.1932 | 0.1483 / 0.1466 |
| Clashscore (phenix.clashscore, hydrogens kept) | 2.9 | 6.8 |
| Rotamer outliers | 1.36 % | 2.74 % |
| Ramachandran outliers / favoured | 0.0 % / 98.0 % | 0.4 % / 97.2 % |
| Bond RMSD / angle RMSD | 0.008 Å / 1.08° | 0.015 Å / 1.40° |
| MolProbity score | 1.19 | 1.86 |
| Copies | 1 (altlocs AB on some residues) | 6, altlocs ABCDEF |
| Atoms (of which H) | 2 220 (0) | 25 909 (12 375) |
| Waters, occupancy sum | 180, 180 | 1 425, 697 |
| ANISOU records | 2 020 | 12 109 |

The entry's own header reports R-free 0.193 and R-work 0.158 on its own flags.

## What the model is

Six complete copies of the protein (altlocs A to F), each at occupancy 1/6, refined together against the working
data with riding hydrogens, restraint weights wc 0.3 / wu 0.25, TLS (one group for the protein) over an isotropic
residual on every protein atom (the total ADP is written as ANISOU records) and isotropic waters. Every water is one
atom: a lettered water belongs to one copy, a water with a blank altloc is shared by all six. The ensemble is the
deliverable; it is not merged back into one model.

The model came from the deposited file in 66 recorded steps (S0000 to S0065), 15 of them accepted and 2 builds, in two
runs: the main run T431c8e up to the six-copy split (S0032) and, from S0033 on, its fork T431c8e_gap with looser gap
bounds (one-step widening of at most 0.010 and a cap of 0.12, against 0.002 and 0.030 in the main run), made because
the 0.002 bound refused every solvent lever on the ensemble. The lineage of S0061: a convergence step (S0003); riding
hydrogens (S0005); a two-copy split from shake (S0013, a build); three convergence steps (S0016, S0018, S0020); the
six-copy split from shake (S0032, a build); restraint weights 1 / 1 (S0033); isotropic protein ADPs in place of
anisotropic ones (S0039, −0.008); water picks at 4, 4 and 3σ on work-only difference maps (S0043, S0046, S0050);
restraint weights 0.3 / 0.25 (S0061). TLS with one group was accepted on a sibling of the lineage (S0047) and is in the
standing recipe from there on.

The gate judged every change against a control, the parent refined with the same command and seeds, and accepted a
change only when R-free fell by at least 2σ of the run's noise floor with the gap and the geometry inside their bounds.
`refinement/steps.md` lists every step with its verdict and `refinement/score_history.txt` is the hash-chained record
the gate wrote.

## Caveats

- **The vault has not been read in this run** (780 work reflections, sealed at preprocessing; `run.json` carries the checksums). No decision used held-out reflections of any kind, and every map that placed an atom excluded the free set, but the gains have not been checked against the vault. That read is the operator's.
- **The gap is 0.0668** against 0.0382 for the deposited model and 0.0612 for the main run's best under the standing bounds (S0042, R-free 0.1540; its record is in `refinement/main_run_T431c8e/`). The fork's bounds let the gap widen by up to 0.010 in one step and cap it at 0.12; the operator judges the fork with the vault at the end.
- **Rotamer outliers 2.74 %** (36 of 1 314 residue copies) are above the gate's 1.5 % cap. The step passed because the count is within one outlier residue per copy of the control's (30), the tolerance rule of 2026-10-21. One Ramachandran outlier (0.4 %). Clashscore 6.8 against 2.9 deposited; the last step (weights 0.3 / 0.25) raised it from 2.8.
- Methionine as selenomethionine, with an anomalous group for Se (f' and f'' refined), was refused twice (S0038, S0042); the density at the SD sites is about a quarter of a selenium's. The residues stay MET.
- Six copies at 1.5 Å: the gate's control is the parent refined with the same seeds, so an accepted gain is relative to that control, not evidence that six copies are the right number for this entry. The two-copy model of the same run (S0020, R-free 0.1688) is in the record.

## Files

| Path | Content |
|---|---|
| `model/3TC7_S0061.pdb` | the released model, PDB, occupancies at four decimals, as the gate wrote it |
| `model/3TC7_S0061.cif` | the same model as mmCIF (gemmi conversion) |
| `maps/3TC7_S0061_map_coeffs.mtz` | phenix.maps coefficients from the work reflections only: `2FOFCWT/PH2FOFCWT` and `FOFCWT/PHFOFCWT` |
| `data/3TC7_data.mtz`, `3TC7_flags.mtz`, `3TC7_split.mtz` | the working data, the inherited flags, the select/report split; the vault is absent from all three |
| `data/prep.json`, `split.json` | how the files were built, with checksums and counts |
| `deposited/3TC7.cif`, `rcsb_entry.json` | the deposited model and the RCSB entry record, as fetched |
| `refinement/score_history.txt`, `score_history.jsonl`, `scorecard.csv` | every step: the facts line, the full metrics, the scorecard row |
| `refinement/steps.md` | the step table |
| `refinement/S0061/` | the released step: facts line, change record, score record |
| `refinement/metaparams.yaml`, `run.json` | the metaparameters of the run and its state (noise floor, standing recipe, the sealed vault's checksums) |
| `refinement/chains/` | the chain scripts that scheduled the steps on the pod, as run, with their logs |
| `validation/` | phenix.clashscore, rotalyze and ramalyze logs of the released model |
| `refinement/main_run_T431c8e/` | the main run's own record after the fork point (its best S0042, R-free 0.1540, under the standing gap bounds) |

## Reproduce

In the harness checkout on the pod (`docs/POD.md` there):

```
bash tools/preprocessing.sh 3TC7 --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/T431c8e 6          # to the six-copy split, S0032
bash scripts/fork_run.sh /home/dev/runs/hr/T431c8e /home/dev/runs/hr/T431c8e_gap
# set gap_widen_max 0.010 and gap_abs_max 0.12 in T431c8e_gap/metaparams.yaml, as scripts/fork_gap_after.sh does
bash scripts/chain_gap.sh /home/dev/runs/hr/T431c8e_gap 6
```

The levers whose logs are `chain_gb`, `chain_iso`, `chain_anisogb`, `chain_semet`, `chain_settle_r` and `chain_after_settle*` were scheduled from one-off scripts that are not in `scripts/`; their logs are included, and every command line of every step is in that step's `change.json` on the pod.
