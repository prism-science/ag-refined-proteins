# 7KR0 — six-copy ensemble representations (E035, Untangler)

**Not a deliverable.** These are six-copy ensemble models of the 7KR0 data. They are a second representation of the same
data, reported in their own table, never as the target's model (campaign PROTOCOL §18.1, `docs/campaign/PROTOCOL.md`). The
released single model is `targets/7KR0/`.

## Caveats

- The best model here is still far from the paper's. 44PS scores 0.06566 full R-free on our flags. The best isotropic
  six-copy model here scores 0.09202 (+0.026). The best anisotropic one scores 0.08789 (+0.022).
- The anisotropic models (E035d) fail the campaign's R-gap gate. Converting to anisotropic B widened R-free − R-work by
  +0.0036 to +0.0041, 22–25σ_gap against the 2σ_gap bar (thresholds_v6, D495). The authors' own rule keeps the conversion:
  R-free fell by 50–55 % of the R-work fall, above their 30 % bar. Both verdicts stand. 44PS itself has a wider gap (0.0172)
  than any model here.
- Every six-copy PDB file here writes protein occupancy 0.17 per copy, so each protein site sums to 1.02. The PDB format
  keeps two decimals; the refinement started from 0.167 × 4 + 0.166 × 2 = 1.000 (E035 design), and Phenix rounded on output.
  PROTOCOL §18.5 asks for exactly 1.000 in the written file; these files do not meet it. The scores below are computed on the
  files as written. 44PS (mmCIF) sums to 1.000.
- E035d step 2 (two more stage-3 cycles after the anisotropic finish) did not test what it was meant to. Its models carry no
  ANISOU records (`scores/E035d_post_*.composition.json`): the anisotropic ADPs did not survive the cycle. Those models score
  0.0913–0.0922, worse than the anisotropic models they started from.
- Composition differs from 44PS in the solvent. The isotropic stage-3 models carry 1 305–1 411 water atoms with summed
  occupancy 248–252; 44PS carries 2 581 with summed occupancy 454. The paper attributes its last step below 0.10 to this
  per-copy solvent (Sec. IV B).
- No MolProbity run on these models in this release. The only geometry on record is stage 1 (D513): clashscore 6.6 and
  rotamer outliers 4 % at loop 11. None of these models meets the campaign's geometry caps.
- σ for this representation comes from five seeds (σ_full 0.00025, σ_select 0.00028, σ_gap 0.00016; E035 floor). Below ten
  seeds PROTOCOL §18.4 calls it provisional.
- Three randomized starts per arm, not the paper's five. ILP solver HiGHS, not CPLEX (CBC segfaulted at the time limit).
  Phenix 2.1-6048, not 2.0. Disclosed in D511 and D513.

## What this is

Passmore, Holton, Zatsepin & Martin, "Optimizing the connectivity of protein conformations to untangle ensemble refinement",
bioRxiv 10.64898/2026.09.17.752399 (posted 2026-09-19); code github.com/Phoelionix/Untangler, branch `conformational_tree`,
commit 1776c8d (citation as recorded in campaign row D511). The paper reassigns altloc labels across an ensemble without
moving atoms, choosing the assignment with the lowest restraint energy by integer linear programming, inside a loop of one
unrestrained and ten restrained phenix.refine macro-cycles. With per-copy water picking (stage 2), manual Coot work
(stage 3) and anisotropic B at the end, it reports a six-conformation model of the 7KR0 dataset: 44PS.

44PS (RCSB, released 2026-09-30) uses the 7KR0 dataset. Its deposited free set is identical to the frozen flags used here
(`scripts/flag_identity.py`, 2026-10-03: 8 712 free, 0 differing; the header's 8 709 is the depositors' count). So its R-free
and ours are on the same held-out reflections.

The campaign ran the paper's pipeline on 7KR0 as experiment line E035 (registered 2026-09-21, D511):

| Stage | Experiment | What it does | Outcome |
|---|---|---|---|
| 1 | E035 | Six copies of the deposited qFit model, 0.5 Å shake, 20 restrained macro-cycles; then the connectivity loop. Arms T (loop), C1 (loop without the optimizer), C2 (restrained only), three randomized starts. | Replicates as a rate effect with a modest endpoint gain (D513). |
| 2 | E035b | Phenix 2.1 `ordered_solvent` picking inside the loop, the authors' settings. | Negative: R-work 0.119 → 0.418 in one update with the authors' template; ≈ +0.02 above base with altlocs off (D514). |
| 2 | E035f | The harness's own picker: six-copy waters at ≥ 3σ mFo−DFc peaks, nothing removed, occupancies refined in the loop. | −0.006 to −0.008 full R-free after one loop on every arm (D514). |
| 3 | E035c | Automated stand-in for the manual stage: water hygiene (occupancy floor 0.02, same-altloc merge), main-chain-only connectivity pass, own pick, full loop. | Null from the stage-1 endpoints; from the E035f models −0.0018 to −0.0036 below the plain loop at equal depth, converged at cycle 3. |
| finish | E035d | Convert to anisotropic B, 10 macro-cycles B only. Then two more stage-3 cycles (step 2). | Passes the authors' 30 % rule, fails the R-gap gate. Step 2 lost the anisotropic ADPs. |

The manual part of the authors' stage 3 (about thirty Coot changes, mostly identity mix-ups between waters and side chains)
is not in any of these models.

## Scores on the frozen flags

Every number in this table was computed on 2026-10-03 by the independent scorer (`scripts/indep_rfree.py`: cctbx fmodel on
all reflections, no outlier rejection) on the frozen 7KR0 data, flags and select/report split, and is read from
`scores/<row>.json`. Atom, water and occupancy counts are from `scores/<row>.composition.json`. Gap = R-free − R-work.
Water atoms counts non-hydrogen atoms in HOH residues, every copy. "Copies × protein occ." is the mean occupancy of
non-water, non-hydrogen atoms per altloc letter.

Rows per stage are the T arm of each randomized start (T, T_r2, T_r3). Stage 1 and E035f rows are the endpoints by the
rule written before the runs (the authors' rule: last loop before R-free-select rose three times in a row; "provisional"
where it never triggered), not the best loop picked afterwards (PROTOCOL §18.2). E035c rows are cycle 3, where the run
converged. "pod only" rows are scored here but their files are not in this release (44PS and 7KR0 are public at RCSB); their pod paths and SHA-256 are in
`provenance.json`.

<!-- rep-table:begin -->
| Stage | Arm | Model | R-free full | select | report | R-work | Gap | Atoms (H) | Copies × protein occ. | Water atoms | Σ water occ. | ANISOU | File |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reference | — | **44PS as deposited (Passmore et al. 2026), six conformations** | 0.06566 | 0.06533 | 0.06600 | 0.04845 | 0.01721 | 17,995 (7,722) | 6 × 0.167 | 2,581 | 453.8 | 10,273 | pod only |
| context | — | 7KR0 as deposited (qFit multiconformer, single model) | 0.11735 | 0.11587 | 0.11886 | 0.11030 | 0.00705 | 4,300 (1,990) | multiconformer (4 letters) | 316 | 309.0 | 2,310 | pod only |
| context | — | 7KR0 standing single-model deliverable (targets/7KR0) | 0.11254 | 0.11038 | 0.11473 | 0.10361 | 0.00893 | 4,298 (1,990) | multiconformer (4 letters) | 314 | 286.6 | 2,308 | pod only |
| E035 | T | stage 1 connectivity loop, endpoint by the pre-registered rule (loop 14) | 0.10448 | 0.10115 | 0.10785 | 0.09642 | 0.00806 | 17,286 (7,722) | 6 × 0.170 | 1,872 | 213.6 | 0 | pod only |
| E035 | T_r2 | stage 1 connectivity loop, endpoint by the pre-registered rule (loop 10) | 0.10414 | 0.10031 | 0.10802 | 0.09533 | 0.00881 | 17,286 (7,722) | 6 × 0.170 | 1,872 | 214.2 | 0 | pod only |
| E035 | T_r3 | stage 1 connectivity loop, endpoint by the pre-registered rule (loop 14, provisional) | 0.10371 | 0.09985 | 0.10762 | 0.09487 | 0.00884 | 17,286 (7,722) | 6 × 0.170 | 1,872 | 214.0 | 0 | pod only |
| E035f | T | stage 2 with the harness picker, endpoint by the pre-registered rule (slot 15) | 0.09491 | 0.09280 | 0.09705 | 0.08604 | 0.00888 | 17,808 (7,722) | 6 × 0.170 | 2,394 | 232.7 | 0 | pod only |
| E035f | T_r2 | stage 2 with the harness picker, endpoint by the pre-registered rule (slot 5) | 0.09517 | 0.09260 | 0.09777 | 0.08611 | 0.00905 | 17,748 (7,722) | 6 × 0.170 | 2,334 | 233.1 | 0 | pod only |
| E035f | T_r3 | stage 2 with the harness picker, endpoint by the pre-registered rule (slot 11) | 0.09372 | 0.09168 | 0.09579 | 0.08443 | 0.00929 | 17,784 (7,722) | 6 × 0.170 | 2,370 | 238.0 | 0 | pod only |
| E035c | T | automated stage-3 cycle, cycle 3 (converged; N = 3) | 0.09202 | 0.08961 | 0.09446 | 0.08324 | 0.00878 | 16,719 (7,722) | 6 × 0.170 | 1,305 | 247.6 | 0 | [E035c2_T_cycle3.pdb](models/E035c2_T_cycle3.pdb), [map](models/E035c2_T_cycle3_map_coeffs.mtz) |
| E035c | T_r2 | automated stage-3 cycle, cycle 3 (converged; N = 3) | 0.09230 | 0.08967 | 0.09496 | 0.08325 | 0.00905 | 16,803 (7,722) | 6 × 0.170 | 1,389 | 248.7 | 0 | [E035c2_T_r2_cycle3.pdb](models/E035c2_T_r2_cycle3.pdb), [map](models/E035c2_T_r2_cycle3_map_coeffs.mtz) |
| E035c | T_r3 | automated stage-3 cycle, cycle 3 (converged; N = 3) | 0.09214 | 0.08988 | 0.09442 | 0.08246 | 0.00968 | 16,825 (7,722) | 6 × 0.170 | 1,411 | 252.0 | 0 | [E035c2_T_r3_cycle3.pdb](models/E035c2_T_r3_cycle3.pdb), [map](models/E035c2_T_r3_cycle3_map_coeffs.mtz) |
| E035d | T | anisotropic-B finish on the E035c cycle-3 model (convert, 10 mc B only) | 0.08789 | 0.08556 | 0.09024 | 0.07505 | 0.01284 | 16,719 (7,722) | 6 × 0.170 | 1,305 | 282.5 | 8,997 | [E035d_T_aniso.pdb](models/E035d_T_aniso.pdb), [map](models/E035d_T_aniso_map_coeffs.mtz) |
| E035d | T_r2 | anisotropic-B finish on the E035c cycle-3 model (convert, 10 mc B only) | 0.08789 | 0.08534 | 0.09047 | 0.07532 | 0.01257 | 16,803 (7,722) | 6 × 0.170 | 1,389 | 284.7 | 9,081 | [E035d_T_r2_aniso.pdb](models/E035d_T_r2_aniso.pdb), [map](models/E035d_T_r2_aniso_map_coeffs.mtz) |
| E035d | T_r3 | anisotropic-B finish on the E035c cycle-3 model (convert, 10 mc B only) | 0.08810 | 0.08592 | 0.09030 | 0.07476 | 0.01334 | 16,825 (7,722) | 6 × 0.170 | 1,411 | 286.8 | 9,103 | [E035d_T_r3_aniso.pdb](models/E035d_T_r3_aniso.pdb), [map](models/E035d_T_r3_aniso_map_coeffs.mtz) |
| E041 | R | line R best R-free: H2_T r1s7 loop + weight stack (wc 0.3, -u 0.25), 10 mc; clashscore 26.7 | 0.06801 | 0.06662 | 0.06942 | 0.04574 | 0.02227 | 18,612 (7,722) | 6 × 0.167 | 3,198 | 562.0 | 10,642 | [E041_R4_S.pdb](models/E041_R4_S.pdb) |
| E041 | R | line R after two clash-cleanup passes on R4_S (water copies on own-conformer H removed, 6 mc each); clashscore 4.5 | 0.06891 | 0.06693 | 0.07092 | 0.04556 | 0.02335 | 17,991 (7,722) | 6 × 0.167 | 2,577 | 545.8 | 10,189 | [E041_CJ_R4_p2.pdb](models/E041_CJ_R4_p2.pdb) |
| E041 | R | CJ_R4_p2 after a 10 mc polish at wc 0.5, -u 0.25; clashscore 4.4 | 0.06896 | 0.06703 | 0.07091 | 0.04577 | 0.02319 | 17,991 (7,722) | 6 × 0.167 | 2,577 | 549.0 | 10,189 | [E041_CJ_R4_polish.pdb](models/E041_CJ_R4_polish.pdb) |
| E035d step 2 | T | two stage-3 cycles after the anisotropic finish (last closing loop) | 0.09193 | 0.08945 | 0.09443 | 0.08281 | 0.00912 | 16,718 (7,722) | 6 × 0.170 | 1,304 | 254.5 | 0 | pod only |
| E035d step 2 | T_r2 | two stage-3 cycles after the anisotropic finish (last closing loop) | 0.09127 | 0.08886 | 0.09371 | 0.08237 | 0.00890 | 16,779 (7,722) | 6 × 0.170 | 1,365 | 253.6 | 0 | pod only |
| E035d step 2 | T_r3 | two stage-3 cycles after the anisotropic finish (last closing loop) | 0.09222 | 0.08996 | 0.09450 | 0.08237 | 0.00985 | 16,790 (7,722) | 6 × 0.170 | 1,376 | 255.9 | 0 | pod only |
| E049 | portable | portable script, end of round 1 (3 sigma pick 224 sites + anisotropic waters); clashscore 4.7, rotamers 1.3 % | 0.08557 | 0.08529 | 0.08585 | 0.07033 | 0.01523 | 16,815 (7,722) | 6 × 0.167 | 1,401 | 411.3 | 9,093 | [E049_r1_aniso_water.pdb](models/E049_r1_aniso_water.pdb) |
| E049 | portable | portable script, end of round 2 (2.5 sigma pick + clash cleanup, anisotropic waters); clashscore 4.5, rotamers 1.3 % | 0.07885 | 0.07647 | 0.08125 | 0.06060 | 0.01825 | 17,211 (7,722) | 6 × 0.167 | 1,797 | 478.3 | 9,489 | [E049_r2_aniso_water.pdb](models/E049_r2_aniso_water.pdb) |
| E049 | portable | portable script, end of round 3 (2.5 sigma pick + clash cleanup; aniso refused); clashscore 4.6, rotamers 1.2 % | 0.07562 | 0.07303 | 0.07823 | 0.05760 | 0.01801 | 17,425 (7,722) | 6 × 0.167 | 2,011 | 508.1 | 9,338 | [E049_r3_pick_cleanup.pdb](models/E049_r3_pick_cleanup.pdb) |
| E049 | portable | portable script, end of round 4 (2.5 sigma pick, 99 sites; aniso refused), run still going; clashscore 4.9, rotamers 1.2 % | 0.07493 | 0.07276 | 0.07712 | 0.05660 | 0.01832 | 17,617 (7,722) | 6 × 0.167 | 2,203 | 528.5 | 9,309 | [E049_r4_pick.pdb](models/E049_r4_pick.pdb) |
| E048 | driver | E044 driver, end of round 2 (cleanup, 2.5 sigma pick, anisotropic waters; connectivity loop refused), run still going; clashscore 4.6 | 0.08378 | 0.08222 | 0.08536 | 0.06879 | 0.01499 | 16,861 (7,722) | 6 × 0.167 | 1,447 | 442.8 | 9,139 | [E048_r2_aniso_water.pdb](models/E048_r2_aniso_water.pdb) |
<!-- rep-table:end -->

The harness's own evaluator (phenix.refine's Wilson outlier rejection) gives the same numbers to within 0.0001; its values
are in `trajectories/`.

## Paired controls

Each stage was judged against its own paired control at equal loop count, in σ of this representation's floor. Numbers in
this section are the harness evaluator's, from the decision rows and the stage logs in `trajectories/`.

- **Stage 1 (E035, D513).** T beat C1 in 54 of 54 paired rows after loop 1 across three starts. Mean ΔT−C1 full −0.0009
  (range −0.0008 to −0.0016); select −1.5 to −5.6σ_select; the report half agreed from loop 2; Δgap −2 to −9σ_gap (T's gap
  narrower, R-work equal). Against C2 the mean was −0.0007 full. Whole-trajectory best full R-free, T / C1 / C2: start 1
  0.10428 / 0.10548 / 0.10473; start 2 0.10377 / 0.10407 / 0.10394; start 3 0.10373 / 0.10395 / 0.10368 (C2 edges T by
  0.00005 on start 3, inside σ_full). Clashscore at loop 11: T 6.6, C1 12.4, C2 9.7 at equal bond and angle RMS. Reading: a
  rate effect (the same R-free in about half the loops) with an endpoint gain of about 0.001 full.
- **Stage 2, Phenix picker (E035b, D514).** Negative. Nine one-parameter diagnostics all ended above the base. Deleting the
  793 copy waters below occupancy 0.02 and re-refining costs nothing (0.10433 vs 0.10447), so the loss is inside
  `ordered_solvent`, not in its culling.
- **Stage 2, own picker (E035f).** After one loop every control arm fell 0.006–0.007 full (C2 0.10489 → 0.09789, C1 0.10554
  → 0.09914), all subsets agreeing; Δgap +0.0004 to +0.0007 (2.5–4σ_gap). T stayed below C1 at every matched loop; mean ΔT−C1
  full over the three starts −0.0016 to −0.0021 (`trajectories/e035f_stage2p/result.json`). The plain loop then plateaued at
  0.094–0.095 (T arms); the controls at 0.096–0.097.
- **Stage 3 (E035c).** From the stage-1 endpoints every operation was null (≤ 0.0002 full). From the E035f loop-2 models,
  against the plain E035f loop from the same model at the same depth: cycle 1 −0.0017 to −0.0023, cycle 2 −0.0020 to −0.0035,
  cycle 3 −0.0018 to −0.0036 full, every subset and every start in the same direction, gaps comparable (0.0088–0.0097). Cycle
  3 moved less than 2σ_full, so the run stopped there.
- **Anisotropic finish (E035d).** No paired control: a one-step conversion judged by the authors' 30 % rule and the R-gap
  gate. Harness, iso → aniso: T 0.09206 → 0.08792, T_r2 0.09233 → 0.08796, T_r3 0.09218 → 0.08812 full; R-work fell
  0.0077–0.0082; ΔR-free/ΔR-work 0.50 / 0.55 / 0.53; Δgap +0.0041 / +0.0036 / +0.0036.

## The remaining gap and E041

Best here against 44PS, full R-free: 0.09202 (isotropic, gate-clean) and 0.08789 (anisotropic, gate-refused) against
0.06566. The visible differences are the solvent (about half the water atoms and half the summed water occupancy of 44PS),
the manual identity fixes the authors made in stage 3, and two further rounds of loop, picking and manual work after the
anisotropic conversion.

E041 (registered 2026-10-03, campaign `state/notes/experiments.md`) replicates 44PS with the campaign harness. Phase A
decomposes the gap: 44PS through one restrained step of the campaign's loop (does the pipeline hold 0.066?); our best
protein with 44PS's waters; 44PS's protein with our waters. Phase B runs the paper's water treatment at scale with the
harness's own picker, an automated stand-in for the manual pass, and the anisotropic finish, repeated. Phase A started on the
pod at 2026-10-03T18:30Z; it had no results when this snapshot was taken. Results will be added here by a later refresh.

## Files

| Path | What it is |
|---|---|
| `models/E035c2_<arm>_cycle3.pdb` | Stage-3 cycle-3 model of each start (isotropic B), the E035d input. |
| `models/E035c2_<arm>_cycle3_map_coeffs.mtz` | The phenix.refine MTZ written with it: F-obs, R-free-flags (identical to the frozen flags: 8 712 free, 0 differing, checked 2026-10-03), F-model, 2FOFCWT/PH2FOFCWT, FOFCWT/PHFOFCWT. |
| `models/E035d_<arm>_aniso.pdb` | Anisotropic-B finish of the cycle-3 model. Fails the R-gap gate. |
| `models/E035d_<arm>_aniso_map_coeffs.mtz` | The MTZ written with it (same columns). |
| `scores/<row>.json` | Independent scorer output for every table row. |
| `scores/<row>.composition.json` | Atoms, hydrogens, ANISOU records, water atoms, summed water occupancy, occupancy per copy, per-site occupancy sum range. |
| `scores/ref_44PS.e041_20261003.json` | The 44PS score recorded at E041 registration, verbatim (same numbers). |
| `trajectories/<stage>/` | Each stage's TRAJECTORY.md and result.json where the stage wrote them (stage 1, E035b, E035f, E035c first run); score logs and READMEs for E035c second run and E035d, which wrote none. |
| `provenance.json` | Pod paths and SHA-256 of every source model and MTZ, Untangler commit, patch-script hashes, Phenix version, frozen-data hashes, campaign commit, SHA-256 of every file here. |
| `provenance_pod.json` | The staging record as written on the pod. |

Open a model with its maps:

```bash
coot representations/7KR0/models/E035d_T_aniso.pdb --auto representations/7KR0/models/E035d_T_aniso_map_coeffs.mtz
```

Re-score a model on the frozen flags:

```bash
phenix.python scripts/indep_rfree.py representations/7KR0/models/E035d_T_aniso.pdb targets/7KR0/data/7KR0_data.mtz \
  targets/7KR0/data/7KR0_flags.mtz targets/7KR0/data/7KR0_split.mtz out.json
```

Refresh from the pod: `scripts/pull_representations.sh` (see `docs/HOW_TO_USE.md`).

## E048 and E049 — blind replications from the deposited 7KR0 (2026-10-09, runs in progress)

Both start from `7KR0.cif` as deposited (the qFit multiconformer single model), build six complete copies at 1/6
occupancy with a 0.2 Å per-atom shake, and run rounds of per-copy water picking, anisotropic waters and clash cleanup.
Every move is judged against the same model refined without it (Δselect ≤ −2σ, Δreport < 0, Δgap ≤ +0.002, clashscore
≤ 5 or ≤ control, rotamer outliers ≤ 1.5 % or ≤ control). 44PS was never an input to either; the replication criterion
was stated before launch (within 0.003 full R-free of E041's 0.0689 with clashscore ≤ 5 and rotamer outliers ≤ 1.5 %).

- **E049** runs `scripts/portable/sixcopy_waters.py` from the campaign repository: one phenix.python file (cctbx + numpy,
  no harness). Rows `E049_r1_aniso_water` … `E049_r4_pick` are the model in force at the end of each round; the run was in
  round 5 when this release was staged (deposited 0.1175 → S0 0.1080 → 0.0857 → 0.0790 → 0.0757 → 0.0750 full R-free, all
  under both geometry caps). Trajectory: `trajectories/e049_portable/`.
- **E048** runs the E044 harness driver on the same start. `E048_r2_aniso_water` is its model in force after round 2
  (0.0840 full); its round-1 pick was refused on the gap bound (+0.0021), which is where the two runs diverge.
  Trajectory: `trajectories/e048_autosix/shaken_s02_dep/`.

The rows will be replaced by the final models when the runs stop; the numbers in the table are the independent scorer's.
