# SPEC — Loop v2: discrete changes, RSCC-gated

**Status:** design, 2026-08-26. Supersedes SPEC.md §6 (change-set evaluation) and deviation D004.
Operator source: Stephanie's notes, relayed 2026-08-26. Where this conflicts with SPEC.md, this wins;
where it conflicts with PROTOCOL.md, PROTOCOL.md still wins.

---

## 0. What changes and why

SPEC v1 evaluated a whole stage's worth of edits as one batch against ΔR-free, because a single water's
effect on R-free is far below the noise floor (D004). That was a workaround for the wrong question.

**The fix: judge each change by whether it fits the density better, and judge the accumulation by R-free.**

> "make one change, refine, log results — discrete changes, log each change … instead of change in
> real space → refine → R-free improve?, check to make sure if it's fitting to RSCC better per change.
> **RSCC is the gate for refinement.**"

RSCC (real-space correlation coefficient) is the correlation between the density the model predicts at a
residue and the density the experiment actually shows there. It is *local*, so it is measurable for one
residue; it is *cheap*, so it can run per change; and it cannot be improved by adding parameters somewhere
else in the structure. It is the right per-change gate. R-free stays as the per-cycle gate — the check that
the accumulated locally-good changes actually explain the data globally.

This also matches PROTOCOL §1.2, which already said it: *"If the change does not improve RSCC, reverse it
and make another change."* v1 did not implement that literally. v2 does.

---

## 1. The two-tier loop

```
per change  (seconds)                          per cycle  (minutes)
─────────────────────                          ──────────────────────
pick ONE change from the work list             full reciprocal refinement (phenix.refine)
apply it                                       evaluate R-free-select vs the frozen noise floor
local real-space refine of that region only    if worse than −k·σ: bisect the accepted set, revert losers
measure RSCC of affected residues, before/after re-measure RSCC globally
GATE: RSCC improved AND geometry sane          write the cycle row + the run log
      AND no new altloc-aware clash
keep → commit; else → revert
log the change either way, with its numbers
```

**Why two tiers.** A full reciprocal refinement is 560–660 s on this hardware; there may be hundreds of
candidate changes per target. Gating each one on a full refinement is impossible, and gating a batch on
R-free hides which member of the batch was the good one. Local real-space refinement of one region costs
seconds, so every change gets its own measurement and its own row.

### 1.1 Per-change contract

| field | meaning |
|---|---|
| `change_id` | stable, deterministic: `<target>.c<NNN>.<type>.<selection-slug>` |
| `change_type` | frozen vocabulary (SPEC §3.5), one token |
| `selection` | the exact atom selection the change touches |
| `tool` + `tool_params` | **every parameter** of the tool that produced it, verbatim |
| `rscc_before` / `rscc_after` | for the changed residue(s) and every residue within 5 Å |
| `rscc_delta` | the gate value |
| `geometry_before` / `geometry_after` | bond/angle RMSD, clashes, local only |
| `verdict` | `accepted` \| `reverted` \| `ambiguous` |
| `reason` | why, in words, when reverted |
| `model_before_sha256` / `model_after_sha256` | provenance |

**Site-restricted reciprocal check (D480, thresholds_v5).** A change that passes the RSCC, neighbour, geometry, clash and occupancy legs is then refined in reciprocal space with only its selection moving (`refinement.refine.sites.individual`, ADP/occupancy selections to match, TLS off, `discrete.local_reciprocal.macro_cycles` = 8, standing weights), paired against the same restricted refinement of the unchanged base on the frozen flags. The candidate arm's R-free-select is a consultation (§3.6). Attributable Δ worse than `+bound_k·σ_select` → the change is dropped (`mode: gate`); otherwise it is kept. The pair is a judge: the model in force stays the real-space candidate (the restricted arm is kept as an artifact), because a no-TLS pass on a TLS-bearing model regresses R-free common-mode (D418). Credit is still only given by the full paired cycle (§1.3), which now runs after `discrete.max_changes_per_cycle` = 5 kept changes.

### 1.2 The RSCC gate

Accept the change when **all** hold:

1. `mean(rscc_after) − mean(rscc_before) ≥ rscc_min_delta` over the changed residues.
2. No neighbouring residue (within 5 Å, unchanged by this edit) drops by more than `rscc_neighbour_drop_max`
   — a change that fits itself by stealing density from its neighbours is not an improvement.
3. Local geometry within tolerance (bond/angle RMSD on the touched residues).
4. No new altloc-aware clash introduced (SPEC §12 + `clash_sweep`).

Frozen in `thresholds_v2.yaml`:

```yaml
discrete:
  rscc_min_delta: 0.01           # a change must improve local fit by at least this
  rscc_neighbour_drop_max: 0.02  # and must not degrade a neighbour by more than this
  neighbour_radius_a: 5.0
  local_refine: real_space       # coot | real_space
  max_changes_per_cycle: 40      # before a full reciprocal pass is forced
  bisect_on_rfree_regression: true
```

### 1.3 The per-cycle R-free gate — **paired against a null control**

> **Amended 2026-08-26 after the first real cycle turned out to be a false positive (D034).** The original
> rule compared the post-change refinement against the base model's *prior* R-free. Those two states differ
> by more than the changes: the post-change model also received another full refinement, which lowers R-free
> on its own. Measured on 3QUE: a no-change re-refinement of the same base moved R-free-select by −0.001994,
> while the four-water cycle moved it by −0.002886. Only **−0.000892 (0.62σ)** was attributable to the
> waters — but the cycle had "passed" a −0.00288 threshold. 69 % of the apparent gain was the refinement.

Every cycle is therefore a **paired comparison**, and both arms start from the identical base model:

```
base model ──┬── refine (no changes)          → r_free_select_null      ← the control arm
             └── apply accepted changes,
                 refine (same seed, params)   → r_free_select_candidate ← the treatment arm

attributable = r_free_select_candidate − r_free_select_null      ← the ONLY number the gate reads
```

- Accept the cycle when `attributable ≤ −k·σ`. The raw drop from the base is recorded but never gated on.
- The control arm's output **becomes the next cycle's base**, so the second refinement is not wasted work:
  it is the same model, better converged, and the baseline advances monotonically without any model change
  being credited for it.
- Cost is two refinements per cycle instead of one (~1 100 s on 3QUE rather than ~550 s). That is the price
  of the number meaning what it says.

After the accepted changes of a cycle, run the full reciprocal refinement and evaluate `r_free_select`.

- Improvement beyond `k·σ` → cycle accepted, all its changes stay.
- Within noise → cycle recorded as `no_change`; the changes stay (they improved local fit and did not hurt
  the global metric) but the cycle counts toward convergence.
- **Regression beyond `k·σ` → bisect.** Split the accepted changes in half, re-refine each half, keep the
  half that does not regress, recurse. Every bisection step is logged. This is how a locally-good change
  that is globally wrong gets caught and named, instead of being buried in a batch.

---

## 2. Inputs

| input | what it is | what we do with it |
|---|---|---|
| `model` (`.cif` / `.pdb`) | the starting atomic model | the parameters to refine |
| `structure factors` (`-sf.cif` / `.mtz`) | the measurements | the data to fit |
| `fasta` | **the construct** — what the crystallographer actually put in the drop | ground truth for what *should* be in the model |
| R-free flags | inherited, frozen | never regenerated (PROTOCOL §3) |

### 2.1 The FASTA is not decoration — it is the work list

The construct sequence says what molecule was in the crystal. The model says what somebody managed to
build. **The difference is the rebuild target**: loops and disordered regions that were never modelled.

`autoref gaps --target T` produces the work list, and it must classify, because the two kinds are not
equally interesting (measured 2026-08-26):

| target | unbuilt | classification |
|---|---|---|
| 3TC7 | 7 residues | Met1 + a six-residue C-terminal His-tag → **terminal, ignore** — purification tags are genuinely absent, not missing |
| 3QUE | 17 residues | Gly1–Glu4 terminal, **plus an internal gap from Asp177** → the internal run is a real disordered loop and a real rebuild candidate |

Classification rule: a gap is `internal` when built residues exist on both sides in the same chain,
`terminal` otherwise. Only `internal` gaps enter the work list; `terminal` ones are recorded and skipped
with the reason. Any gap flanked by residues whose density is itself poor is downgraded to `deferred`.

### 2.2 Molecular-replacement starting models

Per the operator: MR models are the interesting hard case — they start around R-free 0.35, and a large
part of the model may be misplaced or mis-sequenced. For an MR input the loop starts with a correction
phase (register shifts, backbone rebuild) before solvent or alternate conformations are considered at all.
Adding waters to a wrong backbone is how you make a bad model unfixable.

---

## 3. Outputs

### 3.1 `refinement_run.json` — one per run, the single structured record

```jsonc
{
  "run_id": "3QUE.2026-08-26T19:40:00Z",
  "target": "3QUE",
  "inputs": {
    "model":   {"path": "...", "sha256": "...", "format": "mmcif"},
    "sf":      {"path": "...", "sha256": "...", "columns_used": "FP,SIGFP"},
    "fasta":   {"path": "...", "sha256": "..."},
    "flags":   {"path": "...", "sha256": "...", "n_free": 864, "free_value": 0},
    "split":   {"path": "...", "sha256": "...", "n_select": 432, "n_report": 432}
  },
  "hyperparameters": {"macro_cycles": 5, "seed": 1, "k_multiple": 2.0, "rscc_min_delta": 0.01,
                      "thresholds_file": "thresholds_v2.yaml", "thresholds_sha256": "..."},
  "noise_floor": {"sigma_select": 0.00144, "accept_threshold": -0.00288, "n_seeds": 10},
  "gaps": {"internal": [...], "terminal_skipped": [...]},
  "tool_invocations": [
    {"seq": 1, "tool": "phenix.refine", "version": "2.1-6048", "argv": [...], "params": {...},
     "cwd": "...", "exit_code": 0, "wall_clock_s": 561.2, "log": "...", "outputs": [...]}
  ],
  "changes": [ /* the §1.1 record, one per change, accepted AND reverted */ ],
  "cycles":  [ /* per-cycle R-free, bisections, verdicts */ ],
  "outputs": {
    "final_model": {"path": "...", "sha256": "..."},
    "maps": {"path": "...", "sha256": "..."},
    "per_change_models": "runs/3QUE/changes/",
    "archive": {"path": "...", "sha256": "..."}
  },
  "result": {"r_free_start": 0.2862, "r_free_final": null, "r_work_final": null,
             "published_target": 0.25, "reached_target": null}
}
```

Written incrementally (append-safe) so a killed run still has everything up to the kill, and re-readable by
the next process. It is the file you hand someone who asks "what exactly did this do?".

### 3.2 Everything else

- **Every add or remove is logged** — one `changes` row per water, per conformer, per rebuilt residue,
  accepted or reverted, with its RSCC numbers.
- **Every tool invocation saves its parameters** — not just the command line: the resolved parameter set
  (phenix `.eff`, qFit's params file, the Coot script), copied into the run directory.
- **Changed CIF files** — the model after each accepted change under `runs/<target>/changes/<change_id>.cif`,
  plus the per-cycle model. Reverted changes keep their candidate file too, so a rejection is inspectable.

---

## 4. Building: Coot first

Per the operator: *use Coot as much as possible.* Coot's real-space tools take a zone — one residue or a
multi-residue stretch — which is the granularity this loop needs (a strained or mis-traced segment is a
stretch, not a residue; Jaime Fraser, 2026-09-07), and they are fast enough to gate per change: a five-residue
refine / regularize / refine round takes about a second (D477).

| job | first choice | fallback |
|---|---|---|
| rotamer correction | Coot `auto_fit_rotamer` | phenix.real_space_refine on the residue |
| peptide flip | Coot `flip_peptide_using_cid` | — |
| water placement | Coot `add_waters` **and** `phenix.douse`, combination rule (PROTOCOL §5.1) | — |
| water pruning | Coot `find_water_baddies` | phenix retention criteria |
| loop rebuild into a gap | Coot fit-loop / `phenix.fit_loops` | leave unbuilt, record why |
| alternate conformations | qFit proposes, Coot verifies each one | — |
| local real-space refine | Coot refine zone alternated with regularize zone (`coot.refine_zone`, D477; map weight recorded) | mmtbx selection-only refinement (D406); `phenix.real_space_refine` cut+splice |
| zone rebuild | `zone_rsr` proposer: ±2-residue zones around rotamer / Rama / CaBLAM / Cβ / omega outliers and RSCC < 0.70 residues, merged, ≤ 9 residues | — |

**Measured caution already in hand:** Coot's `auto_fit_rotamer` returned success while dropping a residue's
RSCC from 0.969 to 0.653. Coot proposing is not Coot being right — which is the entire argument for the
RSCC gate rather than trusting a tool's own status code.

---

## 5. Hyperparameters and escaping a stuck minimum

| knob | default | when it moves |
|---|---|---|
| `macro_cycles` | 5 | raise for a badly-placed (MR) start, lower for a converged model |
| `seed` | recorded per run | varied only for the noise floor |
| `wxc_scale` / weight optimisation | phenix grid | number of trials recorded |
| `rscc_min_delta` | 0.01 | frozen |

**The stall rule.** Per the operator: *"if only seeing tiny little drops then reset minima in reciprocal
space."* Formally — if the last `stall_cycles` (default 2) full cycles each produced |ΔR-free-select| < σ
while changes were still being accepted locally, the model is in a local minimum that small edits cannot
leave. The escape, in order, stopping at the first that clears σ:

1. Re-run the reciprocal refinement with a fresh weight scan and a different seed.
2. Re-optimise the bulk-solvent and overall anisotropic scaling from scratch rather than from the last state.
3. Simulated annealing — **only** if the model carries no alternate conformations (PROTOCOL §4.1 forbids SA
   after altlocs are built; the guard in `phenix_refine.py` enforces it).
4. If none clears σ, declare the target converged at that minimum and say so. A stuck model is a result.

Every escape attempt is logged with what was tried and whether it worked, because "how many configurations
were tried" is a reportable number (PROTOCOL §4.5).

---

## 6. The concrete goal

Reproduce, on our own pipeline, the improvements published on Dynamic PDB — and do it discretely, so that
the decision log shows *which* changes bought the improvement.

All three noise floors are now measured (10 seeds each, identical refinement, seed the only difference),
so every number below has a stated significance:

| target | deposited (header) | our re-refinement | published better model | gap to close | measured σ | a change must beat |
|---|---|---|---|---|---|---|
| 3TC7 (1.5 Å) | R-free 0.193 | **0.1885** | **0.163** (qFit multiconformer) | 0.0255 | 0.00181 | −0.00362 |
| 3QUE (2.7 Å) | R-free 0.3109 | **0.2668** | **0.25** (ensemble refinement) | 0.0168 | 0.00144 | −0.00288 |
| 7KR0 (0.77 Å) | R-free 0.1172 | **0.1163** | PDB-REDO 0.1233 (worse) | — | 0.000405 | −0.00081 |

Read the gap column against σ: on 3TC7 the distance to the published model is **14× the noise floor**, and on
3QUE **12×**. These are real targets, not noise — and they are large enough that a discrete loop has room to
show *which* changes closed them, which is the whole point of gating per change rather than per batch.

7KR0 is the control: there is no better published model to chase (PDB-REDO's is worse than the deposit), so
the question there is whether the loop can improve on an already-excellent 0.77 Å structure at all, or
correctly decides it cannot.

Two honest notes attached to that table from the start:

- 3QUE's deposited header (0.3109) is not reproducible on our pipeline for a diagnosed reason — it was
  refined with REFMAC5 and we use Phenix; PDB-REDO's own recalculation gives 0.2700 (deviation D008). So
  our re-refinement's 0.2668 is **not** an improvement we made; it is mostly the program difference, and it
  will be reported as the baseline, not as a result. The real question is what we can do *below* it.
- The published 0.25 came from ensemble refinement, which is a different model representation (many copies
  of the structure) than the multiconformer models this loop builds. Matching the number with a
  multiconformer model is a stronger result; failing to match it is not necessarily a failure of the loop.
  Both readings get stated.

---

## 7. Implementation

| module | responsibility |
|---|---|
| `autoref/runlog.py` | the §3.1 structured record — incremental, append-safe, checksummed |
| `autoref/stages/gaps.py` | FASTA-vs-model diff → classified work list (`internal` / `terminal` / `deferred`) |
| `autoref/stages/discrete.py` | the per-change engine: apply → local refine → RSCC → gate → commit/revert → log |
| `autoref/stages/bisect.py` | the per-cycle R-free regression bisection |
| `autoref/stages/escape.py` | the stall rule of §5 |
| `autoref/tools/rscc.py` | extended: `around(model, maps, selection, radius)` returning per-residue RSCC for the changed residues *and* their neighbours |
| `autoref/tools/coot.py` | extended: per-residue apply-and-refine operations returning the modified model |
| `autoref/thresholds_v2.yaml` | new frozen file (v1 is never edited in place) |

CLI: `autoref gaps --target T`, `autoref change --target T --type water_add --selection "..."` (one change,
for debugging), `autoref cycle --target T --discrete`, `autoref run --target T --discrete`.
