# ag-refined-proteins

Crystallographic models refined by an autonomous harness (the *autoresearch* project, Astera Institute), released with
what is needed to use, check and extend them: the model, the map coefficients, the working data and the inherited
free-reflection flags it was scored on, the deposited model it started from, and the complete step record of the run.

This is the hierarchical refinement line (October 2026), on `main` since 2026-10-21. It holds eight targets, from 0.75
to 2.7 Å, each refined from its deposited file by the harness: four six-copy ensembles (8C5N, 7KR0, 7R2H, 3TC7), one
two-copy ensemble (1LZ8) and three single models (9ARN, 4QO4, 3QUE). The earlier campaign's targets and records (the
single-model line, August to October 2026) are on the `release-*` branches and in this repository's history before
2026-10-21. Nothing here is a ceiling: the runs continue (7R2H and 8C5N were still refining at this snapshot) and this
is a dated snapshot of the model in force on each target.

## Results

Every model is scored on the R-free flags inherited unchanged from its deposition, by the harness gate (a fresh cctbx
fmodel on the working data, every reflection, no outlier rejection), so the numbers in a row are on the same held-out
reflections. "Full" is the whole free set; "report" is one half of it, listed as a check that the gains are not on one
half only. **The baseline of every comparison is the re-refined deposited model**: S0001, the deposited model after the
harness's common recipe (phenix.refine, 10 macro-cycles, three seeds, the median). What plain re-refinement gives is
not credited to the agent. The deposited model as scored (S0000) is on each card for reference.

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

Status meanings:

- **improved**: the model in force has a lower full R-free than the re-refined deposited model (S0001) on the same
  flags, through steps the gate accepted one by one against a paired control.

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

Open the model with its maps in Coot:

```bash
coot targets/7KR0/model/7KR0_S0053.pdb --auto targets/7KR0/maps/7KR0_S0053_map_coeffs.mtz
```

A six-copy ensemble shows as altlocs A to F on every residue; Coot's altloc controls show one copy at a time. Load
`targets/7KR0/deposited/7KR0.cif` beside it to see the starting point; both are in the same frame.
`docs/HOW_TO_USE.md` has the rest: recomputing R-free on the flags, reading the step record, continuing the run.

## Method

One paragraph; `docs/METHOD.md` has the detail and the harness repository has the specification. Preprocessing fetches
the entry, removes a vault of 2 % of the work reflections from every working file, keeps the deposited free set
untouched, anonymises the model and refines it with three seeds to measure the noise floor. The run then applies one
change at a time: a refinement option, a water pick on a work-only difference map, the split into C copies, a
connectivity relabel, a Coot fit. Each change is refined beside a control (the parent refined with the same command
and seeds) and judged by one gate: R-free down by at least 2σ against the control, the gap not widened by more than
0.002 and under its cap, clashscore and outliers under their caps or not above the control's. An accepted change is
the new model in force; a refused one changes nothing. Every step is one line in a hash-chained record. The vault is
read once, at the end, as the leak check.

## Caveats that apply to every target

- R-free is comparable only on the same free set. Compare against the "re-refined, our flags" column (or the card's
  S0000 column), never the header.
- The gate's R-free is a few 10⁻⁴ above phenix.refine's logged value for the same model (all reflections kept, fresh
  scaling). Both arms of every step carry the same offset.
- A C-copy ensemble has C times the protein parameters of a single model. The gate's gap bound and cap are what keep
  it honest between vault reads; the vault read is the operator's and the card says when it was last done.
- Geometry numbers come from phenix.clashscore, rotalyze and ramalyze on the file as released, hydrogens kept.

## Provenance

`provenance.json` names the harness repository, branch and commits, the pod and the Phenix build, and the run handle
and step of each released model. The harness (`prism-science/autoresearch`, branch `manzuoni/hierarchical_refinement`)
holds the code, the specification (`docs/SPEC.md`) and the dated plan with every result (`docs/PLAN.md`).

## Refreshing this release

Copy the step's files from the run directory on the pod into `targets/<ID>/` as the card's file table lays them out,
run `python3 scripts/build_index.py` to rebuild `index.json` and `MANIFEST.sha256`, add a line to `CHANGELOG.md`, and
commit with the step id in the message. `scripts/verify_checksums.sh` checks every file against the manifest.

## Licence and citation

CC-BY-4.0 (`LICENSE`). Cite this repository (`CITATION.cff`) and the original PDB entry of each target; its primary
citation is in `targets/<ID>/deposited/rcsb_entry.json`.
