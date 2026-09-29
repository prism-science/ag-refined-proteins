# Campaign Protocol — Autonomous Crystallographic Refinement

> This is the campaign brief, reproduced verbatim from the operator. **Every agent on this
> campaign carries this document.** `CLAUDE.md` tells you how this repository implements it;
> `SPEC.md` is the implementation spec. Where they disagree, this document wins.

**Addressing:** Every agent on this campaign carries this document. If you are the top-level orchestrator, every obligation here is yours. If you are a sub-agent at any depth, the verification, measurement, safety, and reporting standards here apply to your work, but your authoritative SCOPE is your task brief from your parent: do not independently post to Slack, create Drive deliverables, initiate spending, or cancel any sibling agent or in-flight GPU job you did not start unless your brief explicitly assigns it. Campaign-wide cadences and deliverables are the orchestrator's to satisfy.

## 1. Task

Given an initial atomic model and its experimental structure factors, autonomously produce the model that best explains the data, judged by R-free, without increasing R-gap (the difference between R-work and R-free), and keeping the model geometry within acceptable limits set by PDB deposition. The work consists of alternating real-space and reciprocal-space improvement cycles (see additional details in refinement protocol).

The deliverable is a refined model and a complete decision log of the commands/parameters used to move from the initial model to the final model.

### 1.1 Campaign inputs

The operator supplies a target list. Each entry is one crystallographic dataset:

- Initial model (PDB or mmCIF).
- Structure factors (MTZ or mmCIF-SF), with the intensities or amplitudes actually used for refinement identified by column label.
- FASTA file with input construct (FASTA).
- The R-free flag column, if one exists.
- Resolution, space group, and expected composition (chains, ligands, metals, cofactors) as claimed by the depositor or experimenter.

Targets: `<TARGET_LIST>` (→ `targets/targets.yaml`). Data location: `<DATA_ROOT>` (→ `$AUTOREF_DATA_ROOT`, default `/home/dev/data` on the pod).

### 1.2 The metric

R-free is the primary objective. The program aims to decrease R-free by more than the campaign's measured noise floor (Section 4.4), with no unacceptable degradation in geometry or local density fit (Section 4.5) and without increasing R-gap. R-free is a cross-validation statistic (Brünger 1992, 1993). It is only meaningful under the discipline in Section 3. A campaign that improves R-free by corrupting the test set has produced nothing.

If working in real space, judge each individual change by fit to real-space electron density using real-space correlation coefficients (RSCC), within geometry limits. If the change does not improve RSCC, reverse it and make another change.

## 2. Target dossier (required before any refinement)

Before running a single refinement cycle on a target, produce and record a dossier. Nothing downstream may proceed until it exists at `/state/dossier/{target}.json`.

**Data audit.**
- Space group, unit cell, resolution range, completeness overall and in the high-resolution shell, multiplicity, <I/sigI>, CC1/2 by shell.
- Whether the file contains intensities or amplitudes, and which columns.
- Anisotropy of the diffraction limits.
- Twinning tests (L-test, Britton/H-test, intensity moments) and any translational NCS peaks.
- Wilson B.
- Whether the deposited resolution cutoff is defensible, tested by paired refinement (Karplus & Diederichs 2012). Do not change the cutoff on the basis of R-free alone.

**Model audit.**
- Chains, residue ranges, gaps, sequence agreement with the stated construct from FASTA file. Note any protein residues listed in the FASTA file that are not built into the experimental model.
- **Gap table.** For every discrepancy between the FASTA construct and the built model, record one row: `{chain, first_missing_resnum, last_missing_resnum, sequence_from_fasta, gap_type, anchored_ends, max_mfo_dfc_sigma_in_gap, nearest_symmetry_contact}`. `gap_type` is one of `n_terminal`, `c_terminal`, `internal_loop`, `side_chain_truncated`, `sequence_mismatch`. This table is the input to Section 5.5 and part of the composition hypothesis: state per gap whether you expect it to be buildable.
- Ligands present, with their CCD codes resolved by lookup, not from memory.
- Metals and cofactors, and whether the coordination geometry is chemically plausible (CheckMyMetal or equivalent).
- Existing altlocs: count, altloc letters in use, and whether occupancies within each group sum correctly. Protein and nucleic atoms occupancies should sum to 1, HETATMs sum to =< 1.
- Existing waters: count, B-factor distribution, how many sit in negative difference density, how many have no hydrogen-bond partner.
- NCS copies and whether they diverge.

**Composition hypothesis.** State what you expect to find that is not yet modeled: which regions have unmodeled positive difference density, which side chains show Ringer-style secondary peaks, whether the ligand site shows residual density consistent with a second pose. This is the hypothesis the campaign tests. Record it before you start so that post-hoc rationalization is visible as such.

**Prior baselines.** If the target corresponds to a PDB entry, retrieve the PDB-REDO entry for it and record its R-work, R-free, and validation metrics. That is a baseline you must beat, not a target you must match.

If any fold-level or data-level anomaly appears later (a refinement that will not converge, a gate that passes or fails everything, R-free that moves in the wrong direction consistently), revisit this dossier before blaming the software.

## 3. Cross-validation integrity (non-negotiable)

R-free is the metric, so the test set is the most corruptible object in the campaign. These rules are absolute.

1. **Inherit the flags.** If the input file carries R-free flags, use them unchanged, in the same convention (which value means "free"), for every refinement of that target for the entire campaign. Record the flag column name, the free value, the count of free reflections, and their fraction, in the dossier.
2. **Never regenerate flags mid-campaign.** Regenerating flags after any refinement contaminates the test set through the model. If flags must be generated (none present), generate them once, before any refinement, freeze them, checksum the file, and record the checksum on every downstream row. Use thin resolution shells if NCS is present, otherwise a random selection, and state which.
3. **Never enlarge or shrink the test set** to change its statistics.
4. **Never change the resolution cutoff, the sigma cutoff, or the data selection to move R-free.** A resolution-limit change is a pre-registered paired-refinement decision, reported with both the old and new statistics, and R-free values across different data selections are never compared as if they were commensurable.
5. **No refinement against all data at any point**, not even "one last polish." A single all-data refinement permanently destroys the test set for that target.
6. **Selection/reporting split.** R-free will be consulted hundreds or thousands of times in this campaign, for weight optimization, for accept/reject on every water and every altloc. Used that way, it becomes optimistically biased. Therefore, at the start of each target, partition the free reflections into two halves by a frozen random assignment: R-free-select and R-free-report. All automated accept/reject and weight optimization consult R-free-select only. The headline number reported in every deliverable is R-free computed on R-free-report, plus the standard full-test-set R-free for comparability with the literature. Record both, always, plus the count of R-free-select consultations made for that target. If the two diverge by more than the noise floor, say so and treat it as evidence of selection bias.
7. Where the test set is small (fewer than roughly 500 free reflections), note it and consider k-fold cross-validation as implemented in PDB-REDO rather than trusting a single split.

Any violation of 1 through 6 is a campaign-invalidating defect, not a deviation to be logged and moved past. Halt and escalate.

## 4. Refinement protocol

### 4.1 The macro-cycle

A macrocycle consists of at least one change in real space and one round of local refinement. For each macrocycle, the different parts of the macrocycle should be controlled by different agents, with a real space agent making decisions about anything in real space and a reciprocal space agent making decisions about anything in reciprocal space. There should also be a validator agent to run geometric and other validation scripts.

The controller agent should control all of these agents and determine which agent to run. Every time a change is made in real space, it should be followed by a round of refinement. However, the real space agent can determine if multiple changes should be made before sending it back to the controller agent. The controller agent should determine whether the real- or reciprocal-space agents are making too many changes before sending it back.

Within each sub-agent (real and reciprocal), these agents should determine what can be run. Sub-agents can choose multiple tasks by creating their own sub-agents to test different things, then report back to the controller agent. Agents should track what they have done so that if another model comes back and looks similar, they can potentially use the same commands or tasks.

**Reciprocal-space agent (Phenix phenix.refine, cross-checked against REFMAC5 where useful):**
- Coordinate refinement (individual restrained; rigid-body or torsion-angle only if the starting model is badly placed; simulated annealing only when the model is far from convergence, and never after altlocs are built).
- ADP refinement: isotropic, anisotropic, or grouped, chosen by data-to-parameter ratio and justified in the log. TLS groups where resolution and model size warrant, with group selection derived (TLSMD or equivalent), not guessed.
- Occupancy refinement, with altloc groups constrained to sum correctly (Section 5.3).
- Bulk solvent and overall anisotropic scaling. Evaluate the mosaic bulk-solvent model where the flat mask is a poor fit.
- Riding hydrogens are used in refinement at all resolutions, as part of the standing parameter block (Section 4.7.1). Record whether H atoms are retained in the output. Dropping riding H is a deviation and is reported as one.
- Restraint weights (wxc_scale, wxu_scale) optimized against R-free-select, with the number of trial weights recorded.
- Ramachandran, secondary-structure, and reference-model restraints only where resolution justifies them, and disclosed when used, because they inject prior information into the very geometry you later validate.
- Ordered solvent parameters, including alternative location and/or partial occupancy water molecules

**Real-space stage** (Bandicoot / Coot):
- use Coot as much as possible.
- Start at the highest positive difference peak. Every peak above the action threshold of 4 sigma in mFo-DFc is triaged as misplaced backbone, side chain, water, ion, ligand, unmodeled, alternate conformation, or unexplained. The action threshold is a single campaign-wide number: 4 sigma positive, minus 4 sigma negative.
- Coot real space tools can operate on a zone, and it is often advantageous to attempt real space changes in a multi-residue stretch. Use this when multiple regions with different densities are close together.
- You can take a multi-residue stretch and split it at the backbone.
- Density thresholds governing what may be placed, and at what occupancy, are those in Section 5.1. They are not restated here.
- Rotamer and peptide-flip correction: Asn/Gln/His flips from MolProbity/Reduce were applied and then re-idealized.
- Multiconformer building with qFit (protein) and qFit-ligand (ligands) can be useful initially to get a lot of diversity; check for local fit to density before and after qFit manual and remove poor-fitting conformations.
- Water placement and pruning (Section 5.1).
- Local real-space refinement of multi-residue zones with Coot's *refine zone* alternated with *regularize zone* against the sigma-A weighted map, map weight and restraint switches recorded per change; `phenix.real_space_refine` (or the mmtbx selection-only refinement) is the fallback where local geometry needs repair without a full reciprocal pass. Coot's real-space tools take a zone, not only a residue, and a strained or mis-traced segment is a stretch.
- The Coot–refinement alternation is the default loop, not an escape rung: real-space change → restricted paired
  refinement of that change → next change, a full paired cycle after about five kept changes, then the loop resumes from
  the new base and continues while changes are being kept. The size of a change is not a criterion. A water shift, a
  single rotamer, a peptide flip, a partial-occupancy adjustment or a one-residue altloc is proposed and judged exactly
  like a multi-residue rebuild; only the paired verdict decides. When the peaks above the action threshold are used up,
  continue with the triage list at 3 sigma and then with residue-level evidence that carries no peak height at all:
  RSCC outliers, Ringer secondary peaks, rotamer and Ramachandran outliers, UnDowser and clash flags, waters the two
  pickers disagree on. Running out of large peaks is not running out of work.
- After each Coot change, reciprocal-space refinement restricted to the modified residue(s) — `refinement.refine.sites.individual=<selection>` with the ADP and occupancy selections to match, TLS off, 6–10 macro-cycles at the standing weights — paired against the same restricted refinement of the unchanged base. Restricting the moving atoms stops the rest of the model from absorbing noise while one residue is judged (phenix.refine's early macro-cycles otherwise move everything), so a good local change is not rejected for damage done elsewhere. A change whose attributable ΔR-free-select is worse than the noise bound is dropped before it can hide in a batch; after about five kept changes, one full refinement of the whole structure (the paired cycle) credits or reverts the batch, and the solvent stage's water round follows.

The stage order matters and is fixed: build altlocs before final water picking, and re-examine waters after every altloc addition. Placing water into density that belongs to an unmodeled alternate conformation is the single most common way to make a model worse while making R-free look better in the short term.

### 4.2 Cycle ordering across the campaign

The order is the frozen ladder of Section 4.7. In summary, for each target:

1. Acquire the deposited model, the structure factors, and the PDB-REDO entry; complete the dossier (L1).
2. Baseline re-refinement of the input model with no manual model changes, to establish R-work and R-free on your own pipeline and to separate "the model improved" from "the refinement program changed" (L2). Automated ordered solvent runs during this refinement, so the baseline is not change-free; see the note in Section 6.
3. qFit at defaults, then the qFit refinement protocol to the occupancy floor (L3–L4).
4. Real-space pass 1 (L5): chain completion against the FASTA gap table first (Section 5.5), then positive peaks in descending order, then the negative-density stage.
5. Re-refinement in both solvent forms, and selection between them on R-free-select (L6–L7).
6. Real-space pass 2 (L8).
7. Late parameterisation (L9–L10): anisotropic ADPs once the R-free trigger is reached, then partial-occupancy waters and TLS.

Steps 4 through 6 are re-entered, not run once, until the convergence criterion of Section 4.6 is met. Every re-entry that produces no accepted change is recorded as such.

### 4.3 What "accepted" means

A model change is accepted only when all hold:
- ΔR-free-select, from the restricted paired comparison of §4.1, exceeds the frozen quantile of that change class's acceptance null (§4.4b) under the current null measurement, and survives the target's BH correction.
- The change is locally supported: the added or altered atoms have density support at the recorded threshold (real-space correlation coefficient, RSZD, or polder/omit-map density at a stated sigma level).
- Geometry does not degrade beyond tolerance (Section 4.5).
- The change does not introduce altloc-aware clashes (Section 5.4).

A change that lowers R-free while failing any of the others is rejected and logged with its numbers. Report how many such cases occurred; a high count is itself a finding about R-free as an objective.

### 4.4 The noise floor (measure it, do not assume it)

Two quantities are measured per target. They are not interchangeable, and neither substitutes for the other.

(a) σ_abs — absolute run-to-run variability. Re-run the identical refinement N ≥ 10 times with different random seeds from identical input; record the SD of R-free. σ_abs governs the convergence test (§4.6), the error bar on the headline R-free-report, and the band drawn in the trajectory figure (§11.6). We take σ_gap from the same seed set. σ_abs is not an acceptance criterion for model changes; any accept/reject comparison made against it is a defect.

(b) The acceptance null — per target, per change class. For each change_type token that adds or moves atoms, generate N_sham ≥ 50 sham instances with no density support: waters at random positions with no mFo-DFc peak, alternate conformations at residues with no Ringer secondary peak, peptide flips at residues with no residual, zone shifts into flat density. Run every sham instance through the identical restricted paired protocol of §4.1 — same selection syntax, same macro-cycle count, same standing weights, weight optimization off in both arms, same base model — and record ΔR-free-select. That distribution is the null for that class on that target.

The accept threshold for a class is a frozen upper-tail quantile of its null, default the 99th percentile. Record the class, N_sham, the quantile used, and the resulting threshold value.

All null measurements are on R-free-select only. σ scales as ~1/√N_free; a null measured on the full test set reads roughly √2 looser than the gate it is standing in for.

Re-measurement points. The null does not transfer across parameter counts. Measure at L2, re-measure after L4, after the first full solvent rebuild, and after any parameterization change adopted at L9 or L10. Each measurement carries an id NULL-<target>-<step>-<n>, and every per-change row records the id it was judged against.

Multiplicity. Each candidate's ΔR-free-select converts to an empirical p-value against its class null. Apply Benjamini–Hochberg across all accept/reject decisions for the target at a frozen FDR (default 0.05). Report per target: number of decisions, BH threshold, expected false accepts. Where Δ falls beyond the sham range, report p < 1/N_sham; do not interpolate a tail.

Frozen weights. optimize_xyz_weight and optimize_adp_weight are false in both arms of every restricted paired comparison. Weight optimisation happens only at the full paired cycle, and each trial weight counts as one R-free-select consultation (§3.6).

If you also compute an analytic estimate from test-set size, report it alongside the measured null and report the discrepancy. Do not substitute it.

### 4.5 Geometry and validation tolerances

Run MolProbity on every candidate model.
- Clashscore (altloc-aware; see 5.4).
- Ramachandran outliers and favored fraction.
- Rotamer outliers.
- Bond-length and bond-angle RMSD from restraint targets.
- Cis-nonPro peptide count and twisted peptides.
- CaBLAM outliers where resolution is low.
- Per-residue real-space fit outliers.

A change that improves R-free while pushing any of these past tolerance is rejected. State the tolerances numerically in the report. Do not adjust them after seeing results; if you do adjust them, say so and report how many configurations you tried.

### 4.6 Convergence and stopping

A target is converged when three consecutive full macro-cycles produce no accepted change and ΔR-free over those cycles stays inside the noise floor. Record the final R-work, R-free (report half and full test set), R-free minus R-work gap, and all validation metrics.

The R-free minus R-work gap is monitored continuously. A gap that widens while R-free falls is a warning that the model is absorbing noise; investigate before continuing. Measured form (D476, 2026-09-07): on every paired cycle, Δgap = gap(candidate arm) − gap(null arm), judged against σ_gap, the standard deviation of the gap over the noise-floor seeds; a cycle whose R-free-select improved while Δgap > k·σ_gap is flagged `overfit_suspect` on its `cycles` row and in a `GAP-<target>-c<N>` deviations row. A small R-free gain is never quoted without its Δgap.

**No standing number is a ceiling (operator instruction, 2026-09-28).** The deliverable tables in the README, the
`state/current` records and the campaign-state notes in `CLAUDE.md` record what has been reached; they are not targets
and never a reason to stop. A note that a *line* is "at its floor" or "exhausted" (a qFit batch, a solvent stage, a
parameterisation) closes that line, not the target. A target's work ends only by the convergence rule above, by a
budget or a Section 17 time box, or by a Section 3 / Section 12 halt. When a run reaches or passes a recorded number,
it keeps going. When the discrete driver stops a run (cycle cap, escape ladder exhausted, convergence), that ends the
run, not the target: the next action is a new line under Section 17, not a report that the target is finished. The
precedent: on 2026-09-28 a session that kept alternating Coot changes with refinement on 3TC7 took R-free to 0.1583
against a standing record of 0.1728 (operator's number, to be verified on the frozen flags per Section 8 before the
table moves).

### 4.7 The frozen ladder

This is the reference sequence. Section 17 governs departures from it. The ladder is a floor, not a ceiling. Every step remains subject to Sections 3, 4.3, 4.4, and 4.5. A step that lowers R-free while failing an acceptance condition is rejected, not kept.

**L1. Acquire.** Retrieve the deposited model and structure factors, and the PDB-REDO entry for the same accession. The PDB-REDO model is baseline 3 of Section 6. All accessions are resolved by lookup, never from memory (Section 12). Complete the dossier of Section 2 before any refinement.

**L2. Baseline refinement.** Refine the input model with no manual model changes, using the standing parameter block below in its **baseline form**. This is step 2 of Section 4.2 and baseline 2 of Section 6. Measure σ_abs and the initial acceptance nulls here (§4.4). No candidate is scored before both exist.

**L3. qFit at defaults.** Run qFit on the L2 output. Defaults only. Departures from defaults are E-numbered explorations under Section 17.

**L4. qFit refinement script.** Run the qFit refinement protocol to convergence of the occupancy floor (Section 5.2). Guardrail: if R-free rises by more than 0.05 against L2, halt the target and escalate. This is an abort trigger, not an acceptance test. Acceptance is governed by Section 4.3 against the measured noise floor of Section 4.4. Re-measure the acceptance nulls against the L4 output before entering L5.

**L5. Real-space pass 1 (Coot / Bandicoot).**

*Stage 1 — chain completion.* Work the gap table of Section 2 before the peak list, under Section 5.5. A built loop or extension changes the difference map everywhere nearby, so peak triage done first would be repeated. Complete truncated side chains, then terminal extensions, then internal loops. Re-measure the acceptance nulls if the build changed the atom count materially, then recompute maps before stage 2.

*Stage 2 — peak triage.* Work the difference map in descending peak order.

- Start at the highest positive mFo-DFc peak.
- If the peak is large and extended, test whether the backbone and side chains of several consecutive residues need splitting and refitting. Operate on the zone, not the residue (Section 4.1).
- Identify the nearest residues. If the density sits at a side chain, fit an additional side-chain alternate conformation and test whether the residual density is resolved.
- If the density sits at backbone atoms, test a peptide flip.
- If the density is remote from the model or isotropic in shape, place a water. Solvent placement follows Section 5.1, including the two-picker combination rule.
- After every move, perform real-space, local refinement. 
- Judge every individual change by real-space correlation within geometry limits (Section 1.2). Revert changes that do not improve RSCC, then try a different approach.
- Work all positive peaks above the action threshold (4 sigma).
- Then work negative peaks below minus 4 sigma:
  - Delete waters sitting in negative density.
  - Remove alternate conformations sitting in negative density.
  - Test whether a negative peak adjacent to a positive peak indicates that the local model should be shifted into the positive density. Record as `zone_shift`.

Follow every change with restricted reciprocal-space refinement against the paired unchanged base, per Section 4.1.

**L6. Re-refinement, altloc-solvent form.** Refine with the standing parameter block in variant B (partial-occupancy and altloc-aware waters enabled).

**L7. Re-refinement, plain-solvent form.** Refine the same input with variant A (no altloc-aware or partial-occupancy waters). Select between the L6 and L7 models on R-free-select, not on full-set R-free, and count the consultation (Section 3.6). Record both models, both R-free values, and the geometry and clash metrics of each. Report the selection in the decision log as `solvent_model_select`.

**L8. Real-space pass 2.** Work the selected model's difference map in descending peak order:

- Start at the highest positive mFo-DFc peak.
- Identify the nearest residues. If the density sits at a side chain, fit an additional side-chain alternate conformation and test whether the residual density is resolved.
- If the density sits at backbone atoms, test a peptide flip.
- If the density is remote from the model or isotropic in shape, place a water, under Section 5.1.
- Work all positive peaks above the action threshold (4 sigma).

L8 is deliberately narrower than L5: no zone-scale splitting and no negative-density stage. The negative-density stage returns on the next re-entry of L5.

**L9. Anisotropic ADPs.** R-free below 0.18 is the trigger to refine with anisotropic B-factors. Record the data-to-parameter ratio before the switch (Section 4.1), and run the switch as a paired cycle so that both arms are on record. Any adopted parameterisation change invalidates the standing nulls; re-measure before the next real-space pass.

**L10. Late parameterisation.** Once the major difference density is addressed, test in this order, each as a paired null: partial-occupancy waters (where not already selected at L7), and TLS groups with the group selection derived rather than guessed (Section 4.1).

Re-enter L5 through L8 until the convergence criterion of Section 4.6 is met.

#### 4.7.1 Standing parameter block

Filenames are cycle-indexed by the ledger of Section 7. Literal serial names such as `${pdb_name}_002.pdb` are not used, because L6, L7 and L9 each consume the output of the preceding step, not the deposited model.

Solvent keywords are written in their `ordered_solvent.*` scope. Riding hydrogens are on at every resolution.

**Baseline form (L2).**

```bash
phenix.refine \
  "${model_in}" "${data_mtz}" \
  refine.strategy="*individual_sites *individual_adp *occupancies" \
  refinement.main.number_of_macro_cycles=5 \
  refinement.hydrogens.refine=riding \
  refinement.main.ordered_solvent=True \
  ordered_solvent.mode=every_macro_cycle \
  ordered_solvent.include_altlocs=True \
  ordered_solvent.dist_min=2.0 \
  refinement.target_weights.optimize_xyz_weight=true \
  refinement.target_weights.optimize_adp_weight=true \
  refinement.main.random_seed="${seed}" \
  output.prefix="${target}" output.serial="${cycle}"
```

**Variant B (altloc-aware, partially occupied solvent) — used at L6.** The baseline form plus:

```bash
  ordered_solvent.dist_min_altloc=0.03 \
  ordered_solvent.occupancy_min=0.2 \
  ordered_solvent.occupancy=0.33
```

**Variant A (plain solvent) — used at L7.** The baseline form with `ordered_solvent.include_altlocs` and `ordered_solvent.dist_min` removed, so solvent picking runs at Phenix defaults:

```bash
phenix.refine \
  "${model_in}" "${data_mtz}" \
  refine.strategy="*individual_sites *individual_adp *occupancies" \
  refinement.main.number_of_macro_cycles=5 \
  refinement.hydrogens.refine=riding \
  refinement.main.ordered_solvent=True \
  ordered_solvent.mode=every_macro_cycle \
  refinement.target_weights.optimize_xyz_weight=true \
  refinement.target_weights.optimize_adp_weight=true \
  refinement.main.random_seed="${seed}" \
  output.prefix="${target}" output.serial="${cycle}"
```

Every deviation from these three forms is an E-numbered exploration under Section 17, including any change to `dist_min`, to the occupancy parameters, or to the hydrogen model.

## 5. Model building rules

### 5.1 Ordered solvent: Coot and Phenix in combination

Neither program alone is sufficient. Use both, and use each for what it does best.

**Phenix side** (`phenix.refine ordered_solvent`, `phenix.douse`) controlled by the reciprocal space agent:
- Automated peak picking with explicit, frozen criteria: minimum mFo-DFc peak height for placement, minimum 2mFo-DFc density for retention, B-factor ceiling, and permitted distance ranges to donors and acceptors. The minimum distance to the macromolecule is `dist_min=2.0` in the baseline and variant B forms, and the Phenix default in variant A; record which form produced each water.
- Automated removal of waters that fall below the retention criteria after refinement.
- Occupancy and B refinement for the solvent set.
- Use optionality for alternative conformations of water molecules
- Record the placement and retention thresholds on every water; they are part of the provenance.

**Coot side** controlled by the real space agent:
- Find Waters on the difference map as an independent picker, then Check/Delete Waters with the density, distance, and B-factor filters, to catch what the automated pass placed badly.
- Only add a full occupancy (1.0) water molecule if 2mFo-DFc is 3 sigma or above.
- Do not add a water if 2mFo-DFc is below 0.5 sigma.
- Test if partial occupancy water improves the fit to experimental data.
- Visual and scripted triage of every water that the two pickers disagree about. Disagreement between Coot and Phenix on a site is a signal, not noise: it usually means the site is an ion, a partially occupied altloc, a ligand fragment, or an artifact.
- Coot's hydrogen-bond geometry check for waters with no plausible partner.

**Combination rule.** A water is placed only if at least one picker finds it and it survives the other's retention criteria. Every water that one picker places and the other rejects is recorded in a `solvent_disagreements` table with the resolution of the disagreement and the evidence used.

Additional solvent discipline:
- Run UnDowser (MolProbity) to flag waters that are chemically implausible as water: clashing waters, waters in hydrophobic pockets, waters with impossible coordination. These are candidate ions, alternate conformations, or unmodeled ligand atoms. Reassign, do not just delete.
- Waters may be modeled as partially occupied and, where the density warrants, labeled with altlocs. A water that hydrogen-bonds only to conformer A of a residue takes altloc A and that conformer's occupancy. Do not model a full-occupancy water against a partial-occupancy partner.
- The solvent occupancy floor is 0.2, matching `ordered_solvent.occupancy_min` in variant B. Waters refining below it are removed. (This floor is for solvent only; the protein alternate-conformation floor in Section 5.2 is 0.10.)
- Ion assignment must be justified by coordination number, geometry, distances, B-factor consistency with neighbors, and, where available, anomalous difference density. Never assign an ion on peak height alone.
- Record, per cycle, the count of waters added, removed, reassigned to ions, and converted to altloc-tagged waters.

### 5.2 Protein alternate conformations

- **Detect first.** Run Ringer-style electron-density sampling around side-chain dihedrals to identify residues with secondary density peaks below the conventional 1 sigma contour. Record the list before building. This gives an independent expectation against which qFit's output is checked.
- **Build with qFit.** qFit takes the refined single-conformer model and the map and generates parsimonious multiconformer models, selecting conformations with BIC and sampling B-factors. Use it as the primary builder for protein altlocs; use Coot for the cases it misses or gets wrong.
- If there are no altlocs for a protein atom, there should be no alt-loc label.
- **Build segments, not residues.** Backbone heterogeneity is coupled: if residue i has two backbone conformations, residue i+1 usually does too. Altloc letters must be consistent along the connected segment so that conformer A of residue i is chemically continuous with conformer A of residue i+1. Isolated per-residue altlocs that break backbone continuity are a modeling error.
- **Occupancy floor.** After occupancy refinement, remove conformations below the frozen occupancy floor (default 0.10, per the qFit refinement protocol) and re-refine. Iterate until the model is stable with no conformation below the floor.
- **Validate each addition.** Each alternate conformation must be supported by density that was present before it was built (positive mFo-DFc in the region) and absent after (no residual). Record the before and after difference density for each.
- Report the count of alternate conformations added, their occupancy distribution, and the fraction of Ringer-predicted sites that qFit actually built.

### 5.3 Ligand alternate conformations

- **Restraints first.** Generate a restraint dictionary for every ligand with a license-cleared generator, from the correct chemistry, and inspect it. Do not inherit a restraint file of unknown provenance. Record the generator, its version, and the SMILES or CCD code used, resolved by lookup.
- Build with qFit-ligand for alternate poses and internal conformers, including macrocycles and fragments where relevant.
- **Validate with polder maps.** A standard omit map lets the flat bulk-solvent mask flood the omitted region and obscure weak ligand density. Polder maps exclude bulk solvent from the omit region and are the correct tool for judging whether a second ligand conformer is real. Compute a polder map for every ligand and every ligand alternate conformer, and record the density level.
- Record per-ligand RSCC, RSZD, real-space R, occupancy, and B-factors relative to the surrounding protein. A ligand whose B-factors are far above its environment is weakly supported regardless of what R-free says.
- Where the density is genuinely ambiguous between "one conformer plus water" and "two partially occupied conformers," report it as ambiguous. Do not pick the option that lowers R-free and present it as resolved.
- Ligand altlocs and protein altlocs in the binding site must be assigned consistently: if the ligand's conformer A is only compatible with the side-chain conformer A of a contacting residue, the labels must reflect that.

### 5.4 Clash detection with altlocs (read this twice)

Altloc-naive clash detection is the most common source of false failures and false passes in multiconformer models. The rules:

1. **Atoms in different altlocs of the same alternate-conformation group never clash with each other.** Conformer A and conformer B of the same residue are alternative states of the same molecule; they are never simultaneously present. Any clash routine that counts A-versus-B contacts within a group produces garbage.
2. **Blank altloc is shared.** An atom with an empty altloc label is present in every alternate state and must be checked against A, against B, and against every other letter.
3. **Same-letter across residues is a real clash.** Conformer A of residue i and conformer A of residue j are simultaneously present and must not clash.
4. **Cross-letter across residues requires care.** Whether conformer A of residue i coexists with conformer B of residue j depends on whether the two residues are in the same coupled altloc network. Within a coupled segment, the letters are correlated and A-with-B is not a real state. Across independent networks, the letters are not correlated and all combinations occur. The clash routine must know which networks exist. Build the network graph explicitly from the model (connectivity plus shared occupancy groups) and record it.
5. **Occupancy-weighted severity.** A clash between two conformers each at 0.15 occupancy is not equivalent to a full-occupancy clash. Record raw and occupancy-weighted clash counts.
6. **Waters and ligands inherit these rules.** An altloc-tagged water is checked only against compatible conformers.
7. Use tools that implement this correctly and verify that they do. Reduce and Probe (via MolProbity) handle alternate conformations, but the specific invocation matters. Before trusting any clash number in this campaign, construct a small test case with a known coupled two-conformer segment, run the tool, and confirm the reported clash count matches hand analysis. A clash routine that has not been tested this way is not validated.
8. **Occupancy sums.** Within each alternate-conformation group, occupancies sum to the group total (1.0 for a fully occupied group). Assert this on every model written. A group summing to 1.3 is a bug that will silently distort R-free.

Report clashscore computed with altloc-aware logic, and state which tool and invocation produced it.

### 5.5 Building missing residues

The construct is known. The model is what someone managed to build from the density. Where the two disagree, there is either unmodeled protein or genuine disorder, and the difference map tells you which.

**Where the work comes from.** The gap table of Section 2 is the work list. Nothing is built that does not appear on it, and nothing is built from a sequence held in memory: the residue identity and numbering come from the FASTA file, read in the session that does the building. Check the numbering convention before the first residue goes in — deposited author numbering, SEQRES numbering, and construct numbering frequently differ, and a correctly built loop with the wrong residue numbers is a defect that propagates into every downstream ledger row.

**The trigger is density, not absence.** A gap is a candidate only when there is positive mFo-DFc density at or adjacent to it, connected to an anchored terminus. Unmodeled residues with no residual density are disordered; they stay unmodeled and are reported as such. Do not build into flat density to make the model match the construct. Record per gap: built, or not built with the maximum sigma observed.

Before building at a gap, check two things that masquerade as unmodeled protein:
- **Symmetry.** Density near a chain break may belong to a symmetry mate or a crystal contact. Display symmetry copies before interpreting it.
- **Waters.** Automated solvent picking will have placed waters into main-chain density at gap edges. Remove them before building and re-examine the region afterwards, per the stage-order rule of Section 4.1.

**Order of attack, easiest evidence first.**

1. **Truncated side chains** (`side_chain_complete`). Residues present as backbone or CB stubs with side-chain density available. Cheapest and most common. Complete with Coot's rotamer fitting, judged on RSCC and on whether the residual clears.
2. **Terminal extension** (`terminal_extend`). One anchored end, building outward. Add one residue at a time with Coot's *Add Terminal Residue*, real-space refine the new zone, and stop at the first residue whose density will not support it. Chain termini are usually mobile: expect to stop early, and say where you stopped.
3. **Internal loops** (`loop_build`). Both ends anchored, so the geometry is constrained and the failure mode is register rather than placement. Use Coot's loop fitting (database or Ramachandran search) to generate candidates, then fit side chains and check register. Close the loop against both anchors; a loop that only joins at one end has not been built.

**Register is the failure mode that matters.** A loop can be built with excellent backbone density fit and the sequence off by one or more residues, which is worse than leaving the gap empty because it looks finished. Confirm register on side-chain evidence, not backbone: the large and distinctive side chains in the missing stretch (Trp, Tyr, Phe, Arg, Met) must have density where the register puts them. If the register cannot be confirmed, build the backbone as UNK or as a stub rather than asserting a sequence, and record `register_confirmed: false` on the row. Report the count of such stretches in the validation report; do not quietly assign a sequence and let R-free arbitrate.

**Prediction models are proposers only.** OpenFold, Boltz-2 or an equivalent may propose a loop conformation, and PLACER may propose placements. A predicted conformation is a starting model for real-space fitting, never evidence that the loop is there. This is the Section 17 rule and it is not relaxed here.

**Acceptance.** Built residues go through Section 4.3 like any other change, with these additions:

- The new atoms must have 2mFo-DFc main-chain density at a stated sigma level, positive mFo-DFc before the build, and no residual after.
- Per-residue RSCC and RSZD are recorded for every built residue individually, not averaged over the stretch. One well-fitting residue does not carry four that do not.
- Refined B-factors of the built stretch are compared with the neighbouring anchored residues. A loop refining far above its environment is weakly supported regardless of what R-free does.
- New backbone is checked for Ramachandran and CaBLAM outliers specifically, because loop building is where they appear.
- A built stretch that fails on RSCC, B-factor, or geometry is removed, not kept because global R-free improved. Removal is logged as `residue_unbuild` with its numbers.

**Null classes and parameter count.** Building adds atoms, often many, so two things follow. First, each build class carries its own acceptance null under Section 4.4(b): the sham is a stretch of the same length built into a gap or region with no positive difference density, run through the identical restricted paired protocol. `loop_build` and `side_chain_complete` are separate classes; their nulls are not interchangeable, because a six-residue loop and a single side chain do not add comparable parameters. Second, a substantial build changes the data-to-parameter ratio, so the standing nulls are re-measured after chain completion, exactly as after L4.

**Judging the stretch, not the model.** A six-residue loop in a 200-residue protein moves global R-free very little even when correct. The restricted paired comparison of Section 4.1 is therefore the primary test, with the selection covering the built residues and their anchors; the full paired cycle credits or reverts the batch. Do not reject a build on global R-free alone, and do not accept one on it either.

**Ledger.** One per-change row per contiguous built stretch, with `change_type` from the vocabulary in Section 7, plus `{gap_id, residues_built, register_confirmed, evidence_metric, evidence_value, mean_b_built, mean_b_anchor, rama_outliers_new, cablam_outliers_new}`. Gaps considered and not built get a row too, with the reason and the observed sigma.

## 6. Baselines and controls

Every target reports against four models, all refined and validated by your own pipeline:
1. Input model, as deposited or as supplied, statistics recomputed by you (not quoted from the header).
2. Input model, re-refined with the standing baseline form, no manual model changes. Isolates the effect of the refinement program and version from the effect of your building. Note that automated ordered solvent is active in this refinement, so this baseline includes water addition and removal; it is a baseline for *your building decisions*, not a change-free refinement. Record the water delta against model 1.
3. PDB-REDO model for the same entry, where one exists.
4. Your final model.

An improvement over (1) that is not also an improvement over (2) and (3) is a software-version artifact, not a result, and must be reported as such.

**Negative controls**. The sham sets of §4.4(b) are the negative controls. They are run on every target and for every change class in use, not once on one target. Report per class: N_sham, median and 99th-percentile ΔR-free-select, and the fraction of sham changes that the frozen threshold would have accepted. That fraction is the measured false-accept rate of the acceptance rule and is reported in §11.6 whether or not it is flattering.

## 7. Provenance, logging, and reproducibility

Nothing is discarded. If it was computed, it is saved.

**Per-cycle record** (one row per target per macro-cycle, in a durable ledger):
`{target, cycle_index, stage, r_work, r_free_full, r_free_select, r_free_report, r_gap, n_waters, n_protein_altlocs, n_ligand_altlocs, n_atoms, clashscore_altloc_aware, rama_outliers, rota_outliers, bond_rmsd, angle_rmsd, mean_b, ksol, bsol, accepted_changes, rejected_changes, wall_clock_s, program_versions, input_model_sha256, output_model_sha256, mtz_sha256, rfree_flag_sha256}`

**Per-change record** (one row per accepted or rejected model change):
`{target, cycle_index, change_type, selection, evidence_metric, evidence_value, delta_r_free_select, verdict, reason, null_class, null_measurement_id, n_sham, null_quantile, threshold_value, p_empirical, q_value, weights_frozen}`

`change_type` is a token from a frozen vocabulary (`water_add`, `water_remove`, `water_to_ion`, `protein_altloc_add`, `protein_altloc_prune`, `ligand_altloc_add`, `rotamer_fix`, `peptide_flip`, `flip_correction`, `occupancy_regroup`, `zone_shift`, `backbone_split`, `side_chain_complete`, `terminal_extend`, `loop_build`, `residue_unbuild`, `sequence_register_fix`, `solvent_model_select` and so on). Not free text.

**Artifacts retained per cycle:** input and output coordinate files, the MTZ with map coefficients, the refinement log, the validation output, the difference-map peak list, and the exact command line with all parameters. Package one archive per target per cycle rather than one file per object.

**Script versioning.** Pipeline scripts are version-stamped and frozen once production begins. Changes ship as new versioned copies. The script version and every frozen threshold appear on each row.

**Idempotence.** Bookkeeping writes are idempotent on `(target, cycle_index, stage)` so that re-runs cannot double-count.

## 8. Verification discipline

Before relying on any tool, install it and validate it end to end on a real target from this campaign, at representative size, producing the exact output you will consume downstream. Record `{tool, version, status, image_id, wall_clock_s, output_shape, validated_at}` to a shared roster ledger. A roster row is PASS only when the tool builds, runs, exits zero, and its output parses and is consumed successfully by the next stage.

Specific checks that must be run and whose output must be saved:
- The clash-routine altloc test case in 5.4(7).
- An occupancy-sum assertion on a model with known coupled altlocs.
- Confirmation that your R-free flag handling reproduces the depositor's R-free on the deposited model to within the noise floor. If you cannot reproduce the published R-free from the published model and data, you do not yet understand the data file, and no refinement result from that target is trustworthy. Diagnose before proceeding.
- A round-trip test: write a multiconformer model, read it back, confirm altloc labels and occupancies survive unchanged through every program in the pipeline. Silent altloc mangling on file round-trip is a known class of failure.

Treat anomalies as bugs until investigated: an R-free of exactly zero, a gate that passes or fails everything, a validation metric that never moves, an impossible runtime, a water count that changes when nothing else did.

Before committing significant compute to a plan, run the cheapest check that could falsify it.

## 9. Delegation and parallelism

Delegate aggressively. Suggested decomposition:
- One sub-agent per (target × stage) cell for production work. Targets are independent; run them in parallel. Within a stage, the controller / real-space / reciprocal-space / validator split of Section 4.1 applies.
- TOOL-BRINGUP agents, one per tool (Phenix, Coot in headless/scripted mode, qFit, qFit-ligand, MolProbity/Reduce/Probe, restraint generator, Ringer, REFMAC5 if used, validation tooling). Each writes a working `run_<tool>.py` into shared state and proves it on a canary before any production dispatch.
- Standing singletons: a CLOCK agent, a BUDGET agent, a WATCHDOG, and a SCRIBE that owns all reported numbers. Each runs an internal loop, writes a liveness file every cycle, and never returns between cycles. The orchestrator re-dispatches any singleton whose liveness file is stale by more than two of its cycles.
- One monitor per ten live jobs, scaled down as jobs complete.
- Adversarial reviewers. At least one reviewer that re-runs refinements from raw inputs and generates independent numbers, and at least one that forms its verdict from the raw ledgers and artifacts without seeing your conclusions. Every review finding ships with the exact query or script that produced each number.

The orchestrator retains: cadence, dispatch policy, and the frozen thresholds. It does not do production refinement in its own frame. Orchestrator-frame token cost exceeding one third of campaign total after the first hour is an architecture failure.

Post the delegation architecture within the first hour: how many agents, what each owns end to end, what the orchestrator retains.

## 10. Compute and budget

Refinement is CPU-bound, not GPU-bound. Phenix and Coot workloads parallelize across cores; qFit parallelizes across residues. Size instances accordingly and do not provision GPUs for work that will not use them.

Concurrency is governed by a single campaign-wide integer with a small, named set of authorized writers. Enforcement is at the submitter, mechanically, not by convention.

Every dispatch path appends to a job-metadata ledger immediately after authorization. A dispatch path that cannot append does not dispatch.

The metered figure from the provider, scoped to this campaign's own account object, is the only canonical spend. A rate-card reconstruction is a cross-check and may be used to pause dispatch, never to raise a limit.

Report spend against pace in every status block, with an explicit basis tag (METERED or UNCALIBRATED). An uncalibrated reading never carries a pace adjective.

Budget: `<BUDGET>`. Land within ±10 percent. Under-spend is a planning failure to be explained, not a saving.

Watch every long-running job for liveness and progress. A job alive but producing nothing is a failure in progress: fix and relaunch.

## 11. Deliverables

### 11.1 Per-target refined model
Final model in mmCIF, with:
- Correct altloc labels and occupancy groups, assertion-checked.
- Anisotropic or isotropic ADPs and TLS records as applicable, with the convention documented.
- Hydrogens present or absent as stated, with the choice justified.
- A header or accompanying metadata block recording R-work, R-free (report half and full), test-set size and fraction, resolution range, and the flag file checksum.

### 11.2 Maps
MTZ with F, SIGF, the inherited R-free flags, refined phases, 2mFo-DFc and mFo-DFc coefficients, plus the polder maps computed for ligands and ligand alternate conformers.

### 11.3 Refinement trajectory table
One CSV per campaign, the per-cycle record of Section 7, with every column a real computed number. No sentinels. A value that cannot be computed is a defect to remediate, tracked with `{target, column, reason, owning_frame}`.

### 11.4 Decision log
The per-change record of Section 7. Every added water, every altloc, every rejected candidate, with its evidence and its ΔR-free. This is the artifact that distinguishes a refined model from a model that was fitted to R-free.

### 11.5 Validation report
Per target: MolProbity full output, altloc-aware clashscore with the tool invocation recorded, per-residue real-space fit statistics, ligand validation (RSCC, RSZD, polder density), solvent audit (count, B distribution, UnDowser flags, ions assigned and why), and the four-way baseline comparison of Section 6.

### 11.6 Written report
Publication-quality PDF with:
- Methods sufficient to reproduce the pipeline exactly, including every frozen threshold.
- The R-free trajectory per target, with the noise floor drawn on it.
- The negative-control results from Section 6.
- A results section that leads with the unfavorable reading. Targets where R-free did not improve, or improved only within noise, or improved while geometry degraded, appear first. Ambiguous ligand density is reported as ambiguous.
- Explicit disclosure of every deviation from this protocol, every threshold adjusted after seeing results, and how many configurations were tried.
- Every quantitative claim in the abstract and results regenerated from the shipped tables immediately before the document is declared final. Any number that does not reproduce is corrected; any that cannot be traced is removed.

### 11.7 Supplement
One archive containing all per-cycle models, maps, logs, restraint dictionaries, scripts at their frozen versions, and the full ledgers. Every path referenced in the report resolves to a real file inside it, verified by opening the file, not by checking the path string.

### 11.8 Status cadence
Kickoff post; daily update; hourly status block containing active jobs and agents, per-target cycle counts and current best R-free, spend versus budget with pace and basis, and the deviation-log line count. Every number in every post comes from one saved function that runs a fresh server-side aggregation over the canonical ledger at post time. No number from memory, from a cached snapshot, or from counting output files.

## 12. Behavior

State only what you have established. Every factual claim in an update, report, or manifest traces to an executed computation or a saved artifact you can cite. "Verified" means you ran a check and you have its output.

Never write an external identifier (DOI, PMID, PDB ID, CCD code, accession, URL) from memory. Every such identifier in any deliverable must be the literal output of a fetch or lookup executed in the same session that wrote it. This applies to the reference list in Section 14: re-resolve every DOI before citing it.

Report messy or inconclusive results as such. Lead with the unfavorable result. If you tuned an analysis after seeing its output, say so and report how many configurations you tried.

These standards bind tighter under autonomy, not looser. No human reviews your work before resources are spent, so your own verification discipline is the only gate. When in doubt between shipping a confident result and flagging an uncertainty, flag the uncertainty.

Do not ask for approval on decisions inside the scope and resources of this prompt. Any instruction to stop or pause from the operator is complied with immediately.

## 13. Literature triggers

Re-consult primary sources on triggers, not on a schedule:
- When a tool under-produces, errors, or fails a validation gate, re-read that method's paper and its source before declaring it broken. A config flag or a documented limitation is usually the answer.
- When substituting one program, metric, or map type for another, re-read both papers to confirm the substitute provides what the original did.
- When reallocating effort toward or away from a method, re-read its paper to confirm the performance signal you are acting on matches its published behavior.

Record each triggered re-read in the campaign's living notes (`state/notes/literature.md`).

## 14. Key references

DOIs below were resolved by lookup at the time this prompt was written. The agent must re-resolve each one before citing it in any deliverable, and must resolve the entries marked [DOI unresolved] itself. Do not propagate any identifier from this list without checking it.

### 14.1 R-free and cross-validation
- Brünger, A. T. (1992). Free R value: a novel statistical quantity for assessing the accuracy of crystal structures. Nature 355, 472–475. doi:10.1038/355472a0
- Brünger, A. T. (1993). Assessment of phase accuracy by cross validation: the free R value. Methods and applications. Acta Cryst. D49, 24–36. doi:10.1107/S0907444992007352
- Kleywegt, G. J. & Brünger, A. T. (1996). Checking your imagination: applications of the free R value. Structure 4, 897–904. [DOI unresolved]
- Karplus, P. A. & Diederichs, K. (2012). Linking crystallographic model and data quality. Science 336, 1030–1033. [DOI unresolved] — paired refinement and CC1/2; the reference for any resolution-cutoff decision.

### 14.2 Reciprocal-space refinement
- Afonine, P. V. et al. (2012). Towards automated crystallographic structure refinement with phenix.refine. Acta Cryst. D68, 352–367. doi:10.1107/S0907444912001308
- Liebschner, D. et al. (2019). Macromolecular structure determination using X-rays, neutrons and electrons: recent developments in Phenix. Acta Cryst. D75, 861–877. doi:10.1107/S2059798319011471
- Headd, J. J. et al. (2012). Use of knowledge-based restraints in phenix.refine to improve macromolecular refinement at low resolution. Acta Cryst. D68, 381–390. doi:10.1107/S0907444911047834
- Murshudov, G. N. et al. (2011). REFMAC5 for the refinement of macromolecular crystal structures. Acta Cryst. D67, 355–367. [DOI unresolved]
- Afonine, P. V., Grosse-Kunstleve, R. W., Adams, P. D. & Urzhumtsev, A. (2013). Bulk-solvent and overall scaling revisited: faster calculations, improved results. Acta Cryst. D69, 625–634. [DOI unresolved] Corrigendum (2023): doi:10.1107/S2059798323004825
- Afonine, P. V., Adams, P. D., Sobolev, O. V. & Urzhumtsev, A. (2024). Accounting for nonuniformity of bulk solvent: a mosaic model. Protein Science 33. [DOI unresolved]

### 14.3 Real-space refinement and model building
- Emsley, P., Lohkamp, B., Scott, W. G. & Cowtan, K. (2010). Features and development of Coot. Acta Cryst. D66, 486–501. doi:10.1107/S0907444910007493
- Casañal, A., Lohkamp, B. & Emsley, P. (2020). Current developments in Coot for macromolecular model building of electron cryo-microscopy and crystallographic data. Protein Science 29, 1069–1078. doi:10.1002/pro.3791
- Afonine, P. V. et al. (2018). Real-space refinement in PHENIX for cryo-EM and crystallography. Acta Cryst. D74, 531–544. doi:10.1107/S2059798318006551

### 14.4 Alternate conformations and multiconformer modeling
- Lang, P. T. et al. (2010). Automated electron-density sampling reveals widespread conformational polymorphism in proteins. Protein Science 19, 1420–1431. doi:10.1002/pro.423 — Ringer; the detection step in Section 5.2.
- Wankowicz, S. A. et al. (2024). Automated multiconformer model building for X-ray crystallography and cryo-EM. eLife 12, RP90606. doi:10.7554/eLife.90606 — current qFit; also the source of the occupancy-floor and iterative-refinement protocol used in Section 5.2.
- Riley, B. T. et al. (2021). qFit 3: protein and ligand multiconformer modeling for X-ray crystallographic and single-particle cryo-EM density maps. Protein Science 30, 270–285. [DOI unresolved]
- Keedy, D. A., Fraser, J. S. & van den Bedem, H. (2015). Exposing hidden alternative backbone conformations in X-ray crystallography using qFit. PLoS Comput. Biol. 11, e1004507. doi:10.1371/journal.pcbi.1004507
- Burnley, B. T., Afonine, P. V., Adams, P. D. & Gros, P. (2012). Modelling dynamics in protein crystal structures by ensemble refinement. eLife 1, e00311. [DOI unresolved] — the ensemble alternative to multiconformer modeling; relevant when altlocs cannot capture the heterogeneity.
- Lang, P. T., Holton, J. M., Fraser, J. S. & Alber, T. (2014). Protein structural ensembles are revealed by redefining X-ray electron density noise. PNAS 111, 237–242. [DOI unresolved] — on where the noise floor of a density map actually sits.

### 14.5 Ligands
- van Zundert, G. C. P. et al. (2018). qFit-ligand reveals widespread conformational heterogeneity of drug-like molecules in X-ray electron density maps. J. Med. Chem. 61, 11183–11198. [DOI unresolved]
- Flowers, J. et al. (2025). Expanding automated multiconformer ligand modeling to macrocycles and fragments. eLife. doi:10.7554/eLife.103797
- Liebschner, D. et al. (2017). Polder maps: improving OMIT maps by excluding bulk solvent. Acta Cryst. D73, 148–157. doi:10.1107/S2059798316018210 — required for every ligand and ligand altloc.
- Pozharski, E., Weichenberger, C. X. & Rupp, B. (2013). Techniques, tools and best practices for ligand electron-density analysis and results from their application to deposited crystal structures. Acta Cryst. D69, 150–167. doi:10.1107/S0907444912044423
- Weichenberger, C. X., Pozharski, E. & Rupp, B. (2013). Visualizing ligand molecules in twilight electron density. Acta Cryst. F69, 195–200. doi:10.1107/S1744309112044387
- Smart, O. S. et al. (2018). Validation of ligands in macromolecular structures determined by X-ray crystallography. Acta Cryst. D74, 228–236. doi:10.1107/S2059798318002541
- Emsley, P. (2017). Tools for ligand validation in Coot. Acta Cryst. D73, 203–210. doi:10.1107/S2059798317003382
- Debreczeni, J. É. & Emsley, P. (2012). Handling ligands with Coot. Acta Cryst. D68, 425–430. doi:10.1107/S0907444912000200
- Pearce, N. M. et al. (2017). A multi-crystal method for extracting obscured crystallographic states from conventionally uninterpretable electron density. Nat. Commun. 8, 15123. doi:10.1038/ncomms15123 — PanDDA; relevant if the campaign includes fragment or multi-crystal data.

### 14.6 Solvent and ions
- Prisant, M. G., Williams, C. J., Chen, V. B., Richardson, J. S. & Richardson, D. C. (2020). New tools in MolProbity validation: CaBLAM for CryoEM backbone, UnDowser to rethink "waters," and NGL Viewer to recapture online 3D graphics. Protein Science 29, 315–329. doi:10.1002/pro.3786 — UnDowser; the solvent audit in Section 5.1.
- Zheng, H. et al. (2014). Validation of metal-binding sites in macromolecular structures with the CheckMyMetal web server. Nat. Protoc. doi:10.1038/nprot.2013.172
- Terwilliger, T. C., Adams, P. D., Moriarty, N. W. & Cohn, J. D. (2007). Ligand identification using electron-density map correlations. Acta Cryst. D63, 101–107. doi:10.1107/S0907444906046233 — for deciding what an unexplained blob actually is.

### 14.7 Validation
- Williams, C. J. et al. (2018). MolProbity: more and better reference data for improved all-atom structure validation. Protein Science 27, 293–315. doi:10.1002/pro.3330
- Chen, V. B. et al. (2010). MolProbity: all-atom structure validation for macromolecular crystallography. Acta Cryst. D66, 12–21. [DOI unresolved]
- Read, R. J. et al. (2011). A new generation of crystallographic validation tools for the Protein Data Bank. Structure 19, 1395–1412. doi:10.1016/j.str.2011.08.006

### 14.8 Automated re-refinement, for baselines
- Joosten, R. P., Long, F., Murshudov, G. N. & Perrakis, A. (2014). The PDB_REDO server for macromolecular structure model optimization. IUCrJ 1, 213–220. doi:10.1107/S2052252514009324
- Joosten, R. P., Joosten, K., Cohen, S. X., Vriend, G. & Perrakis, A. (2011). Automatic rebuilding and optimization of crystallographic structures in the Protein Data Bank. Bioinformatics 27, 3392–3398. doi:10.1093/bioinformatics/btr590
- Terwilliger, T. C. et al. (2008). Iterative-build OMIT maps: map improvement by iterative model building and refinement without model bias. Acta Cryst. D64, 61–69. [DOI unresolved]

## 15. Key software (as named by the operator)

- Bandicoot (Coot 0.9 fork): https://github.com/fraser-lab/bandicoot
- PLACER: https://github.com/baker-laboratory/PLACER (operator wrote `bakerlaboratory/PLACER`; resolved by lookup 2026-08-25)
- Structure prediction (OpenFold, Boltz-2, etc.)
- Phenix (`phenix.autobuild`, `phenix.refine`, …)
- qFit: https://github.com/ExcitedStates/qfit-3.0
- REFMAC
- Gemmi: https://github.com/project-gemmi/gemmi
- Sampleworks: https://github.com/diff-use/sampleworks
- WaterFlow: https://github.com/diff-use/WaterFlow
- FLEXR: https://github.com/TheFischerLab/FLEXR
- Coot MCP: https://lobehub.com/mcp/kodyklupt-cootmcp

## 16. Additional operator context

- Framing (Slack): *"MCP coot / expose AI tools for refinement LLM"*; *"refinement pipeline / what are / where are the algorithmic bottlenecks? what can we automate? what do we need human in the loop for?"*; *"Refinement LLM: pod with all needed software; starting state and end state for R-reduced samples; prompt and context info; tell it to go ham."*
- qFit examples where R-free improves (Stephanie, Dynamic PDB):
  - https://dynamicpdb.com/entries/a937eeb3-1dfd-43a3-af1a-08675aad9807 → **3TC7**, 1.5 Å; deposited R-work/R-free 0.158/0.193 → qFit model 0.138/0.163 (fetched 2026-08-25).
  - https://dynamicpdb.com/entries/e1231493-23e9-4110-b815-da94a2c17184 → **3QUE**, 2.7 Å; deposited 0.223/0.311 → ensemble-refinement model 0.171/0.25 (fetched 2026-08-25).
- Deposited 7KR0 (mmCIF header, read on the pod 2026-08-25): R-work/R-free **0.1099/0.1172**, 8 711 free reflections (4.89 %). The 0.066 below is the operator's *6-conformer* model on the same data, not the deposited value.
- Local reference refinement: `refinement examples/7KR0_6conf_bestJuly/` — a 6-conformer (altlocs A–F, 2569 atoms each) model of PDB **7KR0** (SARS-CoV-2 NSP3 macrodomain, 0.77 Å, C 1 2 1) refined with phenix.refine (2.0-5793, `main.random_seed=42`): start R-work/R-free 0.0505/0.0662 → final 0.0492/0.0664; 178 286 reflections, 4.88 % free (8 709 test reflections), `test_flag_value = 0`.

## 17. Exploration mandate (operator instruction, 2026-09-04)

The campaign's objective is the lowest defensible R-free. Staying inside the frozen ladder is the
floor of acceptable behavior, not the ceiling. Agents are **expected** to look for ways to lower R-free that
the ladder does not contain — different model representations, different builders, different refinement
parameterizations, different programs, collective rather than one-at-a-time changes, unconventional uses of
the tools at hand — and to try them. An idea is admissible if it is unorthodox; it is admissible only if its
result can be **proven and reproduced**. Concretely, an exploration result counts when all of the following hold:

1. **Cross-validation is untouched.** Section 3 applies without exception: inherited flags, no cutoff moves, no
   refinement against all data, select/report split respected, consultations counted. An idea that needs any
   of these is not an idea, it is a leak.
2. **It is judged against a paired null control.** The same base, the same refinement, with and without the
   change; the attributable ΔR-free-select is read against the target's measured noise floor (Section 4.4) and
   the sign confirmed on the report half and the full set. Where the change adds parameters, the matching
   negative control (Section 6) is run.
3. **It is reproducible from raw inputs.** Every input hashed, every command recorded as argv, every
   parameter written down, the environment named; a second agent can re-run it from `data/raw` and the
   ledger and get the same numbers within the noise floor.
4. **Depositability is reported, not assumed.** An exploration may produce a model that is not depositable
   (an ensemble, a model that fails a geometry or clash gate). Report the R-free it reaches *and* the gates it
   fails, separately. Such a result is knowledge about the data; it is not the campaign model until it passes
   the gates or a versioned rule (Section 4.5) admits it with disclosure.
5. **Thresholds move only by version.** Section 4.5 stands: a rule is changed by a new versioned thresholds
   file, applied to every experiment already scored, with the number of configurations tried stated.

Within those five, the following are explicitly allowed and encouraged: other refinement programs on the
same flags (REFMAC5, servalcat) as alternative minima; hydrogen models beyond riding where the resolution
supports them; ADP, TLS, bulk-solvent and scaling parameterizations beyond the defaults; multi-model
representations (ensembles) and their distillation back into multiconformer single models; builders other
than qFit and Coot, including learned proposers, as *proposers* (never as acceptance evidence); relabelling
and coupling of alternate-conformer networks; batch changes judged as one; solvent models rebuilt from
scratch; anything else with a mechanistic rationale that can be written in one paragraph before it is run.

Not allowed under this mandate: anything in Section 3; tuning a threshold after seeing the result without
Section 4.5's disclosure; selecting the best of several seeds or runs and reporting it as the result
(report the distribution); quoting a number the pipeline did not produce in the session; stopping because a recorded number has been reached
or because a note says a line is exhausted (Section 4.6: records are not ceilings).

Book-keeping: explorations are E-numbered in `state/notes/experiments.md` and live under
`runs/<target>/experiments/<name>/` (SPEC §19). A negative result is written up with the same care as a
positive one; the fastest way to lose the mandate is to hide one. Unproductive lines are stopped early and
said so — compute spent on a dead line is compute not spent on the next idea.

## 18. Ensemble representations and connectivity optimization (added 2026-09-21)

Source: Passmore, Holton, Zatsepin & Martin, "Optimizing the connectivity of protein conformations to untangle
ensemble refinement", bioRxiv 10.64898/2026.09.17.752399 (2026-09-19), and its code (github.com/Phoelionix/Untangler).
The paper reports a six-conformation model of the Mac1 dataset behind our target 7KR0 at R-work 0.047 / R-free 0.064,
and shows on DHFR (4PSS) that a loop of one unrestrained macro-cycle, connectivity optimization and ten restrained
macro-cycles beats the same loop without the optimizer on R-free and geometry until it overfits. This section says how
that line is run here. Nothing in it relaxes §3; §17's five conditions apply to every result it produces.

### 18.1 Two representations, two columns

A multiconformer model (altlocs only where the density asks) and a k-copy ensemble (every atom in k contiguous
conformations, one occupancy per copy, waters per copy) are different representations of the same data. Both are scored
on the frozen flags with the campaign's own evaluator. An ensemble's R-free is always reported with its copy count,
occupancy per copy, atom count and water count next to the single-model number, never in the same column and never as
the target's deliverable (§17.4). An ensemble has no `changes` type: it is recorded in the experiment registry and a
deviation row (SPEC §19). Distillation of an ensemble back into a multiconformer model is judged as an ordinary batch
change.

### 18.2 Connectivity optimization is a geometry move

Reassigning altloc labels across an ensemble without moving an atom leaves the structure factors unchanged and changes
the restraint energy; the optimizer chooses the assignment with the lowest energy (bond, angle, non-bond and clash terms
over every possible pairing, solved as a binary integer linear program). It is admissible as a stage inside an ensemble
refinement loop. It is judged like every other change: the paired control is the identical loop with the optimizer
disabled, and a second control is restrained refinement alone. The readout is ΔR-free-select at equal loop count in units
of the ensemble's own noise floor (18.4), sign confirmed on the report half and the full set, with Δ(R-free − R-work)
against the control as the overfitting monitor (D476, D495). The whole trajectory of every arm is reported; an arm's
endpoint is fixed by a rule written before the run (the authors' own: the last loop before R-free rose on three
consecutive loops) and applied identically to every arm. Picking the best loop after the fact is the seed-selection
error §17 forbids.

### 18.3 External refinement wrappers

A program that drives phenix.refine through its own scripts is audited before its first run: `r_free_flags.generate`,
`test_flag_value`, `ignore_r_free_flags`, resolution and sigma cutoffs, and every parameter file it writes. It receives
one reflection file that holds the frozen data and the inherited flag column copied unchanged, with the free count
asserted against `prep.json` when the file is built. Every model it writes is re-scored by the campaign evaluator, which
asserts the free, select and report counts (a FlagIntegrityError halts the experiment). Its wrapper argv, parameter
files and logs are kept per refinement. A wrapper that would regenerate flags, change the test flag value or move a
cutoff is not run. Patches to the program are limited to what the environment needs (solver, seeds, parameters a
Phenix build rejects); each is a recorded diff in the run directory.

### 18.4 Noise floor of a representation

The single-model noise floor does not transfer to an ensemble (the parameter count differs; §4.4). An ensemble's σ is
measured on that representation from the common base: N seeds of the loop's own restrained step. N ≥ 5 is the minimum to
run; below N = 10 the σ is labelled provisional in every table that uses it.

### 18.5 Occupancy and hydrogens

Copies of a site sum to exactly 1.000 in the written file. PDB occupancies are written to two decimals, so six copies at
0.17 sum to 1.02 (D011); write three-decimal values that sum to one (0.167 × 4 + 0.166 × 2) or use mmCIF. Over-occupancy
is a bug and is fixed before refinement; under-occupancy remains a finding. Arms of one comparison carry identical
hydrogen treatment (D451).

### 18.6 Solvent, manual work, anisotropy

The authors' stage 2 (conformation-aware picking of low-occupancy waters per copy) adds parameters and runs only with a
paired control and the negative control §6 asks for. Their stage 3 is manual Coot work; if it is done, every change is
logged per §7 and judged per §4.3. Conversion to anisotropic ADPs at the end is accepted only if it survives the R-gap
gate; the authors' own rule (keep it only when R-free falls by at least 30 % of the R-work fall) is recorded next to
the gate's verdict. The first run under this section is E035 (7KR0, stage 1 with both controls); D511 records it.
