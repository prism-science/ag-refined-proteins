# ag-refined-proteins

> This repository is under active development. The models are dated snapshots of refinements that are still running,
> and the numbers will change; the Deposited column gives the date of each model. If you find a problem, please open an
> issue with the target ID and the file you used.

Crystallographic models of eight PDB entries (0.75 to 2.7 Å) re-refined by an agentic workflow, with the data, maps,
validation and step records needed to check and reuse them.

The refinement process was directly prompted to follow a procedure based on the one in the
preprint of Passmore et al. (2026), with their six-conformation model of 7KR0, PDB [44PS](https://www.rcsb.org/structure/44PS),
as the reference model, complemented with additions for an agentic workflow: one change at a time, each refined beside
a control and accepted only when R-free falls on the deposited free set, with a held-out set of reflections as a leak
check and a record of every step.

## Citation

If you use these models, please cite the method they follow:

> Passmore, S. K., Holton, J. M., Zatsepin, N. A., & Martin, A. V. (2026). Optimizing the connectivity of protein conformations to untangle ensemble refinement. *bioRxiv*. https://doi.org/10.64898/2026.09.17.752399

and the original PDB entry of each target (its primary citation is in `targets/<ID>/deposited/rcsb_entry.json`).

## Results

R-free on each entry's own deposited free flags. "PDB" is the deposited model scored the same way. "Deposited" is the
date the model was added to this repository.

<!-- results-table:begin -->
| Target | Res. (Å) | Model | R-free (PDB → ours) | R-work | Gap | Clashscore (PDB → ours) | MolProbity | Deposited |
|---|---|---|---|---|---|---|---|---|
| [8C5N](targets/8C5N/README.md) | 0.75 | S0065 | 0.1571 → **0.0875** | 0.0627 | 0.025 | 7.0 → 14.8 | 2.01 | 2026-11-02 |
| [7KR0](targets/7KR0/README.md) | 0.77 | S0112 | 0.1175 → **0.0725** | 0.0472 | 0.025 | 4.3 → 12.7 | 1.78 | 2026-11-02 |
| [7R2H](targets/7R2H/README.md) | 0.79 | S0076 | 0.1551 → **0.0946** | 0.0650 | 0.030 | 0.0 → 12.1 | 2.08 | 2026-11-02 |
| [9ARN](targets/9ARN/README.md) | 1.41 | S0062 | 0.2944 → **0.2769** | 0.2389 | 0.038 | 1.6 → 1.6 | 0.91 | 2026-10-21 |
| [3TC7](targets/3TC7/README.md) | 1.5 | S0108 | 0.1918 → **0.1504** | 0.0864 | 0.064 | 2.9 → 9.0 | 2.12 | 2026-11-02 |
| [1LZ8](targets/1LZ8/README.md) | 1.53 | S0073 | 0.2826 → **0.2408** | 0.1662 | 0.075 | 5.1 → 1.3 | 1.27 | 2026-10-21 |
| [4QO4](targets/4QO4/README.md) | 1.7 | S0064 | 0.3133 → **0.2747** | 0.2229 | 0.052 | 16.0 → 7.3 | 2.13 | 2026-10-21 |
| [3QUE](targets/3QUE/README.md) | 2.7 | S0057 | 0.2901 → **0.2642** | 0.2124 | 0.052 | 10.6 → 6.3 | 1.98 | 2026-10-21 |
<!-- results-table:end -->

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
coot targets/<ID>/model/<ID>_<step>.pdb --auto targets/<ID>/maps/<ID>_<step>_map_coeffs.mtz   # <step>: the Model column
```

A six-conformer ensemble shows as altlocs A to F on every residue (A to H for the eight conformers of 7R2H). `docs/METHOD.md` describes the procedure and
`docs/HOW_TO_USE.md` how to check the numbers.

## Licence

CC-BY-4.0 (`LICENSE`).
