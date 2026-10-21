# Method

How the released models are produced, in enough detail to read the per-target records. The governing document is the
harness specification, `docs/SPEC.md` in `prism-science/autoresearch` (branch `manzuoni/hierarchical_refinement`); the
dated results are in `docs/PLAN.md` there. This page orients.

## Inputs

For each PDB entry the harness fetches the deposited coordinate file and the deposited structure factors from RCSB
(`targets/<ID>/deposited/`) and builds the working reflection files (`targets/<ID>/data/`, with `prep.json` recording
every choice):

- `<ID>_data.mtz`: the observed data. Amplitudes where the deposition carries them, merged intensities where it
  deposited only intensities (phenix.refine applies French-Wilson). Rows without a measured value are not reflections;
  the counts in `prep.json` are the ones phenix.refine and the gate extract.
- `<ID>_flags.mtz`: the free-reflection flags, inherited unchanged from `_refln.status`. Column `R-free-flags`, test
  value 0. The flags are never regenerated, resized or moved, and no refinement uses all data.
- `<ID>_split.mtz` / `split.json`: the free set split at random into two halves, *select* and *report*. The gate judges on
  the full free set; the report half is listed on the card as a check that the decisions did not fit one half.
- The vault: 2 % of the work reflections, chosen at random, removed from every working file before anything else runs.
  No refinement, map, decision or score sees them until the operator reads the vault one time, at the end, to confirm
  that the R-free gains are not a leak. The card says when the vault was last read.

The model is anonymised (atoms only, no header) and refined with the common recipe and three seeds. The standard
deviation of R-free over the seeds is the run's noise floor σ. These are steps S0000 (the deposited model scored on
the working data) and S0001 (the median seed). S0001 is the baseline of every comparison in this release: a gain is
counted only above what the common recipe alone gives the deposited model (operator, meeting of 2026-10-21). S0000 is
on each card for reference.

## The common recipe

phenix.refine, 10 macro-cycles, individual sites and ADPs, water occupancies, riding hydrogens, no NQH flips, fixed
seed, fixed restraint weights (wc 0.5, wu 1.0 until a weights step is accepted; then the accepted values stand for every
later arm), the deposited flags, no resolution or sigma cutoff. Every command line is recorded before it runs and
checked for anything that would regenerate or ignore the flags.

## One change, one step

The run applies one change at a time to the model in force:

- refinement options: more macro-cycles, anisotropic ADPs for waters or protein, restraint weights, altloc occupancies,
  individual hydrogens;
- solvent: waters picked at a peak height on the mFo−DFc map of the work reflections only, one lettered water per
  peak at 1/C occupancy in the copy it clears (shared when it clears every copy); hygiene; clash fixes that move a
  water to a copy it clears;
- the split into C copies of every protein residue (a representation change, scored and recorded as BUILD, not judged:
  its R-free is not comparable with the single model's);
- connectivity: Untangler's relabel of which atoms belong to which copy, the waters following their copies;
- Coot: auto-fit rotamers on the residues under the strongest difference peaks; population moves between copies.

Each change is refined beside a control: the parent model refined with the same command and the same seeds. The gate
(`score_model.py`) scores both arms with a fresh cctbx fmodel on all working reflections and judges the median seed:

- R-free falls by at least 2σ against the control;
- the gap R-free − R-work widens by at most 0.002 and stays under the run's cap (the first refinement's gap plus 0.005,
  never below 0.03);
- clashscore at or under 15, or not above the control's; rotamer outliers 1.5 %, Ramachandran outliers 0.5 %, bond and
  angle RMSD 0.020 Å and 2.0° the same way.

A geometry step (a relabel, a clash fix, a Coot regularisation) is accepted when R-free is not worse than +2σ and the
clashscore is 10 % below the control's. An accepted step is the new model in force, the median seed of its candidate
arm, never the best seed. A refused step changes nothing. An accepted lever is repeated until it is refused.

## The record

Only the gate writes a step. Each step is a folder (model, change record, score record) and one line in
`score_history.txt`, hash-chained to the line before it; the scorecard has one row for each scored model. The released
model is the model in force at the step named on the card; the card's numbers are read from that step's score record.
