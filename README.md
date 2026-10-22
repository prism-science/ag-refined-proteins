# ag-refined-proteins

> This repository is under active development. The models are dated snapshots of refinements that are still running,
> and the numbers will change. If you find a problem, please open an issue with the target ID and the file you used.

Crystallographic models of eight PDB entries (0.75 to 2.7 Å) re-refined by an agentic workflow, with the data, maps,
validation and step records needed to check and reuse them.

## The idea

The method was not found by the agent. The agent was directly prompted to follow a procedure based on the one in the
preprint of Passmore et al. (2026), with their six-conformation model of 7KR0, PDB [44PS](https://www.rcsb.org/structure/44PS),
as the reference model, complemented with additions for an agentic workflow: one change at a time, each refined beside
a control and accepted only when R-free falls on the deposited free set, with a held-out set of reflections as a leak
check and a record of every step.

## Citation

If you use these models, please cite the method they follow:

> Passmore, S. K., Holton, J. M., Zatsepin, N. A., & Martin, A. V. (2026). Optimizing the connectivity of protein conformations to untangle ensemble refinement. *bioRxiv*. https://doi.org/10.64898/2026.09.17.752399

and the original PDB entry of each target (its primary citation is in `targets/<ID>/deposited/rcsb_entry.json`).

## Results

All numbers are on the free-reflection flags inherited unchanged from each deposition, scored by the harness (a fresh
cctbx fmodel, every reflection kept). Compare them only on the same free set, never with an entry's header. The
baseline is the re-refined deposited model (S0001: phenix.refine, 10 macro-cycles, the median of three seeds), so what
plain re-refinement gives is not credited to the agent. "Report" is one half of the free set, a check that a gain is
not on one half only.

<!-- results-table:begin -->
| Target | Res. (Å) | Entry | Re-refined, our flags (full / report) | This release (full / report) | Δ full | R-work (re-refined → ours) | Gap (re-refined → ours) | Model | Status |
|---|---|---|---|---|---|---|---|---|---|
| [8C5N](targets/8C5N/README.md) | 0.75 | Chitin-binding protein D (CbpD) from Pseudomonas aeruginosa | 0.1294 / 0.1286 | **0.0908 / 0.0910** | −0.0386 | 0.1247 → 0.0675 | 0.0046 → 0.0233 | six-copy ensemble, step S0027 | improved |
| [7KR0](targets/7KR0/README.md) | 0.77 | Crystal structure of SARS-CoV-2 NSP3 macrodomain (C2 crystal form, 100 K) | 0.1095 / 0.1104 | **0.0726 / 0.0740** | −0.0369 | 0.1005 → 0.0467 | 0.0089 → 0.0259 | six-copy ensemble, step S0053 | improved |
| [7R2H](targets/7R2H/README.md) | 0.79 | Cyclophilin D with DMSO | 0.1355 / 0.1365 | **0.0993 / 0.1001** | −0.0362 | 0.1243 → 0.0693 | 0.0112 → 0.0300 | six-copy ensemble, step S0019 | improved |
| [9ARN](targets/9ARN/README.md) | 1.41 | HIV-1 gp41 CHR-NHR reverse hairpin construct | 0.2970 / 0.3157 | **0.2769 / 0.2856** | −0.0201 | 0.2346 → 0.2389 | 0.0624 → 0.0380 | single model, step S0062 | improved |
| [3TC7](targets/3TC7/README.md) | 1.5 | Engineered protein, NESG target OR62 | 0.1856 / 0.1836 | **0.1475 / 0.1466** | −0.0381 | 0.1412 → 0.0806 | 0.0443 → 0.0668 | six-copy ensemble, step S0061 | improved |
| [1LZ8](targets/1LZ8/README.md) | 1.53 | Hen egg-white lysozyme, phased on the anomalous signal of S and Cl | 0.2712 / 0.2659 | **0.2408 / 0.2375** | −0.0304 | 0.2048 → 0.1662 | 0.0664 → 0.0746 | two-copy ensemble, step S0073 | improved |
| [4QO4](targets/4QO4/README.md) | 1.7 | MDM2 (17-111) with compound 16 | 0.3097 / 0.2625 | **0.2747 / 0.2625** | −0.0350 | 0.2443 → 0.2229 | 0.0654 → 0.0518 | single model, step S0064 | improved |
| [3QUE](targets/3QUE/README.md) | 2.7 | Human p38 MAP kinase with Skepinone-L | 0.2853 / 0.2869 | **0.2642 / 0.2585** | −0.0211 | 0.1895 → 0.2124 | 0.0958 → 0.0518 | single model, step S0057 | improved |
<!-- results-table:end -->

Geometry, re-refined → this release (phenix.clashscore with hydrogens kept, rotalyze, ramalyze, the bond and angle
RMSDs of the gate's geometry summary, and the MolProbity score from clashscore, rotamer outliers and Ramachandran
favoured):

<!-- geometry-table:begin -->
| Target | Clashscore | Rotamer outliers % | Ramachandran outliers % | Ramachandran favoured % | Bond RMSD (Å) | Angle RMSD (°) | MolProbity score |
|---|---|---|---|---|---|---|---|
| [8C5N](targets/8C5N/README.md) | 4.8 → 8.8 | 1.75 → 1.26 | 0.0 → 0.0 | 99.5 → 98.4 | 0.007 → 0.010 | 1.00 → 1.19 | 1.44 → 1.55 |
| [7KR0](targets/7KR0/README.md) | 5.3 → 7.7 | 1.33 → 1.54 | 0.0 → 0.0 | 98.8 → 97.0 | 0.008 → 0.007 | 1.10 → 0.99 | 1.38 → 1.74 |
| [7R2H](targets/7R2H/README.md) | 4.3 → 7.8 | 0.00 → 0.99 | 0.0 → 0.0 | 96.9 → 93.8 | 0.008 → 0.009 | 1.07 → 1.10 | 1.40 → 1.84 |
| [9ARN](targets/9ARN/README.md) | 3.2 → 1.6 | 3.03 → 0.00 | 0.0 → 0.0 | 100.0 → 100.0 | 0.010 → 0.004 | 1.03 → 0.52 | 1.48 → 0.91 |
| [3TC7](targets/3TC7/README.md) | 1.7 → 6.8 | 1.36 → 2.74 | 0.0 → 0.4 | 98.0 → 97.2 | 0.010 → 0.015 | 1.17 → 1.40 | 1.03 → 1.86 |
| [1LZ8](targets/1LZ8/README.md) | 4.1 → 1.3 | 1.90 → 0.48 | 0.0 → 0.0 | 97.6 → 93.7 | 0.011 → 0.005 | 1.15 → 0.75 | 1.48 → 1.27 |
| [4QO4](targets/4QO4/README.md) | 2.6 → 7.3 | 2.41 → 3.53 | 0.0 → 0.0 | 98.8 → 95.6 | 0.011 → 0.016 | 1.30 → 1.63 | 1.33 → 2.13 |
| [3QUE](targets/3QUE/README.md) | 10.4 → 6.3 | 12.87 → 3.63 | 0.3 → 0.3 | 93.8 → 96.8 | 0.013 → 0.006 | 1.44 → 1.26 | 2.79 → 1.98 |
<!-- geometry-table:end -->

"Improved" means a lower full R-free than the re-refined deposited model on the same flags.

## What is in a target directory

```
targets/<ID>/
  README.md                 the card: the two models on the same flags, what the model is, caveats, files, reproduction
  model/<ID>_<step>.pdb     the released model (occupancies at four decimals) and .cif (mmCIF)
  model/<ID>_S0001.pdb      the re-refined deposited model, the baseline of every comparison
  maps/<ID>_<step>_map_coeffs.mtz   2mFo-DFc and mFo-DFc coefficients from the work reflections only
  data/<ID>_data.mtz        the working data: the deposited structure factors without the vault (2 % of the work set)
  data/<ID>_flags.mtz       the inherited free flags (column R-free-flags, 0 = free)
  data/<ID>_split.mtz       the select / report halves of the free set (column SPLIT)
  data/prep.json, split.json   how the files were built; checksums and counts
  deposited/<ID>.cif, rcsb_entry.json   the deposited model and the RCSB entry record
  refinement/score_history.txt   one line for each step, hash-chained: parent, change, R-free before and after, sigma,
                                 R-work, gap, clashscore, rotamers, atoms, waters, verdict
  refinement/score_history.jsonl, scorecard.csv   the same steps with every metric; the scorecard rows
  refinement/steps.md            the step table
  refinement/<step>/             the released step: FACTS.txt, change.json, score.json
  refinement/S0001/, S0000/      the baseline step and the deposited model as scored
  refinement/metaparams.yaml, run.json   the run's fixed metaparameters and its state
  refinement/chains/             the scripts that scheduled the steps on the pod
  validation/                    phenix.clashscore, rotalyze, ramalyze logs of the released model and of the baseline
```

## Use

Open a model with its maps in Coot:

```bash
coot targets/7KR0/model/7KR0_S0053.pdb --auto targets/7KR0/maps/7KR0_S0053_map_coeffs.mtz
```

A six-copy ensemble shows as altlocs A to F on every residue. `docs/METHOD.md` describes the procedure and
`docs/HOW_TO_USE.md` how to check the numbers.

## Licence

CC-BY-4.0 (`LICENSE`).
