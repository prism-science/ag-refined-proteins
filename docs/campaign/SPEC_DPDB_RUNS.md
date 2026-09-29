# SPEC — Loop v3: per-run campaigns to reproduce the Dynamic PDB improvements

**Status:** design + implementation, 2026-08-27. Builds on `SPEC_LOOP_V2.md` (the discrete, RSCC-gated
engine and the paired null-control cycle) and turns it into a **runnable, per-run, per-target campaign**.
Where this conflicts with SPEC_LOOP_V2 it wins; where either conflicts with PROTOCOL.md, PROTOCOL.md wins.

---

## 0. The goal, in numbers

Two Dynamic PDB entries are the operator's focus. Every number below is the literal output of a lookup
executed in the session that wrote this file (dynamicpdb.com, fetched 2026-08-27), or of `autoref status`
on the pod (`state/status/2026-08-27T0327Z.md`).

| target | Dynamic PDB entry | deposited (R-work / R-free) | published better model | method of the better model |
|---|---|---|---|---|
| **3TC7** (1.5 Å, P 31 2 1) | `entries/a937eeb3-1dfd-43a3-af1a-08675aad9807` | 0.158 / **0.193** | 0.138 / **0.163** | qFit multiconformer model |
| **3QUE** (2.7 Å, P 21 21 21) | `entries/e1231493-23e9-4110-b815-da94a2c17184` | 0.223 / **0.311** | 0.171 / **0.250** | ensemble refinement |

Our own pipeline (Phenix 2.1-6048, inherited flags, select/report split) currently stands at:

| target | our re-refined baseline (R-free full / report) | σ_select (10 seeds) | one cycle must beat | gap to published |
|---|---|---|---|---|
| 3TC7 | 0.188471 / 0.183577 | 0.001811 | −0.003622 | 0.0255 (≈ 14 σ) |
| 3QUE | 0.266801 / 0.271062 | 0.001440 | −0.002880 | 0.0168 (≈ 12 σ) |

**"Replicate the loss"** means three things, and each is reported separately:

1. **Close the gap.** Reach (or approach) the published R-free with a depositable model built by our loop.
2. **Attribute it.** Every unit of R-free bought must be traceable to a *named* change with its own row —
   this is the part Dynamic PDB does not give and the whole reason for gating per change.
3. **Fail honestly.** If the loop cannot reach the number, the run says how far it got, what it tried, how
   many configurations, and why it stopped. A stuck model is a result.

Two caveats travel with the table from the start (unchanged from SPEC_LOOP_V2 §6):

- 3QUE's deposited 0.311 is a REFMAC5 number; Phenix recomputes the same model/flags at 0.2871 (D008/D102).
  The **baseline for 3QUE is our 0.2668**, never the header, and the 0.311→0.2668 drop is *not* ours.
- 3QUE's published 0.25 came from **ensemble refinement**, a different model representation. Matching it
  with a multiconformer + TLS model is a stronger result; not matching it is not a failure of the loop.

---

## 1. The unit of work is a run

A **run** is one invocation of the loop on one target, with one identity, one directory, one structured
record, and one decision log. Nothing about a run is shared with another run except the campaign ledger
(which every run appends to) and the campaign's `current` model pointer (which a run *may* advance).

```
run_id  = <TARGET>.<UTC start, e.g. 2026-08-27T18:40:12Z>          (or --run-id, must be unique)
run_dir = $AUTOREF_RUNS/<TARGET>/runs/<run_id>/
```

```
runs/3TC7/runs/3TC7.2026-08-27T18:40:12Z/
  command.txt                 the exact argv + env that started the run
  run_state.json              checkpoint after every cycle (resume point)
  refinement_run.jsonl        append-only truth (SPEC_LOOP_V2 §3.1) — one line per event
  refinement_run.json         materialised view of the sidecar, rewritten atomically after every append
  DECISIONS.md                human-readable decision log, appended as the run goes
  run_summary.json            written at finish: start/final numbers, published target, gap closed, why stopped
  base/                       cycle 0: the re-refinement that produced the base model + map coefficients
  changes/<change_id>.cif     every candidate model, accepted AND reverted (SPEC_LOOP_V2 §3.2)
  cycles/c001/
    proposals/<stage>/        every proposer's raw output and its resolved parameters
    discrete/<change_id>/     apply/, rsr/, rscc_before/, rscc_after/, geometry/, change_result.json
    paired/                   null_arm/, candidate_arm/, paired_cycle.json
    bisect/                   (only on regression) one dir per bisection step + bisect.json
    escape/                   (only on stall) the escape refinement(s)
    cycle.json                everything the driver decided this cycle and why
  cycles/c002/ ...
```

A durable copy of `refinement_run.json` also lands in `$AUTOREF_STATE/runs/<run_id>.json`, so the record
survives even if the run directory is archived or lost. Killed runs are resumable: `run_state.json` holds
the last completed cycle, the current base model and map coefficients, the R-free history and the escape
ladder position; `autoref run-discrete --target T --resume <run_id>` reopens the sidecar and continues.

---

## 2. The driver, one cycle at a time

```
cycle 0 (base)      current model  ──refine──▶  base model + 2mFo−DFc / mFo−DFc coefficients
                    (skipped when the current model already carries map coefficients)

each cycle c ≥ 1
  1. RSCC table of the base model, once (phenix.real_space_correlation, detail=residue)   ~30 s
  2. for stage in LADDER:                                                                 (§3)
        changes = propose(stage, base, maps, rscc table)      → list[Change], ordered by evidence
        results += discrete.run_changes(changes, ...)         → ONE change at a time, RSCC-gated
        (the running model and its RSCC table advance after every accepted change)
  3. n = number of accepted changes
     n == 0  → single re-refinement of the base (advances the base; counts as a quiet cycle)
     n  > 0  → PAIRED cycle (SPEC_LOOP_V2 §1.3): null arm = base refined with no changes;
               treatment arm = model with the n changes refined identically (same seed, same params)
               attributable = R-free-select(treatment) − R-free-select(null)
  4. verdict on `attributable` against the frozen noise floor (k·σ):
        ≤ −k·σ            accepted   — changes credited; base ← treatment arm
        (−k·σ, +k·σ]      no_change  — NOT credited; counts toward convergence. attributable ≤ 0: changes stay
                                        (D411), base ← treatment arm. attributable > 0: base ← treatment arm with
                                        probability exp(−attributable/σ) (v8 Metropolis, D499), else ← null arm
        > +k·σ            regressed  — bisect the accepted set (SPEC_LOOP_V2 §1.3); culprits demoted to
                                        `rejected`; base ← best non-regressing subset, else the null arm
  5. stall check (§4): the last `stall.stall_cycles` cycles each accepted changes locally but moved
     R-free-select by less than σ → take the next rung of the escape ladder (one rung per cycle)
  6. convergence (PROTOCOL §4.6 via `stages.convergence`): three consecutive cycles with no *credited*
     cycle and |ΔR-free-select| within k·σ → stop; OR the escape ladder is exhausted → stop, and say so
     (a stop ends this run, not the target: the next action is a new line under PROTOCOL §17 / §4.6, never
     "the target is finished")
  7. checkpoint run_state.json; append DECISIONS.md; write cycle.json; advance `state/current/<T>.json` —
     only when the run has a credit (D484), its best base is not worse than the standing record on R-free-select
     (D499) and the deliverable's R-gap does not widen beyond deliverable_k·σ_gap (D495)
```

Every refinement in the loop goes through `autoref/tools/phenix_refine.py` (flag guard, semaphore, jobs
row). The paired cycle's two arms run concurrently (2 × nproc 1); with two targets running at once that is
the pod's four CPUs.

**Why the treatment arm becomes the base on `no_change`.** SPEC_LOOP_V2 §1.3 says the changes stay when
the cycle is within noise. A base that does not contain them would silently revert them. The cycle is still
not credited, so the convergence rule and the status table only count cycles that cleared k·σ. The drift
of un-credited cycles is tracked (`cumulative_uncredited` in `run_state.json`, printed in every cycle's
DECISIONS block) so a slow ratchet of sub-threshold cycles cannot hide: the moment it exceeds +k·σ the
driver **reverts to the last credited base**, rewrites every kept-uncredited change row to `rejected`
with the cumulative number as the reason, and resets. Nothing new is invented here — the bar is the same
k·σ, applied to the sum instead of the single cycle.

**Metropolis on the within-noise-but-worse band (thresholds_v8, D499).** D411 drew the keep/drop boundary at
attributable = 0. σ_select is the measured noise of exactly this comparison, so +0.5σ and −0.5σ are the same
evidence, and a hard zero is a bias toward the changes that were lucky on the consulted half; greedy descent on a
noisy objective stops at the first plateau (Marcus Collins's review, 2026-09-16). From v8 a `no_change` cycle with
0 < attributable ≤ k·σ keeps its treatment arm with probability p = exp(−attributable / T), T = `temperature_sigma`
· σ_select (1.0σ: no new constant), from a deterministic draw u = sha256(target, cycle, seed) that is written to
`paired_cycle.json`, `cycle.json` and DECISIONS.md with p. Nothing else moves: the credit bar, the regression bar and
its bisection, the R-gap gate, the select/report divergence gate, the geometry and clash gates, and promotion (credit
only). The walk is bounded by the drift guard above, which now fires after every Metropolis keep as well; the
last-credited pointer is the run's start base until the first credit, so the walk can never end below the start model
(a missing pointer falls back to the run's best base by R-free-select, tracked from cycle 0).
`autoref/metropolis.py` holds the rule; `paired.run_paired_cycle` applies it when the frozen thresholds carry
`paired.metropolis.enabled`.

**Promotion is a comparison, not a consequence of credit (D499).** A credit says the treatment arm beat *its own
null arm* by k·σ; it says nothing about the standing deliverable, which may have been reached by a different run or
protocol. `_promote` therefore refuses a credited run whose best base is worse than (or ties, from a different model) `state/current/<T>.json` on
R-free-select, or whose report half is worse than the standing record's beyond k·σ_report (D508), and writes a `PROMOTE-<T>-c<N>` / `PROMOTE-REPORT-<T>-c<N>` deviations row saying so. Of the thirteen credits on record
(2026-09-16), six never moved a deliverable: 3TC7 c058 (E029: better than its H-free null, worse than c057 on
report/full), 3TC7 c064 and c068 (deliverable gap bound, D495/D498), 7KR0 c017/c019/c021 (sampleworks distillation
experiments credited against their own null arms at 0.226/0.124/0.126 full, above the 0.113 deliverable).

---

## 3. The proposer ladder

Each stage returns a list of `Change`s (SPEC_LOOP_V2 §1.1: `change_id`, frozen `change_type`, exact
`selection`, `tool`, **every** `tool_params`, `apply_fn`). Proposers never refine; the engine does. A
proposer that fails writes a `defects` row and returns nothing — it never kills the run.

| stage | change_type | proposer (tool, evidence, order) | per-change gate (SPEC_LOOP_V2 §1.2 + D303) |
|---|---|---|---|
| `correction` | `rotamer_fix` | MolProbity rotamer outliers ∪ residues with RSCC < `geometry.rscc_outlier_protein`; Coot `auto_fit_rotamer` (D022: Coot's own status is *not* trusted) | mean ΔRSCC ≥ +0.01, neighbours, geometry, clashes |
| `correction` | `peptide_flip` | CaBLAM / Ramachandran outliers; Coot `flip_peptide_using_cid` | same |
| `solvent` | `water_remove` | waters with RSCC < `solvent.water_rscc_min` (0.70), ∪ Coot `check_waters` failures, worst first | removed residue must have been **below** the floor |
| `solvent` | `water_add` | `phenix.douse` ∧ Coot `find_waters` agreement within 1.0 Å (PROTOCOL §5.1), strongest peak first | added water must reach RSCC ≥ 0.70; no new clash |
| `protein_altloc` | `protein_altloc_prune` | conformers with occupancy < `altloc.occupancy_floor` (0.10); remaining letters rescaled to the group's sum | removed conformer below `altloc.conformer_rscc_min` |
| `protein_altloc` | `protein_altloc_add` | Ringer secondary sites (`altloc.ringer_secondary_sigma`), strongest first; **qFit per residue** (`qfit_protein --residue`), the multiconformer residue spliced into the model | new conformer(s) ≥ 0.70, neighbours, geometry, altloc-aware clashes |
| `adp_model` | `tls_regroup` | reciprocal-space parameterisation, tested as the **opposite** of what the base refinement has in force (read from its `refine_decisions.json`). Note: by the SPEC §6.1 rule TLS is *already on* for both targets (3QUE: d_min 2.7 ≥ 2.0; 3TC7: chain of 251 > 200 residues), so the toggle under test is TLS **off**. **No atom moves**, so there is no RSCC to gate; judged **only** by the paired R-free gate, as a one-change cycle, once per run; within noise it is *not* adopted (it has no local evidence of its own) | paired attributable ≤ −k·σ |

Default ladders (overridable with `--stages`):

- **3TC7** (1.5 Å, 1 altloc residue, 180 waters): `correction → solvent → protein_altloc`. The published
  model is qFit's; the third stage is where the gap should close, one residue at a time, with a row each.
- **3QUE** (2.7 Å, 0 altlocs, 14 waters, ligand 3FF, internal gap 177–182): `correction → solvent →
  adp_model → protein_altloc`. D028 named Asp176 (RSCC 0.54) as the first thing to fix. The `adp_model`
  cycle asks whether the ADP parameterisation the §6.1 rule chose (TLS on) is actually earning its
  parameters at 2.7 Å — the answer is a number either way. qFit last, because at 2.7 Å per-residue
  conformers are weakly determined. The ladder is read as: cycle 1 runs the stages *before* `adp_model`,
  cycle 2 is the `adp_model` toggle, every later cycle runs all real-space stages.

Per-cycle caps come from the frozen file: `discrete.max_changes_per_cycle` (40) accepted changes before a
reciprocal pass is forced. Proposers are also capped per cycle (`--max-per-stage`, default 20) so a cycle
does not spend hours on one stage; what was not attempted is listed by name in `cycle.json`.

---

## 4. Stall and escape (SPEC_LOOP_V2 §5, made concrete)

Stalled ⇔ the last `stall.stall_cycles` (2) real-space cycles each accepted ≥ 1 change locally **and**
each moved R-free-select by less than σ. Then, one rung per cycle, stopping at the first that clears
**−k·σ** against the base (a paired comparison: both the escape refinement and the base's own
re-refinement start from the same model). The stall window restarts after an escape rung: a rung that
cleared has moved the minimum, and a rung that failed is followed by the next rung directly.

1. `reweight_reseed` — different `random_seed`, fresh weight optimisation, +3 macro-cycles.
2. `rescale_bulk_solvent` — `bulk_solvent_and_scale.mode=slow` (re-fits solvent and anisotropic scale from
   scratch rather than from the last state).
3. `simulated_annealing` — **refused by the guard when the model carries altlocs** (PROTOCOL §4.1); the
   ladder records the refusal and skips.

Every rung is a `changes` row of type `weight_change` (tool `phenix.refine`, `tool_params` = the parameter
diff), so "how many configurations were tried" is a count, not a recollection (PROTOCOL §4.5). A rung
that clears the bar makes its parameters the run's defaults from then on.

---

## 5. What every run writes, and where the numbers come from

- `refinement_run.json` — SPEC_LOOP_V2 §3.1, with `changes[]` (accepted and reverted), `cycles[]`,
  `tool_invocations[]` (resolved parameter files copied under `params/`), inputs with sha256, the frozen
  noise floor, the thresholds file and its hash.
- `DECISIONS.md` — one block per cycle: what was proposed, what passed RSCC and why the rest did not, the
  two arms' R-free, the attributable delta against k·σ, the verdict, bisection culprits, stall/escape.
- Ledger rows: `changes` (one per change), `cycles` (one per cycle, `stage=rerefine`), `bisections`,
  `defects`, `jobs`, `rfree_consultations` (each bisection step and the treatment arm consult
  R-free-select; the null arm does not — it is a control, not a decision).
- `state/current/<T>.json` advances to the run's base when `--promote` (default) — the next run starts
  where this one ended.
- Headline numbers are **R-free-report** and **R-free-full**; **R-free-select** is read only by the gates.
  Status posts come only from `autoref status`.

---

## 6. Running it on the pod

```
# once per target (already done for 3TC7 and 3QUE — dossier, verify, noise floor, baseline all exist)
# per run:
export AUTOREF_THRESHOLDS=/home/dev/workspace/autoref/thresholds_v2.yaml
nohup /home/dev/envs/autoref/bin/python -m autoref run-discrete --target 3TC7 --max-cycles 8 \
      > /home/dev/runs/3TC7.run-discrete.$(date -u +%Y%m%dT%H%M%SZ).log 2>&1 &
nohup /home/dev/envs/autoref/bin/python -m autoref run-discrete --target 3QUE --max-cycles 8 \
      > /home/dev/runs/3QUE.run-discrete.$(date -u +%Y%m%dT%H%M%SZ).log 2>&1 &
```
`scripts/run_dpdb.sh <TARGET> [--max-cycles N] [--stages a,b,c]` wraps exactly that and prints the run
directory. Progress: `autoref runs --target 3TC7` (lists runs, cycles, current numbers) and
`tail -f <run_dir>/DECISIONS.md`.

Cost model (measured on this pod, D304/D031/literature notes): one full refinement ≈ 550–660 s (3QUE),
one RSCC table ≈ 30 s, one discrete change ≈ 40 s + the proposer's own cost (qFit per residue: minutes).
A cycle with 20 changes and a paired refinement ≈ 25–40 min; a 3TC7 cycle with 20 qFit residues ≈ 1.5 h.

---

## 7. Acceptance criteria for this spec's implementation

1. `autoref run-discrete --target 3TC7` runs end-to-end on the pod, produces the §1 layout, and every
   number in `run_summary.json` re-derives from `refinement_run.jsonl`.
2. Every accepted change has a `changes` row with RSCC before/after, neighbours, local geometry, clash
   result, model hashes and a candidate file that opens.
3. The paired gate never credits a cycle whose null arm explains the drop (D034 cannot recur).
4. Killing a run and resuming it produces one contiguous record (`rebuild.truncated_tail` at most once).
5. Unit tests cover the driver's verdict logic, the stall/escape ladder, the per-run layout, resume, and
   the qFit-splice `apply_fn` on a fixture — with every external tool mocked, nothing else.
6. Reported: for each target, start → final R-free (report + full), the published number, the fraction of
   the gap closed, the list of credited changes, and the honest reading of the ensemble caveat.

---

## 8. Implementation map

| file | role |
|---|---|
| `autoref/stages/run_discrete.py` | the §2 driver: run identity, layout, cycles, verdicts, stall, convergence, checkpoint/resume, DECISIONS.md, run_summary.json |
| `autoref/stages/proposers.py` | the §3 proposers → `list[Change]`; the qFit residue splice; rotamer/flip/water factories |
| `autoref/stages/escape.py` | the §4 stall detector and escape ladder (pure logic + parameter diffs) |
| `autoref/stages/paired.py` | extended: `no_change` vs regression, `next_base` per §2, map coefficients of each arm, per-arm parameter overrides (for `adp_model` and escape rungs) |
| `autoref/stages/discrete.py` | extended: `changes_dir` so candidate files live under the run; water removal deletes in place (D406a); local refinement is now selection-only |
| `autoref/cctbx/local_rsr.py` + `tools/real_space.py::refine_selection` | **D406c**: real-space refinement of *only* the selection with the whole model's restraints and every other atom fixed (`mmtbx individual_sites.easy`), replacing the cut-and-splice that strained every boundary bond; ~4 s per change instead of ~60 s |
| `autoref/tools/qfit.py` | **D406b**: accepts qFit's `--residue` output names (`C_N_qFit_residue.pdb`); **D423**: also `.cif` output names (qFit writes in the format of its input) and `restore_hetero_residues` for ligands qFit renames; **D433**: `_as_pdb_for_qfit` — qFit 3's mmCIF reader raises `KeyError` on any model carrying a `_struct_conn` loop |
| `autoref/cctbx/local_rsr.py` (weight scan) | **D407**: the local refinement's map weight is chosen as the largest on a grid whose *local* bond/angle RMSD stays within the gate's own budget (pre-change RMSD + `rel_max`), measured on the pre-change model — the gate defines the geometry budget, the refinement searches inside it |
| `autoref/stages/proposers.py::splice_qfit_residue` | **D408**: raw per-residue qFit occupancies (sums 0.66–0.78 measured) are rescaled to the residue's group sum, as qFit's segment step does for whole-protein runs; refused below 0.5 |
| `autoref/runlog.py` | extended: `run_dir` so the record lives under the run |
| `autoref/cli.py` | `run-discrete`, `runs`, `change` |
| `scripts/run_dpdb.sh` | pod launcher |
| `autoref/stages/paired.py::PairedArmError` | **D423**: an arm whose refinement wrote no model fails with the phenix log path, not a `TypeError` |
| `autoref/stages/run_discrete.py::_promote` | **D423**: the campaign model is the run's **best** base, not its last (quiet cycles drift inside k·σ) |
| `autoref/report/status.py::aggregate` | **D427**: the status table reports the campaign model and the best *credited* cycle; a `MIN` over all cycle rows had surfaced a rejected experiment arm as a target's best |
| `autoref/stages/run_discrete.py::_finish` | **D430**: no gap is reported against a published R-free measured on a different free set (`published_better.comparable_to_our_flags: false`) |
| `autoref/cctbx/ensemble_rfree.py` (+ `ensemble_rfree_probe.py`) | **D425**: R-free of a multi-model ensemble, with bulk-solvent masks averaged over the members — a single union mask reads 0.30 where the program reads 0.25; validated against a third party's ensemble to 0.002 (**D431**) |
| `scripts/experiments/` | the batch-change experiments: whole-protein qFit run/judge/gate-legs/prune (**D424**, **D426**, **D428**, **D429**), solvent as one batch (**D432**), published models scored on our flags (**D430**, **D431**), the neighbour-rule diagnosis and its RSCC noise floor |
| `tests/test_run_discrete.py`, `tests/test_escape.py`, `tests/test_proposers_v3.py`, `tests/test_qfit_tools.py`, `tests/test_paired_arm_error.py` | the §7(5) tests |

Nothing in `thresholds_v2.yaml` changes. No new numeric constant is introduced by this spec: caps and
floors are the frozen v2 values; the only new knobs are run-shape arguments (`--max-cycles`,
`--max-per-stage`, `--stages`) that bound *how much* is attempted, never *what passes*.
