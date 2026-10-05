# Exploration registry (PROTOCOL §17, SPEC §19)

One row per exploration. Rationale is written before the run; result after. Attributable Δ is R-free-select,
treatment − null, against the target's σ_select. "Gates" lists legs failed under the thresholds file in force.

| id | target | name / script | rationale (one paragraph, written first) | paired control | result (attributable Δ, σ) | gates failed | deviation |
|---|---|---|---|---|---|---|---|
| E001 | 3TC7 | C — whole-protein qFit as ONE batch (`exp_qfit_whole_run.py`, `_resume.py`, `_gates.py`) | The per-change loop converged (run2); D413 showed conformers act collectively, so judge qFit's whole output as one change. | `runs/3TC7/experiments/qfit_whole/paired` (c32) | −0.00873 (4.8σ) | geometry, clashes (20.6), density | D424 |
| E002 | 3TC7 | C2 — per-conformer prune of C by the frozen rules (`exp_qfit_whole_c2.py`) | Remove only conformers a frozen rule rejects; keep the rest of the batch. | `c2/paired` (c33) | see D426 | clashes | D426 |
| E003 | 3TC7 | C3 — re-prune C2 with C2's evidence | Iterate the prune on refined evidence. | `c3/paired` (c34) | regressed (+0.006 vs base) | — | D428 (majors were pruned) |
| E004 | 3TC7 | C4 — prune from refined C2, majors kept | Test whether anything remains after C2 removed majors. | `c4/paired` (c35) | −0.00043 | dead end | D429 |
| E005 | 3TC7 | C5 — prune from refined C, all majors kept | Majors are the base's own conformers; prune only failing minors. | `c5/paired` (c36) | −0.00530 (2.9σ) | density (26 neighbours) | D429 |
| E006 | 3TC7 | C6 — C5's prune on the UNREFINED qFit coordinates | Controlled test of the starting coordinates. | `c6/paired` (c38) | −0.00541 | geometry, clashes (11.2), density | D434 |
| E007 | 3TC7 | C7 — segment-consistent prune (`exp_qfit_whole_c7.py`) | C5 broke backbone segments (D436); make each letter consistent along its segment. | `c7/paired` (c39) | −0.00612 (3.4σ) | clashes (17.3), density | D437 |
| E008 | 3TC7 | C8 — physical prunes propagated segment-wide (`exp_qfit_whole_c8.py`) | Keep clash/occupancy kills, propagate them; drop map-shift kills. | `c8/paired` (c40) | −0.00500 (2.8σ) | clashes (10.7), density | D439 |
| E009 | 3TC7 | C9 — C8 minus clash hubs TYR52 D / ARG182 C (`exp_qfit_whole_c9.py`) | Two minors carry most of C8's clashes; a conformer incompatible with every conformer of its neighbour cannot exist. | `c9/paired` (c41) | running 2026-09-04 | — | — |
| E010 | 3QUE | ensemble ptls sweep (`exp_ensemble_3que.sh 0.6 / 1.0`) | 3QUE's recorded number is an ensemble (D425/D431); ptls is its main knob; default 0.8 gave 0.2476. Scored with `ensemble_rfree.py` on our flags/halves. | none (representation, not a single-model change) | 0.6: 0.2485/0.2326/0.2652; 0.8: 0.2476/0.2375/0.2583 (best); 1.0: 0.2534/0.2402/0.2671 (full/select/report) | n/a (not depositable) | D446 |
| E011 | 7KR0 | whole-protein qFit as one batch (`exp_qfit_whole_run.py 7KR0 4`) | Per-residue qFit builds single conformers at 0.77 Å (D440); the operator's hand-built 6-conformer model proves 0.047 of R-free is there on identical flags. Try the segment-level builder. | `qfit_whole/no_h/paired` (c8) | c6 void (H confound, D451); c7 failed (phenix cannot hydrogenate altloc waters); **c8 heavy-atom fair: +0.00332 (8σ worse)** | clashes 9.3 → 12.1; 6 residues lose density; 51/9 neighbours | D453 |
| E017 | 3TC7 | C10 — C9 + water audit + per-residue rebuild of failing protein neighbours (`exp_qfit_whole_c10.py`, `autoref/stages/solvent_audit.py`) | Under v3 every candidate still fails on a few waters at H-bond distance of a new conformer and 1–3 protein neighbours (D442). PROTOCOL §4.1 orders the waters re-examined under the frozen rules (remove below floor; tag to compatible letters on a < 2.2 Å conflict; otherwise retain, recorded); the protein neighbours get the campaign's own per-residue qFit on the batch model so they are judged as split residues. One change set, paired against the campaign model, gates under v2 (row) and v3 with the audit as part of the set. | `c10/paired` (c42) | −0.005024 (2.8σ); 75/75 split; audit retained 6/6 waters; qFit single at 27/245 | clashes (9.8), density (A27, A245, A739, ACY401 under v3) | D449 |
| E018 | 3TC7 | segment occupancy constraints on the C9 batch (`exp_qfit_whole_e018.py`, `run_e018.sh`) | Backbone segment letters refined with per-residue occupancies (D445): D of 41–54 is 0.00 at one residue and 0.58 two residues later. qFit's `create_restraints_file.py` constrained groups tie a letter along its segment (SPEC §10.2) and were never applied. Candidate = refined C9, constraints on the candidate arm only; per-segment occupancies printed as C12's evidence. | `e018/paired` (c43) | −0.004589 (2.5σ) but **void**: qFit's per-letter constraint file left 64 residues over-occupied | rejected as a bug | D450 |
| E020 | 3TC7 | C12 — C9 + GLU245 segment extension, refined with per-segment COUPLED occupancy constraints (`exp_qfit_whole_c12.py`, `autoref/stages/segment_constraints.py`) | E018 redone with a constraint file that couples a segment's letters to sum to 1 (D450), plus PROTOCOL §5.2's fix for the unsplit residue bonded to a split segment (GLU245 takes 243–244's letters). Occupancy sums asserted after refinement; per-segment occupancies printed as the next prune's evidence. | `c12/paired` (c44) | **−0.002841 (1.6σ, no_change)** with coherent occupancies; extension skipped (241–246 already single) | clashes (11.0), density (v3: 4 waters + A27/A245/A224) | D452 |
| E022b | 7KR0 | k-state from short ensemble, k=2/3/6 (`exp_kstate.py`) | representation test at 0.77 Å where data can support copies | `kstate_k*/paired` (c9/10/13) | **rejected: +0.020/+0.021/+0.020 (worse), clashes 15/20/27 (D463)** | — | D463 |

## Ideas queued (rationale to be completed before each run)

- E012 7KR0 — **hydrogen model** (`exp_hydrogens_toggle.py 7KR0 5`): riding vs individually refined hydrogens, one paired cycle. **Result 2026-09-04: rejected, attributable +0.00113 (2.8σ worse) with R-work −0.0005 — over-fitting; riding stays (D447).**
- E013 3QUE — **ensemble → multiconformer distillation** (`exp_ensemble_distill.py 3QUE <ensemble> <cycle>`, rationale in its docstring): side chains clustered across the 25 ptls-0.8 members (average-linkage heavy-atom RMSD, cut 1.2 Å), clusters ≥ 15 % kept (≤ 3), medoids written as altlocs on the campaign model with occupancies = populations; backbone and waters unchanged. **Result 2026-09-04: rejected, attributable +0.00865 (6σ worse), R-work +0.005, 58/68 split residues pass, clashes 3.7 → 7.7 (D448).**
- E022 7KR0/3QUE — **k-state whole-molecule model** (`exp_kstate.py <T> <ensemble> <cycle> --k K [--uniform]`, `run_kstate.sh`; written 2026-09-04, first runs on 3QUE k=6 uniform / k=4 populations): the operator's 7KR0 model is six complete copies (A–F at every residue, D011) — a representation between a single model and an ensemble, and depositable. Build k complete conformers from an ensemble of the target (cluster members globally, medoids as copies, occupancies = populations, jointly refined with one constrained group per copy), judge like any change. First on 3QUE (ensemble exists, D425); for 7KR0 an ensemble must be run first (E023).
- E021 7KR0 — **diagnostic** (`exp_compare_6conf.py`): **done 2026-09-04 — six complete copies at 0.17 each, RSCC mean +0.006 vs ours, none worse (D454); the gain is the representation.**
- E023 7KR0 — **ensemble refinement** (`TARGET=7KR0 bash exp_ensemble.sh 0.8`): source of k states for E022; hours at 0.77 Å single-threaded. Launched 2026-09-04.
- E019 3QUE — **ensemble → ADP distillation**: the ensemble's gain at 2.7 Å is a distributed disorder description, not discrete states (D448). Convert each atom's positional spread across the 25 members into an anisotropic ADP (U = covariance of member positions, added to a base B) on the single model, then refine with ADPs starting from there — tests whether the single model's ADP refinement is stuck in a worse minimum than the ensemble implies. One paired cycle; cheap.
- E014 3TC7 — **network coupling**: the 18 cross-network clashes that are consistently re-letterable (D439) become non-coexisting when the two segments share an occupancy constrained group; test on C9's model.
- E015 any — **alternative program minima**: servalcat / REFMAC5 refinement of the campaign model on the same flags, scored by our evaluator; a different minimum is a different starting point for the ladder.
- E016 7KR0 — **solvent rebuilt from scratch** at sub-Å (all waters removed, `phenix.douse` + Coot re-pick, anisotropic water ADPs), judged as one batch.

## E024 3QUE — TLS partition search (single depositable model, 2.7 Å)
- **Rationale (before run):** at 2.7 Å the single model's harmonic B-factor under-captures correlated motion; TLS is the depositable, parameter-cheap way to model it, and `phenix.find_tls_groups` returns exactly one partition. Correlated motion is where the (non-depositable) ensemble gets its edge, so a better partition could recover part of that gain in depositable form. Sweep the granularity axis: whole molecule (1 group) / auto / 50-residue blocks (7) / 25-residue blocks (14), same base/seed/settings, auto arm = re-refine null (D418 regression common-mode), accept only on r_free_select past 2σ (0.00288), headline r_free_report.
- **Result 2026-09-06 (negative):** best arm blocks50 beats auto by 0.00088 on select = 0.6σ (< 2σ bar) and its report/full both worsen (0.2721/0.2629 vs auto 0.2662/0.2605) — over-fit, not a gain. perchain +0.00196, blocks25 +0.00173 (both worse). All arms' full R-free 0.2605–0.2646 > standing deliverable 0.2589 (re-refine regression). TLS partition is not a lever; auto grouping already optimal. 3QUE single model confirmed at its 2.7 Å floor. See D467. `runs/3QUE/experiments/tls_partition/summary.json`.

## E025 7KR0 — sampleworks learned local generator (density-guided partial diffusion)
- **Registered 2026-09-06, rationale before run.** All discrete-disorder / qFit / ensemble routes on 7KR0 are exhausted (D468): none reach the operator model's 0.0673, which is a six-copy ensemble our single-model tools cannot build (D454). sampleworks (diff-use/sampleworks) drives a generative structure model (Boltz-2 / RF3 / Protenix) with **partial diffusion from the input structure + real-space density guidance** on a local selection, producing an ensemble of physically-plausible alternate conformers — a learned local proposer that fills the niche where per-residue qFit is intractable at 0.77 A (D466).
- **Mechanism:** `sampleworks-guidance`/`run_grid_search.py --model {rf3|boltz2} --proteins CSV --scalers pure_guidance --partial-diffusion-step N --ensemble-sizes 8 --gradient-weights "0.0 ... 0.05" --align-to-input`. Input CSV: name, structure (cif), density (2Fo-Fc CCP4/mtz), resolution, selection. gradient-weight 0.0 = unguided (a built-in generation null); higher = more density steering. Checkpoints baked in the sampleworks image at /checkpoints/.
- **Integrity (PROTOCOL §3 / §13 / §17):** the guidance target is a 2Fo-Fc **map** (F+PHI), NOT raw F_obs+free-flags — identical in kind to what qFit reads. The generator is a PROPOSER only. The building map is computed from the 7KR0 base model, which was refined with the frozen flags and the free set held out. Acceptance is never on the generator's own score: sampleworks conformers → altloc multiconformer model → OUR paired control (null = base re-refined on the working set, candidate = base+conformers re-refined on the working set, both frozen flags) → R-free on the untouched free set, accept only on r_free_select past 2σ, headline r_free_report; then RSCC + altloc-clash + occupancy + geometry gates. No free reflection ever steers acceptance. This is the same proposer contract qFit runs under.
- **Plan:** (1) GPU sampleworks pod up; (2) build 7KR0 region inputs (2Fo-Fc map from base refinement, structure, selection on a disordered region); (3) smoke one region, one gradient weight, ensemble 8; (4) adapter to gates; (5) sweep gradient weight, judge; negative results recorded with the same care.
- **Result:** (pending)

### E025 progress 2026-09-06 — pipeline stood up end-to-end (boltz2), output not yet usable
- **Milestone: the learned generator runs end-to-end on the campaign, integrity-preserving.** sampleworks `swgen` pod up (H100, sampleworks image, checkpoints baked) mounting the autoresearch PVC — autoresearch untouched. boltz2 pure_guidance on 7KR0 (single-conformer heavy-atom start + 2Fo-Fc CCP4 map): `Guidance run successfully!`, density loss 0.515 → 0.393 (guidance pulls the model into the map), 2-model ensemble + full trajectory written to /home/dev/swout. boltz2 needs no live MSA (cached MSA found). The density target is a map (like qFit); no free reflection touched — proposer contract intact.
- **Bring-up notes (for reproducibility):** image ships deps+checkpoints, NOT source → sync sampleworks src, run `python -m sampleworks.cli.guidance` with `PYTHONPATH=.../src`, env `PATH`/`CUDA_HOME`/`LD_LIBRARY_PATH` set to the pixi env so torch JIT-compiles the `dilate_points_cuda` op (nvcc 12.9 + ninja in-env). Input must be a clean single-conformer heavy-atom **PDB** (phenix mmCIF and gemmi mmCIF both fail atomworks entity/sequence parsing; PDB carries the sequence). Cross-pod NFS writes have delayed visibility — stage inputs on the pod's local disk.
- **Blocker to usable output (next):** atom-count mismatch model=1281 vs input=1282 (one atom, likely C-terminal OXT / a missing side-chain atom) → boltz initialized x_init from the PRIOR, not the input, so it free-generated: CA-RMSD ~5.9 Å uniform even after Kabsch (global drift, not local disorder). Fixes: (1) make the input atom set exactly match boltz's sequence-built set so x_init = true structure; (2) raise `--partial-diffusion-step` (~120, per the RF3 occ-sweep scripts) so the input is only lightly noised → local perturbations. Then superpose, extract per-residue alternates, build altloc model, judge through paired control + gates on the frozen flags.

### E025 progress 2026-09-06 (v2) — generator produces usable, localized, density-guided ensembles
- **Fix applied:** removed C-terminal OXT so the input atom set (1281) matches boltz's sequence-built set → boltz seeds x_init from the true structure (no atom-mismatch warning); `--partial-diffusion-step 120` (per RF3 occ-sweep) lightly noises the input.
- **Result:** boltz2 pure_guidance, ensemble 4, 7KR0. Density loss 0.507 → 0.394. Post-alignment CA-RMSD 0.17–0.25 A (local perturbation, not the earlier 5.9 A free-generation drift). Movement is localized at flexible/disorder sites; largest and most ensemble-variable is **Glu A170** (1.68 A, spread 0.58) and **Leu A169** — both carry alternate conformers in the deposited 7KR0. The generator independently flags real alt-conf sites. (Backbone-CA probe; 75-77 is side-chain disorder, needs all-atom probe.)
- **Next (adapter → R-free):** superpose each generated model onto the base frame (Kabsch on stable CA core, transform in hand), graft the ensemble-variable residues as altloc conformers onto the base, assign occupancies (sum=1), then paired control: null = base re-refined on the working set, candidate = base + generated altlocs re-refined, R-free on the held-out free set; RSCC + altloc-clash + occupancy + geometry gates. Consider an all-atom (side-chain) mover probe and a guidance-strength sweep to reach 75-77.

### E025 CONCLUSION 2026-09-07 — boltz2 density guidance: validated proposer/detector, not a route past a sub-A deposited model
Full arc: generator stood up end-to-end (integrity-preserving, reads map only) → validated as disorder DETECTOR (46/54 flagged residues = deposited altloc sites, D470) and cross-validated PROPOSER (conformers lower held-out R-free vs stripped baseline, −0.0067 sign-consistent, D469). R-free outcomes on 7KR0 (deposited 0.1137; operator ensemble 0.0673):
- per-residue new disorder on the intact deposited model: sub-noise, no_change (D470).
- whole-molecule multi-copy K=4 (strong guidance): full 0.1239, biggest signal (−0.0178 vs stripped null) but ABOVE deposited 0.1137 (D471).
- diversity is capped: noise (pdstep 60==90, D472) and guidance strength (weak-guidance more-diverse copies score WORSE, 0.1262 vs 0.1239, D473) both confirm a fit-vs-diversity tradeoff — density guidance gives tight-well-fit OR diverse-poor-fit copies, never both, because the density is the crystallographic mean.
- **Bottom line: boltz2 density guidance does not beat the deposited 0.1137 and cannot approach 0.0673. The gap is the thermal-ensemble representation (phenix.ensemble_refinement samples diverse-AND-data-consistent copies; gradient guidance cannot), which does not complete on this pod at 0.77 A (D466).** boltz's validated roles (detector, proposer) are real and reusable. Reproducible: swgen pod bring-up + adapter (`exp_sw_distill.py` --multicopy) documented; generated ensembles staged on the autoresearch PVC; swgen pod torn down (home PVC kept).

### E026 — Coot refine-zone / regularize-zone as proposer and as local-refine engine (registered 2026-09-07, rationale before run)
- **Rationale (Jaime Fraser, 2026-09-07):** Coot's real-space tools operate on a zone, and it is often the multi-residue stretch, not the residue, that needs the move; alternate *real space refine zone* with *regularize zone*, aggressively, and control the weight matrix. Per-residue qFit is intractable at 0.77 Å (D466) and whole-protein qFit regresses (D453); a zone-level real-space proposer is the route "to get better than qFit" for local strain and mis-traced segments. Mechanism: `zone_rsr` proposer (D477) → the unchanged per-change gates (RSCC, neighbour, local geometry, altloc-aware clash, occupancy) → paired R-free with the R-gap monitor (D476).
- **Knobs:** `discrete.coot_zone` in thresholds_v4 — map_weight 50.0 (chapi default; GUI 60.0), n_cycles 20, rounds 2, regularize_between true, use_rama/use_torsion false, window 2, max_zone_len 9. Regularize is refinement at map weight 0 (unsetting the map does nothing in chapi 1.3.3).
- **Plan:** (1) smoke on the 7KR0 standing model — propose zones, push two through the gates with the frozen engine and one with the Coot engine (`scripts/experiments/exp_zone_rsr_smoke.py`, results in `runs/7KR0/experiments/zone_rsr_smoke/result.json`); (2) one `correction`-stage paired cycle per target under v4 (`scripts/run_dpdb.sh <T> --stages correction --max-cycles 1`), R-free-select and Δgap both reported; (3) weight sweep map_weight ∈ {20, 50, 100} × rounds ∈ {1, 2, 4} on the best-responding target, one paired cycle each, also with `use_rama` on where d_min ≥ 2.5 Å; (4) engine comparison real_space vs coot on the same accepted changes. Kill rule: if (2) passes no zone change through the RSCC gate on any target, the line stops and says so.
- **Result (1), smoke, 2026-09-07/08** (`runs/{3QUE,7KR0}/experiments/zone_rsr_smoke/result.json`, thresholds_v4, frozen engine = mmtbx selection refinement):
  - 3QUE: 12 zones proposed in 33 s (11 CaBLAM-flagged residues + 3 below RSCC 0.70). Of the three worst-fit zones evaluated, **A174–176 passed the full per-change gate** — zone RSCC 0.7136 → 0.7300 (+0.0164 against the +0.01 bar), neighbour worst drop 0.0039, geometry within band, no new altloc-aware clash, occupancies intact — the first `zone_rsr` acceptance; A115–122 (+0.0026, one new clash) and A309–313 (+0.0025) were reverted. Its paired R-free effect is step (2).
  - 7KR0: 11 flagged residues form 6 zones; 5 contain alternate conformations and are skipped in this version, leaving A90–92 (CaBLAM), already at RSCC 0.990 — Coot moved it 0.026 Å rms and the gate read −0.0008: nothing to fix there. Altloc-aware zones are the 7KR0 work and need a per-conformer Coot call (open).
  - **Bug found and fixed on the way:** Coot's `write_coordinates` carries no ANISOU, and both the residue splice (`zero_aniso`) and the whole-file Coot engine turned the zone (or the whole model) isotropic; on 7KR0 that alone read as −0.008 RSCC on the zone and −0.27 on untouched waters. Zone coordinates are now spliced positions-only (`splice_positions`), tensors kept — the −0.008 became −0.0008 and the 3QUE acceptance appeared.
  - **Coot as the sole local refiner fails the frozen geometry budget by construction:** on 3QUE A115–122 a Coot-refined zone reads 0.0136–0.0159 Å bond RMSD under phenix restraints at weight 50 / 20 / 8 and 20 / 200 / 1000 cycles, pure regularize included (`runs/verify_20260907/coot_geom/`), against 0.0025 Å for the base; the engine's budget ladder walked all three rungs on both targets and none was within +0.003 Å. Coot proposes, the mmtbx engine re-idealises: `discrete.local_refine` stays `real_space`.
- **Next:** step (2) — one `correction`-stage paired cycle on 3QUE and 3TC7 under v4 (`scripts/run_dpdb.sh <T> --stages correction --max-cycles 1`), R-free-select and Δgap reported; then the weight sweep (3) and per-conformer zones for 7KR0.

### E027 — site-restricted reciprocal refinement per change (registered 2026-09-08, rationale before run)
- **Rationale (Spencer, Stephanie; D480):** judge each Coot change by a reciprocal-space refinement that moves only the modified residue(s), paired against the unchanged base refined the same way, then batch about five kept changes into one full refinement. Prevents overfitting elsewhere (the R-gap point) and stops good local changes being rejected for whole-model drift in phenix.refine's early macro-cycles.
- **Knobs (thresholds_v5):** `discrete.local_reciprocal` — macro_cycles 8, bound_k 2.0 (drop when attributable ΔR-free-select > +2σ_select), standing weights (no optimisation), TLS off; `discrete.max_changes_per_cycle` 5.
- **Plan:** (1) smoke: rerun the E026 zone smoke on 3QUE under v5 so the zone that passed the local gates (A174–176) goes through the restricted pair (`exp_zone_rsr_smoke.py --target 3QUE --thresholds thresholds_v5.yaml`); (2) one `correction` cycle per target under v5 via `scripts/run_dpdb.sh <T> --stages correction --max-cycles 1`: five kept changes → full paired cycle, R-free-select, Δgap and the new per-cycle record reported; (3) compare against the same cycle under v4 (no restricted step) on 3TC7, where D474 showed the water cycles as the overfit-risk zone. Kill rule: if the restricted step drops every change that the local gates passed on every target, report and reconsider bound_k.
- **Result (1), smoke 2026-09-08** (`runs/3QUE/experiments/zone_rsr_smoke/changes/3QUE.c063.zone_rsr.A174-176/local_reciprocal.json`): phenix.refine accepts the restricted parameterisation (`sites.individual=chain A and resseq 174:176`, matching ADP/occupancy selections, TLS off, 8 macro-cycles, 2764 atoms fixed). Null arm R-free-select 0.26482 / full 0.27038; candidate 0.26515 / 0.27134; **attributable +0.00033 (within +2σ_select = 0.00288) → kept for the batch**; Δgap +0.0006; each arm 2 min. Common-mode finding: both arms sit ~0.011 above the base (0.2589 full) — the D418 TLS-model regression under a no-TLS pass — so the restricted pair is used as a judge and the real-space candidate stays the model in force (changed before merge; D480). Step (2) launched on all three targets under v5; the first launch (`*.20260908v5`) hit the empty-selection bug on water changes (D483) and was relaunched as `*.20260908v5b` (3TC7 correction,solvent,protein_altloc from c051; 3QUE correction,solvent from c071 — qFit builds nothing at 2.7 Å; 7KR0 correction,solvent from c031).

### E028 — riding hydrogens on 3TC7 and 3QUE (registered 2026-09-09, rationale before run)
- **Rationale:** SPEC §6.1 and PROTOCOL §4 both say riding hydrogens are on during refinement, but the harness never
  adds them (`RefineParams.add_hydrogens=False`) and the deposited 3TC7 and 3QUE models carry none, so every 3TC7 and
  3QUE refinement of the campaign — noise floors, deliverables, both arms of every paired cycle — ran without
  hydrogens (composition checked 2026-09-09 with iotbx: 3TC7 2509 atoms / 0 H, 3QUE 2850 / 0 H; 7KR0 carries its
  1990 riding H from the deposition). Riding H add no parameters, contribute to F_calc and to the non-bonded
  restraints; at 1.5 Å the expected effect on R-free is a few thousandths, at 2.7 Å smaller and mostly geometric
  (clashes). This is protocol compliance judged as a change: one paired cycle per target, candidate arm
  `main.find_and_add_hydrogens=True hydrogens.refine=riding`, null arm the standing refinement, same seed and
  standing overrides. Not run on 7KR0 (already has H; E012 covers the individual-H question).
- **Script / cycles:** `exp_refine_param.py 3TC7 54 --knob riding_h --eid E028`; `exp_refine_param.py 3QUE 74
  --knob riding_h --eid E028 --refine-extra <run5 standing: water occupancies + pinned TLS>`; thresholds_v5.
- **Result, first run 2026-09-09 (mis-specified, kept for the record):** `phenix.refine main.find_and_add_hydrogens=True`
  adds hydrogens to **waters only** — the 3TC7 c054 candidate output carries 462 H = 2 × 231 waters and no protein H
  (`runs/3TC7/experiments/e028_riding_h/result.json`). As a water-hydrogen test it is null: attributable +0.00065 (0.4σ),
  report +0.00006, full +0.00035, Δgap +0.0007 (0.3σ_gap), `no_change`. The 3QUE arm (c074) crashed inside phenix.refine
  (`CCTBX_ASSERT(f.use_u_iso())` in ADP weight optimisation: freshly added H against `adp.individual.isotropic=all`),
  no model written, `defects` row. Protein riding H must be added before refinement, as SPEC §6.1 says: **E028b** uses
  `mmtbx.reduce2 approach=add add_flip_movers=False` on the base and passes the hydrogenated model as
  `--candidate-model` (knob `riding_h_pre`): 3QUE 2854 H added, 2850 heavy atoms unchanged (max 0.0008 Å); 3TC7 2323 H
  added, 2509 heavy atoms unchanged except the four ring atoms of Phe A81, which reduce2 relabelled CD1↔CD2 / CE1↔CE2
  (each "moved" 2.36–2.39 Å = the symmetric partner's position; identical scatterers, identical F_calc). `phenix.ready_set`
  fails on this Phenix (eLBOW chemical-components reader). Cycles 3TC7 c057 (aniso + H) and c058 (H + iso B + TLS,
  the E029 combination) / 3QUE c077. Models in `runs/<T>/experiments/e028b_hydrogenate/refine_001H.cif`.
- **Result E028b, 3TC7 (c057, `runs/3TC7/experiments/e028b_riding_h_pre/result.json`), 2026-09-09: ACCEPTED.** Candidate =
  the deliverable with 2323 riding hydrogens from reduce2 (4832 atoms), null = the deliverable, both refined under the
  standing anisotropic protocol, seed 1. Attributable **−0.009941 on R-free-select (5.5σ_select)**; report 0.18003 →
  **0.16726**, full 0.18411 → **0.17276**, R-work 0.14727 → 0.13515; `model_vs_data` 0.184 → 0.173 agrees; Δgap +0.0008
  (0.3σ_gap — riding H add no parameters, and the gap says so); bond RMSD 0.013 → 0.007, angle 1.319 → 1.042; 135 vs 143
  trial weights. The first run's water-only hydrogens (c054) had given nothing, so the whole effect is the protein
  hydrogens' scattering at 1.5 Å. The largest single credited change of the campaign on 3TC7 (its whole gain over the
  deposited model had been −0.007 full). Consequences: independent re-score, full §7 record and promotion (D488); the
  noise floor was measured on the hydrogen-free protocol and is re-measured on the new base before any further change
  is judged against it (PROTOCOL §4.4). **Follow-up (D491):** the credit reproduces from its input in 10/10 seeds
  (`c000/noise_floor_h_input/`, σ_select 0.00042, mean full 0.1731) plus four more (`repro/`, 0.1728–0.1735); but re-refining
  the credited model under the standing optimised weights runs away in 8/10 seeds (ADP weights 1300–3300, R-free → 0.185,
  `c000/noise_floor_h/`), and is stable with the ADP weight fixed (3/3 at 0.1723–0.1726, `rerefine_fixedadp/`). 3TC7 runs now
  carry `optimize_adp_weight=False` as a standing override; the judging-protocol noise floor is measured under it.
- **Result E028b, 3QUE (c077, `runs/3QUE/experiments/e028b_riding_h_pre/result.json`): REJECTED under the standing
  protocol, attributable +0.016267 (11σ_select), R-work 0.2159 → 0.2366, report +0.0104, full +0.0134, `model_vs_data`
  +0.0139; Δgap −0.0073.** Two mechanisms, both recorded: (1) before refinement the hydrogenated model already scores
  worse (phenix Start R-work/R-free 0.2256/0.2736 against 0.2215/0.2650) — after ~60 hydrogen-free cycles the heavy
  atoms and B of this 2.7 Å model have absorbed the hydrogen density, so adding H back over-counts it until positions
  and B relax; (2) they could not relax: phenix's ADP weight optimisation on the hydrogen-bearing model chose
  `Best ADP weight 0.006` against 0.313 in the null arm (xyz weight 16.7 vs 26.6), freezing the B-factors, and R-work
  ROSE during refinement (0.2256 → 0.2289). Hydrogen B were reduce2's parent-B values, idealised by phenix to 1.2×
  parent each macro-cycle (both arms' logs: "Idealize ADP of riding H"); H occupancies equal their parents'. A weight
  optimiser that lands on a 50× smaller ADP weight is a refinement-protocol interaction, not evidence about hydrogens,
  so **E028c** re-runs the pair with the weights fixed in both arms (`optimize_xyz_weight=False`,
  `optimize_adp_weight=False`, phenix's default wxc_scale 0.5 / wxu_scale 1.0; cycle c079). Kill rule: if the fixed-weight
  pair also regresses beyond 2σ, riding hydrogens are dropped for 3QUE and the disagreement with SPEC §6.1 is recorded.
- **Result E028c (c079, `runs/3QUE/experiments/e028c_riding_h_pre/result.json`): REJECTED again — riding hydrogens are
  dropped for 3QUE (D490).** Both arms with phenix's default fixed weights (wxc_scale 0.5, wxu_scale 1.0, no optimisation):
  null R-work 0.1965 / select 0.2556 / report 0.2715 / full 0.2634; candidate 0.1819 / **0.2731** / 0.2613 / 0.2673 —
  attributable **+0.017455 on select (12σ)**, full +0.0039 (`model_vs_data` +0.0035 agrees), while the report half moved
  the other way (−0.0102): the two halves disagree by 0.02, and the gap widened +0.0186 (5.1σ_gap; R-work fell 0.015 with
  R-free up). Fixed default weights over-fit this 2.7 Å model in both arms (null gap 0.067 against 0.046 under the
  standing optimised protocol), and hydrogens make it worse, not better. Two protocols, two regressions, unstable halves:
  the hydrogen-bearing model of 3QUE is not a better model of these data. The 2.7 Å hydrogen-free minimum the campaign
  reached has absorbed the hydrogen density into heavy-atom positions and B (Start R-free +0.009 on adding H); a
  hydrogen-bearing 3QUE would have to be re-refined from the deposited (REFMAC, riding-H) model, which is a different
  chain, not a change to this one. Recorded as a disclosed deviation from SPEC §6.1 for 3QUE.

### E029 — ADP parameterisation by data-to-parameter ratio (registered 2026-09-09, rationale before run)
- **Rationale:** PROTOCOL §4 asks for the ADP model to be "chosen by data-to-parameter ratio and justified". 3TC7 sits
  exactly on the frozen boundary (`refine.aniso_max_dmin` 1.5, d_min 1.49995) and inherited anisotropic U from the
  deposition: 41 048 reflections over 2 509 atoms × 9 parameters is 1.8 reflections per parameter, gap R-free −
  R-work 0.037; PDB-REDO chose isotropic B for this entry (`BREFTYPE ISOT`). 3QUE has 10 790 reflections for 2 850
  atoms × 4 parameters (3.8 per atom, < 1 per parameter) with a 0.048 gap; the ensemble's gain there (D425) says
  the disorder is under-described, the gap says the individual B are over-fitted — both can hold. Arms: 3TC7
  isotropic B + TLS (`find_tls_groups`) vs the standing anisotropic; 3QUE one or two isotropic B groups per residue
  (phenix `group_adp`) + the pinned TLS vs individual B. Each is one paired cycle against the standing refinement;
  the R-gap monitor reads whether a gain arrives with a narrowing gap. A negative on 3QUE kills the "over-fitted
  ADP" reading and leaves E019 (ensemble → ADP distillation) as the next ADP test.
- **Script / cycles:** `exp_refine_param.py 3TC7 55 --knob iso_tls --eid E029`; `3TC7 56 --knob riding_h+iso_tls`
  (the two E028/E029 changes together, so an interaction is visible); `3QUE 75 --knob group_adp_1`; `3QUE 76 --knob
  group_adp_2`, both with the run5 standing overrides. Harness: `RefineParams.group_adp` added (strategy `group_adp`
  replaces `individual_adp`; `tests/test_phenix_refine.py`).
- **Result 2026-09-09 (negative on both targets; `runs/<T>/experiments/e029_*/result.json`):**
  - **3QUE one B group per residue + TLS (c075): rejected**, attributable **+0.010216** (7.1σ_select), R-work +0.011,
    report 0.2691 → 0.2816, full 0.2619 → 0.2732, `model_vs_data` +0.0085 agrees; Δgap +0.0004 (0.1σ_gap). Two groups per
    residue (c076): +0.002601 (1.8σ), report +0.0007, full +0.0017, `no_change`. Fewer ADP parameters lose fit on the
    free set at once: the individual B are not over-fitted in the harmful sense despite < 1 reflection per parameter —
    the restraints carry them. The "over-fitted ADP" reading is dead; E019 (ensemble → ADP) stays the next ADP test.
  - **3TC7 isotropic B + TLS (c055, 9 TLS groups from `find_tls_groups`): `no_change`**, attributable −0.001708
    (0.9σ_select, below the 2σ bar) with the **report half +0.0048 and full +0.0015 worse** and `model_vs_data` +0.0013
    — the select gain is not confirmed on either other set, so it is noise, not a gain; R-work +0.007, Δgap −0.0055
    (2.4σ_gap narrower, the expected effect of dropping ~12 000 parameters). Anisotropic U stays for 3TC7: at 1.8
    reflections per parameter the data still prefer it on every set that was not consulted. The combined arm
    (riding_h + iso_tls, c056) crashed on the water-hydrogen assertion described under E028 and is re-run as E028b/E029
    c058 with the pre-hydrogenated model.
  - **3TC7 riding H + isotropic B + TLS (c058, re-run with the pre-hydrogenated model after D487): `accepted` against the
    hydrogen-free null** (attributable −0.010409; select 0.17768, report 0.17255, full 0.17515; 9 TLS groups; Δgap −0.0093)
    **but not adopted**: the sibling arm c057 (riding H + anisotropic U, promoted under D488) is better on report (0.16726)
    and full (0.17276) by 0.005 / 0.002, and its select deficit (0.17815 vs 0.17768) is 0.3σ. Same pattern as the
    hydrogen-free pair (c055): isotropic + TLS buys a little on the consulted half and loses on the halves that were not
    consulted. Anisotropic U stays for 3TC7; the ledger row carries the annotation.
  - Wall clock: 3QUE 7–9 min per arm, 3TC7 17–22 min per arm, single-threaded.

### E030 — refinement convergence on 7KR0 (registered 2026-09-09, rationale before run)
- **Rationale:** 7KR0's whole gain over the deposited model is continued refinement (CLAUDE.md: −0.003, ≈11σ, "not
  modelling"), and the latest re-refinement pass still moved the full R-free −0.00026 (v5b c032 null arm) with the
  report half flat. Every pass is 5 macro-cycles with weights re-optimised; on 4 298 atoms (2 308 anisotropic) at
  0.77 Å that may not be converged. Candidate arm: 15 macro-cycles from the deliverable; null arm: the standing 5,
  same seed. If the candidate clears −2σ_select (0.00081) with the R-gap flat, refinement was unconverged and the
  deliverable moves by a credited `weight_change`; if the gain is within noise, the drift is noise and further
  passes on 7KR0 stop. Cheap (single-threaded phenix.refine, ~30 min per 5 macro-cycles).
- **Script / cycle:** `exp_refine_param.py 7KR0 33 --knob macro_cycles:15 --eid E030`; thresholds_v5.
- **Result 2026-09-09 (`runs/7KR0/experiments/e030_macro_cycles15/result.json`, c033): ACCEPTED, marginally.** 15 macro-cycles
  against the standing 5 from the same base and seed: attributable **−0.000845 on R-free-select (2.1σ; bar −0.000810)**,
  report 0.11579 → 0.11547 (−0.0003), full 0.11362 → 0.11303 (−0.0006), R-work 0.10468 → 0.10433, `model_vs_data` 0.1136 →
  0.1130; Δgap −0.00024 (1.2σ_gap narrower); bond/angle 0.012/1.58 vs 0.013/1.57; 96 trial weights vs 66; 60 min vs 38.
  The candidate's own log: 0.1052/0.1139 → 0.1043/0.1130 over 15 cycles, i.e. the extra ten cycles bought 0.0006 of R-free
  beyond the five. Reading: the 7KR0 refinement was not converged, by a small margin. Credited by the letter of the rule
  (all four bars; a parameterisation change has no local-density leg, as E012); independently re-scored, §7 record and
  promotion by `promote_experiment.py` (D489). The judging protocol stays 5 macro-cycles, so the noise floor stands. One
  more 15-cycle pair from the new base (E030b, c035) decides whether anything remains; within noise closes the line.
- **Result E030b (c035, from the c033 base; `runs/7KR0/experiments/e030b_macro_cycles15/result.json`): ACCEPTED at the bar.**
  Attributable **−0.000817 on select against −0.000810** (2.02σ), report 0.11546 → 0.11526, full 0.11332 → 0.11281,
  `model_vs_data` 0.1133 → 0.1128, independent scorer select 0.11126 → 0.11043 / report 0.11533 → 0.11522 / full 0.11328 →
  0.11281 (`verify_20260909/7KR0_e030b_*`); Δgap −0.00025 (1.3σ_gap narrower); geometry unchanged (0.012 / 1.56). The second
  ten extra macro-cycles bought 0.0005 of full R-free, the first ten 0.0006: still not converged, decelerating. Credited and
  promoted (D493); **E030c** (c037) runs the third pass — the rule for stopping is unchanged (within noise closes the line).
- **Result E030c (c037, from the c035 base; `runs/7KR0/experiments/e030c_macro_cycles15/result.json`): ACCEPTED, the clearest
  of the three.** Attributable **−0.001005 on select (2.5σ)**, report 0.11541 → 0.11483 (−0.0006), full 0.11336 → 0.11257
  (−0.0008), `model_vs_data` 0.1133 → 0.1125, independent scorer agrees (`verify_20260909/7KR0_e030c_*`); Δgap −0.00039
  (2.0σ_gap narrower); bond/angle 0.013/1.61 vs 0.012/1.56 (within the band). Per-pass gains 0.0006, 0.0005, 0.0008 — not
  decelerating: at five macro-cycles a pass the 7KR0 refinement is well short of convergence, and the gap narrows each time.
  Promoted (D494). Next, instead of more 15-cycle steps, **E030d** (c039) pairs a single 40-macro-cycle refinement against the
  standing 5 from the new base (~4 h single-threaded); its result decides whether the line closes or a converged-refinement
  protocol becomes the 7KR0 standard (a versioned change, not a per-run override).
- **Result E030d (c039, from the c037 base; `runs/7KR0/experiments/e030d_macro_cycles40/result.json`): `no_change` — the line
  closes.** 40 macro-cycles against the standing 5: attributable −0.000594 on select (1.5σ), report 0.11528 → 0.11465
  (−0.0006), full 0.11302 → 0.11242 (−0.0006), `model_vs_data` 0.1130 → 0.1123; Δgap −0.00049 (2.5σ_gap narrower); geometry
  unchanged; 2 h 9 min vs 38 min. Phenix's own R over the 40 cycles: 0.1036/0.1125 → 0.1034/0.1123 — the model produced by the
  three credited passes is converged to within noise; the remaining headroom (≤ 0.0006 full) is below the bar and the
  candidate is not adopted. Continued refinement took 7KR0 from 0.1137 to 0.1126 full (0.1157 → 0.1148 report) in three
  credited steps; no per-pass macro-cycle change to the protocol is proposed, because a converged base no longer needs it.

### E019 — ensemble → ADP distillation, 3QUE (run registered 2026-09-09; idea queued 2026-09-04)
- **Rationale (before run):** the 25-member ensemble (ptls 0.8) is 0.2476 on our flags against the single model's 0.2589
  (D425), the gain is not discrete states (E013/D448) and E029 has just shown that fewer ADP parameters lose at once
  (group B +0.010), so the individual B are not harmfully over-fitted. The remaining ADP question is whether their
  refinement sits in a worse minimum than the ensemble implies. `exp_ensemble_adp.py`: for every heavy atom of the
  campaign model matched by (chain, resseq, name, altloc) to the 25 members, B_start = mean(B_member) + (8π²/3)·mean|r −
  r̄|², coordinates untouched, TLS-total ANISOU dropped (D418: neutral); unmatched atoms (waters re-picked by the ensemble)
  keep their B. Candidate = that model, null = base, both under the standing 3QUE protocol (individual B + pinned TLS +
  water occupancies). Judged like every change: ΔR-free-select vs 2σ_select (0.00288), sign on report/full and
  `model_vs_data`, Δgap recorded. One cycle (c078), ~10 min per arm. A null result closes the ADP line for 3QUE; a gain
  says the single-model B refinement is trapped and the ensemble's spread is the way out of the trap.
- **Script / cycle:** `exp_ensemble_adp.py <base> runs/3QUE/experiments/ensemble_ptls0.8/input_ensemble.pdb
  runs/3QUE/experiments/e019_ensemble_adp/base_ensB.cif` then `exp_refine_param.py 3QUE 78 --knob adp_start --eid E019
  --candidate-model <that> --refine-extra <run5 standing>`; thresholds_v5.
- **Result 2026-09-09 (`runs/3QUE/experiments/e019_adp_start/result.json`, c078): `no_change`, attributable −0.001154
  (0.8σ_select), report −0.00013, full −0.00066, `model_vs_data` −0.0006 — every set agrees in sign, none beyond noise.
  R-work rose 0.2159 → 0.2265 while R-free held: Δgap −0.0113 = **3.1σ_gap narrower** (the monitor flags only widening).
  Refined mean B 51.8 → 54.8. Reading: the individual-B refinement started from the ensemble's spread lands on a
  less over-fitted model at the same R-free — the B are not "trapped" in a worse R-free minimum, but the standing
  refinement buys ~0.01 of R-work the free set does not confirm. Not a credit; the model in force is unchanged. The
  distilled B are a candidate starting point for any later 3QUE change that would otherwise be judged against a
  null arm carrying the over-fitted B; the 2835/2850 match and per-atom table are in `base_ensB.per_atom.json`.

### E031 — waters clashing with one conformer take that residue's compatible letters, 7KR0 (registered 2026-09-09)
- **Rationale (before run):** the 7KR0 deliverable's altloc-aware clashscore (10.2 in the c032 record; cap 5.0) is
  dominated by rule `R2_blank_shared`: 21 of the 41 kept pairs are a full-occupancy blank-altloc water against an atom of
  ONE conformer of a split residue (14 waters — HOH 487 vs Phe 168 B at 0.96 Å overlap, HOH 352 vs Arg 141 B, HOH 202 /
  203 vs Asp 66 A / B, HOH 207 / 217 vs Glu 170 B / A, …). PROTOCOL §5.1: such a water takes the conformer it can
  coexist with, at that conformer's occupancy; §5.4 counts the overlap otherwise. The change is a relabelling with
  occupancy change and no coordinate move (`solvent_audit.tag_clashing_waters`, unit-tested): one copy per compatible
  letter at the letter's occupancy; a water clashing with every letter is removed. Judged as one batch: paired
  R-free-select vs ±2σ (0.00081), sign on report/full and `model_vs_data`, Δgap; altloc-aware clashscore of both refined
  arms (must not rise); RSCC of every tagged copy ≥ 0.70; occupancy sums; geometry band. Expected: the clashscore falls
  by roughly the weight of those 21 pairs; R-free moves little (the waters already refine at partial occupancy, mean
  0.93). An R-free-neutral result is geometry compliance to report, not a credit (D484 keeps the campaign model).
- **Script / cycle:** `exp_water_altloc_tag.py 7KR0 34 --eid E031`; thresholds_v5.
- **Result 2026-09-09 (c034, from the D485-restored base; `runs/7KR0/experiments/e031_water_altloc_tag/result.json`):
  R-free-neutral, geometry-compliant.** The frozen clash tool on the base kept 37 pairs (altloc-aware 9.22); 12 blank waters
  clashed with one conformer only → 11 tagged (HOH 201 → B 0.46, 202 → B 0.40, 203 → A 0.60, 204 → A 0.86, 205 → A 0.58,
  206 → B 0.41, 222 → A 0.59, 245 → A 0.55, 297 → B 0.47, 352 → A 0.86, 487 → A 0.59), 1 removed (HOH 207, clashing with
  both letters of Glu 170). Paired: attributable **−0.000142 on select (0.35σ; `no_change`)**, report +0.0006, full +0.0002,
  `model_vs_data` +0.0002, Δgap 0.00001. **Altloc-aware clashscore of the refined arms: null 9.46 → candidate 4.48; MolProbity
  clashscore 5.48 → 2.24 — both under the frozen cap of 5.0 for the first time on this target.** Tagged-copy RSCC ≥ 0.70 for
  10/11 (HOH 206 B at 0.58 fails the floor); bond/angle 0.013/1.59 vs 0.013/1.57; occupancy report unchanged (the three
  under-occupied groups 75–77, a D012-type finding). Reading: PROTOCOL §5.1 applied to the deposited water model removes most
  of the campaign's 7KR0 clash caveat at no cost in R-free. Not a credit, so not adopted by the harness (D484); adoption is the
  operator's decision under PROTOCOL §17(4). **E031b** re-runs the same procedure from the new base (E030, c033) at c036 so a
  clean candidate exists; the HOH 206 copy below the floor is a retention-rule case for that run to record.
- **Result E031b (c036, from the E030 base; `runs/7KR0/experiments/e031b_water_altloc_tag/result.json`):** 14 blank waters
  clashed with one conformer only (the c033 base adds HOH 207 → A 0.41, 218 → B 0.43, 488 → A 0.71 to the E031 list), 14
  tagged, none removed. Paired: attributable −0.000223 (0.55σ; `no_change`), report +0.0003, full 0.0000, `model_vs_data`
  0.0000, Δgap −0.0003. **Altloc-aware clashscore 9.46 → 4.98, MolProbity clashscore 5.48 → 2.49** (caps 5.0 / 5.0). 13/14
  tagged copies ≥ 0.70 RSCC; HOH 206 B at 0.65 (0.58 in E031) is the one below the retention floor and would go under
  SPEC §9 in an adopted version. Geometry band ok; occupancy report: the three known under-occupied groups only. Same
  reading as E031: the deposited water model's PROTOCOL §5.1 violations account for about half of the 7KR0 clash caveat,
  and fixing them costs nothing in R-free. The candidate arm's model is the clean version for the operator's decision; the
  procedure (`exp_water_altloc_tag.py`, 40 min) re-applies to whatever base is current.

### E032 — scaling and scattering parameterisations at 0.77 Å, 7KR0 (registered 2026-09-10, rationale before run)
- **Rationale:** 7KR0 is converged under the standing protocol (E030d) and every modelling route is exhausted, so what is
  left in reciprocal space is the physics of F_calc itself. Two phenix.refine defaults are approximations chosen for speed,
  not accuracy at sub-Å resolution: (1) the atomic form-factor table — `n_gaussian` fits each element with as few Gaussians
  as meet a tolerance; the Waasmaier–Kirfel (`wk1995`) and International Tables (`it1992`) tabulations are the reference
  fits and differ from it most at high sinθ/λ, which is exactly where 0.77 Å data live; (2) the bulk-solvent grid —
  `bulk_solvent_and_scale.mode=fast` searches k_sol/b_sol coarsely. Neither adds a parameter, so the R-gap should not
  move. Each is one paired cycle against the standing refinement of the c037 base (5 macro-cycles, weights optimised,
  seed 1); judged on select vs 2σ_select (0.00081), sign on report/full, Δgap under the v6 gate. Kill rule: within noise
  closes the reciprocal-parameterisation line for 7KR0.
- **Script / cycles:** `exp_refine_param.py 7KR0 40 --knob scattering:wk1995 --eid E032`; `… 41 --knob scattering:it1992`;
  `… 42 --knob bulk_solvent:slow`; thresholds_v6. Harness: `RefineParams.scattering_table` (X-ray tables only) and the
  `scattering:`/`bulk_solvent:` knobs.
- **Result 2026-09-10 (c040–c042, `runs/7KR0/experiments/e032_*/result.json`): all three within noise; the line closes.**
  Null arm (standing, from c037) R-work 0.10358 / select 0.11080 / report 0.11528 / full 0.11302.
  - `wk1995`: select 0.11080 (attributable **+0.000003**, 0.0σ), report **0.11462 (−0.0007)**, full 0.11270 (−0.0003),
    `model_vs_data` −0.0003, Δgap −0.00025; geometry unchanged. Better on both halves that were not consulted, exactly
    zero on the one that was — not creditable by the rule, recorded as the one candidate worth revisiting if the
    protocol is ever re-based (it adds no parameters).
  - `it1992`: +0.000073 (0.2σ), full 0.0000, report −0.0001 — indistinguishable from `n_gaussian`.
  - `bulk_solvent_and_scale.mode=slow`: +0.000382 (0.9σ), full +0.0005, report +0.0005, R-work +0.0012 — the finer
    grid lands on a slightly worse k_sol/b_sol pair; `fast` stays.
  Reading: at 0.77 Å the form-factor tabulation and the bulk-solvent grid are not where 7KR0's remaining R-free is.

### E033 — reference-model restraints on 3QUE from a 1.22 Å structure of the same protein (registered 2026-09-10)
- **Rationale (before run):** 3QUE (human p38α MAP kinase with Skepinone-L, 2.7 Å; REFMAC deposition) is at its floor for
  every modelling and ADP lever tried (D465, D467, D490, D492, E019, E029). The one knowledge-based restraint the campaign
  has not used is the reference model (Headd et al. 2012, in PROTOCOL's reading list): at low resolution, dihedral
  restraints to a higher-resolution structure of the same protein pull side-chain and backbone torsions toward
  well-determined conformations without fixing coordinates, typically improving geometry and R-free by a few
  thousandths. PROTOCOL §4 allows such restraints "only where resolution justifies them, and disclosed" — 2.7 Å
  qualifies, and the E-row and any D-row disclose them. Reference chosen by an RCSB sequence search executed
  2026-09-10 (identity ≥ 0.95, X-ray, resolution ≤ 1.8 Å: 108 entries; sorted by resolution): **6SP9**, 1.22 Å,
  "Fragment KCL802 in complex with MAP kinase p38-alpha" (PHENIX-refined), fetched from files.rcsb.org (SHA-256 in the
  run directory), hydrogens and waters stripped, written as `data/raw/refs/6SP9_ref.pdb`. Candidate arm: the standing 3QUE
  refinement plus `reference_model.enabled=True file=6SP9_ref.pdb` (phenix defaults: sigma 1.0, limit 15°, main and
  side chains, fix_outliers); null arm: the standing refinement; same seed and standing overrides (water occupancies,
  pinned TLS). Judged on select vs 2σ_select (0.00288), sign on report/full, Δgap under the v6 gate, geometry band. If
  credited, the restraints become part of the 3QUE protocol (disclosed) and the noise floor is re-measured under it.
- **Script / cycle:** `exp_refine_param.py 3QUE 83 --knob reference_model:/home/dev/data/raw/refs/6SP9_ref.pdb --eid E033
  --refine-extra <run5 standing>`; thresholds_v6.
- **Result 2026-09-10 (c083, `runs/3QUE/experiments/e033_reference_model6SP9_ref/result.json`): negative — `no_change` on the
  gate and a geometry failure.** Attributable +0.000554 on select (0.4σ); report 0.26909 → **0.27674** (+0.0077), full 0.26187
  → 0.26589 (+0.0040), `model_vs_data` +0.0037; R-work +0.008; Δgap −0.0040 (1.1σ_gap, narrower only because R-work rose
  more than R-free). Geometry: bond RMSD 0.002 → 0.005 Å, angle RMSD 0.466 → 1.051° — outside the frozen +0.30° band
  (`geometry_ok` false). phenix applied the restraints (reference_model block in the log; 4 unresolved dihedrals). Reading:
  pulling 3QUE's torsions toward the 1.22 Å fragment-complex conformations fights both the density and the ideal geometry
  at 2.7 Å; the standing model's torsions are already where the data put them. Reference-model restraints are not a lever
  here; the E-series on 3QUE closes at 0.2589 / 0.2644 with every reciprocal-space and restraint parameterisation tried
  (TLS partition, group B, ensemble B, hydrogens ×2, reference model) recorded as negative. No deviation row: nothing was
  adopted and no rule changes; the change row `3QUE.c083.restraint_regen.reference_model6SP9_ref` is `no_change` with the
  geometry failure in its reason.

### E034 — is a legacy model's noise floor convergence variance? σ from a converged base, 1LZ9 (registered 2026-09-17, rationale before run)
- **Rationale.** Phase 2 (D501) measured every noise floor the standard way: ten seeds of one 5-macro-cycle re-refinement of the
  deposited model. For the CNS/REFMAC-era entries the floors are enormous — 1LZ9 σ_select 0.005895 (credit bar −0.0118), 6UDY 0.0087
  (−0.0174), 4QO4 0.0019 — and the same models keep moving on every further pass: 1LZ9's R-free-select went 0.2941 (baseline
  re-refinement) → 0.2789 (the run's cycle 0) → 0.2737 (cycle 2) with only ten sub-floor waters removed in between, and its run ended
  with nothing credited because nothing can clear 0.012. A floor measured on an unconverged model is the spread of where one pass
  lands, not the reproducibility of a converged refinement; if σ from a converged base is several times smaller, the phase-2 method
  needs a convergence step before the floor (the 7KR0 precedent: E030's 15-macro-cycle passes, D489), and the phase-2 verdicts on the
  legacy targets must be read as "not measurable", not "no improvement".
- **Design.** `scripts/experiments/exp_noise_floor_converged.py 1LZ9 <run final model> --eid E034 --n 10`: the same seed machinery as
  `stages/noise_floor` (same RefineParams, frozen data/flags, split evaluation; `jobs` rows), output under
  `runs/1LZ9/experiments/e034_nf_converged/`, compared with the standing row's σ, means and σ_gap. The start model is the run's final
  base `1LZ9.20260917T053914Z/cycles/c004/escape/null_arm/refine_001.cif` (six 5-macro-cycle passes from the deposited model). The
  `noise_floor` table is keyed on target alone, so the script writes NO row — replacing the judging σ is an operator decision.
  thresholds_v8. Cheap: ten refinements of a 1214-atom lysozyme.
- **Result 2026-09-17 (`runs/1LZ9/experiments/e034_nf_converged/result.json`, 10/10 seeds): the floor from the converged base is
  3.5× smaller.** σ_select 0.005895 → **0.001665** (ratio 0.28), σ_report 0.00532 → 0.001806, σ_full 0.005568 → 0.001332;
  σ_gap unchanged (0.00178 → 0.00202). Means: R-free-select 0.2872 → 0.2774, full 0.2758 → 0.2661 — the ten seeds from the
  six-pass model land 0.010 lower than the ten seeds from the deposited model, and 0.0035 *above* the six-pass model's own
  select (0.2739): re-refinement of a base regresses it a little (the D418 effect), and the standing floor is mostly the
  spread of where the first pass from the deposited model lands. Under this σ the credit bar would be −0.0033, not −0.0118.
  Reading: for the legacy CNS/REFMAC/X-PLOR entries the phase-2 floors measure convergence variance, not test-set noise; the
  phase-2 verdicts on them ("nothing credited") mean "not measurable at this bar", not "no improvement". The D491 lesson
  applies — the floor must be measured from the model the cycles are judged from, which in phase 2 is the re-refined
  baseline (the run's cycle-0 input), not the deposited file. **E034b** (launched 2026-09-17T09:2xZ, `e034b_nf_converged/`)
  measures the floor from exactly that model (`c000/baseline_rerefine/refine_001.cif`, one pass in) to see whether the
  D491-consistent input alone recovers most of the reduction or a convergence step is needed.
- **E034b result 2026-09-17 (`e034b_nf_converged/result.json`, 10/10): the one-pass baseline does NOT recover it.** From
  `c000/baseline_rerefine/refine_001.cif`: σ_select **0.004219** (ratio 0.72 to the standing 0.005895), σ_report 0.006099 (larger),
  σ_full 0.005115, σ_gap 0.001098; means select 0.2828, full 0.2729. So the floor stays at 0.004–0.006 one pass in and reaches
  0.0017 only after six passes: the legacy model needs a convergence step (several 5-macro-cycle passes, or E030's 15-macro-cycle
  passes, D489) before either the floor or the cycles are meaningful. Recommendation (D506, not adopted here): a versioned
  `noise_floor.converge_passes` (or baseline macro-cycles) applied before the floor, the floor re-measured from that model, and the
  phase-2 runs on the legacy targets repeated from their standing records under it. No judging row was changed;
  adopting either floor for the phase-2 targets is a D-row decision (the D488/D491/D496 precedent), and the runs would be
  repeated from the standing records under it.

### E035 — connectivity optimization of a six-copy 7KR0 ensemble (Untangler, Passmore et al. 2026), stage 1 with paired controls (registered 2026-09-21, rationale before run)
- **Source.** Passmore, Holton, Zatsepin & Martin, "Optimizing the connectivity of protein conformations to untangle ensemble
  refinement", bioRxiv 10.64898/2026.09.17.752399 (posted 2026-09-19; PDF read 2026-09-21, text in the run directory). Code:
  github.com/Phoelionix/Untangler, branch `conformational_tree`, commit 1776c8d (cloned 2026-09-21). The paper's Mac1 model
  (their PDB ID 44PS: six conformations, anisotropic B, 178 288 reflections, 8 709 free, R-work 0.0473, R-free 0.0642, Table II) is
  built on 7KR0's data — the same 0.77 Å dataset as our target — and the operator's six-copy model scored 0.0673 on our flags
  (D455). 44PS, 45KK and 45PC were not yet released at RCSB on 2026-09-21 (`data.rcsb.org` returned 404 for all three; 7KR0, 4PSS,
  5KXK, 4PTH, 1AHO resolved).
- **Mechanism (one paragraph).** An ensemble model's altloc labels can be reassigned without moving any atom, so the model's
  structure factors are unchanged while its geometry energy E changes: which altloc of atom m bonds to which altloc of atom n is
  a choice. Refinement never explores that choice (it would have to pass through coordinates that fit the density badly), so
  ensembles get trapped in "conformation mix-ups" with strained geometry. Untangler writes the choice as a binary integer linear
  program over "geomections" (bond, angle, non-bond and clash terms for every altloc pairing), minimizes E with an ILP solver, and
  alternates that with phenix.refine: one unrestrained macro-cycle (atoms find density), connectivity optimization (labels find
  geometry), ten restrained macro-cycles. On DHFR 4PSS the paper's Fig. 9 shows the loop beating two controls (same loop without
  the optimizer; restrained refinement only) on R-free and geometry until overfitting past loop 13. The R-free effect, if real,
  comes from letting the six copies relax to lower-energy conformations that then fit better — a different lever from every
  single-model route the campaign has exhausted on 7KR0 (D453, D463, D466, D468, D469–D473).
- **Design.** Target 7KR0, frozen data.mtz and inherited flags (free = 0, n_free 8712; the Untangler template has
  `r_free_flags.generate=False`, `test_flag_value=0`, so it refines against the same test set; the scorer asserts the counts).
  Base B0: deposited 7KR0.pdb (a qFit multiconformer model, as the paper's inputs) → `split_qfit_to_6conf.py` (six contiguous
  copies A–F, waters split, 0.5 Å shake; the paper's construction) → occupancies set to sum to exactly 1.000 per site
  (0.167 ×4 + 0.166 ×2; the splitter's 0.167 ×6 = 1.002 is the D011 rounding artefact) → deposited REMARK 290 block restored →
  20 restrained macro-cycles at the paper's geometry weight wc = 0.5, seed 42. Arms from B0, same seed: **T** = the paper's
  stage-1 loop (`untangle.py` defaults: 1 unrestrained mc, connectivity optimization, 10 restrained mc, wc 0.5); **C1** = the same
  loop with the optimizer disabled (paper Fig. 9 green); **C2** = 10 restrained mc per loop (Fig. 9 blue). Loop cap 26 (the
  code's default), time box 48 h from launch. σ of the six-copy representation: five seeds of the loop's restrained step (10 mc)
  from B0. Scoring: `exp_untangler_score.py` through `autoref.flags.evaluate` (consult=False) on every loop model of every arm.
- **Pre-registered readout.** Primary: Δ_k = R-free-select(T_k) − R-free-select(C1_k) at equal loop count, in σ_select units,
  sign confirmed on report and full; secondary vs C2; Δgap (T − C1) in σ_gap units as the overfitting monitor. Endpoint per arm
  by the paper's own rule applied identically (last loop before three consecutive rises in select), with the whole trajectory
  reported. "Replicated" = Δ beyond −2σ_select at the endpoints with report/full agreeing and Δgap not beyond +2σ_gap. The absolute
  R-free of T is reported against the single-model deliverable (0.1126 full) and the operator's six-copy model (0.0673) as a
  representation-level number: an ensemble has no `changes` type (SPEC §19; D427) and is not a deliverable (CLAUDE.md). Geometry
  and altloc-aware clashes of the endpoint model are reported separately (PROTOCOL §17.4).
- **Departures from the paper, disclosed.** ILP solver CBC (PuLP's bundled COIN-OR) instead of CPLEX 21.1.1 (IBM academic
  licence not obtainable autonomously; the paper says PuLP's default is COIN-OR and used CPLEX for speed) — solve-time limits
  therefore bind more often, which can only weaken T. Phenix 2.1-6048 (paper: 2.0 for water picking; stage 1 does not pick
  waters). Stage 2 (conformation-aware water picking) and stage 3 (manual Coot work) are not part of E035; stage 2 is E035b if
  stage 1 replicates. Patches to the code are limited to solver choice, environment-driven control flags, seed and thread count
  (`scripts/experiments/untangler_patch.sh`; the diff is written into every arm directory).
- **Scripts / layout.** `scripts/bringup_untangler.sh` (tcsh, gnuplot, clone, venv `/home/dev/envs/untangler`, pulp 3.0.2 + CBC),
  `scripts/experiments/exp_untangler_7kr0.sh {setup,base,floor,arms,score}`, `scripts/experiments/exp_untangler_score.py`;
  `runs/7KR0/experiments/e035_untangler/{PROVENANCE.txt,base,floor,arms/{T,C1,C2},rfree,scores.json,trajectory.json,result.json,
  TRAJECTORY.md}`. Thresholds in force: v8 (nothing in E035 consults the select half or touches a ledger `changes` row).
- **Environment notes (2026-09-21, before any arm ran).** Three defects fixed before the base refinement would start, all
  outside the science: (1) the wrapper's phenix templates carry a `refinement.main.ddr` block that Phenix 2.1-6048 rejects as
  unrecognized PHIL (removed from all six templates); (2) `Refine.sh` tests the geometry weight with `(( $wc == 0 ))`, which
  fails on 0.5 (float-safe comparison); (3) the wrapper takes one reflection file and our `data.mtz` carries no flag column, so
  `e035_merge_mtz.py` copies the inherited `R-free-flags` array next to FP,SIGFP (178324 reflections, 8712 free, asserted; SHA-256
  cb925bdb…). Base B0 started 2026-09-21T18:24Z: 17286 atoms (six copies, waters split), initial R-work/R-free 0.4845/0.4966
  after the 0.5 Å shake; 20 macro-cycles at wc 0.5, seed 42.
- **Environment note 2 (2026-09-21T20:24Z).** All three arms died at import under the venv's Python 3.9: `Solver.py:2435` uses a
  backslash inside an f-string expression (PEP 701, Python ≥ 3.12); the README's "tested with python 3.9" does not hold for this
  branch. Venv rebuilt on a uv-managed 3.12 (every module untangle.py imports compiles; only the unused
  `tensions_to_chimerax_colors.py` does not), arms relaunched from the same B0 and seed. The five floor seeds were unaffected.
  B0 after 20 macro-cycles (phenix log): R-work 0.1149 / R-free 0.1213 on its own flags line; harness score below.
- **Environment note 3 (2026-09-21T20:5xZ).** Arm T died in its first ILP solve: `untangle.py` uses the sites formulation
  (`Solver_sites_formulation.py`), which selects CPLEX independently of `Solver.py`; the patch now sets CBC in both. T relaunched
  from the same B0 and seed ~35 min behind C1/C2 (pairing is at equal loop count, so the lag is immaterial). First solve
  statistics from the crashed attempt: 8 619 bond, 98 610 angle and 203 clash geomections, clashscore 19.7 on the unrestrained
  model, ensemble subsets of five copies per subproblem.
- **Environment note 4 (2026-09-21T21:51Z): floor protocol corrected.** The arms' restrained step is `Refine.sh … -c 0.5 -u 1 -n 10
  -s 0.0 -q 0.1 -W -N` (untangle.py's `default_refine_water_occupancies=True`: the occupancies of the ~1 900 per-copy waters are
  refined each loop; NQH flips off). The first floor omitted `-W` and sat at full 0.11675 (σ_select 0.00006, σ_report 0.00010,
  σ_full 0.00005 over five seeds) while C2's loop 1 with `-W` reached 0.11117 — water-occupancy refinement alone is worth ≈0.0055
  on this representation. Kept as `floor_noW/` (aside), floor re-measured with the identical flags into `floor/`; σ for the
  paired table comes from the corrected floor. First control loops on our flags: C1_k1 (1 unrestrained + 10 restrained) full
  0.11205 / report 0.11498 / select 0.10915; C2_k1 (10 restrained) 0.11117 / 0.11517 / 0.10720; B0 was 0.12131. Both controls
  are already below the single-model deliverable's full R-free (0.1126) with about four times its atoms — representation-level
  numbers, not deliverables (§18.1).
- **Environment note 5 (2026-09-21T23:24Z–23:50Z).** Arm T died a second time, in loop 2's fourth ILP subproblem: CBC exited
  non-zero with an empty log (PuLP raises `PulpSolverError`). Re-running CBC 2.10.3 on the leftover problem files (197 MB MPS,
  21 MB warm start) with 8 or 1 threads, with or without the warm start, exits 0 every time — a transient process failure, not a
  property of the problem. Patch (6): the solve call retries up to three times (same settings, one thread, no warm start), each
  retry logged; patch (7): `UNTANGLER_RESUME_LOOP=k` resumes an arm at its saved `current<k>.pdb`. T relaunched at loop 1 from
  its recorded loop-1 model (same seed), so loop 2 is redone rather than the whole arm; C1/C2 untouched. Corrected floor
  (`-W -N`): σ_select 0.00028, σ_report 0.00024, σ_full 0.00025, σ_gap 0.00016; mean full 0.11118 = C2's loop 1 (0.11117).
  First paired row (loop 1): T select 0.10862 / report 0.11605 / full 0.11232 vs C1 0.10915 / 0.11498 / 0.11205 (ΔT−C1 −1.9σ on
  select, +4.5σ_report on report, +1.1σ_full on full, Δgap +0.9σ_gap) and C2 0.10720 / 0.11517 / 0.11117. Divergent sign; no
  reading before several loops.
- **Environment note 6 (2026-09-22T00:11Z).** With the retry in place T failed again in loop 2: attempts 0 (8 threads) and 1
  (1 thread) both raised `PulpSolverError`; attempt 2 (no warm start) ran to its 180 s limit with no feasible incumbent
  (`Status: Not Solved`) and the code then asserted on an unassigned site. Standalone reproductions of every failed problem
  file — PuLP's exact arguments, 180 s, with and without the Phenix library path — exit 0; the container cgroup shows no OOM.
  The exit status was never visible because PuLP discards it. Patch (6) reworked: attempts are same-settings then one thread,
  the no-warm-start fallback is dropped, and on persistent failure the incumbent (warm start = current assignment) is kept for
  that subproblem and logged (`E035_solver_failures.txt`); `scripts/experiments/cbc_retry.sh` (PuLP `path` via
  `UNTANGLER_CBC_PATH`) runs CBC, records any non-zero exit status to `logs/cbc_wrapper_failures.log` and retries the identical
  command once. T relaunched at loop 1 again (00:11Z); C1 at loop 4, C2 at loop 4, untouched.
- **Environment note 7 (2026-09-22T00:45Z–01:04Z): solver changed to HiGHS.** The wrapper recorded the CBC exit status: 139
  (SIGSEGV), on loop 2's first subproblem, at ~195 s — i.e. when the 180 s limit fires. Reproduced standalone with PuLP's exact
  arguments on the saved problem (373 327 binaries, 857 309 constraints, 197 MB MPS + 21 MB warm start): CBC 2.10.3 segfaults
  with 8 threads and with 1 thread; CBC 2.10.13 (static release from coin-or/Cbc, sha256 86d52bb5…) segfaults too. HiGHS
  (highspy, PuLP's `HiGHS` API) solves the same problem to an integer-feasible solution at the limit (202 s incl. a 30 s MPS
  read in the test; status Optimal / Solution Found, objective 8.19e8). Patch (6) gains `UNTANGLER_SOLVER=highs`; T killed and
  relaunched at loop 1 (its loop-1 model on record is unchanged) with HiGHS at 01:04Z. The CBC attempts are kept as
  `logs/arm_T.attempt*.log` and `logs/cbc_wrapper_failures.attempt6.log`. Substitution chain now: CPLEX (paper) → CBC (PuLP
  default, crashes) → HiGHS; the paper itself notes PuLP's solver is interchangeable.
- **Interim (2026-09-22T05:30Z, T at loop 3; C1 loop 7; C2 loop 8; all on HiGHS/frozen flags).** ΔT−C1 at equal loop count:
  loop 1 select −1.9σ but report +0.0011 / full +0.0003 (divergent); loop 2 −1.5σ / −0.0004 / −0.0004 (all three agree);
  loop 3 −2.3σ / **−0.0015 / −0.0011**, Δgap −6.3σ_gap (T's gap narrower). T's R-work equals C1's at loop 3 (0.09952 vs 0.09956)
  while its R-free is lower — the paper's Fig. 9 signature (no R-work effect, R-free effect). Against restrained-only C2 T is
  still +2.3σ worse on select at equal loop (the unrestrained step costs R each loop). C2 has plateaued: full 0.10620 / 0.10621 /
  0.10625 at loops 6–8 with R-work still falling (0.09753 → 0.09716), i.e. it has started to overfit; C1 still falls slowly
  (0.10652 at loop 7). T's per-loop decrements are the largest of the three (0.11232 → 0.10866 → 0.10735 full). Open question
  for the next T loops: does T pass below C2's plateau (0.1062 full)? Provisional σ (N = 5). Full per-arm table in
  `TRAJECTORY.md`.
- **Interim (2026-09-22T07:45Z, T at loop 4; C1 loop 9; C2 loop 10).** ΔT−C1 at equal loop count is monotone in the paper's
  direction: full +0.0003 / −0.0004 / −0.0011 / **−0.0016** at loops 1–4 (select −1.9 / −1.5 / −2.3 / **−4.9σ**; report −0.0018 at
  loop 4; Δgap −8.7σ_gap, T's gap narrower). T's R-work equals C1's at every loop (0.09870 vs 0.09885 at loop 4): the gain is on
  R-free only, as in the paper's Fig. 9. T at loop 4 (full 0.10650) reaches what the controls needed 8 loops for (C1 0.10634 at
  loop 8; C2 0.10625) and is below C2 at equal loop on the full set (0.10650 vs 0.10670) while still +2.5σ behind it on select.
  Both controls have plateaued (C2 0.1060–0.1063 full over loops 6–10, R-work still falling → overfitting onset; C1 −0.0002/loop).
  **Geometry, whole model (MolProbity, `geometry/<arm>_k4/`):** T clashscore 6.9, rotamer outliers 5.6 %, Cβ deviations 8, RMS
  bonds/angles 0.0076 Å / 1.36°, MolProbity score 2.03; C1 12.5 / 5.6 % / 12 / 0.0073 / 1.31° / 2.26; C2 9.5 / 3.6 % / 1 /
  0.0067 / 1.01° / 2.09. Against the identical loop without the optimizer, T removes half the clashes and a third of the Cβ
  deviations at equal bond/angle RMS (the paper's reduced-strain claim); C2's cleaner side chains are the price the unrestrained
  step exacts in T and C1 alike. Untangler's own Holton wE, scored on copy A only, is *worse* for T (165–187) than for the controls
  (115–125) — a single-altloc metric, reported as such, not confirmed by the whole-model numbers. None of the three is near the
  frozen caps (rotamer 1.5 %, clash 5.0): stage-1 ensembles are not depositable models (§17.4, §18.1).
- **Interim (2026-09-22T14:00Z, T loop 7; C1 loop 13; C2 loop 16).** ΔT−C1 at equal loop count, full: −0.0011, −0.0016, −0.0008,
  −0.0007, −0.0006 at loops 3–7 (select −2.3 to −4.9σ; report agrees at every loop since 2; Δgap −5 to −9σ_gap). T is level with
  C2 on select at equal loop (+0.2σ at loop 7) and 0.0002 ahead on full. **Nuance:** T's descent has almost stopped (full 0.10634 →
  0.10603 → 0.10597 at loops 5–7) while the controls, given more loops, have passed T's current level (C1 0.10581 at loop 13; C2
  0.10537 at loop 16, both still creeping down ~0.0001/loop). So far the optimizer's effect is a rate effect — the same R-free
  reached in about half the loops — and whether an endpoint advantage remains is what the pre-registered endpoint comparison
  decides; no arm has triggered the stopping rule yet.
- **Environment note 8 (2026-09-22T14:30Z).** T died in loop 8's connectivity step: a subproblem returned `Status: Optimal` but the
  read-back found no label variable above 0.5 for site 1390.O (a water) → `AssertionError`. Cause: PuLP's `HiGHS` API maps
  `kTimeLimit` (and `kIterationLimit`, `kInterrupt`) to `LpStatusOptimal`/`IntegerFeasible` unconditionally and copies back
  `getSolution().col_value`, which is the fractional LP relaxation when HiGHS hits the limit without a MIP incumbent. Patch (6)
  extended: after each solve the solution is validated (HiGHS `primal_solution_status == kSolutionStatusFeasible` and every
  integer variable within 1e-3 of an integer); otherwise the pre-solve values (the incumbent) are restored and the subproblem is
  logged as skipped in `E035_solver_failures.txt`. T relaunched at loop 7 from its recorded loop-7 model (14:34Z); loop 8 is redone.
  Loops 1–7 on record are unaffected (every solve in them had an incumbent).
- **Paper-alignment check (2026-09-22T15:30Z; the operator's copy of the PDF has identical text to the bioRxiv v1).** Item by
  item against Sec. IV A–B and App. C–D, verified on the running configuration: six contiguous copies by copying altlocs ✓; ANISOU
  dropped, so B-factors isotropic (2310 records in the deposition, 0 in B0) ✓; 0.5 Å average shake then ≥ 20 restrained
  macro-cycles ✓ (20); geometry weight wc = 0.5 in every restrained step ✓; loop = 1 unrestrained mc (wc 0, waters held) →
  connectivity optimization → 10 restrained mc ✓; optimizer: no untwist moves ✓, Z² cost ✓, one solution per loop ✓,
  subproblems on random copy subsets over 5 rounds with the 20/4/2/1.01/0.8 outlier relaxation and warm starts ✓, new clashes
  forbidden ✓, non-bond geomections excluded ✓ (weight 0), angle weight ×800 ✓, 3-min limit and 0.5 % gap ✓, random site/
  geomection fixing ✓; controls = the paper's green and blue ✓; endpoint rule = the authors' ✓. Code defaults the paper does not
  mention, applied identically to every arm and disclosed: reference-coordinate restraints (σ 0.1 Å) during the 'unrestrained'
  step, water-occupancy refinement and NQH flips off in the restrained step, riding hydrogens. Substitutions: HiGHS for CPLEX,
  Phenix 2.1 for 2.0. **Two design gaps closed now:** (1) the paper repeats each arm 5× from starts displaced 0.1 Å on average
  and refined 6 mc — replicates 2 and 3 launched 15:24Z (`arms/{T,C1,C2}_r{2,3}`, bases `B0_r2/B0_r3` from B0 with `-s 0.1 -n 6`,
  seeds 102/103; arms paired within replicate at seed 42; three starts per arm, not five — CPU); (2) Fig. 9 reads a 3-point
  moving average — added to `TRAJECTORY.md`. Time box for the replicate arms: 2026-09-24T12:00Z. Not run: stage 2 (per-copy
  water picking; the wrapper's defaults 0.17/0.05/0.51 differ from App. D's 0.33/0.02 and must be set if E035b runs) and stage 3.
- **Interim (2026-09-22T20:15Z; replicate 1: T loop 9, C1 18, C2 22; replicates 2–3: controls loop 3, T loop 1).** T resumed its
  descent after the loop 5–7 flattening: full 0.10597 → 0.10562 → 0.10538 at loops 7–9. ΔT−C1 at equal loop, full: −0.0006,
  −0.0007, −0.0009 at loops 7–9 (select −2.3/−1.6/−1.5σ; report −0.0005/−0.0010/−0.0014; Δgap −5 to −6σ_gap) — nine loops, every
  subset in T's favour since loop 2. ΔT−C2 at equal loop, full: −0.0002 to −0.0007 (loops 2–9), select level. Given more loops the
  controls keep sinking slowly: C1 0.10578 at loop 18 (its select has risen twice in a row, not yet three), C2 0.10473 at loop 22
  — below T's loop-9 value by 0.0007. So the equal-loop claim (Fig. 9) is reproduced with three-fold margin over σ on every row;
  the endpoint question stays open because no arm has met the stopping rule. Replicates 2 and 3 (paper's randomized starts)
  at loop 1: ΔT−C1 full −0.0004 in both, ΔT−C2 +0.0003/+0.0000 — same early pattern as replicate 1. The scorer's endpoint
  function was corrected to the pre-registered rule (no endpoint until three consecutive rises; latest loop marked
  provisional otherwise); nothing reported earlier used an endpoint.
- **Interim (2026-09-22T23:10Z; replicate 1: T loop 11, C1 21, C2 24; replicates 2–3: T loop 3, controls 5–6).** T's loop 11:
  select 0.10193 / report 0.10772 / full **0.10481** vs C1 at loop 11 0.10300 / 0.10934 / 0.10615 (−3.8σ, −0.0016, −0.0013; Δgap
  −6.4σ_gap) and vs C2 at loop 11 (−2.4σ select, −0.0012 full). **T at loop 11 is below the best value either control reached in
  its whole trajectory**: C1's best 0.10563 (loop 21), C2's best 0.10473 (loop 22; since risen to 0.10485 and 0.10492 at loops
  23–24 with select rising twice in a row — one more rise triggers its endpoint at loop 22). Eleven equal-loop rows, every one in
  T's favour on full since loop 2; T's own descent re-accelerated (0.10538 → 0.10523 → 0.10481 at loops 9–11). Replicates at
  loop 3: ΔT−C1 full −0.0010 (r2, −2.0σ select) and −0.0006 (r3, −2.4σ); ΔT−C2 full −0.0009 / −0.0006. The rate-vs-endpoint
  question of the loop-7 note is resolving toward an endpoint advantage as well, pending the stopping rule and the box.
- **Interim (2026-09-23T01:20Z; replicate 1: T loop 12, C1 23, C2 finished at its 26-loop cap).** T loop 12: select 0.10155 /
  report 0.10791 / full **0.10471** vs C1 at 12 (−4.6σ, −0.0012, −0.0012; Δgap −5.4σ_gap) and vs C2 at 12 (−3.5σ select, −0.0011
  full). C2's complete trajectory: best full 0.10473 (loop 22), final 0.10489 (loop 26), best select 0.10183; it oscillated over
  its last five loops without meeting the stopping rule. **T at 12 loops is below every value C2 produced in 26 and C1 in 23
  (C1 best 0.10557), on select and on full**, and is still descending (0.10523 → 0.10481 → 0.10471). Replicates 2–3 at loop 4:
  ΔT−C1 full −0.0009 / −0.0010 (select −2.7σ / −3.6σ), ΔT−C2 full −0.0009 / −0.0009 — same picture as replicate 1 at loop 4.
- **Interim (2026-09-23T04:15Z; replicate 1: T loop 13, C1 25, C2 done at 26; replicates 2–3: T loop 5, controls 9–10).**
  Replicate 1, loop 13: T 0.10151 / 0.10742 / **0.10445** vs C1 0.10279 / 0.10887 / 0.10581 (−4.6σ, −0.0015, −0.0014; Δgap
  −7.2σ_gap) and vs C2 at 13 (−3.5σ, −0.0013 full). T is now 0.0003 below C2's best over 26 loops and 0.0010 below C1's best over
  25 (0.10548). Replicates at loop 5: r2 ΔT−C1 full −0.0008 (−3.7σ select), ΔT−C2 −0.0008 (−3.4σ); r3 ΔT−C1 −0.0013 (−5.0σ),
  ΔT−C2 −0.0013 (−2.2σ). Thirteen equal-loop rows in replicate 1 and five in each replicate, every one with T ahead of C1 on
  full since loop 2 and ahead of C2 since loop 2–3. No arm has met the stopping rule; T still descending.
- **Environment note 9 (2026-09-23T15:15Z).** T died at 05:50Z in loop 15's connectivity step and was found 9.4 h later (the
  session's watcher had lapsed): HiGHS declared a subproblem infeasible; the kept-incumbent fallback (note 8) restored the
  variable values but left PuLP's status flags at Infeasible, and the authors' own check (`assert l>0, "Solution was
  infeasible!"`) fired. Fix: the fallback now calls `assignStatus(LpStatusOptimal, LpSolutionIntegerFeasible)` on the restored
  incumbent. T relaunched at loop 14 from its recorded loop-14 model (15:14Z); T_r2/T_r3 carry the fix for any relaunch but were
  not restarted (running, no errors). Because the outage was harness-side, replicate 1's time box is extended to match the
  replicates' (2026-09-24T12:00Z); loops 1–14 on record are unaffected. State at 15:12Z: replicate 1 C1 and C2 finished at the
  26-loop cap (C1 best full 0.10548, final 0.10554; C2 best 0.10473, final 0.10489; neither met the stopping rule); T loop 14
  0.10450 full (−0.0012 vs C1 at 14, −5.3σ select; −0.0011 vs C2 at 14, −4.4σ). Replicates: T_r2 loop 10 0.10416 and T_r3 loop
  10 0.10401 full, each below its own controls' entire trajectories so far (C1_r2 best 0.10424 over 18 loops; C1_r3 0.10436 over
  18; C2_r2 0.10435 over 21, where the stopping rule triggered at loop 14; C2_r3 0.10420 over 21). Mean ΔT−C1 full over the
  three replicates at equal loop: −0.0008 to −0.0010 (loops 7–10); mean ΔT−C2 −0.0006 to −0.0008.
- **Result (2026-09-28; all nine arms finished; thresholds_v8 in force; frozen flags; harness evaluator).** The paper's stage-1
  claim (Fig. 9) replicates; its headline number does not, and stage 1 alone was never expected to reach it. Equal loop count:
  T beat the identical loop without the optimizer (C1) in every one of 54 paired rows after loop 1 across three starts — mean
  ΔT−C1 full −0.0009 (−0.0008 to −0.0016), select −1.5 to −5.6σ, report agreeing at every row from loop 2, Δgap −2 to −9σ_gap
  (T's gap narrower, R-work equal); against restrained-only C2 the mean is −0.0007 full. Whole-trajectory best full R-free, T /
  C1 / C2: replicate 1 (26 loops each) **0.10428** / 0.10548 / 0.10473; replicate 2 (T 14 loops, controls 26) **0.10377** /
  0.10407 / 0.10394; replicate 3 (T 14, controls 26) **0.10373** / 0.10395 / 0.10368. T with 14 loops matches or beats what the
  controls reach in 26 except replicate 3, where restrained-only refinement edges it by 0.00005 after 26 loops (σ_full 0.00025).
  Endpoints by the pre-registered stopping rule: replicate 1 T loop 14 (0.10450 full) vs C1 and C2 never triggered (final 0.10554,
  0.10489); replicate 2 T loop 10 (0.10416) vs C2 loop 14 (0.10435), C1 never; replicate 3 T provisional loop 14 (0.10373) vs C2
  loop 19 (0.10419), C1 never. Whole-model geometry at loop 11: T clashscore 6.6 vs C1 12.4 vs C2 9.7 at equal bond/angle RMS;
  the controls' clashscores rise over their long runs (C1 13.3 at 21, C2 11.2 at 24). **Verdict: replicated as a rate effect with a
  modest endpoint gain (≈ 0.001 full R-free, ≈ 4σ_select at matched loops), robust to three starts; solver substitution HiGHS for
  CPLEX.** Absolute: the six-copy stage-1 models sit at 0.104 full R-free — below the single-model deliverable (0.1126) with four
  times its atoms, not depositable (rotamer outliers 4 %, clashscore 6.6), not a deliverable (§18.1) — and far from the paper's
  0.064, which the authors reached only with stage 2 (per-copy low-occupancy waters; they state R-free stayed above 0.10
  without it), stage 3 (≈ 30 manual Coot changes, anisotropic B, hundreds of macro-cycles) and CPLEX. Replicate T arms stopped
  at loop 14 through the harness-side status bug of note 9 (fixed after they had loaded the old module); their 14 paired rows
  and their controls' 26 loops stand. Deviation row: D513. Next: E035b (stage 2).

### E035b — stage 2 of Passmore et al. on 7KR0: conformation-aware water picking inside the connectivity loop, paired
(registered 2026-09-28, rationale before run)
- **Rationale.** E035 reproduced the paper's stage-1 effect but left the six-copy model at 0.104 full R-free; the authors say
  (Sec. IV B) they could not get below 0.10 without fitting low-occupancy waters to the non-flat bulk solvent, per copy, with
  Phenix's conformation-aware picking inside the loop, and that this stage is automated. Mechanism: with six copies the bulk
  solvent mask is the same for all copies while the real solvent differs around each conformation; per-copy partial-occupancy
  waters (picked in the second half of each restrained step, initial occupancy 0.33, floor 0.02, altloc-tagged, occupancies
  refined) model that difference, and the connectivity optimizer then relabels waters and protein together (their Fig. 12).
  Parameters exactly as App. D: 12 restrained macro-cycles when picking, `ordered_solvent` in `second_half` mode, initial
  occupancy 0.33, minimum 0.02, minimum separation from other-conformation altlocs 0.03 Å, final filtering step ignored, wc 0.5.
  The wrapper's water-occupancy variables are dead code (its seds do not match the templates), so the templates carry the App. D
  values (patch 8).
- **Design.** Bases: each replicate's stage-1 T arm final model (loop 26 / 14 / 14; the model in force, no selection), REMARK 290
  restored. Arms from each base, same seed 42: **T** (untangling + picking), **C1** (picking, no untangling); replicate 1 also
  **C2** (picking, restrained only). Loop cap 12; time box 2026-09-30T12:00Z; HiGHS; every model scored by the harness evaluator
  with the free counts asserted. Water counts per copy and the occupancy distribution are recorded per loop. Anisotropic B
  conversion at the end (App. D, Mac1 only) is a separate step, E035c, judged under the R-gap gate and the authors' 30 % rule.
- **Pre-registered readout.** ΔT−C1 at equal loop count (select in σ_select, sign on report/full, Δgap in σ_gap), endpoints by
  the stopping rule, whole-trajectory best; plus the absolute distance to the paper's 0.064 and to the single-model deliverable,
  reported as representation-level numbers (§18.1). "Water picking helps" = T(stage 2) below T(stage 1) at its endpoint on all
  three subsets beyond 2σ; "untangling still helps with picking" = ΔT−C1 beyond −2σ_select with report/full agreeing.
- **Environment note 1 (2026-09-28T17:00Z).** A first launch went out from a copy patched with the main-branch version of the patch
  script (sections 6–7 and the HiGHS switch missing); stopped within minutes, nothing scored, relaunched from the complete
  script.
- **Environment note 2 (2026-09-28T20:00Z): stage 2 as configured destroys the model — arms stopped.** First model (C2, loop 1,
  restrained refinement + picking): 1 872 → 300 waters, full R-free 0.1045 → **0.2127**. The phenix log shows the mechanism inside
  the first ordered-solvent update: the q & B filter dropped 1 850 → 1 040 waters (R-free 0.1055 → 0.1245: the sub-0.02 copy
  waters carried real signal), then "Add new water" placed 239 waters and R-work jumped 0.119 → **0.418** in one step — only
  possible if the new waters are placed with grossly excess scattering (e.g. a water in every copy at 0.33, or 0.03 Å from other
  copies' atoms); water-only occupancy/ADP refinement recovered to 0.24, the next filter to 0.19, and every later macro-cycle
  repeated the damage. Phenix 2.1 defaults vs the authors' template: `include_altlocs` False vs True, `dist_min_altloc` 0.5 vs
  0.03 Å, `occupancy` 1.0 vs 0.33, `occupancy_min` 0.2 vs 0.02, `ignore_final_filtering_step` False vs True. The authors used
  Phenix 2.0, where conformation-aware picking was introduced; 2.1 evidently behaves differently under these values. Four
  one-cycle diagnostics launched from the stage-2 base through the same wrapper, one parameter each (`diag/*.eff`,
  `arms/diag_*`): A `dist_min_altloc` = 1.8, B initial occupancy 0.167 (max 0.2), C `include_altlocs` = False, D the authors'
  values unchanged (reference). Question for the authors: which Phenix build and picker settings produced their per-copy waters.
- **Environment note 3 (2026-09-28T21:00Z): diagnostics A–D.** One restrained macro-cycle from the stage-2 base with the picker
  in `every_macro_cycle` mode, one parameter changed each. Filter step (identical in all four, before any picking): 1 847 → 1 041
  waters, R-free 0.1051 → 0.1238 — the removed waters are the 793 copy waters below occupancy 0.02 (base water B max 38, so the
  B ceiling removed nothing); atoms with near-zero occupancy still carve the bulk-solvent mask, which is where the +0.019 comes
  from (a mask effect of the stage-1 representation, recorded as a finding). Add step: D (authors' values) 762 → 1 239 waters,
  R-work 0.194 → **0.419**; A (`dist_min_altloc` 1.8 instead of 0.03) identical to D to the last digit — the parameter is inert in
  this Phenix build; C (`include_altlocs` False) 1 051 → 1 120, R-work 0.117 → 0.160; B confounded by my own occupancy ceiling
  (0.2 removed every water above it) but its add step (+522 waters at 0.167) still +0.12. So `include_altlocs = True` is the
  catastrophic knob in 2.1, and even without it 69 added waters raise R-work by 0.04, which is physically possible only if they
  sit on existing atoms. Two more diagnostics launched with the picker's distance mask widened from Phenix's default
  (backbone atoms only) to all atoms: E (mask all, altlocs off), F (mask all, altlocs on).
- **Environment note 4 (2026-09-28T21:20Z): diagnostics E/F and the relaunch.** Full-cycle endpoints of the diagnostics (this
  refinement's own R, base at its start 0.0968 / 0.1051): C (altlocs off) 0.1021 / 0.1097 with 1 108 waters; E (altlocs off,
  distance mask all atoms) after water refinement 0.1086 / 0.1156 vs C's 0.1085 / 0.1150 — the mask setting is irrelevant;
  A = D (authors' values) 0.1547 / 0.1612 with 752 waters. The picker's added waters in C carry no altloc, occupancy 0.24–0.46,
  B ≈ 12, nearest atom 2.1 Å (median): sane waters that the connectivity optimizer then labels, which is what the paper says
  happened in their runs too. Decision: stage 2 runs with `include_altlocs = False` (patch 8, switchable back with
  `UNTANGLER_PICK_ALTLOCS=1`), Phenix's default distance mask, everything else per App. D. The one-time mask loss from filtering
  the 793 sub-0.02 copy waters (+0.019) is accepted as the paper's own floor applied to our base and is recovered by picking
  within one cycle to within 0.005. Seven arms relaunched 21:17Z (attempt 3; attempt 2's outputs kept in `attempt2_altlocs/`);
  the E035c dry run's picking loop still uses the old template and is a mechanics test only.
- **Environment note 5 (2026-09-29T03:40Z): attempt 3 stopped after loop 2.** With `include_altlocs = False` the picking loop
  does not recover: replicate 1, harness numbers, full R-free — C2 loop 1 0.1146, loop 2 **0.1239** (base 0.1045); T loop 1 0.1156
  vs C1 0.1168 (−0.0012); T_r3 loop 1 0.1087 vs C1_r3 0.1047 (replicate 3's base loses less to the filter). Inside each solvent
  update (C2 loop 2): filter 1 076 → 1 053, add → 1 076, water-only occupancy/ADP refinement reports 0.1036, then the post-refinement
  q & B filter culls the waters whose occupancies fell below 0.02 and R-free returns to 0.124; the cycle settles at ≈ 0.123 on
  phenix's numbers. The picker re-adds only 3σ difference peaks (≈ 70–90 per update) while the sub-0.02 sites it removed never
  come back, so the loop is a permanent +0.02 loss relative to the stage-1 model whose near-zero copy waters shaped the bulk-solvent
  mask. All seven arms, the stage-2 floor and both chains stopped; nothing scored is a result. Three 12-cycle single-loop
  diagnostics from B0 (picking on, altlocs off): G `occupancy_min = 0.0` (no occupancy culling), H `primary_map_cutoff = 2.0`
  (weaker peaks), I water-occupancy refinement off. Decision rule: the variant whose loop ends below the base on full R-free with
  a non-decreasing water count becomes the stage-2 configuration; if none does, per-copy picking in Phenix 2.1 is recorded as
  not reproducing the paper's stage 2 and E035b closes as a negative result.
- **Environment note 6 (2026-09-29T05:30Z): the near-zero waters are not a scoring artefact.** Deleting every water below
  occupancy 0.02 from the stage-1 finals and re-scoring with the harness evaluator changes nothing: T loop 26 full 0.10453 →
  0.10453 (793 waters removed; below 0.05: 858 removed → 0.10467), C1 0.10554 → 0.10554, C2 0.10489 → 0.10489
  (`e035_untangler/ghostfree/ghostfree.json`). So the E035 numbers stand as clean cross-validated values and no mask effect
  enters the evaluator. The +0.019 seen inside phenix.refine when its filter removes those waters is phenix's *own* bulk-solvent
  mask (built from all atoms regardless of occupancy) changing under it; the refinement that follows then re-converges the
  model against the hole-free mask, and that re-converged model scores worse on the free set (C2 loop 1 0.1146, loop 2 0.1239)
  — i.e. the stage-1 coordinates and ADPs had been optimised against a bulk-solvent model that the picker's culling removes,
  which is the paper's non-flat-solvent argument seen from the other side. Diagnostic G (no occupancy culling) still loses
  0.016 at its first update because the picker's distance and map filters remove ~200 more of the same waters.
- **Environment note 7 (2026-09-29T03:45Z): culling the near-zero waters is harmless — note 6's mechanism is withdrawn.**
  Diagnostics J and K: the loop's plain restrained step (10 mc, `-c 0.5 -u 1 -s 0.0 -q 0.1 -W -N`, seed 42, no picker) from
  the stage-1 T loop-26 model with every water below occupancy 0.02 deleted (J, 1 079 water copies) and from the unmodified
  model (K, 1 872). Harness, full R-free: J **0.10433** (select 0.10172, report 0.10697, gap 0.0087), K **0.10447**
  (0.10191 / 0.10706 / 0.0085); input 0.10453. Phenix's own line passed through 0.122 at macro-cycles 2–3 in both and ended
  at 0.1044 / 0.1045. So the 793 sub-0.02 copy waters carry nothing that phenix.refine needs either, and the +0.02 that the
  stage-2 loop settles at is produced inside `ordered_solvent` itself — the add step and the water-only occupancy/ADP
  refinement between the two filters (note 5's sequence: filter → add → refine → post-filter), not the culling. The
  "bulk-solvent mask" reading in note 6 is withdrawn; the +0.019 printed after the first filter is a transient of phenix's
  scaling state (J shows the same excursion with no picker at all). `arms/diag_{J_ghostfree,K_ref}/`.
- **Environment note 8 (2026-09-29T04:50Z): diagnostics G/H/I final — none qualifies.** One 12-macro-cycle picking loop from
  the stage-2 base (input full 0.10453, 1 872 water copies), harness numbers: G `occupancy_min = 0` **0.11933** (select
  0.11779 / report 0.12088; 1 580 waters), H `primary_map_cutoff = 2.0` **0.11008** (0.10842 / 0.11176; 1 150), I water
  occupancies fixed **0.11185** (0.11029 / 0.11342; 1 119). All three end above the base with fewer waters, so by the rule
  in note 5 none becomes the stage-2 configuration. `arms/diag_{G_occmin0,H_peak2,I_noW}/`.
- **Result (2026-09-29): negative — Phenix 2.1's `ordered_solvent` does not reproduce the paper's stage 2 on this base.**
  With the authors' template (`include_altlocs = True`, 0.33 / 0.02) the add step destroys the model (R-work 0.119 → 0.418
  in one update; C2 loop 1 full R-free 0.1045 → 0.2127); with altlocs off the loop settles ≈ +0.02 above the base (C2 loop 2
  0.1239) and none of eight one-parameter variants (A–I) ends below it. The culling of near-zero copy waters is not the
  cause (note 7: J 0.10433 vs K 0.10447 with no picker); the loss arises inside the picker's add / water-refine / re-filter
  sequence. The stage-2 mechanism itself is confirmed by E035f, where the harness's own picker (adds six-copy waters at
  ≥ 3σ difference peaks, removes nothing) lowers every control arm by 0.006–0.007 full R-free in one loop. Question for the
  authors stands: which Phenix build and settings produced their per-copy waters. Deviation row D514.

### E035f — stage 2 of Passmore et al. on 7KR0 with the harness's own per-copy water picker (registered 2026-09-29, rationale
before run)
- **Rationale.** E035b could not reproduce the paper's stage 2 because Phenix 2.1's `ordered_solvent` culls the low-occupancy
  copy waters the stage-1 loop had refined against (notes 2–6; the culling, not the picking, is the loss). The mechanism the
  paper relies on — per-copy partial-occupancy waters at difference peaks, occupancies refined, labels left to the connectivity
  optimizer — does not need Phenix's picker. `scripts/experiments/e035_pick_waters.py` (phenix.python, `mmtbx.find_peaks` on the
  fmodel built exactly as the harness evaluator builds it) adds a water at every mFo-DFc peak ≥ 3σ that is 2.2–6.0 Å from the
  model and ≥ 1.8 Å from other peaks, as six copies (altlocs A–F, chain z, occupancy 0.33/6 each, 0.15 Å seeded shake: the
  `split_qfit_to_6conf.py` representation), and removes nothing; the loop's `-W` refines every water occupancy, so unsupported
  copies fall to zero as the stage-1 waters did. Picker check on the stage-1 T endpoint (loop 14 replicate 1 is the endpoint;
  the check used loop 26, `e035f_pickdev/`): 55 sites in 10 s; before any refinement full R-free 0.10453 → 0.10326 (six-copy)
  / 0.10293 (single common water) with select +0.0015 / report −0.0040 — the halves disagree in sign at this step, so nothing is
  claimed from it; it shows the file is valid and the added scatterers are not destructive.
- **Design.** `exp_untangler_7kr0.sh stage2p <stage-1 dir> "T:14 C1:26 C2:26 T_r2:10 C1_r2:26 T_r3:14 C1_r3:26" 12` in
  `e035f_stage2p/`: bases are the stage-1 endpoint models by the stopping rule (result.json), same seven-arm structure as E035b
  (T untangling + picking, C1 picking + unrestrained/restrained refinement without the optimizer, C2 picking + restrained only;
  replicates 2–3 T and C1). One loop = pick → one loop of the arm's kind with Phenix's picker off; slots 2i−1 hold the loop
  outputs; loop cap 12; time box 2026-10-01T12:00Z; every model scored by the harness evaluator. Readout as E035b's
  pre-registered readout (ΔT−C1 at equal loop count in σ_select with report/full agreeing and Δgap; endpoints by the stopping
  rule; "picking helps" = T(stage 2p) below T(stage 1) at its endpoint on all three subsets beyond 2σ). Stage 3 (E035c, no
  Phenix picking) runs from the same stage-1 endpoints in parallel; whichever line ends lower seeds the anisotropic finish.
- **Environment note 1 (2026-09-29T02:50Z).** First launch crashed in all seven arms at untangle.py's initial Holton score:
  the picker wrote the model without the REMARK 3 header and the score reads R-work/R-free from it (`n/d` → ValueError).
  Fixed: the picker carries the input's REMARK records forward with the R VALUE lines set to the picked model's own
  recomputed R (T: 0.1045 → 0.1034 full before refinement, 58 sites). Relaunched 02:47Z; attempt 1 kept in
  `arms.attempt1_headerless/`.
- **Interim 1 (2026-09-29T04:10Z): first loop, control arms — the paper's stage-2 effect appears.** One pick (54–58 sites,
  six copies each at 0.055, nothing removed) followed by the arm's own step (C1: 1 unrestrained + 10 restrained mc with
  water occupancies refined; C2: the 10 restrained mc), harness numbers, full R-free (select / report; R-gap):
  C2 0.10489 → **0.09789** (0.09616 / 0.09965; 0.0096 vs 0.0092), C1 0.10554 → **0.09914** (0.09774 / 0.10056; 0.0098 vs
  0.0093), C1_r2 0.10408 → **0.09746** (0.09556 / 0.09937; 0.0096 vs 0.0089). Δfull −0.0064 to −0.0070 (≈ 25σ_full), all
  three subsets agreeing in sign; Δgap +0.0004 to +0.0007 (2.5–4σ_gap, would be `overfit_suspect` for a single-model
  deliverable under thresholds_v6 — recorded, representation-level per §18.1). Water copies 1 872 → 2 196–2 220, of which
  882–984 sit below occupancy 0.02 after refinement. This is what the authors describe (Sec. IV B): the per-copy
  low-occupancy waters are what takes the six-copy model below 0.10, and Phenix 2.1's own picker could not do it because
  its filters remove them (E035b). Where the gain sits: after refinement every picked site keeps a summed occupancy ≥ 0.05
  (C2: median 0.29, 44 of 56 sites ≥ 0.2, one site 1.01 — a full water), concentrated in 139 of the 336 copies (the per-copy
  distribution the mechanism predicts), while the pre-existing waters' summed occupancy is unchanged (212 → 209). C1_r3
  0.10416 → 0.09738 (−0.0068).
- **Interim 2 (2026-09-29T05:00Z): first T arm.** T_r2 loop 1 (pick → unrestrained mc → connectivity solve → 10 restrained
  mc): 0.10416 → **0.09611** full (select 0.09333, report 0.09892; gap 0.0088), −0.0081 against its stage-1 endpoint and
  −0.00135 below its paired control C1_r2 at the same loop (select −0.0022 ≈ 8σ_select, report −0.0005, both the same sign;
  the T arm's R-gap is the narrower, 0.0088 vs 0.0096). Water copies 2 226. T_r3 loop 1: 0.10373 → **0.09563** (0.09318 /
  0.09810; gap 0.0091), −0.0018 below C1_r3 (0.09738). T loop 1: 0.10450 → **0.09699** (0.09563 / 0.09837; gap 0.0083),
  −0.0022 below C1 (0.09914) and −0.0009 below C2 (0.09789). All three T arms sit below their controls after one loop, on
  every subset. Scorer tables (paired rows at k = 2i−1, σ from the stage-1 floor linked in): `e035f_stage2p/TRAJECTORY.md`,
  `result.json`; replicate 1 loop 1 ΔT−C1 −7.5σ_select, ΔT−C2 −1.9σ_select, Δgap T−C1 −9.2σ_gap.
- **Interim 3 (2026-09-29T06:00Z): control arms, loop 2.** Still descending: C2 0.09789 → 0.09754, C1 0.09914 → 0.09819,
  C1_r2 0.09746 → 0.09682, C1_r3 0.09738 → 0.09681 (full; −0.0004 to −0.0010; gaps 0.0097–0.0106). The second pick raises
  R-free before refinement (C1_r3 k = 2 0.09922 against k = 1 0.09738) and refinement more than recovers it, so the later
  peaks are weaker and their copies mostly refine to zero. T arms in loop 2. Stage 3 will be re-seeded from the E035f
  endpoints when the arms stop.
- **Environment note 2 (2026-09-29T14:55Z): every arm died at a loop boundary — the orchestrator was overwritten while
  running (D504).** At 05:35Z I shipped a new version of `exp_untangler_7kr0.sh` to every experiment directory, including
  this one, while the stage was running; bash reads scripts incrementally and each loop calls `bash $0 oneloop`, so the
  control arms failed at their loop-3 start ("syntax error near unexpected token `)'", `logs/stage2p_C2_26.log`) and the T
  arms after loop 2. Lost: ~8 h of wall clock, no models (every completed loop output is on disk). Fix: `RESUME=1` continues
  each arm from its last completed loop output (highest odd slot), and stages are now launched from a per-run copy of the
  script (`scripts/run_<utc>/`) that is never overwritten. Resumed 14:54Z: T/T_r2/T_r3/C1/C1_r3 at loop 3, C2/C1_r2 at loop 4.
- **Interim 4 (2026-09-29T15:05Z): T arms loop 2, controls loop 3 — the controls plateau, the T arms keep descending.**
  Full R-free (select / report; gap): T loop 2 **0.09677** (0.09484 / 0.09871; 0.0091), T_r2 **0.09568** (0.09326 /
  0.09813; 0.0091), T_r3 **0.09467** (0.09231 / 0.09706; 0.0089) — −0.0002 / −0.0004 / −0.0010 from loop 1. Controls at
  loop 3: C2 0.09757 (+0.00003 from loop 2), C1_r2 0.09693 (+0.0001): flat, with gaps 0.0102–0.0105 against the T arms'
  0.0089–0.0091. T−C1 at matched loop: −0.0014 (T vs C1 0.09819), −0.0011 (T_r2 vs C1_r2 0.09682), −0.0021 (T_r3 vs
  C1_r3 0.09681); the third pick adds only 2–17 sites. Best six-copy model so far: T_r3 loop 2, 0.09467.
- **Interim 5 (2026-09-29T17:20Z): loop 3 (T) / loops 3–4 (controls), after the resume.** T **0.09617** (select 0.09445,
  report 0.09791; gap 0.0088), T_r2 **0.09526** (0.09275 / 0.09779; 0.0091), T_r3 **0.09452** (0.09228 / 0.09679; 0.0093):
  −0.0006 / −0.0004 / −0.0002 from loop 2, with picks of 5 or fewer sites — the descent is now the connectivity loop's,
  not the picker's. Controls: C1 loop 3 0.09800, C2 loop 4 0.09738, C1_r2 loop 4 0.09658, C1_r3 loop 3 0.09666 (−0.0002
  to −0.0004 per loop, plain refinement). T−C1 at matched loop: −0.0018, −0.0013, −0.0021. Best model: T_r3 loop 3, 0.09452.
- **Interim 6 (2026-09-29T20:00Z): loop 4.** T **0.09582** (select 0.09428, report 0.09738; gap 0.0090), T_r2 **0.09494**
  (0.09283 / 0.09708; 0.0093), T_r3 **0.09413** (0.09211 / 0.09618; 0.0092): −0.0003 to −0.0004 per loop, steady. Controls
  (scorer endpoints, provisional): C1 loop 5 0.09757, C2 loop 7 0.09711, C1_r2 loop 6 0.09620, C1_r3 loop 5 0.09663.
  The stage-3 cycle on these models (E035c second run) beats the plain loop from the same seed by 0.0017–0.0023 (E035c
  interim 4).
- **Interim 7 (2026-09-29T21:45Z): loop 5 — the plain loop is flattening.** T 0.09567 (−0.0002), T_r2 0.09501 (+0.0001,
  first non-improvement), T_r3 0.09397 (−0.0002); gaps 0.0090–0.0095. Controls: C1 loop 7, C2 loop 8, C1_r2 loop 7 in the
  rescorer's tables. The endpoint rule has not triggered on any arm.
- **Interim 8 (2026-09-30T00:00Z): loop 6.** T 0.09544 (−0.0002), T_r2 0.09504 (+0.00003, second flat loop), T_r3 0.09385
  (−0.0001). The plain loop is at its plateau at 0.094–0.095; the arms run on to the 12-loop cap for the paired tables.
- **Interim 9 (2026-09-30T02:10Z): loop 7.** T 0.09531 (−0.0001), T_r2 0.09460 (−0.0004), T_r3 0.09387 (0.0000). C2 has
  reached the 12-loop cap.
- **Interim 10 (2026-09-30T05:10Z): loop 8.** T 0.09501 (−0.0003), T_r2 0.09455 (0.0000), T_r3 0.09388 (0.0000). All four
  control arms have reached the 12-loop cap; the T arms run on to theirs.
- **Result:** pending.

### E035c — automated stand-in for the authors' stage 3 on 7KR0 (registered 2026-09-28, rationale before run)
- **Rationale.** Stage 3 in the paper is manual: about thirty Coot changes per model, mostly identity mix-ups between waters and
  side chains, with the connectivity loop, water picking and water-occupancy refinement re-run between rounds; the authors say
  no automated method for identity mix-ups exists. What *is* automatable from their own late-stage tips (README, App. D): (a) the
  water rules — delete waters below occupancy 0.05, merge neighbouring waters whose occupancies sum below 0.35; (b) after
  picking, a main-chain-only connectivity optimization with no unrestrained step, to remove the clashes and unlabelled waters
  picking leaves; (c) another picking loop. E035c runs that cycle, N times, from each stage-2 final model, paired: T arms take
  (a)+(b)+(c), C1 arms (a)+(c). It is an approximation of stage 3 and is reported as one; the identity mix-ups the authors fixed
  by hand are left to the campaign's own real-space loop (PROTOCOL §4.1, §5.1) as E035e if E035c converges above 0.064.
- **Design.** `exp_untangler_7kr0.sh stage3 <stage-2 dir> "T:k C1:k T_r2:k C1_r2:k T_r3:k C1_r3:k" N` with N = 6 (box
  2026-10-02T12:00Z); loop-model slots k = 3i−1 hold the paired picking outputs; hygiene reports (`hygiene/*.hygiene.json`) record
  waters deleted, merged and left per loop; every model scored by the harness evaluator. Readout: ΔT−C1 at k = 3i−1 in σ_select
  with report/full agreeing and Δgap; T(stage 3) vs T(stage 2 final) at the endpoint; absolute distance to 0.064.
- **Environment note 1 (2026-09-28T19:20Z, dry run on the stage-1 T final, `e035c_dryrun/`).** The README's water rules cost
  R-free when applied to a stage-1 model: deleting waters below occupancy 0.05 removed 858 of 1 872 water copies and merging
  neighbours below a 0.35 sum merged 256 pairs; the harness scored the result at full 0.11272 against 0.10453 for the input
  (+0.008). Those 0.02–0.05 waters are legitimate under App. D's own picking floor (0.02) and evidently carry bulk-solvent
  signal. Decision: the hygiene floor is App. D's 0.02 (not 0.05); the merge rule stays; hygiene is scored per loop so its cost
  or benefit is on record. The main-chain-only optimization pass itself ran correctly (25 solves, wrapper R-free 0.106 on its own
  flags line). Two harness bugs fixed in the one-loop primitive: it truncated a model by copying it onto itself, and it copied the
  input without the REMARK 290 header untangle.py needs.
- **Environment note 2 (2026-09-29T02:49Z): launched from the stage-1 endpoints, without Phenix picking.** E035b's picking
  loop settles +0.02 above its base (E035b notes 5–6) and its last diagnostics were still above base at macro-cycle 8, so
  stage 3 was started from the stage-1 endpoint models (result.json: T:14 C1:26 C2:26 T_r2:10 C1_r2:26 T_r3:14 C1_r3:26) with
  `STAGE3_PICK=0` (the closing loop of each stage-3 cycle runs without `ordered_solvent`), N = 6, via
  `e035_pipeline_chain.sh` (`CHAIN_SRC`/`STAGE3_SPECS`; `e035c_stage3/`). This is a change from the registered design
  (seeds were to be the stage-2 finals): stage 3 here tests the water rules and the main-chain-only optimization on their own.
  The own-picker stage 2 (E035f) runs in parallel from the same seeds; the anisotropic finish (E035d) follows the chain.
- **Environment note 3 (2026-09-29T03:00Z): the merge rule collapsed per-copy waters; first launch stopped.** Hygiene on the
  T seed deleted 797 waters below 0.02 (free of cost, E035b note 6) and merged 301 pairs, leaving 774 of 1 872 copies; the
  harness scored the result at full 0.11306 against 0.10450 (C1: 0.11379 vs 0.10554), +0.008 before any refinement — the
  same loss the dry run (note 1) had charged to the 0.05 floor. The cause is the merge: the script paired waters across
  altlocs, and the six copies of one site (0.5 Å apart, ≈ 0.17 each) are exactly "neighbours within 1.2 Å with occupancies
  summing below 0.35". The authors' rule is for duplicates within a conformer. Fixed to same-altloc pairs only; the chain and
  its seven arms were killed 3 min after launch and relaunched from the same seeds (`arms.attempt1_crossaltloc/`).
- **Environment note 4 (2026-09-29T03:20Z): deletions leave residue-number gaps that Untangler rejects; second launch
  stopped.** With the same-altloc merge the hygiene step is free (T: full 0.10451 vs 0.10450; 797 deleted, 0 merged), but the
  control arms crashed in the first loop at `OrderedAtomLookup` (`assert res_num-1 in [last, last_skipped]`): the deleted
  waters left gaps in chain z's numbering, which the optimizer's atom lookup requires gap-free. The hygiene script now
  renumbers the surviving waters consecutively per chain (T seed: 1 071 renumbered, 171–1245, no gaps). All stage-3
  processes killed and relaunched from the same seeds (`arms.attempt2_gaps/`).
- **Environment note 5 (2026-09-29T03:20Z): third launch stopped for the same assertion.** The lookup's numbering is global
  across chains (protein A 1–169, waters z 170–…, the split script's convention) and the first water (z 170, occupancy 0)
  had been deleted, so renumbering from the first surviving water still left a gap after residue 169. Waters are now
  renumbered from the last non-water residue + 1 (both seeds: last protein 169, first water 170, no gaps). Attempt 3 kept in
  `arms.attempt3_firstwater/`; relaunched 03:19Z. E035f is unaffected (its picker appends waters to the existing numbering).
- **Interim 1 (2026-09-29T04:40Z): control arms, first stage-3 loop (hygiene + the arm's own step, no picking, k = 2).**
  Harness full R-free: C2 0.10489 → 0.10482 (−0.0001), C1 0.10554 → 0.10571 (+0.0002), C1_r2 0.10408 → 0.10409 (0.0000);
  1 073–1 179 water copies left. Hygiene plus one more refinement loop from a converged stage-1 model is a null operation,
  as expected; the stage-3 question is whether the T arms' main-chain-only pass adds anything, read at k = 3i−1 against
  these. The gain in the parallel line is E035f's picking (interim 1 there), so stage 3 proper will be re-run from the
  E035f endpoints once they stop.
- **Interim 2 (2026-09-29T05:30Z): T arms after the main-chain-only pass (k = 1).** T 0.10450 → 0.10469 (+0.0002), T_r2
  0.10416 → 0.10397 (−0.0002), T_r3 0.10373 → 0.10371 (0.0000): the main-chain-only connectivity pass with no unrestrained
  step is a null operation on a converged stage-1 model (all within σ_full 0.00025). Its purpose in the paper is to repair
  what picking leaves behind, so its test belongs to the stage-3 run seeded from E035f. The closing loops (full
  untangling, k = 2) are running.
- **Environment note 6 (2026-09-29T14:55Z): same D504 incident as E035f note 2** — the control arms died after loop 1,
  the T arms after their closing loop 1. Resumed 14:54Z with `RESUME=1` from a per-run script copy (T arms at loop 2 from
  slot 2, controls at loop 3 from slot 5).
- **Interim 3 and stop (2026-09-29T15:05Z): closing loop 1 (k = 2) is null; line stopped.** T 0.10450 → 0.10443, T_r2
  0.10416 → 0.10393, T_r3 0.10373 → 0.10356 (−0.0001 to −0.0002, within σ_full); controls −0.0001 to +0.0002 (interim 1).
  With every stage-3 operation a null on the stage-1 endpoints (hygiene, main-chain pass, closing loop), the run from
  these seeds is stopped after one full cycle per arm to give its CPU to E035f; stage 3 proper (with the harness picker,
  `STAGE3_PICK=own`) will run from the E035f endpoints. Models kept in `e035c_stage3/arms/`.
- **Result (from the stage-1 endpoints): null** — the automated stage-3 cycle changes nothing on a converged stage-1
  model (≤ 0.0002 full R-free on all seven arms). The stage-3 question for the E035f models is open.
- **Second run, registered 2026-09-29T15:15Z (`e035c2_stage3/`): the stage-3 cycle on the E035f models, paired against
  the plain picking loop.** Seeds: the E035f T arms' loop-2 outputs (T k3 0.09677, T_r2 k3 0.09568, T_r3 k3 0.09467). One
  cycle = hygiene (0.02 floor, same-altloc merge, gap-free renumbering) → main-chain-only connectivity pass (no unrestrained
  step) → harness pick (`STAGE3_PICK=own`, six-copy waters at ≥ 3σ) → full untangling loop; N = 3 (box 2026-09-30T12:00Z),
  closing-loop outputs at k = 3i−1. The paired reading is against the same arm continuing in E035f (pick → untangling loop
  from the same model), i.e. the E035f T arm at loop 2+i: any difference is what hygiene and the main-chain pass add on a
  model that picking has changed, which is the authors' stated reason for stage 3. Launched from a per-run script copy.
- **Environment note 7 (2026-09-29T17:05Z): picker call failed once.** Hygiene is free on these seeds (T 0.09677 → 0.09673,
  T_r2 0.09568 → 0.09571, T_r3 0.09467 → 0.09458; 980–1 081 near-zero copies deleted, 0 merges) and the main-chain pass ran
  (T: 0.09680 after it), but the `STAGE3_PICK=own` branch passed its default picker arguments as one quoted word, so the
  picker exited on "unrecognized arguments" and the arms stopped. Fixed (word-split like stage2p) and a resume-at-pick-step
  added (`RESUME=1` picks up from the main-chain output, slot 3i−2); T and T_r2 resumed 16:58–16:59Z (T's first pick: 18
  sites, 0.09680 → 0.09612 before refinement), T_r3 resumes automatically when its main-chain pass ends.
- **Interim 4 (2026-09-29T20:00Z): cycle 1 — the stage-3 cycle beats the plain picking loop from the same model.** Seeds
  are the E035f loop-2 models; the paired reference is E035f loop 3 (pick → untangling loop from the same model). Full
  R-free (select / report; gap), cycle 1 vs E035f loop 3: T **0.09389** (0.09178 / 0.09603; 0.0086) vs 0.09617 (0.09445 /
  0.09791; 0.0088) → −0.0023; T_r2 **0.09354** (0.09096 / 0.09615; 0.0092) vs 0.09526 → −0.0017; T_r3 **0.09285** (0.09036
  / 0.09537; 0.0097) vs 0.09452 → −0.0017. Select −0.0027 / −0.0018 / −0.0019 (≈ 6–10σ_select), report −0.0019 / −0.0016 /
  −0.0014: the same sign on every subset, gaps comparable. What differs from the plain loop: hygiene removed ~1 000
  near-zero water copies before the connectivity solve (a smaller ILP within the same 3-min limit), the main-chain-only
  pass, and a pick on the cleaned model (18 sites for T against 5 in the plain loop). Best six-copy model: T_r3, 0.09285.
  Cycles 2–3 running.
- **Interim 5 (2026-09-29T23:30Z): cycle 2.** T **0.09232** (select 0.08973, report 0.09494; gap 0.0088), T_r2 **0.09225**
  (0.08999 / 0.09454; 0.0088), T_r3 **0.09217** (0.09005 / 0.09432; 0.0096): −0.0016 / −0.0013 / −0.0007 from cycle 1.
  Paired against the plain loop at the same depth (E035f loop 4: 0.09582 / 0.09494 / 0.09413): −0.0035 / −0.0027 / −0.0020
  full, select −0.0046 / −0.0028 / −0.0021, report −0.0024 / −0.0025 / −0.0019 — every subset, every replicate. The
  stage-3 cycle is worth ≈ 0.001–0.0016 per cycle where the plain loop is worth ≈ 0.0002. Best six-copy model: T_r3
  cycle 2, 0.09217 full. Cycle 3 running; if it still moves by more than 2σ_full the run is extended to six cycles with
  `RESUME=1` (time box 2026-09-30T12:00Z).
- **Interim 6 (2026-09-30T03:40Z): cycle 3 — converged.** T **0.09206** (select 0.08973, report 0.09441; gap 0.0088), T_r2
  0.09233 (0.08982 / 0.09487; 0.0091), T_r3 0.09218 (0.09004 / 0.09435; 0.0097): −0.0003 / +0.0001 / 0.0000 from cycle 2,
  all within 2σ_full, so the run is not extended. The third pick added 2 sites. Against the plain loop at the same depth
  (E035f loop 5: 0.09567 / 0.09501 / 0.09397): −0.0036 / −0.0027 / −0.0018.
- **Result (second run, 2026-09-30):** the automated stage-3 cycle (hygiene with the 0.02 floor and same-altloc merge →
  main-chain-only connectivity pass → harness pick → full untangling loop) takes the six-copy model from the E035f loop-2
  state (0.0947–0.0968 full) to **0.0921–0.0923** in three cycles on all three randomized starts, 0.002–0.0036 below the plain
  picking loop from the same models at the same depth, on every subset, with R-gaps 0.0088–0.0097 (plain loop 0.0090–0.0097).
  It converges at cycle 3. Best six-copy model: T cycle 3, `e035c2_stage3/arms/T/Untangler/output/7KR0_6conf_B0_current8.pdb`,
  full 0.09206 / select 0.08973 / report 0.09441 (R-work 0.0832). The manual part of the authors' stage 3 (identity
  mix-ups fixed by hand) is not in this cycle; what remains between 0.092 and the paper's 0.064 is that, the anisotropic
  finish (E035d), and whatever their two further rounds delivered. Representation-level result (§18.1); nothing promoted.

### E035d — the authors' anisotropic-B finish on 7KR0 (registered 2026-09-28, rationale before run)
- **Rationale.** App. D: for Mac1 the B factors were converted to anisotropic and refined with restraints until convergence, then
  the loop, water addition and manual adjustments were repeated twice more. Their acceptance rule for the conversion: keep it only
  if R-free falls by at least 30 % of the R-work fall. Here: `phenix.refine convert_to_anisotropic=True` with 0 macro-cycles, then
  10 macro-cycles of B-factor-only refinement through the wrapper (`-x -N -W`, seed 42), scored before and after on the frozen
  flags; kept only if the 30 % rule holds and Δgap does not exceed +2σ_gap (D495). Applied to each arm's stage-3 final; if kept,
  two more stage-3 loops follow (the authors' "two additional times").
- **Environment note 1 (2026-09-29T05:35Z): dry run.** Mechanics test and first read of the 30 % rule on an interim model,
  the E035f T_r3 loop-1 model (full 0.09563, isotropic B, 2 226 water copies), in `e035d_dryrun/` (`aniso T_r3_k1_aniso`):
  `phenix.refine convert_to_anisotropic=True` with 0 macro-cycles, then `Refine.sh -c 0.5 -u 1 -n 10 -x -N -W` (B factors
  only, seed 42); scored before and after by the harness. Not a result of E035d proper, which applies to stage-3 finals.
- **Interim 1 (2026-09-29T06:30Z): dry-run result — the authors' rule keeps it, the campaign's R-gap gate refuses it.**
  Harness, iso → aniso: R-work 0.08655 → 0.07901 (−0.0075), full R-free 0.09563 → **0.09231** (−0.0033; select 0.09318 →
  0.09063, report 0.09810 → 0.09400, same sign), R-gap 0.0091 → **0.0133** (+0.0042 ≈ 26σ_gap). ΔR-free / ΔR-work = 0.44,
  above the authors' 0.30, so by their rule the conversion is kept; under thresholds_v6 (D495) a Δgap beyond +2σ_gap is
  `overfit_suspect` and would not be adopted for a deliverable. Both verdicts stand on record; the number is
  representation-level (§18.1: six copies, anisotropic B on 17 616 atoms at 0.77 Å). `e035d_dryrun/aniso/T_r3_k1_aniso/`.
- **Environment note 2 (2026-09-30T03:50Z): run on the stage-3 finals.** The three E035c-2 cycle-3 models (T 0.09206, T_r2
  0.09233, T_r3 0.09218 full) each: convert to anisotropic (0 mc), 10 macro-cycles B-only (`-x -N -W`, seed 42), scored before
  and after by the harness; `e035d_aniso/aniso/<arm>_aniso/`. Judged by the authors' 30 % rule and by the R-gap gate
  (+2σ_gap), both quoted. If kept, the authors' "two additional times" (two more stage-3 cycles on the anisotropic model)
  follow as E035d's second step.
- **Result, step 1 (2026-09-30T04:30Z): the conversion passes the authors' rule on all three finals and fails the campaign's
  gate on all three.** Harness, iso → aniso (full; select / report; R-work; gap): T 0.09206 → **0.08792** (0.08973 →
  0.08580 / 0.09441 → 0.09007; R-work 0.08324 → 0.07505; gap 0.0088 → 0.0129), T_r2 0.09233 → **0.08796** (0.08982 →
  0.08560 / 0.09487 → 0.09035; 0.08325 → 0.07532; 0.0091 → 0.0127), T_r3 0.09218 → **0.08812** (0.09004 → 0.08611 /
  0.09434 → 0.09015; 0.08246 → 0.07476; 0.0097 → 0.0134). ΔR-free / ΔR-work = 0.50 / 0.55 / 0.53, above the authors' 0.30:
  kept by their rule. Δgap +0.0041 / +0.0036 / +0.0036 = 22–25σ_gap: `overfit_suspect` under thresholds_v6 (D495), so the
  campaign would not adopt it for a deliverable. Both verdicts stand; the number is representation-level (six copies,
  8 997 ANISOU records). Step 2 (two more stage-3 cycles on the anisotropic models, the authors' "two additional times")
  runs in `e035d_post/` (`STAGE3_PICK=own`, N = 2; the wrapper's template leaves the ADP type to the model, so the loops
  refine anisotropic B). Best six-copy model so far: T aniso, `e035d_aniso/aniso/T_aniso/aniso_final.pdb`, 0.08792 full.

### E036 — one generation of the graph search on 3QUE: does the restricted-pair ranking predict the combined full pair? (registered 2026-10-01, rationale before run)
- **Rationale.** The serial driver judges one change at a time, five per cycle, and 64 of its 70 credits were water edits
  (`state/exports/changes.csv`, 2026-09-18). `docs/md/SPEC_GRAPH_SEARCH.md` §2 replaces the cycle with a generation: every
  proposer runs on one base, every candidate is judged by its own site-restricted pair concurrently, the accepted set is
  corrected for multiplicity (PROTOCOL §4.4(b), D507), non-conflicting winners are combined, and the combinations are judged by
  full pairs against shared null arms. The design rests on one assumption that has never been measured: that a candidate's
  restricted-pair attributable (8 macro-cycles, selection only) predicts its contribution to a combined full refinement. If
  it does not, the generation adopts the wrong subsets and the leave-one-out table says so.
- **Design.** Base: the standing 3QUE model (`state/current/3QUE.json`, 0.2589 full), the D421/D485 water-occupancy override
  on every arm. `scripts/run_graph.sh 3QUE --max-generations 1 --beam 1 --max-candidates 60 --n-null 5` under
  `thresholds_v9` with the sham nulls of E037 measured first (`--measure-nulls`); every stage (correction, solvent,
  protein_altloc, gaps, zone) plus the protocol toggles of SPEC §2.6. Lane `graph`, 28 slots. Readout, pre-registered: (1) the
  rank correlation (Spearman) between each winner's restricted attributable and its leave-one-out contribution
  (full_delta − loo_delta) in the combined set; (2) whether the "all winners" set is credited (≤ −2σ_select against the
  shared null, no R-gap or divergence flag) and whether its report half agrees in sign; (3) wall-clock of the generation
  against the serial driver's last 3QUE cycle (D492: ≈ 25–40 min per 5 kept changes). Negative outcome = (1) below 0.3 or
  (2) regressed with `interaction_only`; then the combination step is redesigned (pairwise pairs) before any wider run.
- **Not claimed.** Nothing is promoted by this run (`--no-promote`); the deliverable moves only under the D484/D499/D508
  rules from a later run.

### E037 — per-class sham nulls on the canonical trio (PROTOCOL §4.4(b), the D507 measurement) (registered 2026-10-01, rationale before run)
- **Rationale.** Every verdict on record is a k·σ_abs verdict; §4.4(b) requires the acceptance null to be measured per change
  class from ≥ 50 unsupported changes through the identical restricted pair. D507 priced it at 15 h wall for thirteen targets
  at 20 slots; with the pool it is one wave per class. The result sets the `thresholds_v9` bars and lets every recorded
  verdict be re-judged (`scripts/experiments/exp_retro_v9.py`, the D442 procedure).
- **Design.** `autoref sham-null --target T --classes water_add,water_remove,protein_altloc_add,rotamer_fix,peptide_flip,zone_rsr
  --n 50` on the standing model of 3QUE, 3TC7 and 7KR0 (`stages/sham_null.py`, draws deterministic from
  sha256(target, node, class, i), standing `refine_extra` per target, weights frozen, 8 macro-cycles, selection only). Rows:
  `sham_null` (values, 99th-percentile threshold per class) and one `changes` row per instance (`control_random_*`).
  Readout: per target × class the threshold against the standing −2σ_select bar, and the retro table (how many recorded
  credits survive). Expected from D497: on 3TC7 (σ_select 0.00008) the sham thresholds are far wider than 2σ and most of the
  sub-0.001 water credits of 3TC7.20260910v6 do not survive; on 3QUE the two bars should be close.
- **Not claimed.** No verdict on record changes until a D-row adopts v9 (D515 registers the file; adoption is the operator's).

### E038 — transfer proposals into 3QUE from isomorphous 1.6 Å p38α entries (registered 2026-10-01, rationale before run)
- **Rationale.** 3QUE is the one canonical target where per-residue conformers are weakly determined (2.7 Å). 108 deposited
  p38α entries share its cell (`targets/canonical.yaml`, p38a tier B); 6Y4X (1.60 Å) and 9MHB (1.65 Å) are the best. A
  water, an alternate conformation or a rotamer seen at 1.6 Å in the same lattice is a proposal, not evidence: judged on
  3QUE's own flags it uses none of 3QUE's reflections (PROTOCOL §3 untouched). E033's reference-model restraints from 6SP9
  (+0.0006, null) were the restraint form of the same information; a per-site proposal can be rejected per site.
- **Design.** Onboard 6Y4X and 9MHB (`scripts/onboard_series.sh --anchor 3QUE 6Y4X 9MHB`) so their models are refined on
  their own data under the campaign protocol first (a transfer source is the re-refined model, not the header model).
  Then one generation on 3QUE with `--stages transfer` only (`stages/proposers.py::transfer_*`, superposition stats in every
  `tool_params`), judged exactly as E036. Readout: number of transfer proposals by kind, how many pass the local gates, how
  many are BH-accepted, the credited combined set with Δreport, and the per-kind acceptance rate against the native proposers
  of E036 on the same base.
- **Smoke (2026-10-01T17:16–17:26Z, `runs/3QUE/graph/3QUE.graph-smoke-20261001/`, thresholds_v9, `--no-measure-nulls
  --no-promote`, solvent only, 8 candidates, 2 null seeds, lane graph 20 / untangler 8).** Machinery check, not the E036
  readout. All 8 local evaluations ran concurrently (≈ 20 s wall); 6 adds and 1 removal failed RSCC; A5012 (+0.00180) and
  A5015 (−0.00048) through the restricted pair, judged on the k·σ fallback (no null for the class): none accepted, nothing
  combined. Base continued as its re-refined null arm (Δselect +0.0013, inside the band). Consultations: select 2. Measured:
  restricted arm ≈ 118 s, full arm ≈ 10 min, peak RSS ≈ 1.3 GB per 3QUE refinement (`jobs.max_rss_mb`). A concurrent
  `autoref sham-null --n 4 --node-id SMOKE-20261001` measured water_add values +0.0011/+0.0030/+0.0005/+0.0012 (too few to use;
  kept under its own node id so no real generation reads it).

### E039 — is D512's 3TC7 gain plain phenix.refine? Phenix water picking on the standing model, paired (registered 2026-10-02, rationale before run)
- **Rationale.** D512 lists the operator's 3TC7 components as qFit residue build + connectivity optimisation, water picking
  (−0.018), riding H with a fixed ADP weight (−0.007) and XYZ weight optimisation (−0.006). The standing model (0.1728 full,
  `state/current/3TC7.json`, E028b c057) already carries riding H with the fixed ADP weight (D496) and the wrapper optimises
  the XYZ weight by default (`RefineParams.optimize_xyz_weight=True`). The largest component, Phenix's in-refinement water
  picking (`main.ordered_solvent`), has never been run on that model: the campaign's waters come from the discrete solvent
  stage. If most of 0.1728 → 0.1583 is ordered_solvent, a plain refinement reproduces it on our frozen flags. A second
  possibility is checked by the same numbers: if 0.1583 came from a refinement that generated its own free set (the D430
  precedent: the Dynamic PDB 3TC7 model was on 1993 free reflections against our 2075), no arm here approaches it.
- **Design.** `scripts/experiments/exp_refine_param.py 3TC7 <c> --knob ordered_solvent` and `--knob ordered_solvent+macro_cycles:10`,
  seeds 1–3 each, standing 3TC7 overrides on both arms (`{"optimize_adp_weight": false, "wxu_scale": 0.03}`), thresholds_v8
  (k·σ, σ_select 0.000084 — the D497 caveat: on 3TC7 the divergence and R-gap gates are the guards that matter), cycle
  indices 901–906 (a block clear of the graph run). Lane `zz_e039` (6 slots taken from 7KR0's 22). Readout: attributable
  ΔR-free-select per seed, report/full sign, Δgap, water count before/after, and the full R-free each arm reaches against
  0.1583. Nothing is promoted by this script; a credited arm would become a graph-search base by a later D-row.
- **Result 2026-10-02 (`runs/3TC7/experiments/e039_ordered_solvent/`, 6/6 paired, thresholds_v8): Phenix water picking does
  not reproduce D512; nothing credited.** Null arms full 0.1730–0.1733 / report 0.1680–0.1686 / select 0.1779–0.1780 /
  R-work 0.1348. `ordered_solvent`: attributable −0.0051/−0.0062/−0.0056 select, full 0.1710/0.1709/0.1714, report
  0.1691/0.1700/0.1705 (worse than null by +0.0011 to +0.0019), R-work 0.126–0.130, Δgap +0.0025 to +0.0065 (16–42σ_gap).
  `+macro_cycles:10`: attributable −0.0064/−0.0066/−0.0066, full 0.1706/0.1702/0.1704, report 0.1695/0.1691/0.1694, Δgap
  +0.0016 to +0.0044. Every arm `overfit_suspect` (D495 gate): the select half falls 0.006 while the report half rises and
  R-work falls twice as far as R-free — not adopted. Best full R-free from plain refinement: 0.1702, 0.012 above 0.1583. The
  operator's number is therefore not plain phenix.refine on these flags: either the manual qFit/connectivity work (the
  graph search's altloc and transfer proposers) or a different free set (D430). The model file is still needed. File searches
  2026-10-02 (local home, pod home, `/mnt/diffuse-shared`, `prism-science` repos incl. `ag-refined-proteins`) found no copy.

### Untangler relabel on single-model nodes (graph candidate, PROTOCOL §18) — pod smoke 2026-10-02/03
- `autoref/tools/untangler.relabel` on the standing 3TC7 model (`runs/3TC7/experiments/untangle_smoke_20261002/`): after four
  fixes (patch script on the pod; REMARK 3 header 'n/d'; hydrogens out of the ensemble view, riding H follow their parent;
  ligands/ions out — 3TC7's acetate broke Untangler's H-parent lookup), the ILP step completes: preparation ≈ 90 s, HiGHS
  subproblems at 120 s each, 3197 s wall, **697 ILP moves, none changes a label of the single model** (the moves swap the
  duplicated copies of unsplit atoms in the ensemble view). Reading: 3TC7's deposited-plus-campaign altloc labelling is already
  connectivity-consistent; no candidate to judge. Enabled for the 7KR0 graph run (`state/untangle.enabled`, 89 split
  residues) where E035 found tangles in the six-copy representation. Cost per node ≤ 3600 s on 4 slots, in parallel with g.0–g.4.

### E040 — 3QUE fixed XYZ weight wxc_scale 0.1, seeded (registered 2026-10-03, rationale before run)
- **Rationale.** In `3QUE.graph-weekend-20261002b` generation 1 the toggle `wxc_scale_0p1` (fixed coordinate-restraint weight
  0.1, optimisation off) moved select −0.0026 (1.8σ_select) and report −0.0046 (2.1σ_report): both halves improved, just inside
  the credit bar, and the edge was refused. One seed cannot separate that from noise; three can.
- **Design.** `exp_refine_param.py 3QUE 911..913 --knob wxc:0.1 --seed 1..3`, standing 3QUE override on both arms
  (D421/D485), thresholds_v8, lane common. Readout: attributable per seed, report/full sign, Δgap. Credited on all three with
  agreeing halves → the next 3QUE graph run starts from that protocol (a D-row).
- **E040 result 2026-10-03 (`runs/3QUE/experiments/e040_wxc01/`, 3/3, thresholds_v8): a real paired gain that does not beat
  the record.** Attributable select −0.00256 / −0.00378 / −0.00376 (seeds 1–3); seeds 2 and 3 **credited** (2.6σ), seed 1
  refused by the R-gap gate (Δgap +0.0099). Report half improves in all three (−0.0047 / −0.0030 / −0.0035); seeds 2–3 narrow the
  gap (−0.0041 / −0.0046). Full R-free null → candidate: 0.2619 → 0.2583, 0.2649 → 0.2615, 0.2658 → 0.2622. The null arms re-refine
  the standing model 0.003–0.007 above its recorded 0.2589 (the D423 best-base effect), so neither credited arm is below the
  deliverable; promotion would be refused (D499). Reading: wxc_scale 0.1 (fixed) is a better 3QUE protocol than optimised XYZ
  weights by ≈ 0.0036 against matched nulls; adopting it means re-measuring 3QUE's sham nulls under it (≈ 7 h at 8 slots) — a
  D-row decision, not made mid-campaign.

### E041 — replicate 44PS (Passmore et al. 2026) on 7KR0's data with this harness (registered 2026-10-03, operator: "go all in")
- **Target, verified this session.** 44PS (RCSB, released 2026-09-30) is the paper's deposited six-conformation re-refinement of
  7KR0's dataset (`pdbx_database_related`: "44PS is a re-refined structure, which uses the dataset of entry 7KR0"). Its
  deposited free set is IDENTICAL to our frozen flags (`scripts/verify/flag_identity.py`: 8712 free, 0 differing; the header's
  8709 is the depositors' count). Scored on our flags (`runs/7KR0/experiments/score_44PS/44PS_on_our_flags.json`): **R-free
  0.06566 full / 0.06533 select / 0.06600 report, R-work 0.04845**; 17 995 atoms, 7 722 H, six altlocs, 2 581 water atoms
  (summed occupancy 454, median 0.15, 24 % below 0.1).
- **Where we stand.** Best six-copy models: E035d aniso finals 0.0879–0.0881 full (fail the R-gap gate); E035c2 cycle 3
  0.0921 (1 305 water atoms, summed occupancy 248); E035d step-2 loopEnd4 0.0913–0.0922 (no better than the finals).
- **The paper's recipe (Appendix D, read 2026-10-03):** six copies shaken 0.5 Å, ≥ 20 restrained mc; connectivity loop (1
  unrestrained mc → ILP → 10 restrained mc at wc 0.5) to convergence; then the loop with conformation-aware Phenix water picking
  in the second half of the restrained step (12 mc), new waters occupancy 0.33, minimum occupancy 0.02, minimum separation from
  other altlocs 0.03 Å, `ordered_solvent.ignore_final_filtering_step=True`, water occupancies refined; ~30 manual Coot changes
  (side chains displaced from density; merging low-occupancy bulk-solvent waters to make room at adjacent features; residues
  moved to their own conformation, refit, reassigned, then ILP), 1–3 loops between manual rounds; anisotropic B near the end, then
  loop + water addition + manual twice more. "Unable to achieve R free below 10 % without the additional treatment for the bulk
  solvent."
- **Design.** Phase A (diagnostics, decompose the 0.022 gap): A1 44PS through one restrained step of our loop (does our pipeline
  hold 0.066?); A2 our best protein + 44PS's waters; A3 44PS's protein + our waters; each one restrained step, same settings,
  scored by the campaign evaluator. Phase B (production, from the best model): the paper's water treatment at scale with our own
  picker (E035b showed Phenix 2.1's picker wrecks six-copy models in our hands; E035f's own picker works) — repeated picking at
  falling thresholds into the bulk solvent with per-copy waters, occupancy refinement, merging of near-coincident low-occupancy
  waters, untangling loop between rounds; an automated stand-in for the manual pass (per-conformer side-chain refits where
  difference density is large, each followed at once by the ILP); anisotropic B late; repeated. Every model scored on the frozen
  flags; quoted with the R-gap and the select/report halves; ensembles are the PROTOCOL §18.1 column, never the deliverable.
