#!/usr/bin/env python3
"""scripts/write_cards.py REPO: write targets/<ID>/README.md for the eight targets, the two README tables (R-free and
geometry), and the provenance entries. The numbers come from the files in targets/<ID>/; the narrative is written here.
Every comparison is against the re-refined deposited model (S0001: the common recipe, the median of three seeds); the
deposited model as scored (S0000) stands beside it on the card (operator, meeting of 2026-10-21). Run from the repository
root: python3 scripts/write_cards.py ."""
import datetime, json, math, re, sys
from pathlib import Path

ROOT = Path(sys.argv[1])
HARNESS = "prism-science/agentic-refinement, branch `manzuoni/hierarchical_refinement`, commit bfed380 (merged into `main` as 7d62e84, 2026-10-21)"
RUNNING = {"7R2H", "8C5N"}   # runs still going at export

T = {
 "7KR0": dict(handle="Tff1b3f", step="S0053", kind="a six-copy ensemble",
   short="Crystal structure of SARS-CoV-2 NSP3 macrodomain (C2 crystal form, 100 K)",
   harness="prism-science/agentic-refinement, branch `manzuoni/hierarchical_refinement` (the model: commit bd972d3; the card: bfed380, merged into `main` as 7d62e84)",
   vault_row="3 400 work reflections (2 %) removed from every working file at preprocessing; read one time, at S0011",
   vault_caveat="**The vault was read once, at S0011** (R-vault 0.0769 against R-free 0.0809, no leak signature). The 42 steps after it used no held-out reflections of any kind in a decision, and every map that placed a water excluded the free set, but the gains since S0011 have not yet been checked against the vault. That read is the operator's.",
   what="""Six complete copies of the protein (altlocs A to F), each at occupancy 1/6, refined together against the working data
with riding hydrogens, anisotropic ADPs on every protein atom and on most waters, restraint weights wc 0.3 / wu 0.25,
and individual water occupancies. Every water is one atom: a lettered water belongs to one copy (its occupancy is
refined; the mean is 0.30), a water with a blank altloc is shared by all six (mean 0.93). Ligands and ions are single.
The ensemble is the deliverable; it is not merged back into one model.

The model came from the deposited file in 54 recorded steps (S0000 to S0053), 15 of them accepted. The accepted levers,
in order: anisotropic water ADPs; the six-copy split (a representation change, scored and recorded but not judged);
water picks at 4, 3, 3, 2.5, 2.5, 2.5 and 2.5σ on work-only difference maps; anisotropic water ADPs again; restraint
weights 0.3 / 0.25; 20-cycle convergence steps; altloc occupancies; and, last, waters in own-copy clashes moved to a
copy they clear.""",
   caveats=[
    "**The gap is 0.0259**, against 0.0089 for the re-refined model and 0.0071 for the deposited model as scored: the six copies and the free water occupancies fit the work set better than the free set. The run's cap is 0.030. A reference six-copy ensemble of this entry built earlier with maps that may have included the free reflections scores 0.0676 / 0.0507 on these flags; its advantage over this model is entirely in its solvent, and that comparison is in the harness plan, not in this release.",
    "**Clashscore 7.7** against 5.3 re-refined and 4.3 deposited; 40 waters sit in own-copy clashes that no other copy can take. Rotamer outliers 1.54 % are just above the gate's 1.5 % cap and passed because the control had the same.",
    "Three mmtbx sub-reports (C-beta deviations, omega, Rama-Z) fail on a six-copy model; the geometry numbers above come from phenix.clashscore, rotalyze and ramalyze.",
   ],
   extra_files=[],
   reproduce="""bash tools/preprocessing.sh 7KR0 --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/Tff1b3f 6""",
   repro_note="The second command runs the lever order that produced this model without an agent; the chain scripts under `refinement/chains/` are the hand-scheduled originals. Seeds are fixed; the same inputs give the same trajectory."),
 "3TC7": dict(handle="T431c8e_gap", step="S0061", kind="a six-copy ensemble",
   short="Engineered protein, NESG target OR62",
   what="""Six complete copies of the protein (altlocs A to F), each at occupancy 1/6, refined together against the working
data with riding hydrogens, restraint weights wc 0.3 / wu 0.25, TLS (one group for the protein) over an isotropic
residual on every protein atom (the total ADP is written as ANISOU records) and isotropic waters. Every water is one
atom: a lettered water belongs to one copy, a water with a blank altloc is shared by all six. The ensemble is the
deliverable; it is not merged back into one model.

The model came from the deposited file in 66 recorded steps (S0000 to S0065), 15 of them accepted and 2 builds, in two
runs: the main run T431c8e up to the six-copy split (S0032) and, from S0033 on, its fork T431c8e_gap with looser gap
bounds (one-step widening of at most 0.010 and a cap of 0.12, against 0.002 and 0.030 in the main run), made because
the 0.002 bound refused every solvent lever on the ensemble. The lineage of S0061: a convergence step (S0003); riding
hydrogens (S0005); a two-copy split from shake (S0013, a build); three convergence steps (S0016, S0018, S0020); the
six-copy split from shake (S0032, a build); restraint weights 1 / 1 (S0033); isotropic protein ADPs in place of
anisotropic ones (S0039, −0.008); water picks at 4, 4 and 3σ on work-only difference maps (S0043, S0046, S0050);
restraint weights 0.3 / 0.25 (S0061). TLS with one group was accepted on a sibling of the lineage (S0047) and is in the
standing recipe from there on.""",
   caveats=[
    "**The gap is 0.0668** against 0.0382 for the deposited model and 0.0612 for the main run's best under the standing bounds (S0042, R-free 0.1540; its record is in `refinement/main_run_T431c8e/`). The fork's bounds let the gap widen by up to 0.010 in one step and cap it at 0.12; the operator judges the fork with the vault at the end.",
    "**Rotamer outliers 2.74 %** (36 of 1 314 residue copies) are above the gate's 1.5 % cap. The step passed because the count is within one outlier residue per copy of the control's (30), the tolerance rule of 2026-10-21. One Ramachandran outlier (0.4 %). Clashscore 6.8 against 2.9 deposited; the last step (weights 0.3 / 0.25) raised it from 2.8.",
    "Methionine as selenomethionine, with an anomalous group for Se (f' and f'' refined), was refused twice (S0038, S0042); the density at the SD sites is about a quarter of a selenium's. The residues stay MET.",
    "Six copies at 1.5 Å: the gate's control is the parent refined with the same seeds, so an accepted gain is relative to that control, not evidence that six copies are the right number for this entry. The two-copy model of the same run (S0020, R-free 0.1688) is in the record.",
   ],
   extra_files=[("`refinement/main_run_T431c8e/`", "the main run's own record after the fork point (its best S0042, R-free 0.1540, under the standing gap bounds)")],
   reproduce="""bash tools/preprocessing.sh 3TC7 --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/T431c8e 6          # to the six-copy split, S0032
bash scripts/fork_run.sh /home/dev/runs/hr/T431c8e /home/dev/runs/hr/T431c8e_gap
# set gap_widen_max 0.010 and gap_abs_max 0.12 in T431c8e_gap/metaparams.yaml, as scripts/fork_gap_after.sh does
bash scripts/chain_gap.sh /home/dev/runs/hr/T431c8e_gap 6""",
   repro_note="The levers whose logs are `chain_gb`, `chain_iso`, `chain_anisogb`, `chain_semet`, `chain_settle_r` and `chain_after_settle*` were scheduled from one-off scripts that are not in `scripts/`; their logs are included, and every command line of every step is in that step's `change.json` on the pod."),
 "1LZ8": dict(handle="Tee73c5", step="S0073", kind="a two-copy ensemble",
   short="Hen egg-white lysozyme, phased on the anomalous signal of S and Cl",
   what="""Two complete copies of the protein (altlocs A and B), each at occupancy 1/2, from a qFit split of the single
model (S0035), refined together with riding hydrogens, restraint weights wc 2 / wu 2, TLS (one group) over an isotropic
residual (the total ADP written as ANISOU records), optimised bulk-solvent mask radii and isotropic waters. Two chloride
ions placed at difference peaks (S0073) are single and at occupancy 1. A lettered water belongs to one copy, a blank one
to both.

The model came from the deposited file in 83 recorded steps (S0000 to S0082), 9 of them accepted and 3 builds. The
lineage of S0073: a convergence step (S0016); TLS, one group (S0020); a convergence step (S0032); the two-copy split
from qFit (S0035, a build); restraint weights 1 / 1 (S0053); the bulk-solvent mask radii optimised (S0060); a
convergence step (S0070); chloride ions at the two mFo−DFc peaks of 4σ and above that no atom explains, next to a
nitrogen (S0073; three waters removed). Restraint weights 2 / 2 were accepted on a sibling of the lineage (S0054) and
are in the standing recipe from there on.""",
   caveats=[
    "**The gap is 0.0746**, above the run's cap of 0.0714; the step passed because the control's gap (0.0754) was higher. The gap was 0.0802 for the deposited model and 0.0864 at the split (S0035); it has narrowed since.",
    "Clashscore 1.3 against 5.1 deposited; rotamer outliers 0.48 % (one residue copy); no Ramachandran outlier; 93.7 % favoured against 96.9 % for the deposited model.",
    "A six-copy fork of this run (Tee73c5_six) reached R-free 0.2627 and did not beat the two-copy model; a three-copy build (S0079) and the levers after it did not beat S0073 either. Both stay in the record; neither is released.",
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
    "The model has no hydrogens: riding hydrogens were refused in this run. Reference-model restraints (S0075 and the later re-test) were refused; a two-copy qFit build (S0069) and a six-copy fork (T40560e_six, R-free 0.3042) did not beat the single model. None of these is released.",
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
    "At 2.7 Å the picks, the hydrogens, the mask and the weight re-tests were all refused after S0057. A six-copy fork of this run (T9884ae_six) was still converging at R-free 0.2834 when this snapshot was taken; it is not released.",
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
    "A six-copy fork of this run (Tba97f6_six, R-free 0.2853) did not beat the single model and is not released. The sulfate pick (S0071), the mask, annealing, isotropic protein ADPs and the water picks were refused after S0062.",
   ],
   extra_files=[],
   reproduce="""bash tools/preprocessing.sh 9ARN --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/Tba97f6 6
bash scripts/chain_tls.sh /home/dev/runs/hr/Tba97f6 6""",
   repro_note="The chain scripts under `refinement/chains/` (chain_target, chain_tls, chain_arn2, chain_arn3, chain_coot, chain_ions, chain_more, chain_noise, chain_qfit) are the hand-scheduled originals with their logs; `chain_after_rota` and `followup` were one-off scripts, and every command line is in the step's `change.json` on the pod."),
 "7R2H": dict(handle="Ta4f3f9", step="S0019", kind="a six-copy ensemble",
   short="Cyclophilin D with DMSO",
   what="""Six complete copies of the protein (altlocs A to F), each at occupancy 1/6, refined together against the working
data with riding hydrogens, anisotropic ADPs on every protein atom and on most waters (191 of 1 637 isotropic),
restraint weights wc 0.3 / wu 0.25 and individual water occupancies. A lettered water belongs to one copy, a water with
a blank altloc to all six. The ligand is single. The ensemble is the deliverable; it is not merged back into one model.

The model came from the deposited file in 26 recorded steps (S0000 to S0025), 6 of them accepted and 1 build. The
lineage of S0019: restraint weights 0.3 / 0.25 (S0008); anisotropic water ADPs (S0012, −0.011); the six-copy split from
shake (S0014, a build, −0.010); water picks at 4σ three times (S0015, S0016, S0017) and at 2.5σ (S0019) on work-only
difference maps. The run continues: the water re-letter, the copy votes and a convergence step were running when this
snapshot was taken, with a fork under looser gap bounds queued after them.""",
   caveats=[
    "**The gap is 0.0300**, at the run's cap of 0.030, against 0.0106 for the deposited model. The two picks after S0019 were refused on the gap rule (S0020, S0024); the queued fork loosens the bound for the operator to judge with the vault.",
    "Clashscore 7.8 against 0.0 for the deposited file (which carries its own hydrogens); rotamer outliers 1.0 % (deposited 0.0 %); no Ramachandran outlier, 93.8 % favoured.",
    "Six copies at 0.79 Å: 16 461 atoms against 2 850 deposited. The deposited model scores 0.1551 on our flags and 0.1355 after the common recipe (S0001); the header reports 0.1549 on its own flags.",
   ],
   extra_files=[],
   reproduce="""bash tools/preprocessing.sh 7R2H --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/Ta4f3f9 6""",
   repro_note="`chain_target.sh` is the one chain of this run; its log is `refinement/chains/chain_target_Ta4f3f9.log`."),
 "8C5N": dict(handle="T5f59f1", step="S0027", kind="a six-copy ensemble",
   short="Chitin-binding protein D (CbpD) from Pseudomonas aeruginosa",
   what="""Six complete copies of the protein (altlocs A to F), each at occupancy 1/6, refined together against the working
data with riding hydrogens, anisotropic ADPs on every protein atom and every water (1 443), restraint weights wc 0.3 /
wu 0.25 and individual water occupancies. A lettered water belongs to one copy, a water with a blank altloc to all six.
Ligands and ions are single. The ensemble is the deliverable; it is not merged back into one model.

The model came from the deposited file in 29 recorded steps (S0000 to S0028), 7 of them accepted and 1 build. The
lineage of S0027: restraint weights 0.3 / 0.25 (S0008); anisotropic water ADPs (S0012, −0.006); the six-copy split from
shake (S0014, a build, −0.017); water picks at 4, 4 and 3σ on work-only difference maps (S0015, S0016, S0018);
anisotropic water ADPs again (S0021); waters in own-copy clashes moved to a copy they clear (S0027: 17 of 36 clashing
waters re-lettered, nothing deleted). The run continues: a convergence step was running when this snapshot was taken,
with a fork under looser gap bounds queued after it.""",
   caveats=[
    "**The gap is 0.0233** against 0.0092 for the deposited model (the run's cap 0.030).",
    "Clashscore 8.8 against 7.0 deposited (the re-letter step brought it down from 9.4); rotamer outliers 1.3 % (deposited 2.3 %); no Ramachandran outlier.",
    "Six copies at 0.75 Å: 17 842 atoms against 2 850 deposited. The copy-vote step (S0028) was refused. The deposited model scores 0.1571 on our flags and 0.1294 after the common recipe (S0001); the header reports 0.1634 on its own flags.",
   ],
   extra_files=[],
   reproduce="""bash tools/preprocessing.sh 8C5N --runs /home/dev/runs/hr --seeds 3 --nproc 3
bash scripts/chain_target.sh /home/dev/runs/hr/T5f59f1 6""",
   repro_note="`chain_target.sh` is the one chain of this run; its log is `refinement/chains/chain_target_T5f59f1.log`."),
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
    status = ("**Status: improved.** The released model is %s with an R-free of %.4f on the deposited free set. The re-refined "
              "deposited model (S0001, the common recipe) scores %.4f and the deposited model as scored (S0000) %.4f on the same "
              "reflections." % (c["kind"], a["r_free"], base["r_free"], dep["r_free"]))
    if tid in RUNNING:
        status += " The run continues; this is the model in force on 2026-10-21."
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
     ("Copies",) + tuple(copies(m) for m in (dep, base, a)),
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
    vault_cav = c.get("vault_caveat") or ("**The vault has not been read in this run** (%s work reflections, sealed at preprocessing; `run.json` carries the checksums). No decision used held-out reflections of any kind, and every map that placed an atom excluded the free set, but the gains have not been checked against the vault. That read is the operator's." % fmt_int(n_vault))
    out = ["# %s — %s" % (tid, title), "", status, "", "| | |", "|---|---|"]
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
            "The gate judged every change against a control, the parent refined with the same command and seeds, and accepted a",
            "change only when R-free fell by at least 2σ of the run's noise floor with the gap and the geometry inside their bounds.",
            "`refinement/steps.md` lists every step with its verdict and `refinement/score_history.txt` is the hash-chained record",
            "the gate wrote.", "", "## Caveats", "", "- " + vault_cav]
    out += ["- " + x for x in c["caveats"]]
    out += ["", "## Files", "", "| Path | Content |", "|---|---|"] + ["| %s | %s |" % f for f in files]
    out += ["", "## Reproduce", "", "In the harness checkout on the pod (`docs/POD.md` there):", "", "```", c["reproduce"], "```", "", c["repro_note"], ""]
    (t / "README.md").write_text("\n".join(out))
    return dict(id=tid, res=res, title=c["short"], dep=dep, base=base, a=a, step=c["step"], kind=c["kind"], handle=c["handle"], utc=utc)

def splice(text, name, body):
    m = re.search(r"(<!-- %s:begin -->\n)(.*?)(<!-- %s:end -->)" % (name, name), text, re.S)
    if not m:
        raise SystemExit("README.md: no %s markers" % name)
    return text[:m.end(1)] + body + text[m.start(3):]

def main():
    info = sorted((card(tid, c) for tid, c in T.items()), key=lambda x: x["res"])
    r1 = ["| Target | Res. (Å) | Entry | Re-refined, our flags (full / report) | This release (full / report) | Δ full | R-work (re-refined → ours) | Gap (re-refined → ours) | Model | Status |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    r2 = ["| Target | Clashscore | Rotamer outliers % | Ramachandran outliers % | Ramachandran favoured % | Bond RMSD (Å) | Angle RMSD (°) | MolProbity score |",
          "|---|---|---|---|---|---|---|---|"]
    for i in info:
        b, a = i["base"], i["a"]
        r1.append("| [%s](targets/%s/README.md) | %g | %s | %.4f / %.4f | **%.4f / %.4f** | −%.4f | %.4f → %.4f | %.4f → %.4f | %s, step %s | improved |" % (
            i["id"], i["id"], i["res"], i["title"], b["r_free"], b["r_free_report"], a["r_free"], a["r_free_report"], b["r_free"] - a["r_free"],
            b["r_work"], a["r_work"], b["gap"], a["gap"], i["kind"].replace("a ", ""), i["step"]))
        arrow = lambda k, f: "%s → %s" % (num(b.get(k), f), num(a.get(k), f))
        r2.append("| [%s](targets/%s/README.md) | %s | %s | %s | %s | %s | %s | %s → %s |" % (
            i["id"], i["id"], arrow("clashscore", "%.1f"), arrow("rota_pct", "%.2f"), arrow("rama_outliers_pct", "%.1f"), arrow("rama_favored_pct", "%.1f"),
            arrow("bond_rmsd", "%.3f"), arrow("angle_rmsd", "%.2f"), num(molprobity(b), "%.2f"), num(molprobity(a), "%.2f")))
    readme = (ROOT / "README.md").read_text()
    readme = splice(readme, "results-table", "\n".join(r1) + "\n")
    readme = splice(readme, "geometry-table", "\n".join(r2) + "\n")
    (ROOT / "README.md").write_text(readme)
    prov = load(ROOT / "provenance.json")
    prov["exported_at"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    prov["baseline"] = "S0001: the deposited model after the common recipe (phenix.refine, 10 macro-cycles, three seeds, the median); every comparison in the cards and the README is against it (operator, meeting of 2026-10-21)"
    for i in info:
        rec = prov["released"].setdefault(i["id"], {})
        rec.update({"run_handle": i["handle"], "step": i["step"], "utc": i["utc"]})
        rec.setdefault("vault_last_read", "never in this run")
        rec["rerefined_r_free_S0001"] = round(i["base"]["r_free"], 5)
    (ROOT / "provenance.json").write_text(json.dumps(prov, indent=1) + "\n")
    print("cards written:", [i["id"] for i in info])

main()
