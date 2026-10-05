# SPEC — Graph search: parallel candidate evaluation on the canonical set

**Status:** proposal 2026-10-01; implemented on branch `graph-search` the same day (§5 steps 1-7); not adopted —
`thresholds_v9` needs a D-row and E036/E037 have not run. Nothing in `thresholds_v8.yaml` changes by this document.
PROTOCOL.md wins where the two conflict; this document changes no rule in PROTOCOL §3. Builds on `SPEC_DPDB_RUNS.md`
(the serial driver) and replaces its §2 loop with a generation loop.

Every number in §0 and §3 is from the ledger exports (`state/exports/`, snapshot 2026-09-18T04:30Z), the
deliverable records (`deliverables/*/current.json`, 2026-09-20), `state/deviations.md` and
`state/notes/experiments.md`. Every PDB ID in §4 is from an RCSB lookup run on 2026-10-01 (`targets/canonical.yaml`).

---

## 0. Where the campaign stands

### 0.1 What produced the gains

| Target | Deposited, our flags | Re-refinement alone | Our model | Beyond re-refinement, and what bought it |
|---|---|---|---|---|
| 3TC7 (1.5 Å) | 0.1915 | 0.1885 | 0.1728 | −0.016: riding hydrogens −0.011 (a protocol change, D488); 51 waters + altlocs at 28 residues −0.004 |
| 3QUE (2.7 Å) | 0.2872 | 0.2668 | 0.2589 | −0.008: three waters added, two removed, water occupancies refined |
| 7KR0 (0.77 Å) | 0.1175 | 0.1163 | 0.1126 | −0.003: two waters removed; three passes of 15 macro-cycles (D489/D493/D494) |
| 6CDX (1.0 Å, phase 2) | 0.2258 | 0.1901 | 0.1716 | −0.018: sub-floor waters removed, altlocs at four residues |
| 12 other phase-2 targets | | | | −0.003 to +0.001; nine of sixteen standing models are the cycle-0 re-refinement |

Change funnel over the whole campaign (`changes.csv`, 2 393 rows):

| Stage | Proposed | Passed local gates | Kept after the restricted pair | Credited |
|---|---|---|---|---|
| correction (rotamer, flip, zone) | 1 040 | 7 | 7 | 0 |
| solvent (add, remove) | 784 | 379 | 273 | 64 |
| protein_altloc (prune, add) | 518 | 83 | 21 | 0 |
| adp_model / rerefine (parameterisation) | 49 | — | — | 6 |

Reading: 64 of 70 credits are water edits. The two model-building stages that were supposed to close the gap to the
published models produced no credit in 1 558 proposals; 99.3 % of correction proposals and 298 of 518 altloc proposals
("qFit built no alternate conformer") died at the local gates. The largest single gains were parameterisation
(hydrogens on 3TC7, −0.011; macro-cycles on 7KR0), not building. The refinement protocol is target-specific: riding
hydrogens are −0.011 on 3TC7 and +0.016 on 3QUE (D490).

### 0.2 The operator's manual loop outran the harness

D512 (2026-09-28): a hand session on 3TC7 that alternated small Coot changes with refinement reported 0.1583 against the
standing 0.1728 (not yet scored on the frozen flags). Its components are ordinary: per-residue qFit build with
connectivity relabelling, water picking (−0.018), riding H with a fixed ADP weight (−0.007), XYZ weight optimisation
(−0.006), Ringer and difference-map cross-validation with one water removed and two cation sites. Nothing in that list is
outside the harness's stage vocabulary. The difference is persistence and breadth: the person tried many small things,
kept compound changes, and judged them against each other; the driver tries one change at a time, five per cycle, and
drops most of them at a +0.01 RSCC gate before R-free is ever consulted. On 7KR0 the E035 line reached 0.088–0.092 as
a six-copy ensemble against 0.1126 for the single model (D513; not depositable, R-gap gate fails), which says the data
hold more than the single-model search has found.

### 0.3 Where the compute went

366 job-hours in the ledger: phenix.refine 282 h (77 %), qFit 39 h, RSCC tables 14 h, R-free evaluations 12 h.
Of the 1 006 paired refinements, 503 are null arms (85 h). Noise-floor seeds are 71 h (25 % of refine time).
Every refinement runs with `nproc=1`. A single-target run's peak demand is two processes (`paired.py:193`,
`discrete.py:359`); on the 32-CPU pod that is 6 % utilisation. The pod was busy only during phase 2, when 13 targets
ran at once under 20 slots.

Measured wall-clock per refinement (`jobs.csv` medians; E-series notes):

| Target | Full refinement, 5 macro-cycles | 15 macro-cycles | Restricted arm, 8 macro-cycles | Local gates per change |
|---|---|---|---|---|
| 3QUE | 549 s | — | ≈ 120 s (E027) | ≈ 40 s |
| 3TC7 | 777 s | — | not measured (bound: 8/5 × 777 s ≈ 21 min) | 34 s median |
| 7KR0 | 1 591 s | 3 600 s | not measured (bound: 8/5 × 1 591 s ≈ 42 min) | 97 s median |

### 0.4 The driver is serial by implementation, not by necessity

`run_discrete.py` → `discrete.run_changes` is a for-loop over candidates ("strictly sequential and strictly
one-at-a-time", `discrete.py:1271`). Each candidate blocks on: apply → local real-space refinement → RSCC → geometry →
clashes → a two-arm restricted reciprocal pair. The only concurrency in a run is the 2-wide thread pool around each
pair. Things that are sequential only because of how the code is written:

- The cycle's full null arm depends only on the base, the seed and `refine_extra`, all known at cycle start; it waits
  until the stage loop ends.
- Candidates within a stage are proposed from one snapshot against fixed maps; their gates are independent unless
  their neighbour shells, clash partners or residues overlap.
- Each candidate's restricted null arm is known as soon as its selection is.
- Bisection halves run one after the other (`bisect.py:177`); escape rungs take one cycle each and each recomputes a
  null.
- Noise-floor seeds run two or three at a time (`AUTOREF_NF_CONCURRENCY`), never ten.
- `model_vs_data` cross-checks, MolProbity and clashscore in the cycle record run one after another.

Things that are sequential by necessity: generation after generation (the base must be fixed while candidates are
judged against it); combination of winners that touch overlapping regions (3QUE c072 regressed +0.0051 as a
three-water interaction, D484); re-measurement of the null after a parameterisation change ("the null does not
transfer across parameter counts", PROTOCOL §4.4); the macro-cycles inside one `phenix.refine`.

### 0.5 The statistics are not ready for a wide search

- Acceptance is k·σ_abs with k = 2 on every verdict on record. PROTOCOL §4.4 (main since 2026-09-17) replaces this
  with a per-class sham null and Benjamini–Hochberg at FDR 0.05; the harness does not implement it (D507).
- The select half has no consultation cap. On 3TC7 the fixed-weight protocol made σ_select 0.00008 and the gate
  credited waters whose report half moved the other way (D497); the divergence gate (v7) is the patch.
- The noise floor is ten seeds of one 5-macro-cycle re-refinement of the deposited model. For legacy models it measures
  convergence spread, not test-set noise (D506: 1LZ9 σ_select 0.0059 → 0.0017 once converged).
- Bisection has three defects (found 2026-10-01, `bisect.py`): `_default_refine_and_evaluate` drops `refine_extra`
  (so the 3QUE occupancy override and the 3TC7 `wxu_scale` are absent from the subsets while the null arm had them) and
  hard-codes `seed=1`; `apply_subset` re-runs each change's raw `apply_fn` without the local real-space refinement, so
  the subsets judged are not the models that were accepted. The driver's call (`run_discrete.py:616`) passes no
  `refine_extra`, so these defaults are always in force in production.

Why this matters for going wide: the best of N noisy candidates clears a fixed 2σ bar by chance with probability
1 − 0.977^N: 11 % at N = 5, 37 % at N = 20, 75 % at N = 60. The expected maximum of 60 null draws is 2.3σ. A generation
of 60 candidates judged on the current gate would credit noise more often than not. The sham null + BH rule PROTOCOL
already prescribes is the correction, and it is a prerequisite for §2, not a refinement of it.

---

## 1. Is refinement linear?

A single `phenix.refine` is an iterative optimiser: macro-cycle n+1 starts from macro-cycle n, and `nproc` only
parallelises parts of one macro-cycle (bulk-solvent grid, weight trials). One refinement cannot be fanned out.

The *search over models* is not linear. Every candidate is an independent refinement of the same base; the harness
serialises them only by implementation (§0.4). The protocol already anticipates fan-out: PROTOCOL §4.1 lets the
real-space and reciprocal-space agents "create their own sub-agents to test different things, then report back", §9
says "delegate aggressively", and §4.4 defines the multiplicity correction a wide search needs. What has to stay in
order is the generation structure: fix a base, judge many candidates against it in parallel, combine the winners and
re-judge the combination, then move the base.

---

## 2. The graph search

### 2.1 Nodes, edges, generations

- A **node** is a model state: model file hash, map coefficients, parameterisation block (`refine_decisions.json`),
  the frozen floor and null ids it was judged under, and its R-free (select / report / full) from its own null arms.
- An **edge** is a change set applied to a node, with its paired verdict: attributable ΔR-free-select, Δreport, Δfull,
  Δgap, the gates, and the null id. Edges are `changes` rows grouped by `edge_id`.
- A **generation** expands one or more bases (the **beam**, §2.5) into candidate edges, judges them all against shared
  null arms of the same base, and selects the next bases.
- The record is a DAG under `runs/<T>/graph/<run_id>/g<NNN>/` with `nodes.json`, `edges.json` and the same per-arm
  directories SPEC_DPDB_RUNS §1 defines. The ledger gains `nodes` and `edges` tables keyed on (target, run_id, node_id);
  `cycles` rows carry `generation` and `parent_node`. Bookkeeping stays idempotent on those keys.

### 2.2 One generation, from one base B

```
g.0  launch, all in parallel on the pool (§3):
       null arms of B: n_null full refinements, seeds 1..n_null (default 5)      ← shared by every candidate
       every proposer on B: correction, solvent, protein_altloc, gaps, zone,
         protocol toggles (§2.6), transfer proposals (§4.2)                         → candidates C_1..C_N
g.1  local gates per candidate (apply, local RSR, RSCC, neighbours, geometry, clashes), N at once;
       record the candidate's footprint: residues touched, 5 Å neighbour shell, clash partners, water slots
g.2  restricted reciprocal pair per surviving candidate (D480: selection-only, 8 macro-cycles, standing weights,
       TLS off): candidate arm + its own restricted null arm, 2·N' refinements at once
g.3  rank by attributable ΔR-free-select; p-value per candidate against its class's sham null (§2.3);
       Benjamini–Hochberg at FDR 0.05 across the generation → the accepted set A
g.4  conflict graph on footprints (§2.4); greedy maximal independent set in rank order → winners W ⊆ A
g.5  combined candidates, full paired refinement each (seed = seeds[0], same refine_extra as the null arms):
       {W}, {W minus w_i} for each of the top m winners, {W per stage}, {top-5 of W}        → k ≈ 5–10 arms at once
g.6  verdict per combined candidate against the shared null arms: credit at ≤ −k·σ_B (σ_B from the n_null seeds,
       never looser than the frozen floor), R-gap gate, divergence gate, geometry and clash caps on the whole model
g.7  adopt: the best combined candidate by select among those passing g.6, with Δreport confirmed not worse than
       +2σ_report (one report consultation per generation); it becomes a node; losers stay in the DAG as edges
g.8  beam: the best w distinct passing nodes become the next generation's bases (§2.5)
```

The real-space candidate stays the model in force, as now; the restricted pair judges. Credit comes only from g.6,
as now from the full paired cycle. Every refinement still goes through `tools/phenix_refine.py` (flag guard, semaphore,
`jobs` row). Nothing in PROTOCOL §3 is touched: same flags, same split, consultations counted per candidate at g.2
(select) and once per generation at g.7 (report).

### 2.3 Multiplicity: the gate for a generation (`thresholds_v9`)

Implements PROTOCOL §4.4(b) as written (D507 lists what is missing):

- `stages/sham_null.py`: per target, per change class (`water_add`, `water_remove`, `protein_altloc_add`,
  `rotamer_fix`, `peptide_flip`, `zone_refine`), ≥ 50 sham instances with no density support, each through the
  identical restricted pair of g.2, weights frozen. Output: the class's ΔR-free-select distribution, id
  `NULL-<target>-<node>-<class>-<n>`. Runs as one parallel wave (§3 cost). Re-measured at the nodes PROTOCOL names:
  after L2, after the first altloc wave, after the first solvent rebuild, after any adopted protocol change.
- Threshold per class: the frozen 99th percentile. p per candidate: empirical, reported as < 1/N_sham beyond the
  sham range, never interpolated.
- BH across the generation's candidates at FDR 0.05; the per-change row carries null id, p and q.
- σ_abs (the seed floor) keeps its PROTOCOL §4.4(a) roles only: the g.6 credit bar on the combined candidate, the
  convergence test, σ_gap, the error bar on the headline.
- `acceptance: {mode: sham_null_bh, n_sham: 50, quantile: 0.99, fdr: 0.05}` in `thresholds_v9.yaml`; everything else
  byte-identical to v8. Every verdict on record is re-judged under v9 (the D442 procedure) and the result tabulated.

### 2.4 Combining winners

Interactions are real (D484). Footprint overlap (shared residue, neighbour shell within 5 Å, clash partner, water
slot) defines the conflict graph; conflicting accepted candidates are not combined in the same generation, the
lower-ranked one waits for the next generation on the new base. The leave-one-out table in g.5 replaces sequential
bisection: if {W} regresses against the best {W minus w_i}, w_i is the culprit; if no single removal recovers it, the
generation adopts the best subset and records `interaction_only`, as `bisect.py` does now. The three `bisect.py`
defects (§0.5) are fixed first because the serial driver still uses it.

### 2.5 Beam, merge, record

Beam width w (run-shape argument, default 2): each generation keeps the best w passing nodes as bases, not one.
Two nodes whose change sets are identical merge. A base that produces no passing combined candidate in three
generations is closed (PROTOCOL §4.6 applied per node). The run stops when every beam is closed or the generation cap
is reached; as now, a stop ends the run, not the target. Promotion (`_promote`, D484/D495/D499/D508) is unchanged and
reads the best node.

The Metropolis rule (v8, D499) applies per beam to the within-noise-but-worse band of a combined candidate exactly as
it applies to a cycle now; the drift guard bounds each beam separately.

### 2.6 Parameterisation branches

Protocol toggles are candidates like any other, as `weight_change` / `hydrogens_toggle` / `adp_model` edges judged by a
full pair against the shared null arms (they have no local evidence, so they skip g.1–g.2): riding hydrogens on/off,
anisotropic vs isotropic + TLS, `wxu_scale` and `wxc_scale` grids, macro-cycles 5/15, bulk-solvent mode, scattering
table, water occupancy refinement. They cost one full refinement each and run in the same wave as g.5. An adopted
toggle creates a node whose floor and sham nulls are re-measured before the next generation (one parallel wave,
blocking). The answers differ per target (3TC7 H −0.011, 3QUE H +0.016), which is why they belong in the search and
not in a fixed ladder.

### 2.7 What stays sequential

Generation after generation; the null re-measurement after an adopted toggle; the conflict ordering inside a
generation; promotion. Everything else fans out.

---

## 3. Cost model

Pool: `AUTOREF_NPROC` slots on the current pod (32 CPU requested, 64 limit, 96 GiB). Single-threaded refinements;
memory per 7KR0 refinement is unmeasured and bounds the slot count for that target (measure RSS before exceeding 20).
Estimates below assume 28 slots and the §0.3 timings; restricted-arm times for 3TC7 and 7KR0 are the upper bounds.

| | 3QUE | 3TC7 | 7KR0 |
|---|---|---|---|
| g.1 local gates, N = 60 | ≈ 2 min | ≈ 2 min | ≈ 4 min |
| g.2 restricted pairs, N' = 30 (60 arms) | 60 × 2 min / 28 ≈ 5 min | 60 × 21 min / 28 ≈ 45 min | 60 × 42 min / 28 ≈ 1.5 h |
| g.5 + nulls + toggles, ≈ 15 full arms | one wave ≈ 9 min | ≈ 13 min | ≈ 26 min (5 mc) |
| one generation | ≈ 20 min | ≈ 1 h | ≈ 2–2.5 h |
| serial driver today, 5 kept changes per cycle | 25–40 min | ≈ 1.5 h | several hours |
| sham null, one class (100 restricted arms) | ≈ 7 min | ≈ 1.3 h | ≈ 2.5 h |

Candidates judged per hour rise by roughly an order of magnitude at the same wall-clock; the null-arm cost per
candidate falls by N because the full null arms are shared. The sham-null measurement D507 priced at 15 h wall for
thirteen targets is an afternoon for the canonical trio once the pool exists.

---

## 4. The canonical set

`targets/canonical.yaml` (this session's lookups). Three proteins, each anchored by the entry refined since 2026-08-25:

| Protein | Tier A (canonical) | Tier B: same form, other resolutions | Tier C: other space groups |
|---|---|---|---|
| IGPS scaffold, S. solfataricus (Q06121); 7 entries ≥ 95 % identity, all designed variants of the NESG OR62 scaffold | 3TC7, 1.50 Å, P 31 2 1 | 4OU1 1.25, 8W40 1.45, 8W3Y 1.45, 8W3Z 1.49 (all P 31 2 1) | 4PEK 1.60, 4LNY 1.93 (P 21 21 21) |
| p38α MAPK14 (Q16539); 392 X-ray entries, 108 isomorphous with 3QUE | 3QUE, 2.70 Å, P 21 21 21, 65 × 74 × 77 Å | ladder 6Y4X 1.60, 9MHB 1.65, 9R25 1.80, 4F9Y 1.85, 3K3J 2.00, 4R3C 2.06, 8ACM 2.14 (apo), 7Z6I 2.25, 5N63 2.40, 9R27 2.60, 8ACO 2.65 (apo) | 6SP9 1.22 I 2 2 2; 5R97 1.44 P 21 21 21 (PanDDA Form1 cell); 5LAR 1.50 P 21 21 21 (69 × 71 × 75); 9CJ4 1.80 C 2; 9CJ1 1.80 P 21; 6ZQS 1.95 P 2 21 21; 2Y8O 1.95 P 31 2 1 |
| SARS-CoV-2 Nsp3 Mac1 (P0DTD1); 864 X-ray entries, 725 in P 43 | 7KR0, 0.77 Å, C 2, 100 K | 7KR1 1.55 Å 310 K (same form); 5RVM 1.03 (7KR0 cell); 7KQW 0.93, 8AZC 0.93 (second C 2 cell) | 7KQO 0.85, 7TX0 0.84, 7TWV 0.90, 7TWJ 0.90 (P 43; the 7TWJ–7TWS pH 4–10 series is seven data sets at 0.90 Å); 6WEY 0.95 P 21 21 21; 9CY0 0.80 P 1 |

Excluded: 2FST and 1KV2 (p38α; no structure factors). 44PS (0.77 Å, C 2, 2026, header R-free 0.0641) is the 7KR0 data
refined as a six-copy model: a representation of the canonical data, scored in the PROTOCOL §18.1 column, not a target.

### 4.1 What each tier is for

- **Tier A** is where R-free is pushed down and where every method is proved. It is unchanged.
- **Tier B** answers whether a method that moved tier A transfers along the resolution axis of the same crystal form:
  the p38α ladder spans 1.60–2.65 Å in one cell; the Mac1 pair 7KR0/7KR1 is the same form at 100 K and 310 K. A method
  credited on tier A is run on tier B under the same v9 gates and reported as a transfer table, not promoted blindly.
- **Tier C** answers whether the result depends on the lattice: the same protein in another space group, with another
  ligand or pH. Tier C runs are method validation, not deliverables, unless the operator promotes one.

Onboarding is `scripts/onboard_target.sh` per entry after a `targets/targets.yaml` row written from the RCSB entry
JSON as D501 did; phase 2 showed thirteen onboardings run in parallel on this pod. Tier B first (19 entries), tier C
after a tier-B result justifies it.

### 4.2 Transfer proposers from the series

A new stage `transfer` proposes into a tier-A target what a higher-resolution isomorphous entry of the same protein
shows: water sites, alternate conformations, rotamers and ligand poses, superposed onto the target (per-residue
identity checked; designed-variant sites skipped), then judged on the target's own flags like any other candidate.
This uses no reflection of the target, so PROTOCOL §3 is untouched. It is the proposer most likely to help 3QUE at
2.7 Å, where per-residue conformers are weakly determined and E033's reference-model restraints from 6SP9 were null
(+0.0006): a proposal is cheaper to judge than a restraint and can be rejected per site. 6Y4X and 9MHB (1.60–1.65 Å,
same cell) are the first sources.

---

## 5. Implementation map

| Step | Files | Rule change? |
|---|---|---|
| 1. Fix `bisect.py` (refine_extra and the paired seed threaded through from the driver; local RSR in subsets) | `stages/bisect.py`, `stages/run_discrete.py`, tests | no |
| 2. Pool: a futures executor bounded by the existing semaphore; `AUTOREF_NPROC` per run to 28; shared null arms in `paired.py` (`run_paired_generation`) | `orchestration/pool.py` (new), `stages/paired.py`, `scripts/run_graph.sh` | no |
| 3. Parallel candidate evaluation against one snapshot with footprints; no commits during evaluation | `stages/discrete.py::evaluate_many` | no (gates unchanged) |
| 4. Sham-null stage, BH, per-change p/q, `thresholds_v9.yaml`; retro-judgement of every verdict on record | `stages/sham_null.py` (new), `accept.py`, `thresholds_v9.yaml`, `scripts/experiments/exp_retro_v9.py` | **yes** (D-row; PROTOCOL §4.4 already requires it) |
| 5. Generation driver, beam, DAG record, `autoref run-graph` | `stages/run_graph.py` (new), `ledger.py` (`nodes`, `edges`), `cli.py` | no |
| 6. Protocol toggles and transfer proposals as stages | `stages/proposers.py` | no |
| 7. Series onboarding (tier B) | `targets/targets.yaml` rows, `scripts/onboard_series.sh` | no |

Steps 1–3 are throughput only and can run under v8 today with the serial gates; step 4 is the prerequisite for any
generation wider than a handful; steps 5–7 follow. Tests: generation verdicts with mocked refinements, BH, conflict
graph, leave-one-out culprit logic, DAG idempotence.

---

## 6. First experiments

- **E036, 3QUE, one generation.** Base: the standing 3QUE model. N ≈ 60 candidates from every proposer plus ten
  protocol toggles, five shared null seeds, under v8 as monitor and v9 as the decision. Cheapest target (§3), and
  the outcome decides whether the restricted-pair ranking predicts the combined full pair, which is the assumption
  the whole design rests on.
- **E037, canonical trio, sham nulls.** The D507 measurement for `water_add`, `water_remove`,
  `protein_altloc_add`, `rotamer_fix`; sets the v9 bars; re-judges every verdict on record. One wave per target.
- **E038, 3QUE, transfer proposals** from 6Y4X and 9MHB after their onboarding; judged as one generation.
- **Verify D512's 0.1583 model** with `scripts/verify/` before anything in §0.2 is used as a number; its component
  list is the proposer roster regardless.

---

## 7. Open decisions for the operator

1. Adopt `thresholds_v9` (sham null + BH) and re-judge the record (D507 asked this already; §3 makes it cheap).
2. Beam width, generation size and null-seed count are run-shape arguments, not thresholds; defaults w = 2, N ≤ 100,
   n_null = 5.
3. Whether tier-B results are deliverables or a transfer table.
4. A consultation budget per target per generation, recorded on the generation row.
5. Whether 44PS is scored on our flags as the §18.1 reference for 7KR0 (its header free set has 8 709 reflections to
   our 8 712; the identity of the two sets must be checked at gate G3 first).

---

## 8. Running several lines at once

Measured on the pod 2026-10-01 (read-only probes; `actl pod exec`), unless marked otherwise.

### 8.1 What the pod is

| | Value | Source |
|---|---|---|
| CPU quota | 64 (request 32) | `/sys/fs/cgroup/cpu.max` = `6400000 100000` |
| Memory limit | 96 GiB | `memory.max`; anonymous use ≈ 0 when idle, the rest page cache |
| Home volume | NFS v3, `nfs-shared`, ReadWriteMany | `mount`; `actl pvcs` |
| GPUs | 4 × H200 visible (`NVIDIA_VISIBLE_DEVICES=all`), not requested | `nvidia-smi -L`; do not use: they are not allocated to this pod |
| Semaphore | `/tmp/autoref-locks`, container-local, `AUTOREF_NPROC` slots | `orchestration/semaphore.py` |

### 8.2 One pod, several CPU lines

Lines that run inside the harness (graph search, the discrete driver, sham nulls, noise floors, onboarding) take slots
from the one semaphore. Lanes (`autoref lanes set graph=18 untangler=8 qfit=4`) reserve contiguous slot blocks per line;
a lane job uses its block, then the common remainder, never another lane's block (`orchestration/semaphore.py`).
`scripts/run_campaign.sh` sets the lanes and launches each line detached with `AUTOREF_LANE` set.

Lines that call `phenix.refine` themselves do not take slots and write no `jobs` rows. The E035 chain is one:
Untangler's `Refinement/Refine.sh` and the anisotropic step's direct `phenix.refine` bypass the semaphore
(`scripts/experiments/exp_untangler_7kr0.sh`). For such a line the lane is a reservation the harness leaves empty: reserve
as many slots as the line's own processes need, and the harness lines cannot crowd it. The bound holds only if the line
itself stays within that count (`UNTANGLER_THREADS`, the number of arms it backgrounds).

Recommended shares with `AUTOREF_NPROC=32`, pending a measured 7KR0 arm size (the `jobs` table now records `max_rss_mb`
per job; before 2026-10-01 nothing measured memory):

| Lane | Slots | What runs |
|---|---|---|
| graph | 18 | graph search on 3QUE, 3TC7, 7KR0 (single-threaded refinement arms; 7KR0 arms are the memory bound) |
| untangler | 8 | the E035 chain (`UNTANGLER_THREADS=8`; its refinements outside the pool) |
| qfit | 4 | a qFit batch (pass `nproc=4`: qFit takes `weight = nproc` slots) |
| common | 2 | MolProbity, RSCC tables, cross-checks |

Memory first: 32 concurrent arms at 1–3 GB each is 32–96 GB, so on 7KR0 the 96 GiB limit binds before the CPU quota.
Lower the graph share for 7KR0 until `max_rss_mb` is known.

### 8.3 Guards added for concurrent lines (2026-10-01)

- **One driver run per target.** `state.target_run_lock`: a second `run-discrete` or `run-graph` on a target already held
  is refused with the holder's run id and pid. Both drivers continue `Current.cycle_index`, and `cycles`/`changes` rows are
  keyed on (target, cycle_index), so two runs would overwrite each other's rows. `--start-cycle` with a disjoint block is
  the explicit escape.
- **Promotion is serialised and atomic.** `_promote` runs under `state.promotion_lock`; `Current.save` writes a tmp file
  and renames. Before, two runs promoting one target compared against a record the other was rewriting.
- **The consultation counter is atomic.** `Ledger.increment_consultations` reads and writes under one lock; the earlier
  form lost increments under threads (PROTOCOL §3.6).
- **Job memory is recorded.** `tools/base.py` polls the child's peak RSS (`VmHWM`) and writes `jobs.max_rss_mb`.

### 8.4 A second pod (GPU lines: sampleworks / Boltz-2)

The learned-proposer line needs a GPU and the `sampleworks` image (`harbor.astera.sh/library/pixi-with-checkpoints:
sampleworks`, `actl pod images`), so it cannot run on this pod. `actl` runs one pod per workspace; a second workspace gets
its own home volume and can mount this one: `actl pod up swgen -n diffuse --profile single --image sampleworks --mount
actl-ws-xraymemory-autoresearch-home` (the volume appears at `/mnt/actl-ws-xraymemory-autoresearch-home`; `single` = 1 GPU,
3 CPU, 64 GiB, available on 3 nodes; `actl pod profiles`). E025's `swgen` pod mounted the volume this way
(`state/notes/experiments.md`, E025); its exact argv was not recorded, and the recipe above has not been run this session.

The second pod must not write this pod's ledger. Every ledger write takes an fcntl lock in the container-local
`/tmp/autoref-locks`, which a second pod does not see, so exclusion would fall back to SQLite's own locks over NFS v3 with
`local_lock=none` — which `ledger.py` already declines to trust, and E025 recorded delayed cross-pod visibility. Rules:

1. On the second pod: `AUTOREF_STATE` = a private directory on the shared volume (e.g. `/mnt/…/state-swgen`),
   `AUTOREF_RUNS` = `/mnt/…/runs` (distinct subdirectories per experiment), `AUTOREF_DATA_ROOT` = `/mnt/…/data` (read
   only), `AUTOREF_LOCK_DIR` = its own `/tmp`. It writes its own ledger and jsonl mirror there.
2. On this pod: `autoref ledger import /home/dev/state-swgen/ledger` replays the mirror into the canonical ledger
   (`Ledger.import_jsonl`): keyed rows are idempotent, each row keeps its own `written_at` and thresholds hash, the
   consultation count is added once per file (a re-import of the same file is refused), unknown tables or columns are
   refused. `--dry-run` reports first.
3. Candidates the second pod proposes are files under `runs/`; they are judged on this pod by the graph driver like any
   other proposal (learned proposers are proposers, never acceptance evidence, PROTOCOL §17).

Not verified: whether the autoref venv under `/home/dev/envs/autoref` runs inside the sampleworks image (different base
image). If it does not, the second pod writes plain files and this pod builds the `changes` rows on import.

### 8.5 What does not parallelise

The E035 chain's hard-coded base path (`e035_pipeline_chain.sh`: `BASE=/home/dev/runs/7KR0/experiments`) and
`/tmp/cbc_wrapper_failures.log` (`cbc_retry.sh`) are per-line, not shared state. Coot runs as one subprocess per
operation in the job's own directory, with no single-instance assumption. Never edit a script while an instance runs
(D504); `run_campaign.sh` launches copies.
