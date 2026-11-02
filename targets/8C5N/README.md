# 8C5N — Sub-atomic resolution structure of the chitin-binding protein D (CbpD) from Pseudomonas aeruginosa

> In development. Refined by an agent that was prompted to follow a procedure based on Passmore et al. (2026), with PDB 44PS as the reference model; see the [citation](../../README.md#citation).

**Status: improved.** The released model is a six-conformer ensemble with an R-free of 0.0875 on the deposited free set. The re-refined deposited model (S0001, the common recipe) scores 0.1294 and the deposited model as scored (S0000) 0.1571 on the same reflections. This is the model in force on 2026-11-02; the run may continue.

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
| Harness | prism-science/agentic-refinement, branch `manzuoni/oct28-trials`, commit 25ec394 (pull request to `main` opened 2026-11-02); the models of 2026-10-21: branch `manzuoni/hierarchical_refinement`, commit bfed380 (merged into `main` as 7d62e84) |
| Run | handle T5f59f1_oct28, step S0065, 2026-10-30 17:47:09 UTC |
| Phenix | 2.1-6048 |
| Gate | ΔR-free ≤ −2σ against the control (σ = 0.00046 from three seeds), gap widened by at most 0.002, gap ≤ 0.0300 or not above the control's, clashscore ≤ 15, rotamer outliers ≤ 1.5 % or not above the control's |

## The three models on the same flags

All three are scored by the harness gate: a fresh cctbx fmodel on the working data with every reflection, no outlier
rejection. S0000 is the deposited model as anonymised at preprocessing; S0001 is that model after the common recipe
(phenix.refine, 10 macro-cycles, three seeds, the median), the baseline that every gain is measured against; the
release is the model in force. Geometry from phenix.clashscore (hydrogens kept), rotalyze and ramalyze; the
MolProbity score from those three.

| | Deposited as scored (S0000) | Re-refined (S0001) | This release (S0065) |
|---|---|---|---|
| R-free | 0.1571 | 0.1294 | **0.0875** |
| R-work | 0.1480 | 0.1247 | 0.0627 |
| Gap R-free − R-work | 0.0092 | 0.0046 | 0.0248 |
| R-free on the select / report halves | 0.1561 / 0.1582 | 0.1302 / 0.1286 | 0.0878 / 0.0872 |
| Clashscore (phenix.clashscore, hydrogens kept) | 7.0 | 4.8 | 14.8 |
| Rotamer outliers | 2.34 % | 1.75 % | 1.48 % |
| Ramachandran outliers / favoured | 0.0 % / 99.5 % | 0.0 % / 99.5 % | 0.0 % / 96.7 % |
| Bond RMSD / angle RMSD | 0.013 Å / 1.58° | 0.007 Å / 1.00° | 0.010 Å / 1.17° |
| MolProbity score | 1.67 | 1.44 | 2.01 |
| Conformers | 1 (altlocs ABC on some residues) | 1 (altlocs ABC on some residues) | 6, altlocs ABCDEF |
| Atoms (of which H) | 2 433 (665) | 2 676 (665) | 18 961 (7 932) |
| Waters, occupancy sum | 161, 161 | 404, 253 | 2 562, 472 |
| ANISOU records | 1 768 | 1 763 | 11 029 |

The entry's own header reports R-free 0.1634 and R-work 0.1537 on its own flags.

## What the model is

Six complete conformers of the protein (altlocs A to F), each at occupancy 1/6, refined together against the working
data with riding hydrogens, anisotropic ADPs on every protein atom and every water, restraint weights wc 0.3 / wu 0.25,
and every water occupancy held at its conformer share: a lettered water (one conformer) at 1/6, a shared water (blank
altloc, all six) at 1. No water occupancy is refined; the 2026-10-21 release refined them. Ligands and ions are single.
The ensemble is the deliverable; it is not merged back into one model.

The model came from the deposited file in 66 recorded steps (S0000 to S0065), 18 of them accepted and 2 builds, in the
main run T5f59f1 (to S0027, the 2026-10-21 release) and its forks: the held-water fork T5f59f1_held, its Coot repair fork
T5f59f1_heldcoot and the trial fork of 2026-10-28 (T5f59f1_oct28). The lineage of S0065: restraint weights 0.3 / 0.25
(S0008); anisotropic water ADPs (S0012); the six-conformer split from shake (S0014, a build); the held-water rule (S0030, a
build, from the split: every water set to its conformer share, occupancy refinement off); water picks at 4 and 3σ on
work-only difference maps (S0031, S0034); anisotropic water ADPs (S0037, R-free 0.0891); a convergence step (S0040,
0.0879); the Coot water repair (S0046, R-free 0.0871, the lowest of the line: the waters in protein density deleted, each
conformer of the residues next to them fitted in Coot); conformer B-factors more than 3 times apart reset to the site median
(S0049, a repair); the water repair again (S0050: no water in protein density left); the B-factor reset again (S0055, a
repair); the B-factor reset by the density (S0065, a repair: a conformer's B above the site median reset to the median where
that conformer's 2mFo-DFc density is at least half the site's; conformer-B outliers 31 → 3, R-free −0.3σ against the control).
From S0030 on, the Coot checks gated every step. Refused after S0055: a 3σ and a 2.5σ pick with the range-of-motion rule
(S0056, S0058), the Phenix restraint weights 1 / 1 (+6.2σ on the held Coot line), anisotropic water ADPs (S0060), a
convergence step (S0061), the peak repair (S0062) and Untangler's relabel (S0063).

The gate judged every change against a control, the parent refined with the same command and seeds, and accepted an
improving change only when R-free fell by at least 2σ of the run's noise floor with the gap and the geometry inside their
bounds. From 2026-10-27 the gate also holds the model checks of `docs/METHOD.md` (waters in protein density, conformer-B
outliers, residues in difference density, the tallest peak, Holton's wE) and accepts a repair: a change that lowers one
check with R-free not worse than 2σ against its control.
`refinement/steps.md` lists every step with its verdict and `refinement/score_history.txt` is the hash-chained record
the gate wrote.

## Caveats

- **The vault was read on 2026-10-22 at S0027 (the release of 2026-10-21)** (the operator's read; 2 000 held-out work reflections): R-vault 0.1480 → 0.0995 from S0001 to that model, against R-free 0.1294 → 0.0908 on the deposited free set; the difference of the two changes is -2.3 σ of the sampling noise (σ 0.0044). The vault confirms the gain within the noise. That model is a sibling of this lineage, which forks before it and has not been read. No decision used held-out reflections of any kind, and every map that placed or moved an atom excluded the free set.
- **R-free 0.0875 is 0.0004 above S0046 (0.0871), the lowest of the line.** The four steps after S0046 were accepted as repairs: a change that lowers a check with R-free not worse than 2σ against its control. From the 2026-10-21 release (S0027) to S0065 the waters in protein density fell 62 → 4, the conformer-B outliers 20 → 3; the residues with an atom beyond ±3.5σ stay at 21 (20). The 2026-10-21 model refined the water occupancies; the reviewers (Spencer Passmore and Stephanie Wankowicz, 2026-10-27) found waters in protein density and extreme conformer B-factors on it, and the held-water rule and the Coot repairs are the answer.
- **The gap is 0.0248** against 0.0046 for the re-refined model (the run's cap 0.030). **Clashscore 14.8** is at the gate's cap of 15, against 8.8 at the 2026-10-21 release and 4.8 re-refined: the held-water picks added waters at full conformer share. Rotamer outliers 1.48 %; no Ramachandran outlier.
- Six conformers at 0.75 Å: 18 961 atoms against 2 850 deposited. The deposited model scores 0.1571 on our flags and 0.1294 after the common recipe (S0001); the header reports 0.1634 on its own flags. The checks of this model: 21 residues with an atom beyond ±3.5σ, 2 next to a positive peak of 3.5σ or more, the tallest peak 10.5σ, wE 741 (Holton's weighted geometry energy; 521 at the 2026-10-21 release).

## Files

| Path | Content |
|---|---|
| `model/8C5N_S0065.pdb` | the released model, PDB, occupancies at four decimals, as the gate wrote it |
| `model/8C5N_S0065.cif` | the same model as mmCIF (gemmi conversion) |
| `model/8C5N_S0001.pdb` | the re-refined deposited model (S0001, the common recipe, the median of three seeds): the baseline of every comparison |
| `maps/8C5N_S0065_map_coeffs.mtz` | phenix.maps coefficients from the work reflections only: `2FOFCWT/PH2FOFCWT` and `FOFCWT/PHFOFCWT` |
| `data/8C5N_data.mtz`, `8C5N_flags.mtz`, `8C5N_split.mtz` | the working data, the inherited flags, the select/report split; the vault is absent from all three |
| `data/prep.json`, `split.json` | how the files were built, with checksums and counts |
| `deposited/8C5N.cif`, `rcsb_entry.json` | the deposited model and the RCSB entry record, as fetched |
| `refinement/score_history.txt`, `score_history.jsonl`, `scorecard.csv` | every step: the facts line, the full metrics, the scorecard row |
| `refinement/steps.md` | the step table |
| `refinement/S0065/` | the released step: facts line, change record, score record |
| `refinement/S0001/`, `S0000/` | the baseline step and the deposited model as scored: facts lines and score records |
| `refinement/metaparams.yaml`, `run.json` | the metaparameters of the run and its state (noise floor, standing recipe, the sealed vault's checksums) |
| `refinement/chains/` | the chain scripts that scheduled the steps on the pod, as run, with their logs |
| `validation/` | phenix.clashscore, rotalyze and ramalyze logs of the released model (`*_S0065.*`) and of the re-refined baseline (`*_S0001.*`) |

## Reproduce

In the harness checkout on the pod (`docs/POD.md` there):

```
bash tools/preprocessing.sh 8C5N --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/T5f59f1 6                                                  # to the six-conformer split, S0014
bash scripts/chain_heldwater.sh /home/dev/runs/hr/T5f59f1 /home/dev/runs/hr/T5f59f1_held S0014 6          # S0030 to S0040
bash scripts/chain_coot_repair.sh /home/dev/runs/hr/T5f59f1_held /home/dev/runs/hr/T5f59f1_heldcoot S0040 6   # S0046 to S0050
bash scripts/chain_oct28.sh /home/dev/runs/hr/T5f59f1_heldcoot /home/dev/runs/hr/T5f59f1_oct28 S0050       # S0055 to S0065
```

The chain scripts under `refinement/chains/` are the hand-scheduled originals with their logs (`chain_oct28_T5f59f1_oct28.log` for the trial fork). The held-water and Coot repair chains ran on the source forks; every command line of every step is in that step's `change.json` on the pod.
