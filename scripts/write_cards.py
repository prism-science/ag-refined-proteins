#!/usr/bin/env python3
"""scripts/write_cards.py REPO: write targets/<ID>/README.md for the eight targets, the two README tables (R-free and
geometry), and the provenance entries. The numbers come from the files in targets/<ID>/; the narrative is written here.
Every comparison is against the re-refined deposited model (S0001: the common recipe, the median of three seeds); the
deposited model as scored (S0000) stands beside it on the card (operator, meeting of 2026-10-21). Run from the repository
root: python3 scripts/write_cards.py ."""
import datetime, json, math, re, sys
from pathlib import Path

ROOT = Path(sys.argv[1])
HARNESS = "prism-science/agentic-refinement, branch `manzuoni/nov03-consolidated`, commit 62eeafa (pull request #70 to `main`) for 7KR0, 8C5N and 3TC7 of 2026-11-05; branch `manzuoni/oct28-trials`, commit 25ec394, for 7R2H of 2026-11-02; the models of 2026-10-21: branch `manzuoni/hierarchical_refinement`, commit bfed380 (merged into `main` as 7d62e84)"
# The operator's vault read of 2026-10-22 (prism-science/agentic-refinement, docs/PLAN.md, 2026-10-22 12:10Z): the model read, R-vault and
# R-free from S0001 to that model, the vault's size, the noise sigma of a paired change, z = (dR-vault - dR-free) / sigma, and whether the
# model read is on the lineage of the released model.
VAULT = {
 "7KR0": dict(at="S0053 (the release of 2026-10-21; also S0011 on 2026-10-18)", rv=(0.1054, 0.0725), rf=(0.1095, 0.0726), n=3400, sigma=0.0032, z=+1.2, lineage=False, verdict="holds"),
 "8C5N": dict(at="S0027 (the release of 2026-10-21)", rv=(0.1480, 0.0995), rf=(0.1294, 0.0908), n=1991, sigma=0.0044, z=-2.3, lineage=False, verdict="holds"),
 "7R2H": dict(at="S0032 of the gap fork", rv=(0.1346, 0.0982), rf=(0.1355, 0.0965), n=2000, sigma=0.0045, z=+0.6, lineage=True, verdict="holds"),
 "3TC7": dict(at="S0061 (the release of 2026-10-21)", rv=(0.1906, 0.1493), rf=(0.1856, 0.1475), n=780, sigma=0.0088, z=-0.4, lineage=True, verdict="holds"),
 "3QUE": dict(at="S0057", rv=(0.2941, 0.2735), rf=(0.2853, 0.2642), n=200, sigma=0.0160, z=+0.0, lineage=True, verdict="holds"),
 "9ARN": dict(at="S0062", rv=(0.2751, 0.2643), rf=(0.2970, 0.2769), n=306, sigma=0.0192, z=+0.5, lineage=True, verdict="holds"),
 "1LZ8": dict(at="S0073", rv=(0.2422, 0.2517), rf=(0.2712, 0.2408), n=260, sigma=0.0158, z=+2.5, lineage=True, verdict="fails"),
 "4QO4": dict(at="S0064", rv=(0.2671, 0.3009), rf=(0.3097, 0.2747), n=200, sigma=0.0214, z=+3.2, lineage=True, verdict="fails"),
}

def vault_caveat(tid, n_vault_fmt):
    v = VAULT[tid]
    head = "**The vault was read on 2026-10-22 at %s** (the operator's read; %s held-out work reflections): R-vault %.4f → %.4f from S0001 to that model, against R-free %.4f → %.4f on the deposited free set; the difference of the two changes is %+.1f σ of the sampling noise (σ %.4f)." % (
        v["at"], n_vault_fmt, v["rv"][0], v["rv"][1], v["rf"][0], v["rf"][1], v["z"], v["sigma"])
    if v["verdict"] == "fails":
        head += (" **The vault does not confirm the gain: R-vault rose while R-free fell.** The free set is small, the gate's margin (two seed σ) is about"
                 " 30 times smaller than the free set's own sampling noise of a paired change, and the run judged about 80 steps; the accepted gains are"
                 " most likely fitted to the free set. The model is released as the record of the run, not as a confirmed improvement.")
    else:
        head += " The vault confirms the gain within the noise."
    if not v["lineage"]:
        head += " That model is a sibling of this lineage, which forks before it and has not been read."
    elif tid in ("7R2H", "3TC7"):
        head += " The steps accepted after that model have not been read."
    head += " No decision used held-out reflections of any kind, and every map that placed or moved an atom excluded the free set."
    return head

T = {
 "7KR0": dict(handle="Tff1b3f_x", step="S0144", kind="a six-conformer ensemble", snapshot="2026-11-05",
   short="Crystal structure of SARS-CoV-2 NSP3 macrodomain (C2 crystal form, 100 K)",
   vault_row="3 400 work reflections (2 %) removed from every working file at preprocessing; read at S0011 and at S0053, siblings of this lineage; not read on this lineage",
   what="""Six complete conformers of the protein (altlocs A to F), each at occupancy 1/6, refined together against the working
data with riding hydrogens, anisotropic ADPs on every protein atom and on the waters, restraint weights wc 0.3 / wu 0.25,
and every water occupancy held at its conformer share: a lettered water (one conformer) at 1/6, a shared water (blank
altloc, all six) at 1. No water occupancy is refined; the 2026-10-21 release refined them. Ligands and ions are single.
The ensemble is the deliverable; it is not merged back into one model.

The model came from the deposited file in 147 recorded steps (S0004 to S0150; the record of S0000 to S0003 is in the
`refinement/S0000/` and `S0001/` files), 26 of them accepted and 3 builds, in the main run and its forks: the held-water
fork (Tff1b3f_held, then Tff1b3f_held2), the trial fork of 2026-10-28 (Tff1b3f_oct28), the clash fork of 2026-11-03
(Tff1b3f_nqh) and the exploratory fork of 2026-11-04 (Tff1b3f_x). The lineage of S0144: anisotropic
water ADPs (S0006); the six-conformer split from shake (S0007, a build); the held-water rule (S0082, a build: every water set
to its conformer share, occupancy refinement off); water picks at 4, 4 and 3σ on work-only difference maps (S0084, S0085,
S0088); anisotropic water ADPs three times (S0090 to S0092); a pick at 2.5σ (S0094); a 20-cycle convergence step (S0098);
conformer B-factors more than 3 times apart reset to the site median (S0103, a repair); a pick at 2.5σ that puts no water
within 2.6 Å of a protein atom of any conformer, the range-of-motion rule (S0105, R-free 0.0723, the lowest of the
line); the same B-factor reset again (S0112, a repair: conformer-B outliers 109 → 50, R-free +1.1σ against the control),
the release of 2026-11-02; B to occupancy for conformers whose side-chain B is above twice the site median (S0120, R-free
0.0724); then the clash term (Phenix's nonbonded weight, which phenix.refine sets to 16 at this resolution): 300 (S0124,
clashscore 13.6 → 2.6 for +6.4σ, explored rather than refused), 200 (S0128), B to occupancy again (S0135, 0.0726 / 6.4)
and 40 (S0144, held as the standing weight from then on).
From S0082 on, the Coot checks gated every step (waters in protein density, conformer-B outliers, residues beyond ±3.5σ
and next to positive peaks, the tallest peak, Holton's geometry energy wE). Refused after S0105: anisotropic water ADPs
(S0106), the Phenix restraint weights 1 / 1 (S0107, +6.2σ), a convergence step (S0108), the peak repair (S0109) and
Untangler's relabel on two trees (S0110, S0113). From 2026-11-04 the gate's verdict was advisory and a Referee kept
or set aside each step (seven rounds of parallel levers): hydrogens refined individually, the clash term at 110 to 300,
B to occupancy at 1.5, and Untangler on every head were set aside or refused; at the standing weight 40 the line
converged (R-free 0.0727 to 0.0728, clashscore 5.6 to 6.0).""",
   caveats=[
    "**The reference model scores lower.** PDB 44PS, the six-conformation model of these data from Passmore et al. (2026) and the reference model the agent was given, scores R-free 0.0657 and R-work 0.0485 on the same free set (scored 2026-10-03 by the earlier campaign's scorer), against 0.0728 / 0.0461 for this release. This release does not reach the reference.",
    "**This release trades R-free for geometry.** Against the release of 2026-11-02 (S0112: R-free 0.0725, clashscore 12.7, wE 575) this model reads R-free 0.0728 (+0.0003, about 2σ of the seed noise) with clashscore 5.8 and wE 386: the clash term at weight 40 against Phenix's own 16. Heavier weights (110 to 300) took the clashscore to 2.5 to 3.9 at 3 to 8σ of R-free and are not released.",
    "**Conformer-B outliers rose to 191** (50 at S0112): the B-to-occupancy steps (S0120, S0135) move a conformer's excess B into its occupancy and leave the conformers' B-factors further apart. The gap is 0.0266 against 0.0089 for the re-refined model.",
    "**The tallest difference peak, 10.6σ, is at Ser111**: the OG atoms of the conformers spread along a column where the data hold one position. The deepest point is −8.9σ. 3 waters lie within 2.2 Å of a protein atom of their own conformer (18 at S0112). Rotamer outliers 1.77 %.",
    "Three mmtbx sub-reports (C-beta deviations, omega, Rama-Z) fail on a six-conformer model; the geometry numbers above come from phenix.clashscore, rotalyze and ramalyze.",
   ],
   extra_files=[],
   reproduce="""bash tools/preprocessing.sh 7KR0 --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/Tff1b3f 6                  # to the six-conformer split, S0007
bash scripts/chain_heldwater.sh /home/dev/runs/hr/Tff1b3f /home/dev/runs/hr/Tff1b3f_held S0007 6
bash scripts/chain_held_levers.sh /home/dev/runs/hr/Tff1b3f_held2 6       # the sibling fork from the held BUILD S0082, sanity_count_k 2
bash scripts/chain_oct28.sh /home/dev/runs/hr/Tff1b3f_held2 /home/dev/runs/hr/Tff1b3f_oct28 S0098
bash scripts/fork_run.sh /home/dev/runs/hr/Tff1b3f_nqh /home/dev/runs/hr/Tff1b3f_x       # then scripts/round.sh RUN JOBS 6 S0120, rounds 1-7
phenix.python tools/score_model.py heads --run /home/dev/runs/hr/Tff1b3f_x              # the Referee's branches and decisions""",
   repro_note="The chain scripts under `refinement/chains/` are the hand-scheduled originals with their logs (`chain_oct28_Tff1b3f_oct28.log` for the trial fork; the earlier campaign's `chain*_7KR0.sh` stay for the record). The rounds of 2026-11-04 and 2026-11-05 (the jobs files, the round reports, `heads.json` and `trajectory/referee.txt`) are on the pod under the fork; the held-water and held-lever chains ran on the source forks; every command line of every step is in that step's `change.json` on the pod."),
 "3TC7": dict(handle="T431c8e_nqh", step="S0123", kind="a six-conformer ensemble", snapshot="2026-11-05",
   short="Engineered protein, NESG target OR62",
   what="""Six complete conformers of the protein (altlocs A to F), each at occupancy 1/6, refined together against the working
data with riding hydrogens, restraint weights wc 0.3 / wu 0.25, TLS (one group for the protein) over an isotropic residual on
every protein atom (the total ADP is written as ANISOU records) and isotropic waters. Selenium stands in place of sulfur in
conformer A of Met73, Met109 and Met237 (MSE, one sixth selenium at each site); Met154 and Met200 are sulfur in every
conformer. A lettered water belongs to one conformer, a water with a blank altloc to all six. The ensemble is the
deliverable; it is not merged back into one model.

The model came from the deposited file in 116 recorded steps (S0000 to S0115), 19 of them accepted and 2 builds, in the
main run T431c8e to the six-conformer split (S0032) and in its forks: T431c8e_gap with looser gap bounds (to S0061, the
2026-10-21 release), the Coot repair fork T431c8e_coot (S0086), the trial forks of 2026-10-28 (T431c8e_oct28: S0104;
T431c8e_oct28b: S0106) and T431c8e_oct29 (S0108). The lineage of S0108 to S0061 is on the 2026-10-21 card; after it: the
Coot repair of the residues in difference density (S0086: each conformer fitted into the work-only map of the model with that
conformer's residues at occupancy 0, the rotamer fitted then 20 cycles of real-space refinement, kept where the density
correlation did not fall; 42 waters that the moved side chains overlapped deleted; R-free +2.0σ against the control, a
repair); selenomethionine in conformers A and B of the five methionines, one third selenium (S0104: the tallest peak 13.7 →
7.7σ, R-free −7.0σ); the revert to selenium in conformer A of Met73, Met109 and Met237 only (S0106: the deepest point of the
difference map −11.0 → −5.3σ, a repair of the hole, R-free −1.9σ); the Coot repair again (S0108: 26 waters deleted, R-free
−10.5σ against its control, the gap 0.003 narrower, clashscore 9.5 → 9.0), the release of 2026-11-02; then, in the clash
fork T431c8e_nqh, the clash term (Phenix's nonbonded weight, 100 by default at this resolution) at 300 (S0116, clashscore
9.0 → 3.5, R-free 0.1521) and at 1000 (S0123, clashscore 0.8, R-free 0.1553).""",
   caveats=[
    "**This release trades R-free for geometry.** Against the release of 2026-11-02 (S0108: R-free 0.1504, clashscore 9.0, wE 707) this model reads R-free 0.1553 (+0.0049) with clashscore 0.8 and wE 322: the clash term at weight 1000 against Phenix's default of 100. S0116 (weight 300: R-free 0.1521, clashscore 3.5) is the milder trade and stays in the record on the pod.",
    "**Partial selenomethionine.** The SD sites hold about 18 electrons against 16 for sulfur: the crystal is partly selenomethionine. Selenium in every conformer was refused (+11σ, 2026-10-20); one third (S0104) left every Se atom in negative density; one sixth at three of the five methionines is what the maps support. The check that accepted S0106 (the deepest point of the difference map) was added after S0105, the same change on another fork, was refused by 0.06σ; the fork T431c8e_oct28b ran it with fresh arms, and the operator took the result.",
    "Six conformers at 1.5 Å: the gate's control is the parent refined with the same seeds, so an accepted gain is relative to that control, not evidence that six conformers are the right number for this entry. The two-conformer model of the main run (S0020, R-free 0.1688) is in the record.",
    "**The gap is 0.0623** against 0.0443 for the re-refined model. Rotamer outliers 2.89 %; one Ramachandran outlier (0.4 %); bond RMSD 0.019 Å; MolProbity score 1.40. The tallest work-only mFo-DFc peak is 5.7σ, the deepest point −4.6σ.",
   ],
   extra_files=[("`refinement/main_run_T431c8e/`", "the main run's own record after the fork point (its best S0042, R-free 0.1540, under the standing gap bounds)")],
   reproduce="""bash tools/preprocessing.sh 3TC7 --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/T431c8e 6          # to the six-conformer split, S0032
bash scripts/fork_run.sh /home/dev/runs/hr/T431c8e /home/dev/runs/hr/T431c8e_gap
# set gap_widen_max 0.010 and gap_abs_max 0.12 in T431c8e_gap/metaparams.yaml, as scripts/fork_gap_after.sh does
bash scripts/chain_gap.sh /home/dev/runs/hr/T431c8e_gap 6                                   # to S0061
bash scripts/chain_coot_repair.sh /home/dev/runs/hr/T431c8e_gap /home/dev/runs/hr/T431c8e_coot S0061 6   # S0086
bash scripts/chain_oct28.sh /home/dev/runs/hr/T431c8e_coot /home/dev/runs/hr/T431c8e_oct28 S0086       # S0104
# T431c8e_oct28b: a fork of T431c8e_oct28 with quality_hole_tol 1.0 and quality_hole_drop 1.5; refine_step.py semet --revert --pairs --kind sanity from S0104 (S0106)
bash scripts/chain_oct29.sh /home/dev/runs/hr/T431c8e_oct28b /home/dev/runs/hr/T431c8e_oct29 S0106     # S0108
bash scripts/fork_run.sh /home/dev/runs/hr/T431c8e_oct29 /home/dev/runs/hr/T431c8e_nqh                     # then refine_step.py nonbonded --weight 300 (S0116) and --weight 1000 (S0123)""",
   repro_note="The chain scripts under `refinement/chains/` are the hand-scheduled originals with their logs. The levers whose logs have no script there were scheduled from one-off scripts; every command line of every step is in that step's `change.json` on the pod."),
 "1LZ8": dict(handle="Tee73c5", step="S0073", kind="a two-conformer ensemble",
   short="Hen egg-white lysozyme, phased on the anomalous signal of S and Cl",
   what="""Two complete conformers of the protein (altlocs A and B), each at occupancy 1/2, from a qFit split of the single
model (S0035), refined together with riding hydrogens, restraint weights wc 2 / wu 2, TLS (one group) over an isotropic
residual (the total ADP written as ANISOU records), optimised bulk-solvent mask radii and isotropic waters. Two chloride
ions placed at difference peaks (S0073) are single and at occupancy 1. A lettered water belongs to one conformer, a blank one
to both.

The model came from the deposited file in 83 recorded steps (S0000 to S0082), 9 of them accepted and 3 builds. The
lineage of S0073: a convergence step (S0016); TLS, one group (S0020); a convergence step (S0032); the two-copy split
from qFit (S0035, a build); restraint weights 1 / 1 (S0053); the bulk-solvent mask radii optimised (S0060); a
convergence step (S0070); chloride ions at the two mFo−DFc peaks of 4σ and above that no atom explains, next to a
nitrogen (S0073; three waters removed). Restraint weights 2 / 2 were accepted on a sibling of the lineage (S0054) and
are in the standing recipe from there on.""",
   caveats=[
    "**The gap is 0.0746**, above the run's cap of 0.0714; the step passed because the control's gap (0.0754) was higher. The gap was 0.0802 for the deposited model and 0.0864 at the split (S0035); it has narrowed since.",
    "Clashscore 1.3 against 5.1 deposited; rotamer outliers 0.48 % (one residue in one conformer); no Ramachandran outlier; 93.7 % favoured against 96.9 % for the deposited model.",
    "A six-conformer fork of this run (Tee73c5_six) reached R-free 0.2627 and did not beat the two-conformer model; a three-conformer build (S0079) and the levers after it did not beat S0073 either. Both stay in the record; neither is released.",
   ],
   extra_files=[],
   reproduce="""bash tools/preprocessing.sh 1LZ8 --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/Tee73c5 6""",
   repro_note="The chain scripts under `refinement/chains/` (chain_target, chain_tight, chain_weights, chain_ens, chain_qfit, chain_more, chain_coot, chain_anneal, chain_ions, chain_lz2) are the hand-scheduled originals with their logs; the levers whose logs have no script (`chain_occhet`, `chain_qfit3`, `chain_reference`, `chain_six3`) were scheduled from one-off scripts, and every command line is in the step's `change.json` on the pod."),
 "4QO4": dict(handle="T40560e", step="S0064", kind="a single model",
   short="MDM2 (17-111) with compound 16",
   what="""A single model, as deposited, refined with restraint weights wc 0.3 / wu 0.25 and individual isotropic ADPs,
without hydrogens, with sulfate ions placed at difference peaks (S0050) and the loop 69 to 72 of chain A built (S0064),
which the deposited model lacks.

The model came from the deposited file in 80 recorded steps (S0000 to S0079), 5 of them accepted and 2 builds. The
lineage of S0064: restraint weights 0.3 / 0.25 (S0009); a convergence step (S0017); sulfate ions at the mFo−DFc peaks
of 5σ and above that no atom explains, next to a nitrogen (S0050, −0.014); a convergence step (S0052); residues 69 to
72 of chain A built by phenix.fit_loops into the work-only 2mFo−DFc map, their rotamers fitted by Coot, one side chain
with a map correlation under 0.3 cut to CB (S0064, −0.009).""",
   caveats=[
    "**Rotamer outliers 3.5 %** (three residues) are above the gate's 1.5 % cap; the step passed because the control had the same three. The deposited model has 6.0 %. Clashscore 7.3 against 16.0 deposited; no Ramachandran outlier, 95.6 % favoured.",
    "**The gain since the baseline is on the select half only.** R-free on the select / report halves is 0.3592 / 0.2625 at S0001 and 0.2874 / 0.2625 at S0064, with 264 reflections in each half; the re-refinement had moved them the other way (0.3368 / 0.2909 at S0000). Halves this small are noisy, and the vault read is the check.",
    "The gap is 0.0518 against 0.0654 for the re-refined model and 0.0502 for the deposited model as scored (the run's cap 0.0704).",
    "The model has no hydrogens: riding hydrogens were refused in this run. Reference-model restraints (S0075 and the later re-test) were refused; a two-conformer qFit build (S0069) and a six-conformer fork (T40560e_six, R-free 0.3042) did not beat the single model. None of these is released.",
   ],
   extra_files=[],
   reproduce="""bash tools/preprocessing.sh 4QO4 --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/T40560e 6
bash scripts/chain_ions.sh /home/dev/runs/hr/T40560e 6
bash scripts/chain_loop.sh /home/dev/runs/hr/T40560e 6""",
   repro_note="The levers whose logs have no script in `refinement/chains/` (`chain_loop2`, `chain_loop3`, `chain_occhet`, `chain_qfit2`, `chain_reference*`, `chain_zones`) were scheduled from one-off scripts; every command line is in the step's `change.json` on the pod."),
 "3QUE": dict(handle="T9884ae", step="S0057", kind="a single model",
   short="Human p38 MAP kinase with Skepinone-L",
   what="""A single model refined with restraint weights wc 2 / wu 2, TLS in three groups (phenix.find_tls_groups) over an
isotropic residual (the total ADP written as ANISOU records), secondary-structure and Ramachandran restraints, and
reference-model torsion restraints to PDB 3LFF, the same kinase at higher resolution (phenix reference_model, sigma 1.0,
limit 15, the sequences aligned by phenix; the file is `refinement/S0057/reference_model_3LFF.pdb`). No hydrogens;
61 isotropic waters.

The model came from the deposited file in 71 recorded steps (S0000 to S0070), 5 of them accepted and 1 build. The
lineage of S0057: TLS, three groups (S0027); restraint weights 2 / 2 (S0034); Coot auto-fit of the rotamer outliers
(S0041); secondary-structure and Ramachandran restraints (S0052); the reference-model restraints (S0057: R-free
0.2685 → 0.2642, R-work 0.1963 → 0.2124, rotamer outliers 8.2 → 3.6 %).""",
   caveats=[
    "**The reference-model restraints pull the torsions toward 3LFF.** R-work rose by 0.016 while R-free fell by 0.004, so the gap closed from 0.072 to 0.052; the side-chain conformations of this model are not independent evidence. The restraint file and its options are in the step's record.",
    "**Rotamer outliers 3.6 %** (11 residues) are above the gate's 1.5 % cap; the step passed because the control had 25. One Ramachandran outlier (0.3 %, as in the deposited model), 96.8 % favoured against 95.0 %. Clashscore 6.3 against 10.6 deposited.",
    "At 2.7 Å the picks, the hydrogens, the mask and the weight re-tests were all refused after S0057. A six-conformer fork of this run (T9884ae_six) was still converging at R-free 0.2834 when this snapshot was taken; it is not released.",
   ],
   extra_files=[("`refinement/S0057/reference_model_3LFF.pdb`", "the reference model of the torsion restraints (PDB 3LFF as fetched)")],
   reproduce="""bash tools/preprocessing.sh 3QUE --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/T9884ae 6
bash scripts/chain_lowres.sh /home/dev/runs/hr/T9884ae 6
bash scripts/chain_que2.sh /home/dev/runs/hr/T9884ae 6
bash scripts/chain_que3.sh /home/dev/runs/hr/T9884ae 6""",
   repro_note="The reference lever itself (`chain_reference_T9884ae.log`) and the levers whose logs have no script (`chain_after_mask`, `chain_after_tls`, `chain_occhet`, `chain_wref`) were scheduled from one-off scripts; every command line is in the step's `change.json` on the pod."),
 "9ARN": dict(handle="Tba97f6", step="S0062", kind="a single model",
   short="HIV-1 gp41 CHR-NHR reverse hairpin construct",
   what="""A single model with the deposited alternate conformations (altlocs A and B on some residues), refined with
restraint weights wc 2 / wu 2, secondary-structure and Ramachandran restraints, anisotropic ADPs on the protein and the
waters, and TLS in two groups (phenix.find_tls_groups). No hydrogens; 38 waters.

The model came from the deposited file in 75 recorded steps (S0000 to S0074), 9 of them accepted and 2 builds. The
re-refinement with the common recipe (S0001) scored above the deposited model (0.2970 against 0.2944), so the levers
were applied to S0000. The lineage of S0062: secondary-structure and Ramachandran restraints (S0056); anisotropic water
ADPs (S0060); TLS, two groups (S0062, −0.010). Restraint weights 2 / 2 (S0049) were accepted on another branch and are
in the standing recipe.""",
   caveats=[
    "The gap is 0.0380 against 0.0402 for the deposited model. Clashscore 1.6 (deposited 1.6), no rotamer outlier, no Ramachandran outlier, 100 % favoured.",
    "A run of the same entry with the data cut at 1.85 Å (handle Tf7cc84, `d_min_cut` 1.85) reached R-free 0.2598 at its S0002 with the same TLS lever. Its numbers are on a different reflection set and are not comparable with this card; it is not released. The entry's header reports 1.41 Å.",
    "A six-conformer fork of this run (Tba97f6_six, R-free 0.2853) did not beat the single model and is not released. The sulfate pick (S0071), the mask, annealing, isotropic protein ADPs and the water picks were refused after S0062.",
   ],
   extra_files=[],
   reproduce="""bash tools/preprocessing.sh 9ARN --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/Tba97f6 6
bash scripts/chain_tls.sh /home/dev/runs/hr/Tba97f6 6""",
   repro_note="The chain scripts under `refinement/chains/` (chain_target, chain_tls, chain_arn2, chain_arn3, chain_coot, chain_ions, chain_more, chain_noise, chain_qfit) are the hand-scheduled originals with their logs; `chain_after_rota` and `followup` were one-off scripts, and every command line is in the step's `change.json` on the pod."),
 "7R2H": dict(handle="Ta4f3f9_oct28", step="S0076", kind="an eight-conformer ensemble", snapshot="2026-11-02",
   short="Cyclophilin D with DMSO",
   what="""Eight complete conformers of the protein (altlocs A to H), each at occupancy 1/8, refined together against the
working data with riding hydrogens, TLS (one group) over isotropic protein ADPs, anisotropic water ADPs, restraint
weights wc 0.3 / wu 0.25 and individual water occupancies. A lettered water belongs to one conformer, a water with a
blank altloc to all eight. The ligand is single. The ensemble is the deliverable; it is not merged back into one model.

The model came from the deposited file in 77 recorded steps (S0000 to S0076), 16 of them accepted and 2 builds, in the
main run Ta4f3f9 (to S0019, the 2026-10-21 release) and its forks: Ta4f3f9_gap with looser gap bounds, the
eight-conformer fork Ta4f3f9_g8 and the trial fork of 2026-10-28 (Ta4f3f9_oct28). The lineage of S0076: restraint weights
0.3 / 0.25 (S0008); anisotropic water ADPs (S0012); the six-conformer split from shake (S0014, a build); water picks at 4σ
three times and at 2.5σ (S0015 to S0019); isotropic protein ADPs in place of anisotropic ones (S0030); TLS, one group
(S0032); a pick at 2.5σ (S0035); eight conformers from six, the first two duplicated (S0046, a build); anisotropic water ADPs
(S0051, R-free 0.0954); conformer B-factors more than 3 times apart reset to the site median (S0062, a repair);
anisotropic water ADPs again (S0071); the B-factor reset by the density (S0076: a conformer's B above the site median
reset to the median where that conformer's 2mFo-DFc density is at least half the site's; R-free 0.0954 → 0.0946).""",
   caveats=[
    "**A 24σ difference peak that the model does not explain.** The tallest point of the work-only mFo-DFc map lies between Glu23 and Lys25, 1.2 to 1.8 Å from the OE2 atoms of six conformers of Glu23. A phosphate (R-free +9.1σ, the deepest point −22σ), a potassium ion (B 75 Å²) and a water (occupancy 0.38, 1.45 Å from Glu23 OE1) were refused at the site; no rotation of Glu23 reaches it; it is most likely the NZ of Lys25 in a rotamer no conformer has. The Coot refit of Lys25 and Glu23 in each conformer moved Lys25 in four conformers and left the peak. The site needs a person at Coot.",
    "**S0076 was judged twice.** The same change was refused as a repair (S0075: R-free −2.7σ against the control, but no check fell by 10 %) and then judged as an improving step from the same parent (S0076, accepted on the R-free rule, the arms from the refinement cache). One change under two bars; the record discloses it.",
    "**The gap is 0.0296** against 0.0112 for the re-refined model, under the fork's bounds (a widening of at most 0.010 in one step, a cap of 0.12; 0.002 and 0.030 in the main run). Clashscore 12.1 against 4.3 re-refined (the deposited file carries its own hydrogens and scores 0.0); rotamer outliers 1.76 % are above the 1.5 % cap and passed against the control; Ramachandran outliers 0.6 %.",
    "**Eight conformers at 0.79 Å**: 21 496 atoms against 2 850 deposited. The conformer B-factors spread again after each reset (319 atoms in four or more conformers with B-factors more than 3 times apart at S0076; the spread returns to about 2.7 times under refinement). The water occupancies are refined on this line: 98 lettered waters with occupancy above 1.5/8 lie within 2.2 Å of another conformer's atom, 14 within 2.2 Å of their own. The held-water rule, which gave the best 8C5N and 7KR0 models, did not pay on 7R2H (fork Ta4f3f9_held, R-free 0.112).",
    "The deposited model scores 0.1551 on our flags and 0.1355 after the common recipe (S0001); the header reports 0.1549 on its own flags.",
   ],
   extra_files=[],
   reproduce="""bash tools/preprocessing.sh 7R2H --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/Ta4f3f9 6                                            # to S0019
bash scripts/fork_run.sh /home/dev/runs/hr/Ta4f3f9 /home/dev/runs/hr/Ta4f3f9_gap                    # looser gap bounds, as fork_gap_after.sh sets them
bash scripts/chain_grow.sh /home/dev/runs/hr/Ta4f3f9_gap /home/dev/runs/hr/Ta4f3f9_g8 8             # eight conformers, S0046 and S0051
bash scripts/chain_oct28.sh /home/dev/runs/hr/Ta4f3f9_g8 /home/dev/runs/hr/Ta4f3f9_oct28 S0051      # S0062 to S0076""",
   repro_note="The chain scripts under `refinement/chains/` are the hand-scheduled originals with their logs (`chain_oct28_Ta4f3f9_oct28.log` for the trial fork). The step S0076 was run by hand (`coot_repair.py bfactors --criterion density --kind improving`); every command line of every step is in that step's `change.json` on the pod."),
 "8C5N": dict(handle="T5f59f1_nqh", step="S0074", kind="a six-conformer ensemble", snapshot="2026-11-05",
   short="Chitin-binding protein D (CbpD) from Pseudomonas aeruginosa",
   what="""Six complete conformers of the protein (altlocs A to F), each at occupancy 1/6, refined together against the working
data with riding hydrogens, anisotropic ADPs on every protein atom and every water, restraint weights wc 0.3 / wu 0.25,
and every water occupancy held at its conformer share: a lettered water (one conformer) at 1/6, a shared water (blank
altloc, all six) at 1. No water occupancy is refined; the 2026-10-21 release refined them. Ligands and ions are single.
The ensemble is the deliverable; it is not merged back into one model.

The model came from the deposited file in 66 recorded steps (S0000 to S0065), 18 of them accepted and 2 builds, in the
main run T5f59f1 (to S0027, the 2026-10-21 release) and its forks: the held-water fork T5f59f1_held, its Coot repair fork
T5f59f1_heldcoot and the trial fork of 2026-10-28 (T5f59f1_oct28). The lineage of S0065: restraint weights 0.3 / 0.25
(S0008); anisotropic water ADPs (S0012); the six-conformer split from shake (S0014, a build); the held-water rule (S0030, a
build, from the split: every water set to its conformer share, occupancy refinement off); water picks at 4 and 3σ on
work-only difference maps (S0031, S0034); anisotropic water ADPs (S0037, R-free 0.0891); a convergence step (S0040,
0.0879); the Coot water repair (S0046, R-free 0.0871, the lowest of the line: the waters in protein density deleted, each
conformer of the residues next to them fitted in Coot); conformer B-factors more than 3 times apart reset to the site median
(S0049, a repair); the water repair again (S0050: no water in protein density left); the B-factor reset again (S0055, a
repair); the B-factor reset by the density (S0065, a repair: a conformer's B above the site median reset to the median where
that conformer's 2mFo-DFc density is at least half the site's; conformer-B outliers 31 → 3, R-free −0.3σ against the control),
the release of 2026-11-02; then, in the clash fork T5f59f1_nqh: the clash term (Phenix's nonbonded weight) at 300 (S0067,
clashscore 14.8 → 4.2, R-free 0.0882), B to occupancy for conformers whose side-chain B is above twice the site median
(S0072, 0.0884 / 3.2) and the clash term at 1000 (S0074, 0.0889 / 1.2).
From S0030 on, the Coot checks gated every step. Refused after S0055: a 3σ and a 2.5σ pick with the range-of-motion rule
(S0056, S0058), the Phenix restraint weights 1 / 1 (+6.2σ on the held Coot line), anisotropic water ADPs (S0060), a
convergence step (S0061), the peak repair (S0062) and Untangler's relabel (S0063).""",
   caveats=[
    "**This release trades R-free for geometry.** Against the release of 2026-11-02 (S0065: R-free 0.0875, clashscore 14.8, wE 741) this model reads R-free 0.0889 (+0.0014) with clashscore 1.2 and wE 309: the clash term at weight 1000, where phenix.refine's own default at this resolution is 16. Rotamer outliers 1.37 %; no Ramachandran outlier; MolProbity score 1.25.",
    "**The gap is 0.0243** against 0.0046 for the re-refined model (the run's cap 0.030). Conformer-B outliers 33 (3 at S0065): the B-to-occupancy step moves a conformer's excess B into its occupancy. The tallest work-only mFo-DFc peak is 9.8σ, the deepest point −6.6σ; no water overlaps protein.",
    "Six conformers at 0.75 Å: 18 961 atoms against 2 850 deposited. The deposited model scores 0.1571 on our flags and 0.1294 after the common recipe (S0001); the header reports 0.1634 on its own flags.",
   ],
   extra_files=[],
   reproduce="""bash tools/preprocessing.sh 8C5N --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/T5f59f1 6                                                  # to the six-conformer split, S0014
bash scripts/chain_heldwater.sh /home/dev/runs/hr/T5f59f1 /home/dev/runs/hr/T5f59f1_held S0014 6          # S0030 to S0040
bash scripts/chain_coot_repair.sh /home/dev/runs/hr/T5f59f1_held /home/dev/runs/hr/T5f59f1_heldcoot S0040 6   # S0046 to S0050
bash scripts/chain_oct28.sh /home/dev/runs/hr/T5f59f1_heldcoot /home/dev/runs/hr/T5f59f1_oct28 S0050       # S0055 to S0065
bash scripts/fork_run.sh /home/dev/runs/hr/T5f59f1_oct28 /home/dev/runs/hr/T5f59f1_nqh                       # then refine_step.py nonbonded --weight 300 / ensemble_edit.py b-to-occ / nonbonded --weight 1000: S0067, S0072, S0074""",
   repro_note="The chain scripts under `refinement/chains/` are the hand-scheduled originals with their logs (`chain_oct28_T5f59f1_oct28.log` for the trial fork). The held-water and Coot repair chains ran on the source forks; every command line of every step is in that step's `change.json` on the pod."),
}


def load(p): return json.loads(Path(p).read_text())
def fmt_int(n): return "{:,}".format(int(round(n))).replace(",", " ") if isinstance(n, (int, float)) else "n/a"
def num(x, f): return (f % x) if isinstance(x, (int, float)) else "n/a"

def molprobity(m):
    g = m.get("geometry") or {}
    if isinstance(g.get("molprobity_score"), (int, float)):
        return g["molprobity_score"]
    try:   # the MolProbity formula from the three components (the scorer's own value when it has one)
        c, ro, fav = m["clashscore"], m["rota_pct"], m["rama_favored_pct"]
        return 0.426 * math.log(1 + c) + 0.33 * math.log(1 + max(0.0, ro - 1)) + 0.25 * math.log(1 + max(0.0, 100 - fav - 2)) + 0.5
    except (KeyError, TypeError):
        return None

def metrics_of(t, recs, step):
    r = recs.get(step)
    m = dict(r["metrics"]) if (r and r.get("metrics")) else {}
    p = t / "refinement" / step / "score.json"
    if not m and p.exists():
        m = dict(load(p).get("after") or {})
    rp = t / "refinement" / step / "rescored.json"   # the same model scored again by the current scorer at release
    if rp.exists():
        for k, v in load(rp).items():
            if m.get(k) is None and k != "note":
                m[k] = v
    return m

def copies(m):
    if not m.get("copies"):
        return "n/a"
    if m["copies"] == 1:
        return "1" + (" (altlocs %s on some residues)" % m["altlocs"] if m.get("altlocs") else "")
    return "%d, altlocs %s" % (m["copies"], m["altlocs"])

def card(tid, c):
    t = ROOT / "targets" / tid
    e = load(t / "deposited/rcsb_entry.json"); prep = load(t / "data/prep.json"); run = load(t / "refinement/run.json")
    recs = {}
    for l in (t / "refinement/score_history.jsonl").read_text().splitlines():
        r = json.loads(l); recs[r["step"]] = r
    dep, base, a = metrics_of(t, recs, "S0000"), metrics_of(t, recs, "S0001"), metrics_of(t, recs, c["step"])
    facts = (t / ("refinement/%s/FACTS.txt" % c["step"])).read_text().strip()
    meta = (t / "refinement/metaparams.yaml").read_text()
    mg = re.search(r"^gap_widen_max:\s*([0-9.]+)", meta, re.M); gwm = float(mg.group(1)) if mg else None
    gcap = run.get("gap_max"); sigma = (run.get("noise_floor") or {}).get("sigma_r_free")
    utc = facts.split()[1]
    res = e["rcsb_entry_info"]["resolution_combined"][0]; sg = e["symmetry"]["space_group_name_H_M"]
    cite = e.get("rcsb_primary_citation") or {}
    progs = ", ".join(dict.fromkeys(s["name"] for s in e.get("software", []) if s.get("classification") == "refinement"))
    ref = (e.get("refine") or [{}])[0]
    n_vault = run.get("n_vault") or (prep.get("bunker") or {}).get("n"); n_work = prep["n_work"]; n_free = prep["n_free"]
    vault_pct = 100.0 * n_vault / (n_work + n_vault) if n_vault else 0.0
    phenix = (run.get("phenix_version") or "").replace("Version: ", "").replace("; Release tag: ", "-") or "2.1-6048"
    title = e["struct"]["title"].strip().rstrip(".")
    status = ("**Status: %s.** The released model is %s with an R-free of %.4f on the deposited free set. The re-refined "
              "deposited model (S0001, the common recipe) scores %.4f and the deposited model as scored (S0000) %.4f on the same "
              "reflections." % ("improved" if VAULT[tid]["verdict"] == "holds" else "lower R-free, not confirmed by the vault", c["kind"], a["r_free"], base["r_free"], dep["r_free"]))
    if c.get("snapshot"):
        status += " This is the model in force on %s; the run may continue." % c["snapshot"]
    else:
        status += " The model is the release of 2026-10-21; the run has had no accepted step since."
    if VAULT[tid]["verdict"] == "fails":
        status += " **The vault read of 2026-10-22 does not confirm the gain** (see Caveats)."
    gate = "ΔR-free ≤ −2σ against the control (σ = %s from three seeds), gap widened by at most %s, gap ≤ %s or not above the control's, clashscore ≤ 15, rotamer outliers ≤ 1.5 %% or not above the control's" % (
        num(sigma, "%.5f"), num(gwm, "%g"), num(gcap, "%.4f"))
    rows = [
     ("Resolution", "%g Å" % res), ("Space group", sg),
     ("Data", "%s (%s); %s reflections in the working files, %s work and %s free" % (prep["intensities_or_amplitudes"], prep["data_labels"], fmt_int(prep["n_reflections"]), fmt_int(n_work), fmt_int(n_free))),
     ("Free set", "the deposition's own flags, inherited unchanged (%.2f %%); select / report halves %s / %s" % (100 * prep["fraction_free"], fmt_int(prep["n_select"]), fmt_int(prep["n_report"]))),
     ("Vault", c.get("vault_row") or "%s work reflections (%.0f %%) removed from every working file at preprocessing and sealed; not read in this run (the read is the operator's)" % (fmt_int(n_vault), vault_pct)),
     ("Deposited refinement program", progs or "n/a"),
     ("Released by the PDB", (e["rcsb_accession_info"]["initial_release_date"] or "")[:10]),
     ("Primary citation", "%s (%s %s), DOI %s" % ((cite.get("title") or "").rstrip("."), cite.get("journal_abbrev"), cite.get("year"), cite.get("pdbx_database_id_DOI"))),
     ("Harness", c.get("harness") or HARNESS),
     ("Run", "handle %s, step %s, %s UTC" % (c["handle"], c["step"], utc.replace("T", " ").replace("Z", ""))),
     ("Phenix", phenix),
     ("Gate", gate),
    ]
    def row(label, key, f):
        return (label, num(dep.get(key), f), num(base.get(key), f), num(a.get(key), f))
    three = [
     ("R-free", num(dep.get("r_free"), "%.4f"), num(base.get("r_free"), "%.4f"), "**%.4f**" % a["r_free"]),
     row("R-work", "r_work", "%.4f"), row("Gap R-free − R-work", "gap", "%.4f"),
     ("R-free on the select / report halves",) + tuple("%s / %s" % (num(m.get("r_free_select"), "%.4f"), num(m.get("r_free_report"), "%.4f")) for m in (dep, base, a)),
     row("Clashscore (phenix.clashscore, hydrogens kept)", "clashscore", "%.1f"),
     row("Rotamer outliers", "rota_pct", "%.2f %%"),
     ("Ramachandran outliers / favoured",) + tuple("%s / %s" % (num(m.get("rama_outliers_pct"), "%.1f %%"), num(m.get("rama_favored_pct"), "%.1f %%")) for m in (dep, base, a)),
     ("Bond RMSD / angle RMSD",) + tuple("%s / %s" % (num(m.get("bond_rmsd"), "%.3f Å"), num(m.get("angle_rmsd"), "%.2f°")) for m in (dep, base, a)),
     ("MolProbity score",) + tuple(num(molprobity(m), "%.2f") for m in (dep, base, a)),
     ("Conformers",) + tuple(copies(m) for m in (dep, base, a)),
     ("Atoms (of which H)",) + tuple("%s (%s)" % (fmt_int(m.get("n_atoms")), fmt_int(m.get("n_h"))) for m in (dep, base, a)),
     ("Waters, occupancy sum",) + tuple("%s, %s" % (fmt_int(m.get("n_water_atoms")), fmt_int(m.get("water_occ_sum"))) for m in (dep, base, a)),
     ("ANISOU records",) + tuple(fmt_int(m.get("n_anisou")) for m in (dep, base, a)),
    ]
    hdr = "The entry's own header reports R-free %s and R-work %s on its own flags." % (ref.get("ls_R_factor_R_free"), ref.get("ls_R_factor_R_work"))
    files = [
     ("`model/%s_%s.pdb`" % (tid, c["step"]), "the released model, PDB, occupancies at four decimals, as the gate wrote it"),
     ("`model/%s_%s.cif`" % (tid, c["step"]), "the same model as mmCIF (gemmi conversion)"),
     ("`model/%s_S0001.pdb`" % tid, "the re-refined deposited model (S0001, the common recipe, the median of three seeds): the baseline of every comparison"),
     ("`maps/%s_%s_map_coeffs.mtz`" % (tid, c["step"]), "phenix.maps coefficients from the work reflections only: `2FOFCWT/PH2FOFCWT` and `FOFCWT/PHFOFCWT`"),
     ("`data/%s_data.mtz`, `%s_flags.mtz`, `%s_split.mtz`" % (tid, tid, tid), "the working data, the inherited flags, the select/report split; the vault is absent from all three"),
     ("`data/prep.json`, `split.json`", "how the files were built, with checksums and counts"),
     ("`deposited/%s.cif`, `rcsb_entry.json`" % tid, "the deposited model and the RCSB entry record, as fetched"),
     ("`refinement/score_history.txt`, `score_history.jsonl`, `scorecard.csv`", "every step: the facts line, the full metrics, the scorecard row"),
     ("`refinement/steps.md`", "the step table"),
     ("`refinement/%s/`" % c["step"], "the released step: facts line, change record, score record"),
     ("`refinement/S0001/`, `S0000/`", "the baseline step and the deposited model as scored: facts lines and score records" + (" (`S0000/rescored.json`: the same model scored again by the current scorer at release, for the geometry fields the scorer of 2026-10-14 did not write)" if tid == "7KR0" else "")),
     ("`refinement/metaparams.yaml`, `run.json`", "the metaparameters of the run and its state (noise floor, standing recipe, the sealed vault's checksums)"),
     ("`refinement/chains/`", "the chain scripts that scheduled the steps on the pod, as run, with their logs"),
     ("`validation/`", "phenix.clashscore, rotalyze and ramalyze logs of the released model (`*_%s.*`) and of the re-refined baseline (`*_S0001.*`)" % c["step"]),
    ] + c["extra_files"]
    vault_cav = vault_caveat(tid, fmt_int(n_vault))
    note = ("> In development. Refined by an agent that was prompted to follow a procedure based on Passmore et al. (2026), "
            "with PDB 44PS as the reference model; see the [citation](../../README.md#citation).")
    out = ["# %s — %s" % (tid, title), "", note, "", status, "", "| | |", "|---|---|"]
    out += ["| %s | %s |" % r for r in rows]
    out += ["", "## The three models on the same flags", "",
            "All three are scored by the harness gate: a fresh cctbx fmodel on the working data with every reflection, no outlier",
            "rejection. S0000 is the deposited model as anonymised at preprocessing; S0001 is that model after the common recipe",
            "(phenix.refine, 10 macro-cycles, three seeds, the median), the baseline that every gain is measured against; the",
            "release is the model in force. Geometry from phenix.clashscore (hydrogens kept), rotalyze and ramalyze; the",
            "MolProbity score from those three.", "",
            "| | Deposited as scored (S0000) | Re-refined (S0001) | This release (%s) |" % c["step"], "|---|---|---|---|"]
    out += ["| %s | %s | %s | %s |" % r for r in three]
    out += ["", hdr, "", "## What the model is", "", c["what"], "",
            "The gate judged every change against a control, the parent refined with the same command and seeds, and accepted an",
            "improving change only when R-free fell by at least 2σ of the run's noise floor with the gap and the geometry inside their",
            "bounds. From 2026-10-27 the gate also holds the model checks of `docs/METHOD.md` (waters in protein density, conformer-B",
            "outliers, residues in difference density, the tallest peak, Holton's wE) and accepts a repair: a change that lowers one",
            "check with R-free not worse than 2σ against its control.",
            "`refinement/steps.md` lists every step with its verdict and `refinement/score_history.txt` is the hash-chained record",
            "the gate wrote.", "", "## Caveats", "", "- " + vault_cav]
    out += ["- " + x for x in c["caveats"]]
    out += ["", "## Files", "", "| Path | Content |", "|---|---|"] + ["| %s | %s |" % f for f in files]
    out += ["", "## Reproduce", "", "In the harness checkout on the pod (`docs/POD.md` there):", "", "```", c["reproduce"], "```", "", c["repro_note"], ""]
    (t / "README.md").write_text("\n".join(out))
    return dict(id=tid, res=res, title=c["short"], snapshot=c.get("snapshot") or "2026-10-21", dep=dep, base=base, a=a, step=c["step"], kind=c["kind"], handle=c["handle"], utc=utc)

def splice(text, name, body):
    m = re.search(r"(<!-- %s:begin -->\n)(.*?)(<!-- %s:end -->)" % (name, name), text, re.S)
    if not m:
        raise SystemExit("README.md: no %s markers" % name)
    return text[:m.end(1)] + body + text[m.start(3):]

def main():
    info = sorted((card(tid, c) for tid, c in T.items()), key=lambda x: x["res"])
    r1 = ["| Target | Res. (Å) | Model | R-free (PDB → ours) | R-work | Gap | Clashscore (PDB → ours) | MolProbity | Deposited |",
          "|---|---|---|---|---|---|---|---|---|"]
    for i in info:
        d, a = i["dep"], i["a"]
        r1.append("| [%s](targets/%s/README.md) | %g | %s | %s → **%s** | %s | %s | %s → %s | %s | %s |" % (
            i["id"], i["id"], i["res"], i["step"], num(d.get("r_free"), "%.4f"), num(a.get("r_free"), "%.4f"), num(a.get("r_work"), "%.4f"),
            num(a.get("gap"), "%.3f"), num(d.get("clashscore"), "%.1f"), num(a.get("clashscore"), "%.1f"), num(molprobity(a), "%.2f"), i["snapshot"]))
    readme = (ROOT / "README.md").read_text()
    readme = splice(readme, "results-table", "\n".join(r1) + "\n")
    (ROOT / "README.md").write_text(readme)
    prov = load(ROOT / "provenance.json")
    prov["exported_at"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    prov["line"] = "hierarchical refinement (C-conformer ensembles)"
    prov["harness"] = {"repository": "prism-science/agentic-refinement", "branch": "manzuoni/nov03-consolidated", "commit_of_the_models": "62eeafa (7KR0, 8C5N, 3TC7 of 2026-11-05, branch manzuoni/nov03-consolidated); 25ec394 (7R2H of 2026-11-02, branch manzuoni/oct28-trials); bfed380 for the four targets unchanged since 2026-10-21", "commit_at_release": "62eeafa (branch manzuoni/nov03-consolidated; pull request #70 to main)"}
    prov["baseline"] = "S0001: the deposited model after the common recipe (phenix.refine, 10 macro-cycles, three seeds, the median); every comparison in the cards and the README is against it (operator, meeting of 2026-10-21)"
    for i in info:
        rec = prov["released"].setdefault(i["id"], {})
        rec.update({"run_handle": i["handle"], "step": i["step"], "utc": i["utc"]})
        v = VAULT[i["id"]]
        rec["vault_last_read"] = "2026-10-22 at %s: R-vault %.4f (S0001 %.4f), R-free %.4f (S0001 %.4f), z %+.1f, %s%s" % (
            v["at"], v["rv"][1], v["rv"][0], v["rf"][1], v["rf"][0], v["z"], v["verdict"], "" if v["lineage"] else "; a sibling of the released lineage")
        rec["rerefined_r_free_S0001"] = round(i["base"]["r_free"], 5)
    (ROOT / "provenance.json").write_text(json.dumps(prov, indent=1) + "\n")
    print("cards written:", [i["id"] for i in info])

main()
