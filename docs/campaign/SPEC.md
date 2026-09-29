# SPEC — `autoref`: autonomous crystallographic refinement harness

Version: **spec-v1 (2026-08-25)**. Implements `PROTOCOL.md` (the operator's campaign brief, which wins on any conflict). `CLAUDE.md` is the agent operating manual. This document is the engineering contract: environment, layout, data model, frozen thresholds, stage algorithms, verification gates, orchestration, and phase plan.

---

## 0. Scope and non-goals

**In scope.** For each target (initial model + structure factors + FASTA), autonomously produce a model with lower R-free than four baselines (input-recomputed, input-re-refined, PDB-REDO, ours), within geometry tolerance, with a complete per-change decision log, per-cycle ledger, artifacts, validation report, and written report. The campaign's outputs (start state → end state → trajectory + decisions) are *also* the training/exploration corpus for a future "refinement LLM" (§16).

**Non-goals (v1).** Cryo-EM; fragment/PanDDA multi-crystal work; neutron; training any model. Structure predictors (Boltz-2/OpenFold via `sampleworks`) and WaterFlow/PLACER are *optional evidence generators* (§10.4, §11.4), not required for the pipeline to converge.

---

## 1. Environment

| Item | Value (verified 2026-08-25 on the pod) |
|---|---|
| Pod | `actl pod up autoresearch -n diffuse --profile cpu-medium --image phenix --pvc-size 100Gi` (owner `xraymemory`) |
| Host | `ssh workspace.actl-ws-xraymemory-autoresearch.devspace` (needs a live `actl pod up/sync`); fallback `actl pod exec -n diffuse -- <cmd>` |
| Image | `harbor.astera.sh/library/phenix:phenix2.1-6048-2026-06-09` — Ubuntu 22.04, **Phenix 2.1 release 6048** at `/opt/phenix`, Python 3.9.23 (Phenix's), `uv 0.7.8`, `gemmi` CLI at `/opt/phenix/bin/gemmi` |
| Limits | cgroup **4 CPU / 16 GiB** (host shows 104 cores — do not trust `nproc`; use `AUTOREF_NPROC=4`) |
| Storage | home PVC `/home/dev` (nfs-shared, all_squash → files owned by `nobody`; `git config --global safe.directory '*'` required); `/mnt/diffuse-shared` (team RWX); `/programs` = SBGrid (read-only; only `phenix`, `pymol` installed) |
| User | `root` |
| Network | outbound HTTPS OK (RCSB, PDB-REDO, GitHub) |
| Synced tree | local `~/hax/astera/autoresearch` ⇄ `/home/dev/workspace`; excludes per `.actlignore` (`data/raw`, `runs/`, `*.mtz`, …) |

### 1.1 Interpreters (two-interpreter design)

1. **Harness interpreter** — `uv` venv `/home/dev/envs/autoref` (Python 3.12): `gemmi`, `numpy`, `scipy`, `pandas`, `pyyaml`, `reciprocalspaceship`, `biopython`, `rich`, `typer`, `requests`, `matplotlib`. Runs the `autoref` CLI, ledgers, parsing, orchestration. Shells out to Phenix.
2. **cctbx interpreter** — `phenix.python` (3.9). Small, single-purpose scripts under `autoref/cctbx/` that need `mmtbx`/`iotbx` (fmodel evaluation on flag subsets, occupancy-group introspection, map values at atoms, Ringer). Invoked by the harness as subprocesses with JSON on stdout. Never import cctbx from the harness interpreter.
3. **qFit** — `uv` venv `/home/dev/envs/qfit` (Python 3.11), `pip install git+https://github.com/ExcitedStates/qfit-3.0.git`. Provides `qfit_protein`, `qfit_ligand`, `qfit_final_refine_xray.sh` (which itself calls Phenix ≥1.21).
4. **Coot (headless)** — micromamba env `/home/dev/envs/coot` with **bioconda `coot-headless` 1.3.3** (chapi Python bindings + libcootapi, no GUI). This is the Linux substitute for Bandicoot (macOS-only, Coot 0.9 fork) and for the macOS-only `cootmcp`; substitution disclosed per PROTOCOL §13 (re-read: Emsley 2010; Casañal 2020). Our own tool surface over chapi is `autoref/tools/coot.py`.

Env activation is done per-subprocess by the wrappers (`source /opt/phenix/phenix_env.sh`; venv `bin/` paths), never globally.

### 1.2 Path variables

| Var | Default | Meaning |
|---|---|---|
| `AUTOREF_ROOT` | `/home/dev/workspace` | synced repo |
| `AUTOREF_DATA_ROOT` | `/home/dev/data` | `raw/<ID>/` downloads, `pdbredo/`, `targets/<target>/` prepared inputs |
| `AUTOREF_STATE` | `/home/dev/state` | canonical ledgers (SQLite), dossiers, locks, liveness; symlinked from `/state` (PROTOCOL §2 path) |
| `AUTOREF_RUNS` | `/home/dev/runs` | `<target>/c<cycle:03d>/<stage>/` working dirs + per-cycle archives |
| `AUTOREF_NPROC` | `4` | concurrency integer (PROTOCOL §10) |
| `AUTOREF_THRESHOLDS` | `autoref/thresholds_v1.yaml` | frozen thresholds |

`state/exports/` in the repo receives CSV/JSON *exports* of the canonical ledgers (`autoref ledger export`) so they are visible locally; the SQLite file itself is never synced.

---

## 2. Repository layout

```
autoresearch/
  PROTOCOL.md            campaign brief (verbatim)         SPEC.md  (this)      CLAUDE.md (agent manual)
  pyproject.toml         package `autoref` (harness interpreter)
  autoref/
    __init__.py          __version__ = "0.1.0"; SCRIPT_VERSION stamp on every ledger row
    cli.py               `autoref` typer app: fetch | dossier | verify | noise-floor | baseline | cycle | run | status | ledger | daemon
    config.py            paths (§1.2), env resolution, thresholds loader (frozen; hash recorded)
    thresholds_v1.yaml   FROZEN numeric thresholds (§8–§11); changing = new file thresholds_v2.yaml + deviation row
    vocab.py             frozen change_type vocabulary (§3.5), stage names, verdicts
    hashing.py           sha256 of files; canonical hash of models (atoms+altloc+occ+B) for round-trip checks
    ledger.py            SQLite schema + idempotent upserts + exports (§3.3)
    flags.py             R-free flag audit/inheritance/freeze; select/report split (§5)
    model.py             gemmi-based model introspection: chains, gaps, altloc groups, occupancy sums, waters, ligands, altloc network graph (§12)
    tools/               one wrapper per external tool; each exposes run(...)->dataclass, parse(...), canary()  (§4)
      phenix_refine.py  xtriage.py  molprobity.py  clash.py  ringer.py  qfit.py  polder.py  douse.py
      elbow.py  tls.py  real_space.py  coot.py  rscc.py  pdbredo.py  rcsb.py  paired_refinement.py
    cctbx/               scripts run under phenix.python (JSON out)
      rfree_split.py  occ_groups.py  map_at_atoms.py  peaks.py  roundtrip_check.py
    stages/              dossier.py  noise_floor.py  baseline.py  correction.py  solvent.py  altloc.py  ligand.py  macro_cycle.py  negative_controls.py  convergence.py
    checks/              verification gates (§14): altloc_clash_case.py  occupancy_sum.py  roundtrip.py  rfree_reproduce.py  gate_sanity.py
    orchestration/       semaphore.py (concurrency integer) job_ledger.py  daemons.py (clock/watchdog/scribe)
    report/              status.py (THE aggregation function)  figures.py  validation_report.py  written_report.py  supplement.py
  scripts/               bringup_pod.sh  fetch_raw.sh  (shell glue only)
  targets/targets.yaml   target list (§3.1)
  state/                 dossier/ (synced copies)  exports/  status/  notes/literature.md  deviations.md
  tests/                 pytest for pure-python parts (ledger idempotence, vocab, model introspection on fixtures)
  refinement examples/   operator-supplied 7KR0 6-conformer reference (read-only)
  datasets/              refinement-pairs export (§16)
```

---

## 3. Data model

### 3.1 `targets/targets.yaml`

```yaml
version: 1
targets:
  - id: 7KR0            # campaign target id (unique token)
    pdb_id: 7KR0        # for RCSB/PDB-REDO lookups; null if unreleased
    model: raw/7KR0/7KR0.cif          # relative to AUTOREF_DATA_ROOT
    sf:    raw/7KR0/7KR0-sf.cif       # mmCIF-SF or MTZ
    fasta: raw/7KR0/7KR0.fasta
    sf_labels: null                   # e.g. "I,SIGI" / "FP,SIGFP"; null = audit chooses & records
    rfree_column: null                # null = audit discovers; recorded in dossier
    claimed: {resolution: 0.77, space_group: "C 1 2 1", chains: [A], ligands: [], metals: [], cofactors: []}
    notes: "SARS-CoV-2 NSP3 macrodomain, 0.77 Å; deposited R-work/R-free 0.1099/0.1172 (header)"
  - id: 7KR0-6conf
    pdb_id: 7KR0
    model: examples/7KR0_6conf_bestJuly/input/7KR0_6conf_best_to_aniso4_loopEnd0-1_adp_refine.pdb
    sf:    raw/7KR0/7KR0-sf.cif
    fasta: raw/7KR0/7KR0.fasta
    notes: "operator's 6-conformer model; flags must be shown identical to the deposited set (gate G3) before use"
  - id: 3TC7   # 1.5 Å, Dynamic PDB qFit example: 0.193 → 0.163
  - id: 3QUE   # 2.7 Å, Dynamic PDB ensemble example: 0.311 → 0.25
```

### 3.2 Data root layout

```
$AUTOREF_DATA_ROOT/
  raw/<PDBID>/  <ID>.cif <ID>.pdb <ID>-sf.cif <ID>.fasta rcsb_entry.json pdbredo/{<id>_final.cif,.pdb,.mtz,data.json} MANIFEST.sha256 FETCHED
  targets/<target>/
    input_model.cif        as supplied (copied, sha256 in dossier)
    data.mtz               converted SF with the columns actually used (§5.1)  — FROZEN, sha256 in dossier
    flags.mtz              R-free flags only (inherited or generated-once)  — FROZEN, sha256 on every ledger row
    split.json             free-reflection → {select|report} assignment (frozen random, seed recorded)
    ligands/<CCD>.cif      restraint dictionaries + generator provenance
```

### 3.3 Ledgers (SQLite `$AUTOREF_STATE/ledger.sqlite`; exported to CSV)

All tables carry `script_version`, `thresholds_sha256`, `written_at`. Upserts keyed as shown (PROTOCOL §7 idempotence).

| Table | Key | Columns |
|---|---|---|
| `cycles` | `(target, cycle_index, stage)` | exactly the PROTOCOL §7 per-cycle record, written for the model in force after every cycle by `stages/record.py::write_cycle_row` (D479: MolProbity, altloc-aware clashscore and composition by tool call; one `.tar.zst` archive per cycle; `geometry_flag` = the adopted model's violations of the frozen `geometry` caps, a monitor): `r_work, r_free_full, r_free_select, r_free_report, r_gap, n_waters, n_protein_altlocs, n_ligand_altlocs, n_atoms, clashscore_altloc_aware, rama_outliers, rota_outliers, bond_rmsd, angle_rmsd, mean_b, ksol, bsol, accepted_changes, rejected_changes, wall_clock_s, program_versions(json), input_model_sha256, output_model_sha256, mtz_sha256, rfree_flag_sha256` |
| `changes` | `(target, cycle_index, change_id)` | PROTOCOL §7 per-change record: `change_type, selection, evidence_metric, evidence_value, delta_r_free_select, noise_floor, verdict, reason` + `change_set_id, before_diff_density, after_diff_density, rscc_before, rscc_after` |
| `roster` | `(tool, version, image_id)` | `status, wall_clock_s, output_shape, validated_at, canary_target, command` (PROTOCOL §8) |
| `solvent_disagreements` | `(target, cycle_index, site_id)` | `phenix_verdict, coot_verdict, resolution, evidence(json)` (PROTOCOL §5.1) |
| `noise_floor` | `(target)` | `n_seeds, seeds(json), r_free_values(json), sigma_full, sigma_select, sigma_report, analytic_estimate, k_multiple, accept_threshold, frozen_at` |
| `rfree_consultations` | `(target)` | running count of R-free-select consultations (PROTOCOL §3.6) |
| `jobs` | `(job_id)` | `target, stage, cmd, cwd, pid, started_at, ended_at, exit_code, wall_clock_s, host, authorized_by` (PROTOCOL §10 job-metadata ledger) |
| `deviations` | `(deviation_id)` | `target, section, description, configurations_tried, decided_at` — every protocol deviation / post-hoc adjustment |
| `defects` | `(target, column, cycle_index)` | `reason, owning_frame` — un-computable values (PROTOCOL §11.3: no sentinels) |
| `liveness` | `(daemon)` | `last_beat, cycle_s` |

### 3.4 Dossier `$AUTOREF_STATE/dossier/<target>.json` (PROTOCOL §2)

```
{ target, pdb_id, created_at, script_version, thresholds_sha256,
  inputs: { model:{path,sha256,format}, sf:{path,sha256,format,columns_present[]}, fasta:{path,sha256} },
  data_audit: { space_group, unit_cell, resolution:{low,high}, completeness:{overall,high_shell}, multiplicity,
                i_over_sigma:{overall,high_shell}, cc_half_by_shell[], intensities_or_amplitudes, columns_used,
                anisotropy:{eigen_resolution[], ratio}, twinning:{l_test, britton, h_test, moments, twin_laws[]},
                tncs_peaks[], wilson_b, xtriage_log_sha256,
                resolution_cutoff:{deposited, paired_refinement:{cutoffs[], r_at_common[], decision, log}} },
  flags: { column, free_value, n_free, fraction, source: inherited|generated_once, generation_method, flags_sha256,
           split:{seed, n_select, n_report, split_sha256}, small_test_set_warning: bool },
  model_audit: { chains[], residue_ranges[], gaps[], sequence_vs_fasta:{identity, unbuilt_residues[]},
                 ligands:[{ccd, resolved_by:"rcsb_ccd_lookup", name, n_atoms}], metals:[{elem, site, coordination, plausible, tool}],
                 altlocs:{n_groups, letters[], occupancy_sum_violations[]}, waters:{n, b_stats, n_negative_diff, n_no_hbond},
                 ncs:{copies, rmsd_matrix} },
  composition_hypothesis: { unmodeled_positive_peaks[], ringer_secondary_sites[], ligand_residual:{...}, free_text },
  baselines: { pdbredo:{version, r_work, r_free, r_free_final, n_test, validation{...}, fetched_at, source_url},
               header:{r_work, r_free, n_free, resolution} } }
```

### 3.5 Frozen `change_type` vocabulary (`autoref/vocab.py`)

`water_add, water_remove, water_to_ion, water_altloc_tag, ion_add, ion_remove, protein_altloc_add, protein_altloc_prune, protein_altloc_regroup, ligand_altloc_add, ligand_altloc_prune, ligand_repose, rotamer_fix, peptide_flip, flip_correction (NQH), sidechain_rebuild, occupancy_regroup, adp_model_change, tls_regroup, weight_change, hydrogens_toggle, restraint_regen, control_random_water, control_random_altloc`.

Stages: `fetch, dossier, verify, noise_floor, baseline_input, baseline_rerefine, baseline_pdbredo, correction, solvent, protein_altloc, ligand_altloc, rerefine, negative_control, final`. Verdicts: `accepted, rejected, ambiguous, no_change`.

---

## 4. Tool roster and wrappers (`autoref/tools/`)

Each wrapper: `run(...)` builds the exact command line (recorded verbatim in `jobs`), executes under the semaphore (§13.2), captures stdout/stderr to the stage dir, `parse()` returns a typed dataclass, `canary()` runs it on 7KR0 and asserts the output shape the next stage consumes. A roster row is PASS only when canary passes (PROTOCOL §8).

| Tool | Command (verified present) | Used for | Output consumed |
|---|---|---|---|
| Reciprocal refinement | `phenix.refine` | all refinements; `main.random_seed`, `strategy`, `wxc_scale/wxu_scale`, `ordered_solvent`, `adp`, `tls`, `occupancies`, `hydrogens` | `.log` (R-work/R-free/ksol/bsol/rmsd), `.mtz` map coeffs, `.cif` model, `.eff` |
| Data audit | `phenix.xtriage` | §2 data audit (twinning, tNCS, anisotropy, Wilson B, CC1/2 if unmerged intensities) | log → parsed JSON |
| SF conversion | `phenix.cif_as_mtz`, `phenix.reflection_file_converter`, `phenix.mtz.dump`, gemmi | build `data.mtz` and `flags.mtz`. Verified columns: 7KR0 `F_meas_au`+`status`+`pdbx_r_free_flag`; 3TC7 `F_meas_au` **and** `intensity_meas` (+ anomalous pairs) + `status` — **but 3TC7's intensities are 0/0 for 36 868 of 41 052 rows and are rejected**, see deviation D009; 3QUE `F_meas_au`+`status` only. All three refine against `FP,SIGFP` | |
| Validation | `phenix.molprobity` (`--json`?) → fallback log parsing; `phenix.clashscore --json-filename`; `phenix.rama_z`; `phenix.cablam`; `mmtbx.reduce2`/`phenix.reduce` + `phenix.probe`/`mmtbx.probe2` | §4.5 tolerances, NQH flips, clash lists | JSON/log |
| Altloc-aware clash | `phenix.clashscore` + our network-graph post-filter (§12) | clashscore_altloc_aware | |
| Ringer | `mmtbx.ringer` | §5.2 detect-first | CSV of dihedral density scans |
| qFit | `qfit_protein`, `qfit_ligand` (qfit venv). **`qfit_final_refine_xray.sh` is OPTIONAL and never run in production** — it hard-codes `r_free_flags.generate=True` (D017); its protocol is re-implemented by the harness under the §5.1 guards | §5.2/§5.3 building | `multiconformer_model2.pdb`, `qFit_occupancy.params` |
| Polder | `phenix.polder` | §5.3 ligand + ligand-altloc validation | CC(1,2)/CC(1,3), map |
| Solvent | `phenix.refine ordered_solvent=True` and `phenix.douse` | §5.1 Phenix picker | water list |
| Coot headless | chapi (`coot-headless`) | Find Waters / Check-Delete Waters / H-bond check / rotamer & flip tools / RSCC per residue | JSON via our script |
| Real-space fit | `phenix.real_space_correlation` (+ `cctbx/map_at_atoms.py`); **`phenix.map_model_cc` is ABSENT in 2.1-6048** (D021) | RSCC, RSZD-like z-scores, per-residue fit | |
| Local RSR | Coot refine-zone alternated with regularize-zone (chapi `refine_residue_range`; regularize = map weight 0; D477) as the `zone_rsr` proposer and as an optional engine (`discrete.local_refine: coot`); the mmtbx selection-only refinement (D406) is the default engine and the fallback; `phenix.real_space_refine` cut+splice is kept for the canary | §4.1 local geometry repair | zone RSCC before/after, per-pass status, `params_used` |
| Restraints | `phenix.elbow` (license-cleared within Phenix), `phenix.ready_set` | §5.3 restraints-first; CCD code resolved by RCSB lookup | `.cif` dict + provenance |
| TLS | `phenix.find_tls_groups` (substitute for TLSMD web server; disclosed) | §4.1 | groups |
| Metals | `phenix.metal_coordination` + gemmi neighbor analysis (substitute for CheckMyMetal web server; disclosed) | §2 model audit | |
| UnDowser | `phenix.undowser_validation` / `mmtbx.undowser2_validation` | §5.1 solvent audit | table |
| Paired refinement | our `tools/paired_refinement.py` driving `phenix.refine` at cutoff ladder (Karplus & Diederichs 2012) | §2 cutoff decision | R at common resolution |
| PDB-REDO | HTTPS `pdb-redo.eu/db/<id>/{<id>_final.cif,_final.mtz,data.json}` (page-linked; HEAD returns 404, use GET) | §2 baselines, §6 model (3) | |
| RCSB | `files.rcsb.org/download/<ID>[.cif|-sf.cif|.pdb]`, `data.rcsb.org/rest/v1/core/entry/<ID>`, `…/core/chemcomp/<CCD>` | fetch + CCD lookup | |
| REFMAC5 | **absent** (no CCP4 on pod or in SBGrid) — cross-check OPTIONAL; roster row `status=ABSENT` | | |
| Ensemble refinement | `phenix.ensemble_refinement` (Burnley 2012) — only for §5.2 "altlocs cannot capture heterogeneity" disclosure on 3QUE-like targets | optional | |

Program versions are captured once per session (`phenix.version`, `qfit_protein --version`, chapi `coot_version()`, `gemmi --version`) and stamped in `cycles.program_versions`.

---

## 5. Cross-validation implementation (PROTOCOL §3 — non-negotiable)

### 5.1 Data preparation (once per target; then frozen)
1. Convert SF to MTZ with `phenix.cif_as_mtz` (or copy MTZ). Record every column present. Choose the array to refine against: prefer merged **intensities** (`I,SIGI`) so phenix.refine applies French–Wilson; else amplitudes. Record `intensities_or_amplitudes` + labels. Never apply sigma cutoffs.
2. **Flags.** If an R-free column exists (`FREE`, `R-free-flags`, `FreeR_flag`, `status`…): inherit as-is; detect convention (`free_value`) by the minority value (mmCIF `status='f'` → free). Write `flags.mtz` = flags only; sha256 → dossier; `rfree_flag_sha256` on every row. If absent: generate **once** with `phenix.refine … r_free_flags.generate=True` equivalent via `iotbx` (fraction 0.05, `max_free=2000` default recorded), **thin shells** if tNCS/NCS detected else random; seed recorded; frozen; sha256.
3. **Select/report split.** `flags.py` assigns each free reflection to `select` or `report` by a frozen RNG (seed = crc32(target)); `split.json` + sha256. Both halves are disjoint subsets of the inherited free set — the free set is never changed.
4. **Evaluation.** `phenix.refine` sees the full inherited free set (standard). After every refinement, `cctbx/rfree_split.py` rebuilds `fmodel` from the output model + `data.mtz` + `flags.mtz` (same scaling/bulk-solvent as the refinement's final state, `update_all_scales`) and reports `r_free_full`, `r_free_select`, `r_free_report`, `r_work`. Every automated accept/reject reads **only** `r_free_select` and increments `rfree_consultations`. Every deliverable headline is `r_free_report` (+ full for literature comparability).
5. **Guards (hard failures, campaign-halting):** any refinement command whose effective parameters contain `r_free_flags.generate=True` after data prep; any change of `xray_data.high_resolution/low_resolution/sigma_*` outside the pre-registered paired-refinement stage; any `ignore_r_free_flags=True`; a changed `rfree_flag_sha256` mid-target; `n_free` differing from the dossier. `phenix_refine.py` refuses to dispatch on any of these and writes a `deviations` row with `severity=HALT`.
6. `n_free < 500` → dossier `small_test_set_warning=true`; report k-fold as a recommended follow-up (not implemented v1; disclosed).

### 5.2 Gate G3 — reproduce the depositor's R-free

**Measured 2026-08-26.** 7KR0 PASS (recomputed 0.1103/0.1174 vs header 0.1099/0.1172, Δ +0.0002);
3TC7 PASS (0.1537/0.1915 vs 0.158/0.193, Δ −0.0015); **3QUE FAIL** (0.2146/0.2871 vs 0.2225/0.3109,
Δ −0.0238) — diagnosed as REFMAC5-vs-Phenix scaling and allowed to proceed under the stated conditions
(deviation D008). `7KR0-6conf` flag identity: **0 mismatches over 178 324 common reflections**, so the
operator's 6-conformer model is commensurable with the deposited test set.
Run `phenix.refine` with **zero macro-cycles** (`main.number_of_macro_cycles=0`, bulk-solvent + scaling only) on the deposited model and `data.mtz`+`flags.mtz`; R-free must match the header within `max(3σ_noise, 0.005)` of the header value (accounting for hydrogens/anisotropy conventions). Fail → diagnose the data file before anything else (PROTOCOL §8).

---

## 6. Stage pipeline (per target)

```
fetch → prep(§5.1) → dossier(§2) → verify gates (§14: G1..G8) → noise_floor(§7) →
baselines: (1) input recomputed  (2) input re-refined (defaults)  (3) PDB-REDO recomputed →
[macro-cycle loop]
   c.0 occupancy_regroup (scale over-occupied altloc groups to 1.0; under-occupied left alone)  → rerefine → evaluate
   c.1 correction      (NQH flips, rotamer/peptide fixes; Coot+MolProbity evidence)   → rerefine → evaluate
   c.2 solvent-1       (conservative pick; Phenix ⊗ Coot combination rule)            → rerefine → evaluate
   c.3 protein_altloc  (Ringer → qFit → occ refine → prune<floor → validate)          → rerefine → evaluate → re-examine waters
   c.4 ligand_altloc   (elbow restraints → qFit-ligand → polder)                      → rerefine → evaluate
   c.5 solvent-n       (re-pick/re-prune with altlocs)                                → rerefine → evaluate
   until convergence (§4.6): 3 consecutive macro-cycles with no accepted change and |ΔR-free| < floor
negative_controls (≥1 target) → final → validation report → written report → supplement
```

Each `evaluate` = §7 acceptance. Each stage writes one `cycles` row (`stage` distinguishes sub-stages) and N `changes` rows; the working dir `runs/<target>/c<idx>/<stage>/` is archived (`.tar.zst`) with input/output models, MTZ, logs, validation JSON, peak lists, and `command.txt`.

**Change-set evaluation unit (disclosed interpretation of PROTOCOL §4.3).** Reciprocal-space ΔR-free is measured per *change set* (one stage's batch, e.g. "solvent-1 added 41 waters"), because a single water's ΔR-free is far below any measurable noise floor. Every individual change still gets its own `changes` row with its *local* evidence (RSCC/peak/polder) and the batch's `delta_r_free_select` and `change_set_id`. If a batch fails ΔR-free but individual local evidence is strong, the batch is bisected once (halves) and re-evaluated; sub-batches that still fail are rejected. Bisection count is recorded.

### 6.1 Reciprocal-space stage defaults (`tools/phenix_refine.py`)
- Strategy: `individual_sites + individual_adp (+ occupancies when altlocs/partial-occ present)`; rigid-body/TA/SA never by default (SA forbidden after altlocs exist — enforced).
- ADP model by data-to-parameter ratio: anisotropic if `n_refl / n_atoms ≥ 5.0` at the target's resolution **and** d_min ≤ 1.5 Å; else isotropic + TLS (`phenix.find_tls_groups`) when d_min ≥ 2.0 Å or chains > 200 residues. Decision written to the stage log and `cycles.program_versions.adp_model`.
- Bulk solvent: flat mask default; if `ksol/bsol` or the low-res shell R suggest poor fit, evaluate the mosaic model and record both.
- Hydrogens: riding H added with `phenix.ready_set`/`reduce2` for refinement; **retained** in output (documented; consistent across all four baselines).
- Weights: `optimize_xyz_weight=True optimize_adp_weight=True` (phenix's internal grid uses the full free set — recorded as a consultation; count of trial weights parsed from the log). 
- Rama/SS/reference restraints only when d_min > 2.5 Å; disclosed.
- `main.number_of_macro_cycles=5`, `main.random_seed=<seed>` (noise-floor seeds recorded), `nproc=AUTOREF_NPROC`.

### 6.2 Real-space stage
Peaks: `phenix.refine` output mFo-DFc → `cctbx/peaks.py` (peak search ≥ `peak_sigma_triage`) → triage table (water / ion / ligand / altloc / sidechain / unexplained) using distance-to-model, Ringer list, ligand proximity, and B of neighbors. Every peak gets a row in the stage's `peaks.json` with its triage label.

---

## 7. Noise floor and acceptance

**Noise floor (PROTOCOL §4.4).** N=10 seeds (`main.random_seed ∈ {1..10}`) of the *identical* baseline re-refinement. Record all R-free values (full/select/report) → `σ_select = stdev(r_free_select)`. Analytic estimate `σ_analytic ≈ R_free · sqrt(1/(2·n_select))`-style from test-set size is computed and reported with the discrepancy; **never** used as threshold. Frozen per target before the first change.

**Accept threshold.** `k = 2.0` (frozen in `thresholds_v1.yaml`): accept requires `ΔR-free-select ≤ −k·σ_select`. Plus all of: local support (§9–§11 thresholds), geometry within tolerance (§8), no new altloc-aware clashes (§12), occupancy sums valid. Rejections that *lowered* R-free are counted (`cycles.rejected_changes_with_rfree_gain`).

`r_gap = r_free_full − r_work` is tracked per row. v1 rule (kept): a gap widening by > 0.01 between base and candidate while R-free falls raises a `deviations` warning and pauses the target for review (WATCHDOG). v4 rule (D476, `refine.r_gap`): every paired cycle also records `r_gap_null`, `delta_r_gap = gap(candidate) − gap(null)` and `gap_flag`; the flag `overfit_suspect` is set when R-free-select improved while `delta_r_gap > k·σ_gap` (σ_gap = sd of the gap over the noise-floor seeds; `autoref/rgap.py`). `mode: monitor` leaves verdicts unchanged; `mode: gate` withholds credit and does not adopt the candidate.

---

## 8. Geometry tolerances (`thresholds_v1.yaml`, frozen)

Absolute caps (candidate rejected if exceeded) **and** relative caps vs. the previous accepted model:

| Metric | Absolute | Relative (Δ vs prev accepted) |
|---|---|---|
| bond RMSD (Å) | ≤ 0.020 | +0.003 |
| angle RMSD (°) | ≤ 2.0 | +0.30 |
| Ramachandran outliers (%) | ≤ 0.5 | +0.2 |
| Ramachandran favored (%) | ≥ 95 | −1.0 |
| rotamer outliers (%) | ≤ 1.5 | +0.5 |
| clashscore (altloc-aware) | ≤ 10 (≤ 5 at d_min ≤ 1.5 Å) | +1.0 |
| cis-nonPro peptides | no new | 0 |
| twisted peptides | no new | 0 |
| CaBLAM outliers (%) (d_min ≥ 2.5 Å) | ≤ 2.0 | +0.5 |
| per-residue RSCC outliers (RSCC < 0.7, protein) | no new | 0 |

---

## 9. Solvent thresholds (frozen)

Phenix picker (`ordered_solvent` / `douse`): place if mFo-DFc peak ≥ **3.0σ**; retain if 2mFo-DFc ≥ **1.0σ** at the atom, **B ≤ min(80 Å², 2.5·⟨B_protein⟩)**, distance to N/O donor/acceptor **2.4–3.3 Å**, ≥ **2.2 Å** to any non-H atom, occupancy refined ∈ [0.5,1.0] else pruned. Coot picker (chapi `find_waters`): diff map at **3.0σ**; `check_waters`: delete if 2mFo-DFc < **0.8σ**, B > 80, min distance < 2.3 Å or > 3.4 Å, no H-bond partner within 3.4 Å. **Combination rule:** keep iff found by ≥1 picker and survives the other's retention filter; every disagreement → `solvent_disagreements` with resolution + evidence. UnDowser on every solvent set; flagged waters go to ion/altloc/ligand triage — never silently deleted. Ion assignment requires coordination number + geometry + distances + B consistency (+ anomalous map where `ANOM` present), recorded per ion. Altloc-tagged waters take the partner's letter/occupancy.

---

## 10. Protein altloc protocol (frozen)

1. `mmtbx.ringer` on the single-conformer refined model (altlocs stripped copy) → residues with secondary peaks ≥ **0.3σ** (below 1σ) → `ringer_sites` (recorded *before* building).
2. `qfit_protein <2mFo-DFc coeffs from composite-omit or refine mtz> -l 2FOFCWT,PH2FOFCWT model.pdb -p AUTOREF_NPROC` → `multiconformer_model2.pdb`; then `qfit_final_refine_xray.sh` protocol *re-implemented in our wrapper* (so seeds/flags/guards apply): occupancy refinement with `qFit_occupancy.params` constraints, prune conformers < **0.10**, re-refine, iterate until stable (max 5).
3. Segment coupling: build the altloc network graph (§12) from qFit output; per-residue isolated altlocs that break backbone continuity are re-grouped or rejected.
4. Validation per added conformer: positive mFo-DFc (≥ 3.0σ integrated) before, residual < 1.5σ after; RSCC of the conformer ≥ 0.7; recorded before/after.
5. Report: n added, occupancy histogram, fraction of `ringer_sites` built.
6. **Optional evidence (v1.x):** `sampleworks`/Boltz-2 ensembles and FLEXR as *independent* altloc proposers to compare against qFit — never as acceptance evidence.

---

## 11. Ligand protocol (frozen)

1. CCD code resolved via `data.rcsb.org/rest/v1/core/chemcomp/<CCD>` (never from memory); SMILES from that record; `phenix.elbow --smiles … --id CCD --opt` → dictionary inspected (bond-length sanity vs. CCD ideal); provenance recorded.
2. `qfit_ligand map.mtz model.pdb -l 2FOFCWT,PH2FOFCWT "<chain>,<resi>" -sm "<SMILES>" -nc 10000` → poses.
3. `phenix.polder` per ligand and per ligand altloc: record CC(1,2), CC(1,3); "real" iff CC(1,3) > CC(1,2) *and* polder map ≥ 3σ over ≥ 70 % of ligand atoms.
4. Per-ligand RSCC ≥ **0.80**, RSZD ≤ **3.0**, real-space R, occupancy, ⟨B_lig⟩/⟨B_env⟩ ≤ 1.5 (else "weakly supported").
5. Ambiguity rule: if "1 conformer + waters" and "2 conformers" both satisfy 3–4 within noise → verdict `ambiguous`, both models archived, neither claimed.
6. Ligand/protein altloc labels in the site made consistent (network graph).
7. **Optional evidence:** PLACER ensembles (GPU; needs ligand present; ≤600 atoms crop) as an independent pose proposer — not v1.

---

## 12. Altloc-aware clash detection (PROTOCOL §5.4)

`model.py::altloc_networks()` builds the coupled-network graph: nodes = (residue, altloc letter); edges = backbone connectivity between altloc'd neighbors with the same letter, shared occupancy constraint groups (from qFit params / phenix `occupancies.constrained_group`), and ligand–protein site coupling. Clashes from `phenix.clashscore --json-filename` (probe-based; handles altlocs per-letter) are post-filtered: drop pairs (i:L1, j:L2) with L1≠L2, both non-blank, *in the same network*; keep blank-vs-any; keep same-letter; keep cross-letter across independent networks. Output raw and occupancy-weighted counts (`w = occ_i·occ_j` for cross-network, `occ` for blank-vs-letter). **Gate G1** proves this on a synthetic two-conformer coupled segment with hand-counted clashes (`checks/altloc_clash_case.py`), output saved.

Occupancy-sum assertion (`model.py::assert_occupancy_sums`) runs on every model written: protein/nucleic groups = 1.0 ± 0.01; HETATM groups ≤ 1.0 + 0.01. Violation → the stage fails (bug), not a warning.

---

## 13. Orchestration (PROTOCOL §9–§10 mapped to this harness)

### 13.1 Agents
- **Orchestrator** = the interactive Claude Code session: owns cadence, dispatch policy, frozen thresholds, status posts. Does **no** production refinement in its own frame; it dispatches sub-agents (`Agent` tool) and pod jobs.
- **TOOL-BRINGUP sub-agents** (one per tool; parallel): each makes `autoref/tools/<tool>.py` pass its canary on 7KR0 and writes the roster row.
- **Per-(target × stage) sub-agents** for production: brief = PROTOCOL + SPEC + target + stage; they call `autoref cycle --target T --stage S` and report the ledger rows they wrote. Targets run in parallel subject to the concurrency integer.
- **Adversarial reviewers** (≥2): one re-runs refinements from raw inputs; one reads only ledgers/artifacts. Findings ship with the exact query/script.
- **Singletons** — implemented as **pod-side daemons** (`autoref daemon clock|watchdog|scribe|budget`, `nohup`, liveness rows every cycle; orchestrator re-dispatches if stale > 2 cycles). Disclosed adaptation: long-lived LLM agents that "never return" are replaced by deterministic daemons; the SCRIBE's numbers come from `report/status.py::aggregate()` — the single saved aggregation function (PROTOCOL §11.8).

### 13.2 Concurrency and job ledger
`orchestration/semaphore.py`: campaign-wide integer `AUTOREF_NPROC` (=4 on cpu-medium) enforced by a file-lock counting semaphore in `$AUTOREF_STATE/locks/`; authorized writers: `phenix_refine.py`, `qfit.py`, `paired_refinement.py` only. Every dispatch appends to `jobs` **before** exec; if the append fails, the job is not launched.

### 13.3 Budget
No provider metering API is reachable for the Astera cluster → spend is **UNCALIBRATED** by definition: reported as pod-hours × profile from `jobs`/`liveness`, never with a pace adjective. `<BUDGET>` is unset by the operator; status blocks say so explicitly.

### 13.4 Status cadence
`autoref status` renders the hourly block (active jobs/agents, per-target cycle counts, best R-free-report, spend basis, deviation-line count) from `aggregate()` into `state/status/<UTC>.md` (Slack not configured; disclosed). Kickoff + daily posts go to `state/status/` as well.

---

## 14. Verification gates (all must PASS before production on a target)

| Gate | Check | Artifact |
|---|---|---|
| G0 | Roster: every tool in §4 (except ABSENT/OPTIONAL) has a PASS row from a 7KR0 canary | `roster` |
| G1 | Altloc clash test case (synthetic coupled 2-conformer segment; hand count == tool count) | `state/checks/G1_altloc_clash.json` |
| G2 | Occupancy-sum assertion on `7KR0-6conf` (known 6 coupled groups) — **FAILED as designed on 2026-08-26**: all 169 polymer groups sum to 1.020 (D011), and deposited 7KR0 has 4 under-occupied groups (D012). The detector is validated by a deliberately corrupted control. | `state/checks/G2_occ.json` |
| G3 | R-free reproduction of the deposited model within `max(3σ,0.005)` | `state/checks/G3_rfree.json` |
| G4 | Round-trip: multiconformer model through gemmi → phenix.pdbtools → phenix.refine(0 cycles) → qFit read → chapi read/write; altloc letters + occupancies identical (canonical hash) | `state/checks/G4_roundtrip.json` |
| G5 | Gate sanity: acceptance logic on a shuffled/synthetic ΔR-free set passes some and fails some | `state/checks/G5_gate.json` |
| G6 | Ledger idempotence: re-running a stage writes zero new rows | pytest |
| G7 | Flag guard: attempting `r_free_flags.generate=True` after prep is refused | pytest |
| G8 | Negative control (≥1 target): random waters / random altlocs do not pass acceptance | `changes` rows with `control_*` types |

---

## 15. Reporting

- **Validation report** (per target, HTML+JSON): MolProbity full output, altloc-aware clashscore + invocation, per-residue RSCC, ligand table (RSCC/RSZD/polder), solvent audit, four-way baseline table.
- **Written report** (PDF): built from Markdown + matplotlib figures; every number regenerated from `state/exports/*.csv` by `report/written_report.py` at build time (no hand-typed numbers); results section ordered unfavorable-first; deviations table from `deviations`; DOIs re-resolved via `doi.org` at build time (§14 PROTOCOL). PDF renderer: **verified 2026-08-25 — no `pandoc`, `pdflatex`, `xelatex`, or `weasyprint` on the pod**; the written report is built as Markdown + matplotlib figures and rendered to PDF with matplotlib's `PdfPages` (text pages typeset by matplotlib) unless a renderer is added later (recorded here).
- **Supplement**: `supplement.py` packages archives + ledgers + scripts at frozen version; verifies every referenced path by opening it.

---

## 16. Refinement-pairs dataset (training/exploration corpus)

`datasets/refinement_pairs/<target>/` — `start/{model.cif,data.mtz,flags.mtz,dossier.json}`, `end/{model.cif,maps.mtz,validation.json}`, `trajectory.csv` (cycles rows), `decisions.jsonl` (changes rows with evidence), `commands.jsonl` (every command line with sha256 of inputs/outputs). This is exactly the operator's "starting state and end state for R-reduced samples + prompt and context info": each (start, end, decision log) triple is a supervised example of *what an expert refinement pipeline did and why*, and the rejected candidates are negatives.

---

## 17. Phases and milestones

| Phase | Deliverable | Gate |
|---|---|---|
| P0 (day 1) | Docs (PROTOCOL/SPEC/CLAUDE), pod up, envs installed, data fetched, `autoref` skeleton (config/vocab/hashing/ledger/flags/model/phenix_refine/xtriage/molprobity/rcsb/pdbredo), `autoref fetch/dossier` on 7KR0 | roster rows for phenix.refine/xtriage/molprobity |
| P1 | Gates G0–G7 on 7KR0; noise floor on 7KR0; four-way baselines on 7KR0 | `state/checks/*` |
| P2 | Dossiers + noise floors + baselines for 3TC7, 3QUE, 7KR0-6conf | |
| P3 | Macro-cycles to convergence on all targets; negative controls (G8) on 7KR0 | `cycles`, `changes` |
| P4 | Validation reports, written report, supplement, dataset export | |

---

## 18. Known gaps, substitutions, and risks (disclosed)

1. **REFMAC5 absent** (no CCP4). Cross-check skipped; roster `ABSENT`. Adding CCP4 to SBGrid `titles.conf` is a team decision.
2. **Bandicoot** is macOS-only (Coot 0.9.8 fork) and **cootmcp** is macOS-only (AppleScript screenshots). Substitute: bioconda `coot-headless` (chapi) on Linux; same underlying algorithms (Coot 1.3.3), no GUI. PROTOCOL §13 re-read logged in `state/notes/literature.md`.
3. **CheckMyMetal / TLSMD** are web servers → `phenix.metal_coordination` + gemmi geometry / `phenix.find_tls_groups`.
4. **UnDowser** available as `phenix.undowser_validation` / `mmtbx.undowser2_validation` (both present).
5. **Paired refinement** has no Phenix command → scripted ladder; decision rule per Karplus & Diederichs 2012 (R-work/R-free at the *common* lower resolution must not worsen when higher-res data are included).
6. **Weight optimization** inside `phenix.refine` consults the full free set (not select-only) — counted and disclosed; a select-only weight grid is a v1.x option.
7. **Budget metering** unavailable → UNCALIBRATED only. Slack posting not configured → status files.
8. **cpu-medium** may be slow for 0.77 Å anisotropic 6-conformer refinements (~50 min/run on the operator's machine); the noise floor alone is 10 runs. Escalation: `actl pod up --fresh --profile single` (12 CPU limit) — a compute decision, not a protocol one.
9. **7KR0 numbers, verified from the deposited mmCIF header on the pod (2026-08-25):** deposited R-work/R-free = **0.1099 / 0.1172** (8 711 free, 4.89 %, sigma_F cutoff 1.35 in the depositor's refinement). The operator's 6-conformer model (`refinement examples/`) refines to **0.0492 / 0.0664** on the same data — a ΔR-free of ≈ −0.05, i.e. the local example *is* a start→end pair for §16. PDB-REDO v8.04 (flagged "not up to date"): RFCAL 0.1185, final R-free 0.1233, 8 712 test reflections. 3TC7: header 0.158/0.193 (2 075 free) → PDB-REDO 0.1776. 3QUE: header 0.2225/0.3109 (863 free, sigma_F 0.0) → PDB-REDO 0.2701. All are baselines to *recompute* ourselves (§6 model 3), never quoted as ours.
10. `7KR0-6conf` input's flags come from the operator's MTZ (`test_flag_value=0`, 8709 free); gate G3 must prove identity with the RCSB `-sf.cif` flags before the target is used, otherwise it is excluded (a different test set is not commensurable).

## 19. Exploration track (PROTOCOL §17)

Mechanics for the exploration mandate. Nothing here relaxes §5 (cross-validation) or §14 (gates).

- **Registry.** `state/notes/experiments.md`: one row per exploration, `E<nnn>`, with target, one-paragraph
  rationale written *before* the run, the script, the paired-control location, the result (attributable
  ΔR-free-select, σ multiple, report/full confirmation), which gates it passes and fails, and the deviation
  row that records it. The C-series of 2026-08-28/09-04 (whole-protein qFit as one batch, D424–D439) is
  E001–E009 retroactively.
- **Layout.** `runs/<target>/experiments/<name>/` with `command.txt` (argv + AUTOREF_* env), the candidate model
  and its provenance, `paired/{null_arm,candidate_arm}/` from `paired.run_paired_cycle`, and the gate legs from
  `exp_qfit_whole_gates.py` or its successor under `gates*/`. Scripts live in `scripts/experiments/` and are
  committed; each starts with the rationale as its module docstring.
- **Judging.** The paired cycle (§7, SPEC_LOOP_V2 §1.3) is the only R-free instrument; `model_vs_data` on the
  full set is the cross-check. Legs other than R-free are scored under the thresholds file in force *and*
  under any newer versioned file, both recorded. A candidate that passes all legs under the file in force
  may be promoted as the campaign model through the normal `changes`/`cycles` rows; one that passes only
  under a newer file is promoted only after that file is adopted campaign-wide (§4.5 of PROTOCOL, D442).
- **Ledger.** Experiments write ordinary `changes` and `cycles` rows using the frozen vocabulary where a type
  fits (`protein_altloc_add` for a qFit batch, `weight_change` for a parameterisation, `hydrogens_toggle`,
  `adp_model_change`, `tls_regroup`, …). A representation that has no type (an ensemble) is recorded in the
  registry and a `deviations` row, never in `changes`, so `status.aggregate()` cannot mistake it for a
  single-model result (D427). New vocabulary is added by deviation row (D301 precedent).
- **Compute.** An exploration is time-boxed in its rationale; a running line that has produced no
  attributable change after its box is stopped and the stop recorded. Runs that share the pod's 4 CPUs are
  serialised through the semaphore as usual.
- **Programs and environments.** A new program is brought up like any tool (§4): wrapper with `canary()`, a
  `roster` row, its paper re-read (PROTOCOL §13) before its first production use.


## 20. Connectivity-optimization line (PROTOCOL §18)

Implementation of PROTOCOL §18. First instance: E035 (7KR0), 2026-09-21.

- **Program.** Untangler, github.com/Phoelionix/Untangler, branch `conformational_tree`, pinned commit recorded in
  `runs/<T>/experiments/<name>/PROVENANCE.txt`. Brought up by `scripts/bringup_untangler.sh` (tcsh, gnuplot, clone,
  venv `/home/dev/envs/untangler` on a uv-managed Python 3.12 — the branch uses PEP 701 f-strings that 3.9 rejects — with pulp + bundled CBC). ILP solver: HiGHS via `highspy` (the authors used CPLEX, not installable without an
  IBM licence; PuLP's bundled CBC 2.10.3 and the 2.10.13 release both segfault when the time limit fires on these problems,
  E035 note 7). Every patch to the program goes through `scripts/experiments/untangler_patch.sh`
  and lands as `E035_PATCH.diff` in each arm directory; the patch set is: solver selection (CBC by default, `UNTANGLER_SOLVER=highs`, optional CBC wrapper path), retry and
  incumbent fallback on a solver-process failure, control flags / loop cap / seed / threads / resume loop from environment variables, removal of a `refinement.main.ddr` PHIL block Phenix 2.1-6048 rejects, a float-safe
  weight comparison in `Refine.sh`.
- **Data.** One MTZ per experiment with FP, SIGFP from the frozen `data.mtz` and the inherited `R-free-flags` column from
  `flags.mtz`, built by `scripts/experiments/e035_merge_mtz.py` under `phenix.python`, which asserts n_reflections and
  n_free against `prep.json` and records the file's SHA-256. The wrapper's template carries `r_free_flags.generate=False`,
  `test_flag_value=0` (our inherited convention, free = 0), no cutoffs; audited 2026-09-21.
- **Driver.** `scripts/experiments/exp_untangler_7kr0.sh {setup,base,floor,arms,score}`. `base`: deposited model →
  `ConformationTree/split_qfit_to_6conf.py` → occupancies summed to 1.000 → deposited REMARK 290 restored (untangle.py reads
  symmetry from the input header; phenix strips it) → 20 restrained macro-cycles (wc 0.5, seed 42) = B0. `floor`: seeds 1–5 ×
  10 restrained macro-cycles from B0. `arms`: T (`untangle.py` defaults), C1 (`UNTANGLER_CONTROL=1`), C2 (`UNTANGLER_CONTROL=1
  UNTANGLER_NO_UNRESTRAINED=1`), same B0 and seed, detached with `setsid -f`, `command.txt` per arm.
- **Scoring.** `scripts/experiments/exp_untangler_score.py` (autoref env) scores B0, the floor seeds and every
  `output/<base>_current<k>.pdb` of every arm through `autoref.flags.evaluate(..., consult=False, stage="exp_e035")`, which
  writes the usual `rfree_split` JSON and `jobs` rows and asserts the counts. Cache `scores.json` by SHA-256;
  `trajectory.json`, `result.json`, `TRAJECTORY.md` (per-loop table: T, C1, C2 on select / report / full, ΔT−C1 and ΔT−C2 in
  σ_select, Δgap in σ_gap, endpoints by the pre-registered rule).
- **Ledger.** No `changes` or `cycles` rows (representation without a vocabulary type, §19); `jobs` rows come from the
  evaluator; the result is written to the E-row and a D-row. The thresholds file in force is recorded in the E-row.
- **Layout.** `runs/<T>/experiments/e035_untangler/{PROVENANCE.txt,data/,base/,floor/,arms/{T,C1,C2}/Untangler/,rfree/,
  logs/,scripts/}`; the `scripts/` copy is what ran (SHA-256s in PROVENANCE.txt), the repo copy is the source.
