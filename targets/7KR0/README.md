# 7KR0 — Crystal structure of SARS-CoV-2 NSP3 macrodomain (C2 crystal form, 100 K)

> In development. Refined by an agent that was prompted to follow a procedure based on Passmore et al. (2026), with PDB 44PS as the reference model; see the [citation](../../README.md#citation).

**Status: improved.** The released model is a six-conformer ensemble with an R-free of 0.0725 on the deposited free set. The re-refined deposited model (S0001, the common recipe) scores 0.1095 and the deposited model as scored (S0000) 0.1175 on the same reflections. This is the model in force on 2026-11-02; the run may continue.

| | |
|---|---|
| Resolution | 0.77 Å |
| Space group | C 1 2 1 |
| Data | amplitudes (FP,SIGFP); 174 924 reflections in the working files, 166 212 work and 8 712 free |
| Free set | the deposition's own flags, inherited unchanged (4.98 %); select / report halves 4 356 / 4 356 |
| Vault | 3 400 work reflections (2 %) removed from every working file at preprocessing; read at S0011 and at S0053, siblings of this lineage; not read on this lineage |
| Deposited refinement program | PHENIX |
| Released by the PDB | 2020-12-09 |
| Primary citation | Fragment binding to the Nsp3 macrodomain of SARS-CoV-2 identified through crystallographic screening and computational docking (Sci Adv 2021), DOI 10.1126/sciadv.abf8711 |
| Harness | prism-science/agentic-refinement, branch `manzuoni/oct28-trials`, commit 25ec394 (pull request to `main` opened 2026-11-02); the models of 2026-10-21: branch `manzuoni/hierarchical_refinement`, commit bfed380 (merged into `main` as 7d62e84) |
| Run | handle Tff1b3f_oct28, step S0112, 2026-10-29 19:15:07 UTC |
| Phenix | 2.1-6048 |
| Gate | ΔR-free ≤ −2σ against the control (σ = 0.00016 from three seeds), gap widened by at most 0.002, gap ≤ 0.0300 or not above the control's, clashscore ≤ 15, rotamer outliers ≤ 1.5 % or not above the control's |

## The three models on the same flags

All three are scored by the harness gate: a fresh cctbx fmodel on the working data with every reflection, no outlier
rejection. S0000 is the deposited model as anonymised at preprocessing; S0001 is that model after the common recipe
(phenix.refine, 10 macro-cycles, three seeds, the median), the baseline that every gain is measured against; the
release is the model in force. Geometry from phenix.clashscore (hydrogens kept), rotalyze and ramalyze; the
MolProbity score from those three.

| | Deposited as scored (S0000) | Re-refined (S0001) | This release (S0112) |
|---|---|---|---|
| R-free | 0.1175 | 0.1095 | **0.0725** |
| R-work | 0.1104 | 0.1005 | 0.0472 |
| Gap R-free − R-work | 0.0071 | 0.0089 | 0.0253 |
| R-free on the select / report halves | 0.1182 / 0.1168 | 0.1085 / 0.1104 | 0.0749 / 0.0701 |
| Clashscore (phenix.clashscore, hydrogens kept) | 4.3 | 5.3 | 12.7 |
| Rotamer outliers | 0.89 % | 1.33 % | 1.65 % |
| Ramachandran outliers / favoured | 0.0 % / 99.4 % | 0.0 % / 98.8 % | 0.0 % / 98.8 % |
| Bond RMSD / angle RMSD | 0.021 Å / 0.99° | 0.008 Å / 1.10° | 0.008 Å / 1.04° |
| MolProbity score | 1.21 | 1.38 | 1.78 |
| Conformers | 1 (altlocs ABCD on some residues) | 1 (altlocs ABCD on some residues) | 6, altlocs ABCDEF |
| Atoms (of which H) | 4 300 (1 990) | 4 391 (1 990) | 18 184 (7 722) |
| Waters, occupancy sum | 316, 309 | 407, 298 | 2 770, 545 |
| ANISOU records | 2 310 | 2 269 | 10 334 |

The entry's own header reports R-free 0.1172 and R-work 0.1099 on its own flags.

## What the model is

Six complete conformers of the protein (altlocs A to F), each at occupancy 1/6, refined together against the working
data with riding hydrogens, anisotropic ADPs on every protein atom and on the waters, restraint weights wc 0.3 / wu 0.25,
and every water occupancy held at its conformer share: a lettered water (one conformer) at 1/6, a shared water (blank
altloc, all six) at 1. No water occupancy is refined; the 2026-10-21 release refined them. Ligands and ions are single.
The ensemble is the deliverable; it is not merged back into one model.

The model came from the deposited file in 110 recorded steps (S0004 to S0113; the record of S0000 to S0003 is in the
`refinement/S0000/` and `S0001/` files), 26 of them accepted and 3 builds, in the main run and its forks: the held-water
fork (Tff1b3f_held, then Tff1b3f_held2) and the trial fork of 2026-10-28 (Tff1b3f_oct28). The lineage of S0112: anisotropic
water ADPs (S0006); the six-conformer split from shake (S0007, a build); the held-water rule (S0082, a build: every water set
to its conformer share, occupancy refinement off); water picks at 4, 4 and 3σ on work-only difference maps (S0084, S0085,
S0088); anisotropic water ADPs three times (S0090 to S0092); a pick at 2.5σ (S0094); a 20-cycle convergence step (S0098);
conformer B-factors more than 3 times apart reset to the site median (S0103, a repair); a pick at 2.5σ that puts no water
within 2.6 Å of a protein atom of any conformer, the range-of-motion rule (S0105, R-free 0.0723, the lowest of the
line); the same B-factor reset again (S0112, a repair: conformer-B outliers 109 → 50, R-free +1.1σ against the control).
From S0082 on, the Coot checks gated every step (waters in protein density, conformer-B outliers, residues beyond ±3.5σ
and next to positive peaks, the tallest peak, Holton's geometry energy wE). Refused after S0105: anisotropic water ADPs
(S0106), the Phenix restraint weights 1 / 1 (S0107, +6.2σ), a convergence step (S0108), the peak repair (S0109) and
Untangler's relabel on two trees (S0110, S0113).

The gate judged every change against a control, the parent refined with the same command and seeds, and accepted an
improving change only when R-free fell by at least 2σ of the run's noise floor with the gap and the geometry inside their
bounds. From 2026-10-27 the gate also holds the model checks of `docs/METHOD.md` (waters in protein density, conformer-B
outliers, residues in difference density, the tallest peak, Holton's wE) and accepts a repair: a change that lowers one
check with R-free not worse than 2σ against its control.
`refinement/steps.md` lists every step with its verdict and `refinement/score_history.txt` is the hash-chained record
the gate wrote.

## Caveats

- **The vault was read on 2026-10-22 at S0053 (the release of 2026-10-21; also S0011 on 2026-10-18)** (the operator's read; 3 400 held-out work reflections): R-vault 0.1054 → 0.0725 from S0001 to that model, against R-free 0.1095 → 0.0726 on the deposited free set; the difference of the two changes is +1.2 σ of the sampling noise (σ 0.0032). The vault confirms the gain within the noise. That model is a sibling of this lineage, which forks before it and has not been read. No decision used held-out reflections of any kind, and every map that placed or moved an atom excluded the free set.
- **The reference model scores lower.** PDB 44PS, the six-conformation model of these data from Passmore et al. (2026) and the reference model the agent was given, scores R-free 0.0657 and R-work 0.0485 on the same free set (scored 2026-10-03 by the earlier campaign's scorer), against 0.0725 / 0.0472 for this release. This release does not reach the reference.
- **Two 7KR0 models stand, and the operator has not chosen.** This one has the lower R-free. The held Coot line's S0104 (run Tff1b3f_held2coot on the pod: held waters, the Coot water and side-chain repairs, the Phenix weights 1 / 1) reads R-free 0.0736 with clashscore 8.4 and one difference peak of 6σ or more against eleven here: the cleaner map. It is not released.
- **The gap is 0.0253** against 0.0089 for the re-refined model (the run's cap 0.030). Clashscore 12.7 (the cap 15) against 7.7 at the 2026-10-21 release and 5.3 re-refined: the held-water picks added waters, and 18 waters lie within 2.2 Å of a protein atom of their own conformer. Rotamer outliers 1.65 % are above the gate's 1.5 % cap and passed because the control had the same.
- **The tallest difference peak, 10.5σ, is at Ser111**: the OG atoms of the conformers spread along a column where the data hold one position. The Coot refit of each conformer lowered it on a sibling model (10.8 → 7.7σ) and it is back here. The checks of this model: 21 residues with an atom beyond ±3.5σ, 13 next to a positive peak of 3.5σ or more, 50 conformer-B outliers, wE 575 (Holton's weighted geometry energy; 383 at the 2026-10-21 release).
- Three mmtbx sub-reports (C-beta deviations, omega, Rama-Z) fail on a six-conformer model; the geometry numbers above come from phenix.clashscore, rotalyze and ramalyze.

## Files

| Path | Content |
|---|---|
| `model/7KR0_S0112.pdb` | the released model, PDB, occupancies at four decimals, as the gate wrote it |
| `model/7KR0_S0112.cif` | the same model as mmCIF (gemmi conversion) |
| `model/7KR0_S0001.pdb` | the re-refined deposited model (S0001, the common recipe, the median of three seeds): the baseline of every comparison |
| `maps/7KR0_S0112_map_coeffs.mtz` | phenix.maps coefficients from the work reflections only: `2FOFCWT/PH2FOFCWT` and `FOFCWT/PHFOFCWT` |
| `data/7KR0_data.mtz`, `7KR0_flags.mtz`, `7KR0_split.mtz` | the working data, the inherited flags, the select/report split; the vault is absent from all three |
| `data/prep.json`, `split.json` | how the files were built, with checksums and counts |
| `deposited/7KR0.cif`, `rcsb_entry.json` | the deposited model and the RCSB entry record, as fetched |
| `refinement/score_history.txt`, `score_history.jsonl`, `scorecard.csv` | every step: the facts line, the full metrics, the scorecard row |
| `refinement/steps.md` | the step table |
| `refinement/S0112/` | the released step: facts line, change record, score record |
| `refinement/S0001/`, `S0000/` | the baseline step and the deposited model as scored: facts lines and score records (`S0000/rescored.json`: the same model scored again by the current scorer at release, for the geometry fields the scorer of 2026-10-14 did not write) |
| `refinement/metaparams.yaml`, `run.json` | the metaparameters of the run and its state (noise floor, standing recipe, the sealed vault's checksums) |
| `refinement/chains/` | the chain scripts that scheduled the steps on the pod, as run, with their logs |
| `validation/` | phenix.clashscore, rotalyze and ramalyze logs of the released model (`*_S0112.*`) and of the re-refined baseline (`*_S0001.*`) |

## Reproduce

In the harness checkout on the pod (`docs/POD.md` there):

```
bash tools/preprocessing.sh 7KR0 --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/Tff1b3f 6                  # to the six-conformer split, S0007
bash scripts/chain_heldwater.sh /home/dev/runs/hr/Tff1b3f /home/dev/runs/hr/Tff1b3f_held S0007 6
bash scripts/chain_held_levers.sh /home/dev/runs/hr/Tff1b3f_held2 6       # the sibling fork from the held BUILD S0082, sanity_count_k 2
bash scripts/chain_oct28.sh /home/dev/runs/hr/Tff1b3f_held2 /home/dev/runs/hr/Tff1b3f_oct28 S0098
```

The chain scripts under `refinement/chains/` are the hand-scheduled originals with their logs (`chain_oct28_Tff1b3f_oct28.log` for the trial fork; the earlier campaign's `chain*_7KR0.sh` stay for the record). The held-water and held-lever chains ran on the source forks; every command line of every step is in that step's `change.json` on the pod.
