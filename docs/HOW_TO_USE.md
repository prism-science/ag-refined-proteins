# How to use this release

Three levels, cheapest first: look at a model, check a number, continue the work.

## Look

Each target ships the model with map coefficients computed from the work reflections only, so no recalculation is
needed:

```bash
coot targets/7KR0/model/7KR0_S0053.pdb --auto targets/7KR0/maps/7KR0_S0053_map_coeffs.mtz
```

The MTZ carries `2FOFCWT/PH2FOFCWT` (2mFo−DFc) and `FOFCWT/PHFOFCWT` (mFo−DFc). A six-copy ensemble shows as altlocs A
to F on every protein residue, each at occupancy 1/6; a lettered water belongs to one copy, a blank one to all six. To
compare with the starting point, load `targets/7KR0/deposited/7KR0.cif` alongside; both are in the same frame.

To see what the run changed, `targets/7KR0/refinement/steps.md` lists every step with its verdict, and
`refinement/score_history.txt` is the gate's own record: one line per step with the change, R-free before and after,
the margin in σ, R-work, gap, clashscore, rotamer outliers, atom and water counts and the verdict.

## Check

### R-free on the inherited flags (needs Phenix)

The released number comes from the harness gate. The same quantity from Phenix's own tool:

```bash
phenix.model_vs_data targets/7KR0/model/7KR0_S0053.pdb targets/7KR0/data/7KR0_data.mtz \
  f_obs_label=FP r_free_flags_label=R-free-flags
```

Expect a value a few 10⁻⁴ below the card's: Phenix rejects outliers and reports its own scales; the gate keeps every
reflection. Both the released model and the deposited model (`deposited/7KR0.cif`, on the same files) move by the same
offset. The flags file carries the deposition's flags unchanged; `data/prep.json` has the checksums of the source file
and the counts.

### Geometry

`validation/` holds the phenix.clashscore, rotalyze and ramalyze logs of the released file (hydrogens kept). To rerun:

```bash
phenix.clashscore targets/7KR0/model/7KR0_S0053.pdb keep_hydrogens=True
phenix.rotalyze  targets/7KR0/model/7KR0_S0053.pdb
```

On a six-copy model phenix.clashscore's reduce step can exceed Phenix's built-in 120-second limit for larger ensembles;
the harness runs it through a wrapper that raises that limit (`tools/lib/phenix_wrap.py` in the harness).

### Checksums

```bash
bash scripts/verify_checksums.sh
```

## Continue

The harness is `prism-science/autoresearch`, branch `manzuoni/hierarchical_refinement`. On its pod
(`docs/POD.md` there), with the run directory restored from `refinement/` and `data/`, every tool takes `--run RUN
--parent S0053` and prints the facts line of the step it judged:

```bash
source /opt/phenix/phenix_env.sh
phenix.python tools/water_addition.py pick --run RUN --parent S0053 --sigma 2.5 --nproc 6
phenix.python tools/refine_step.py converge --run RUN --parent S0053 --nproc 6
```

`scripts/chain_target.sh RUN` runs the whole lever order that produced this model on any preprocessed run. The vault
read (`score_model.py vault-read`) is the operator's: it scores the model in force against the held-out reflections and
logs the read; the harness denies it to agents and a file `RUN/VAULT_HOLD` blocks it.
