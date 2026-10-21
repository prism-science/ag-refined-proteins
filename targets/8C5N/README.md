# 8C5N — Sub-atomic resolution structure of the chitin-binding protein D (CbpD) from Pseudomonas aeruginosa

**Status: improved.** The released model is a six-copy ensemble with an R-free of 0.0908 on the deposited free set. The re-refined deposited model (S0001, the common recipe) scores 0.1294 and the deposited model as scored (S0000) 0.1571 on the same reflections. The run continues; this is the model in force on 2026-10-21.

| | |
|---|---|
| Resolution | 0.75 Å |
| Space group | P 1 21 1 |
| Data | intensities (IMEAN,SIGIMEAN); 195 643 reflections in the working files, 185 719 work and 9 924 free |
| Free set | the deposition's own flags, inherited unchanged (5.07 %); select / report halves 4 960 / 4 964 |
| Vault | 2 000 work reflections (1 %) removed from every working file at preprocessing and sealed; not read in this run (the read is the operator's) |
| Deposited refinement program | SHELXL, PHENIX |
| Released by the PDB | 2023-06-28 |
| Primary citation | Immunization with lytic polysaccharide monooxygenase CbpD induces protective immunity against Pseudomonas aeruginosa pneumonia (Proc.Natl.Acad.Sci.USA 2023), DOI 10.1073/pnas.2301538120 |
| Harness | prism-science/autoresearch, branch `manzuoni/hierarchical_refinement`, commit bfed380 (merged into `main` as 7d62e84, 2026-10-21) |
| Run | handle T5f59f1, step S0027, 2026-10-21 14:13:07 UTC |
| Phenix | 2.1-6048 |
| Gate | ΔR-free ≤ −2σ against the control (σ = 0.00046 from three seeds), gap widened by at most 0.002, gap ≤ 0.0300 or not above the control's, clashscore ≤ 15, rotamer outliers ≤ 1.5 % or not above the control's |

## The three models on the same flags

All three are scored by the harness gate: a fresh cctbx fmodel on the working data with every reflection, no outlier
rejection. S0000 is the deposited model as anonymised at preprocessing; S0001 is that model after the common recipe
(phenix.refine, 10 macro-cycles, three seeds, the median), the baseline that every gain is measured against; the
release is the model in force. Geometry from phenix.clashscore (hydrogens kept), rotalyze and ramalyze; the
MolProbity score from those three.

| | Deposited as scored (S0000) | Re-refined (S0001) | This release (S0027) |
|---|---|---|---|
| R-free | 0.1571 | 0.1294 | **0.0908** |
| R-work | 0.1480 | 0.1247 | 0.0675 |
| Gap R-free − R-work | 0.0092 | 0.0046 | 0.0233 |
| R-free on the select / report halves | 0.1561 / 0.1582 | 0.1302 / 0.1286 | 0.0907 / 0.0910 |
| Clashscore (phenix.clashscore, hydrogens kept) | 7.0 | 4.8 | 8.8 |
| Rotamer outliers | 2.34 % | 1.75 % | 1.26 % |
| Ramachandran outliers / favoured | 0.0 % / 99.5 % | 0.0 % / 99.5 % | 0.0 % / 98.4 % |
| Bond RMSD / angle RMSD | 0.013 Å / 1.58° | 0.007 Å / 1.00° | 0.010 Å / 1.19° |
| MolProbity score | 1.67 | 1.44 | 1.55 |
| Copies | 1 (altlocs ABC on some residues) | 1 (altlocs ABC on some residues) | 6, altlocs ABCDEF |
| Atoms (of which H) | 2 433 (665) | 2 676 (665) | 17 842 (7 932) |
| Waters, occupancy sum | 161, 161 | 404, 253 | 1 443, 472 |
| ANISOU records | 1 768 | 1 763 | 9 910 |

The entry's own header reports R-free 0.1634 and R-work 0.1537 on its own flags.

## What the model is

Six complete copies of the protein (altlocs A to F), each at occupancy 1/6, refined together against the working
data with riding hydrogens, anisotropic ADPs on every protein atom and every water (1 443), restraint weights wc 0.3 /
wu 0.25 and individual water occupancies. A lettered water belongs to one copy, a water with a blank altloc to all six.
Ligands and ions are single. The ensemble is the deliverable; it is not merged back into one model.

The model came from the deposited file in 29 recorded steps (S0000 to S0028), 7 of them accepted and 1 build. The
lineage of S0027: restraint weights 0.3 / 0.25 (S0008); anisotropic water ADPs (S0012, −0.006); the six-copy split from
shake (S0014, a build, −0.017); water picks at 4, 4 and 3σ on work-only difference maps (S0015, S0016, S0018);
anisotropic water ADPs again (S0021); waters in own-copy clashes moved to a copy they clear (S0027: 17 of 36 clashing
waters re-lettered, nothing deleted). The run continues: a convergence step was running when this snapshot was taken,
with a fork under looser gap bounds queued after it.

The gate judged every change against a control, the parent refined with the same command and seeds, and accepted a
change only when R-free fell by at least 2σ of the run's noise floor with the gap and the geometry inside their bounds.
`refinement/steps.md` lists every step with its verdict and `refinement/score_history.txt` is the hash-chained record
the gate wrote.

## Caveats

- **The vault has not been read in this run** (2 000 work reflections, sealed at preprocessing; `run.json` carries the checksums). No decision used held-out reflections of any kind, and every map that placed an atom excluded the free set, but the gains have not been checked against the vault. That read is the operator's.
- **The gap is 0.0233** against 0.0092 for the deposited model (the run's cap 0.030).
- Clashscore 8.8 against 7.0 deposited (the re-letter step brought it down from 9.4); rotamer outliers 1.3 % (deposited 2.3 %); no Ramachandran outlier.
- Six copies at 0.75 Å: 17 842 atoms against 2 850 deposited. The copy-vote step (S0028) was refused. The deposited model scores 0.1571 on our flags and 0.1294 after the common recipe (S0001); the header reports 0.1634 on its own flags.

## Files

| Path | Content |
|---|---|
| `model/8C5N_S0027.pdb` | the released model, PDB, occupancies at four decimals, as the gate wrote it |
| `model/8C5N_S0027.cif` | the same model as mmCIF (gemmi conversion) |
| `model/8C5N_S0001.pdb` | the re-refined deposited model (S0001, the common recipe, the median of three seeds): the baseline of every comparison |
| `maps/8C5N_S0027_map_coeffs.mtz` | phenix.maps coefficients from the work reflections only: `2FOFCWT/PH2FOFCWT` and `FOFCWT/PHFOFCWT` |
| `data/8C5N_data.mtz`, `8C5N_flags.mtz`, `8C5N_split.mtz` | the working data, the inherited flags, the select/report split; the vault is absent from all three |
| `data/prep.json`, `split.json` | how the files were built, with checksums and counts |
| `deposited/8C5N.cif`, `rcsb_entry.json` | the deposited model and the RCSB entry record, as fetched |
| `refinement/score_history.txt`, `score_history.jsonl`, `scorecard.csv` | every step: the facts line, the full metrics, the scorecard row |
| `refinement/steps.md` | the step table |
| `refinement/S0027/` | the released step: facts line, change record, score record |
| `refinement/S0001/`, `S0000/` | the baseline step and the deposited model as scored: facts lines and score records |
| `refinement/metaparams.yaml`, `run.json` | the metaparameters of the run and its state (noise floor, standing recipe, the sealed vault's checksums) |
| `refinement/chains/` | the chain scripts that scheduled the steps on the pod, as run, with their logs |
| `validation/` | phenix.clashscore, rotalyze and ramalyze logs of the released model (`*_S0027.*`) and of the re-refined baseline (`*_S0001.*`) |

## Reproduce

In the harness checkout on the pod (`docs/POD.md` there):

```
bash tools/preprocessing.sh 8C5N --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/T5f59f1 6
```

`chain_target.sh` is the one chain of this run; its log is `refinement/chains/chain_target_T5f59f1.log`.
