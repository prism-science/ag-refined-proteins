# Method

How the released models were produced, in enough detail to read the per-target records. The governing documents are
the campaign's own, frozen under `docs/campaign/` (PROTOCOL.md for the rules, SPEC.md and SPEC_DPDB_RUNS.md for the
implementation); this page only orients.

## Inputs

For each PDB entry the agent fetched the deposited coordinate file, the deposited structure factors and the sequence
from RCSB (`targets/<ID>/deposited/`), and built two frozen reflection files from the structure factors
(`targets/<ID>/data/`, with `prep.json` recording every choice):

- `data.mtz`: the observed data. Amplitudes (`FP,SIGFP` from `_refln.F_meas_au`) where the deposition carries them;
  merged intensities (`IMEAN,SIGIMEAN`) where the entry deposited only intensities. Rows the depositor marked unmeasured are dropped.
- `flags.mtz`: the free-reflection flags, inherited unchanged from `_refln.status` (`f` = free). Column
  `R-free-flags`, test value 0. The campaign verified that the free set is identical to the deposited one
  (`validation/campaign/checks/`, gate G3, and `scripts/flag_identity.py`).
- `split.mtz` / `split.json`: the free set split at random into two halves of equal size, *select* and *report*.

The flags were never regenerated, resized or moved for the whole campaign, and no resolution or sigma cutoff was
changed to move R-free (PROTOCOL §3). The harness's refinement wrapper refuses commands that would.

## Select and report

Automated accept/reject decisions read R-free on the *select* half only. The *report* half is never consulted by a
decision; it is the number to quote, together with the full set. A gain on select whose report half worsens beyond
2σ is refused as selection bias (thresholds v7 onwards, D497). The number of select consultations per target is in
`ledger/rfree_consultations.csv`.

## Noise floor

Before any change is judged, the deposited model is re-refined ten times with different random seeds under the
standing protocol (5 macro-cycles, `validation/campaign/noise_floor.json`). The standard deviation of R-free over the
seeds, on each set, is the noise floor σ. The credit bar is k·σ_select with k = 2 (`ledger/noise_floor.csv`). For
3TC7 the floor was re-measured under the hydrogen-bearing, fixed-ADP-weight protocol that its released model uses
(`noise_floor_h_wxu003.json`).

## Proposal and local gates

Each cycle the driver proposes changes by class: water additions and removals, alternate conformations added or
pruned, peptide flips, rotamer fixes, zone real-space refinement in Coot, and refinement-protocol changes (hydrogens,
ADP model, weights, TLS grouping). Every change is gated locally before it can be kept: real-space correlation of the
changed atoms and their neighbours against the map (with a floor for removed atoms), geometry within tolerance, no new
altloc-aware clashes, occupancy sums asserted. From thresholds v5 (D480) a kept change is also refined in reciprocal
space with only its own atoms moving, paired against the unchanged base, and dropped if worse than +2σ_select. Every
proposed change is a row in `ledger/changes.csv` with its gate values and verdict.

## Paired cycle and credit

Kept changes are judged in a paired cycle: the same base model refined twice with the same seed, once with the changes
(candidate arm) and once without (null arm). The attributable ΔR-free-select is candidate minus null. Verdicts:

- **credited** (`accepted` in `ledger/cycles.csv`): attributable Δ ≤ −k·σ_select, the report half not worse beyond
  2σ_report, the R-free − R-work gap not wider than the null's by more than 2σ_gap (D495), whole-model geometry
  recorded (a `geometry_flag` if a frozen cap is broken, D479);
- **regressed**: Δ > +k·σ_select; the change set is bisected to find the culprit (`ledger/bisections.csv`);
- **no_change**: within ±k·σ; under thresholds v8 a within-noise-but-worse candidate is kept with probability
  exp(−Δ/σ_select) from a recorded deterministic draw (Metropolis rule, D499), bounded by a drift guard.

The standing model (`refinement/current.json`) moves only on a credit (D484), and only if the credited model is not
worse than the standing record on select and not worse on report beyond 2σ_report (D499, D508). A credit is relative
to the run's own null arm, not to the deposited file: a target can be credited and still be above the deposited model
recomputed on these flags (4QO4 in the 2026-10-03 release).

## What "re-refined, no changes" measures

The mean full R-free of the ten noise-floor seeds is what phenix.refine alone does to the deposited file under the
campaign's protocol (individual sites and ADPs, occupancies of partial atoms, TLS where the resolution or chain length
calls for it, riding hydrogens where the model has them, weight optimisation, 5 macro-cycles; `refine_decisions.json`
records the per-target choice). The difference between that and the released model is the agent's own contribution.
For depositions refined in CNS, REFMAC or X-PLOR the re-refinement itself moves R-free by a lot, in either direction,
and the ten seeds spread according to how far the model is from Phenix's minimum rather than according to test-set
noise (D506). That is why several phase-2 targets credited nothing although their released model is far below the
deposited value.

## Acceptance rule under revision

PROTOCOL §4.3–4.4 were rewritten on 2026-09-17, while the phase-2 runs were in flight, to define acceptance against a
per-class sham null (≥ 50 unsupported changes through the identical restricted paired protocol; 99th-percentile
threshold; Benjamini–Hochberg at FDR 0.05) instead of k·σ. The harness does not implement it and every verdict in this
release is a k·σ verdict (D507). Quote acceptances with that qualification.

## Verification

Every headline number was re-derived by a scorer that shares no code with the harness (`scripts/indep_rfree.py`: cctbx
fmodel on all reflections, no outlier rejection, manual R over work, free, select and report) and by
`phenix.model_vs_data`; the campaign's runs are under `validation/campaign/verify_*/` and the release-time runs under
`validation/release/`. Agreement with the ledger is within 0.001 on every target.

## Programs

Phenix 2.1-6048 (the campaign's single pinned image) for refinement, maps, validation and scoring; Coot 1.3.3 through
its Python API for real-space changes; qFit 2025.4 for some alternate-conformation proposals; gemmi 0.7.5 for the data
files. The roster with each tool's validation status is in the campaign ledger (`roster` table).
