# ag-refined-proteins

Crystallographic models refined by an autonomous harness (the *autoresearch* project, Astera Institute), released with
what is needed to use, check and extend them: the model, the map coefficients, the working data and the inherited
free-reflection flags it was scored on, the deposited model it started from, and the complete step record of the run.

This branch is the starting point of the hierarchical refinement line (October 2026). It holds one target, 7KR0, the
SARS-CoV-2 NSP3 macrodomain at 0.77 Å, refined from the deposited file to a six-copy ensemble. The earlier campaign's
targets and records (the single-model line, August to October 2026) are on `main` and the `release-*` branches.
Nothing here is a ceiling: the run continues and this branch is a dated snapshot of the model in force.

## Results

Every model is scored on the R-free flags inherited unchanged from its deposition, by the harness gate (a fresh cctbx
fmodel on the working data, every reflection, no outlier rejection), so the numbers in a row are on the same held-out
reflections. "Full" is the whole free set; "report" is the half the gate never consults for a decision.

<!-- results-table:begin -->
| Target | Res. (Å) | Entry | Deposited, our flags (full / report) | This release (full / report) | Δ full | Gap (deposited → ours) | Clashscore, rotamer outliers % (deposited → ours) | Model | Status |
|---|---|---|---|---|---|---|---|---|---|
| [7KR0](targets/7KR0/README.md) | 0.77 | Crystal structure of SARS-CoV-2 NSP3 macrodomain (C2 crystal form, 100 K) | 0.1175 / 0.1189 | **0.0726 / 0.0740** | −0.0449 | 0.0071 → 0.0259 | 4.3, 0.9 → 7.7, 1.5 | six-copy ensemble, step S0053 | improved |
<!-- results-table:end -->

Status meanings:

- **improved**: the model in force has a lower full R-free than the deposited model on the same flags, through steps
  the gate accepted one by one against a paired control.

## What is in a target directory

```
targets/<ID>/
  README.md                 the card: the two models on the same flags, what the model is, caveats, files, reproduction
  model/<ID>_<step>.pdb     the released model (occupancies at four decimals) and .cif (mmCIF)
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
  refinement/metaparams.yaml, run.json   the run's fixed metaparameters and its state
  refinement/chains/             the scripts that scheduled the steps on the pod
  validation/                    phenix.clashscore, rotalyze, ramalyze logs of the released model
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

- R-free is comparable only on the same free set. Compare against the "deposited, our flags" column, never the header.
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
