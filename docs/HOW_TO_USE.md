# How to use this release

Three levels, cheapest first: look at a model, check a number, continue the work.

## Look

Each target ships the model with the map coefficients its refinement wrote, so no recalculation is needed:

```bash
coot targets/<ID>/model/<ID>_refined.pdb --auto targets/<ID>/maps/<ID>_refined_map_coeffs.mtz
```

The MTZ carries `2FOFCWT/PH2FOFCWT` (2mFo−DFc) and `FOFCWT/PHFOFCWT` (mFo−DFc) as written by phenix.refine. To compare
with the starting point, load `targets/<ID>/deposited/<ID>.cif` alongside; both are in the same frame.

To see what the agent changed, `targets/<ID>/ledger/changes.csv` lists every proposed change with its selection
(chain, residue), type, gate values and verdict, and `ledger/cycles.csv` says which cycles were credited. The atom
and water counts on the card give the net effect.

## Check

### R-free on the frozen flags (needs Phenix)

```bash
phenix.python scripts/indep_rfree.py targets/<ID>/model/<ID>_refined.cif \
  targets/<ID>/data/<ID>_data.mtz targets/<ID>/data/<ID>_flags.mtz targets/<ID>/data/<ID>_split.mtz out.json
```

`out.json` reports R-work and R-free on the full, select and report sets, computed with cctbx on all reflections and
no outlier rejection; it should match `validation/release/rfree_indep.refined.json` to the digit and the campaign
ledger (`refinement/current.json`) to within 0.001 (the harness applies phenix.refine's Wilson outlier rejection; the
scorer does not). Run the same command on `deposited/<ID>.cif` for the deposited value on the same flags.

With the standard tool instead:

```bash
phenix.python scripts/merge_mtz.py targets/<ID>/data/<ID>_data.mtz targets/<ID>/data/<ID>_flags.mtz <ID>_merged.mtz
phenix.model_vs_data targets/<ID>/model/<ID>_refined.cif <ID>_merged.mtz
```

### The free set is the deposited one

`scripts/flag_identity.py` (needs gemmi and numpy) compares the free set in `<ID>_flags.mtz` with the `_refln.status
== 'f'` set of the deposited structure-factor file, and the amplitudes with `F_meas_au`. The deposited structure-factor
file is not in this repository (it is at RCSB; its SHA-256 is in `data/prep.json` as `sf_sha256`):

```bash
python scripts/flag_identity.py <ID> <ID>-sf.cif targets/<ID>/data/<ID>_data.mtz targets/<ID>/data/<ID>_flags.mtz
```

### Geometry

`validation/release/molprobity.refined.out` is the full `phenix.molprobity` report; the card shows its summary lines.
Re-run with `phenix.molprobity targets/<ID>/model/<ID>_refined.cif`.

### File integrity

```bash
scripts/verify_checksums.sh
```

## Continue

### Refine further on the same free set

Any comparison with the numbers here needs the same flags. Merge the frozen data and flags into one file and pass the
flag column explicitly:

```bash
phenix.python scripts/merge_mtz.py targets/<ID>/data/<ID>_data.mtz targets/<ID>/data/<ID>_flags.mtz <ID>.mtz
phenix.refine targets/<ID>/model/<ID>_refined.cif <ID>.mtz \
  refinement.input.xray_data.r_free_flags.label=R-free-flags \
  refinement.input.xray_data.r_free_flags.test_flag_value=0 \
  refinement.input.xray_data.r_free_flags.generate=False
```

Start from `refinement/command.txt` to reproduce the released model's protocol exactly. Two targets have standing
per-target overrides that matter: 3QUE refines water occupancies (`refinement.refine.occupancies.individual=water`)
and 3TC7 uses a fixed ADP weight (`optimize_adp_weight=False`, `wxu_scale=0.03`); both are in their `command.txt`.
Reproducing the R-free − R-work gap of 3TC7 needs that weight.

Judge a change the way the campaign did: refine the same base with and without it, same seed, and compare R-free on
the select half against σ_select in `ledger/noise_floor.csv`; confirm the sign on report.

### Reproduce a run from raw data

The harness and its documentation are in the campaign repository (`prism-science/agentic-refinement`); the
reproduction levels are described in `docs/campaign/REPRODUCE.md`. Level 0 (verify a number) needs only this
repository and Phenix. Levels 1–2 need the harness: `autoref prep` rebuilds `data.mtz` and `flags.mtz` from the RCSB
files and halts if their SHA-256 differ from the values in `data/prep.json`, so a rerun is on byte-identical data and
the identical free set.

## Machine-readable index

`index.json` has one record per target: entry metadata from RCSB, data and flag hashes, R-free of the deposited,
re-refined and released models on every set, composition, MolProbity summary, the credited cycles with their
attributable deltas, the thresholds version, the refinement protocol, the caveats and the file list with SHA-256.
