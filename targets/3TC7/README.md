# 3TC7 — Crystal Structure of Engineered Protein. Northeast Structural Genomics Consortium Target OR62

> In development. Refined by an agent that was prompted to follow a procedure based on Passmore et al. (2026), with PDB 44PS as the reference model; see the [citation](../../README.md#citation).

**Status: improved.** The released model is a six-conformer ensemble with an R-free of 0.1553 on the deposited free set. The re-refined deposited model (S0001, the common recipe) scores 0.1856 and the deposited model as scored (S0000) 0.1918 on the same reflections. This is the model in force on 2026-11-05; the run may continue.

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
| Harness | prism-science/agentic-refinement, branch `manzuoni/nov03-consolidated`, commit 62eeafa (pull request #70 to `main`) for 7KR0, 8C5N and 3TC7 of 2026-11-05; branch `manzuoni/oct28-trials`, commit 25ec394, for 7R2H of 2026-11-02; the models of 2026-10-21: branch `manzuoni/hierarchical_refinement`, commit bfed380 (merged into `main` as 7d62e84) |
| Run | handle T431c8e_nqh, step S0123, 2026-11-03 07:57:59 UTC |
| Phenix | 2.1-6048 |
| Gate | ΔR-free ≤ −2σ against the control (σ = 0.00027 from three seeds), gap widened by at most 0.01, gap ≤ 0.1200 or not above the control's, clashscore ≤ 15, rotamer outliers ≤ 1.5 % or not above the control's |

## The three models on the same flags

All three are scored by the harness gate: a fresh cctbx fmodel on the working data with every reflection, no outlier
rejection. S0000 is the deposited model as anonymised at preprocessing; S0001 is that model after the common recipe
(phenix.refine, 10 macro-cycles, three seeds, the median), the baseline that every gain is measured against; the
release is the model in force. Geometry from phenix.clashscore (hydrogens kept), rotalyze and ramalyze; the
MolProbity score from those three.

| | Deposited as scored (S0000) | Re-refined (S0001) | This release (S0123) |
|---|---|---|---|
| R-free | 0.1918 | 0.1856 | **0.1553** |
| R-work | 0.1536 | 0.1412 | 0.0930 |
| Gap R-free − R-work | 0.0382 | 0.0443 | 0.0623 |
| R-free on the select / report halves | 0.1904 / 0.1932 | 0.1875 / 0.1836 | 0.1593 / 0.1513 |
| Clashscore (phenix.clashscore, hydrogens kept) | 2.9 | 1.7 | 0.8 |
| Rotamer outliers | 1.36 % | 1.36 % | 2.89 % |
| Ramachandran outliers / favoured | 0.0 % / 98.0 % | 0.0 % / 98.0 % | 0.4 % / 95.6 % |
| Bond RMSD / angle RMSD | 0.008 Å / 1.08° | 0.010 Å / 1.17° | 0.019 Å / 1.70° |
| MolProbity score | 1.19 | 1.03 | 1.40 |
| Conformers | 1 (altlocs AB on some residues) | 1 (altlocs AB on some residues) | 6, altlocs ABCDEF |
| Atoms (of which H) | 2 220 (0) | 2 346 (0) | 25 841 (12 375) |
| Waters, occupancy sum | 180, 180 | 306, 270 | 1 357, 459 |
| ANISOU records | 2 020 | 2 020 | 12 109 |

The entry's own header reports R-free 0.193 and R-work 0.158 on its own flags.

## What the model is

Six complete conformers of the protein (altlocs A to F), each at occupancy 1/6, refined together against the working
data with riding hydrogens, restraint weights wc 0.3 / wu 0.25, TLS (one group for the protein) over an isotropic residual on
every protein atom (the total ADP is written as ANISOU records) and isotropic waters. Selenium stands in place of sulfur in
conformer A of Met73, Met109 and Met237 (MSE, one sixth selenium at each site); Met154 and Met200 are sulfur in every
conformer. A lettered water belongs to one conformer, a water with a blank altloc to all six. The ensemble is the
deliverable; it is not merged back into one model.

The model came from the deposited file in 116 recorded steps (S0000 to S0115), 19 of them accepted and 2 builds, in the
main run T431c8e to the six-conformer split (S0032) and in its forks: T431c8e_gap with looser gap bounds (to S0061, the
2026-10-21 release), the Coot repair fork T431c8e_coot (S0086), the trial forks of 2026-10-28 (T431c8e_oct28: S0104;
T431c8e_oct28b: S0106) and T431c8e_oct29 (S0108). The lineage of S0108 to S0061 is on the 2026-10-21 card; after it: the
Coot repair of the residues in difference density (S0086: each conformer fitted into the work-only map of the model with that
conformer's residues at occupancy 0, the rotamer fitted then 20 cycles of real-space refinement, kept where the density
correlation did not fall; 42 waters that the moved side chains overlapped deleted; R-free +2.0σ against the control, a
repair); selenomethionine in conformers A and B of the five methionines, one third selenium (S0104: the tallest peak 13.7 →
7.7σ, R-free −7.0σ); the revert to selenium in conformer A of Met73, Met109 and Met237 only (S0106: the deepest point of the
difference map −11.0 → −5.3σ, a repair of the hole, R-free −1.9σ); the Coot repair again (S0108: 26 waters deleted, R-free
−10.5σ against its control, the gap 0.003 narrower, clashscore 9.5 → 9.0), the release of 2026-11-02; then, in the clash
fork T431c8e_nqh, the clash term (Phenix's nonbonded weight, 100 by default at this resolution) at 300 (S0116, clashscore
9.0 → 3.5, R-free 0.1521) and at 1000 (S0123, clashscore 0.8, R-free 0.1553).

The gate judged every change against a control, the parent refined with the same command and seeds, and accepted an
improving change only when R-free fell by at least 2σ of the run's noise floor with the gap and the geometry inside their
bounds. From 2026-10-27 the gate also holds the model checks of `docs/METHOD.md` (waters in protein density, conformer-B
outliers, residues in difference density, the tallest peak, Holton's wE) and accepts a repair: a change that lowers one
check with R-free not worse than 2σ against its control.
`refinement/steps.md` lists every step with its verdict and `refinement/score_history.txt` is the hash-chained record
the gate wrote.

## Caveats

- **The vault was read on 2026-10-22 at S0061 (the release of 2026-10-21)** (the operator's read; 780 held-out work reflections): R-vault 0.1906 → 0.1493 from S0001 to that model, against R-free 0.1856 → 0.1475 on the deposited free set; the difference of the two changes is -0.4 σ of the sampling noise (σ 0.0088). The vault confirms the gain within the noise. The steps accepted after that model have not been read. No decision used held-out reflections of any kind, and every map that placed or moved an atom excluded the free set.
- **This release trades R-free for geometry.** Against the release of 2026-11-02 (S0108: R-free 0.1504, clashscore 9.0, wE 707) this model reads R-free 0.1553 (+0.0049) with clashscore 0.8 and wE 322: the clash term at weight 1000 against Phenix's default of 100. S0116 (weight 300: R-free 0.1521, clashscore 3.5) is the milder trade and stays in the record on the pod.
- **Partial selenomethionine.** The SD sites hold about 18 electrons against 16 for sulfur: the crystal is partly selenomethionine. Selenium in every conformer was refused (+11σ, 2026-10-20); one third (S0104) left every Se atom in negative density; one sixth at three of the five methionines is what the maps support. The check that accepted S0106 (the deepest point of the difference map) was added after S0105, the same change on another fork, was refused by 0.06σ; the fork T431c8e_oct28b ran it with fresh arms, and the operator took the result.
- Six conformers at 1.5 Å: the gate's control is the parent refined with the same seeds, so an accepted gain is relative to that control, not evidence that six conformers are the right number for this entry. The two-conformer model of the main run (S0020, R-free 0.1688) is in the record.
- **The gap is 0.0623** against 0.0443 for the re-refined model. Rotamer outliers 2.89 %; one Ramachandran outlier (0.4 %); bond RMSD 0.019 Å; MolProbity score 1.40. The tallest work-only mFo-DFc peak is 5.7σ, the deepest point −4.6σ.

## Files

| Path | Content |
|---|---|
| `model/3TC7_S0123.pdb` | the released model, PDB, occupancies at four decimals, as the gate wrote it |
| `model/3TC7_S0123.cif` | the same model as mmCIF (gemmi conversion) |
| `model/3TC7_S0001.pdb` | the re-refined deposited model (S0001, the common recipe, the median of three seeds): the baseline of every comparison |
| `maps/3TC7_S0123_map_coeffs.mtz` | phenix.maps coefficients from the work reflections only: `2FOFCWT/PH2FOFCWT` and `FOFCWT/PHFOFCWT` |
| `data/3TC7_data.mtz`, `3TC7_flags.mtz`, `3TC7_split.mtz` | the working data, the inherited flags, the select/report split; the vault is absent from all three |
| `data/prep.json`, `split.json` | how the files were built, with checksums and counts |
| `deposited/3TC7.cif`, `rcsb_entry.json` | the deposited model and the RCSB entry record, as fetched |
| `refinement/score_history.txt`, `score_history.jsonl`, `scorecard.csv` | every step: the facts line, the full metrics, the scorecard row |
| `refinement/steps.md` | the step table |
| `refinement/S0123/` | the released step: facts line, change record, score record |
| `refinement/S0001/`, `S0000/` | the baseline step and the deposited model as scored: facts lines and score records |
| `refinement/metaparams.yaml`, `run.json` | the metaparameters of the run and its state (noise floor, standing recipe, the sealed vault's checksums) |
| `refinement/chains/` | the chain scripts that scheduled the steps on the pod, as run, with their logs |
| `validation/` | phenix.clashscore, rotalyze and ramalyze logs of the released model (`*_S0123.*`) and of the re-refined baseline (`*_S0001.*`) |
| `refinement/main_run_T431c8e/` | the main run's own record after the fork point (its best S0042, R-free 0.1540, under the standing gap bounds) |

## Reproduce

In the harness checkout on the pod (`docs/POD.md` there):

```
bash tools/preprocessing.sh 3TC7 --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/T431c8e 6          # to the six-conformer split, S0032
bash scripts/fork_run.sh /home/dev/runs/hr/T431c8e /home/dev/runs/hr/T431c8e_gap
# set gap_widen_max 0.010 and gap_abs_max 0.12 in T431c8e_gap/metaparams.yaml, as scripts/fork_gap_after.sh does
bash scripts/chain_gap.sh /home/dev/runs/hr/T431c8e_gap 6                                   # to S0061
bash scripts/chain_coot_repair.sh /home/dev/runs/hr/T431c8e_gap /home/dev/runs/hr/T431c8e_coot S0061 6   # S0086
bash scripts/chain_oct28.sh /home/dev/runs/hr/T431c8e_coot /home/dev/runs/hr/T431c8e_oct28 S0086       # S0104
# T431c8e_oct28b: a fork of T431c8e_oct28 with quality_hole_tol 1.0 and quality_hole_drop 1.5; refine_step.py semet --revert --pairs --kind sanity from S0104 (S0106)
bash scripts/chain_oct29.sh /home/dev/runs/hr/T431c8e_oct28b /home/dev/runs/hr/T431c8e_oct29 S0106     # S0108
bash scripts/fork_run.sh /home/dev/runs/hr/T431c8e_oct29 /home/dev/runs/hr/T431c8e_nqh                     # then refine_step.py nonbonded --weight 300 (S0116) and --weight 1000 (S0123)
```

The chain scripts under `refinement/chains/` are the hand-scheduled originals with their logs. The levers whose logs have no script there were scheduled from one-off scripts; every command line of every step is in that step's `change.json` on the pod.
