"""Stage representations/7KR0/ (the E035 Untangler line) on the campaign pod.

Copies the frozen six-copy models and their map-coefficient MTZ, re-scores every model in the table with the
independent scorer (scripts/verify/indep_rfree.py, verbatim), records composition (copies, occupancy per copy, atoms,
water atoms, summed water occupancy, ANISOU count), copies each stage's TRAJECTORY.md / result.json / score logs, hashes
everything and writes a tarball. Read-only on the campaign: it only writes under STAGE.

Usage (pod, phenix env sourced): python3 stage_representations_on_pod.py <STAGE>
"""
import glob, hashlib, json, os, shutil, subprocess, sys, tarfile, time

STAGE = sys.argv[1]
OUT = os.path.join(STAGE, "representations", "7KR0")
E = "/home/dev/runs/7KR0/experiments"
T = "/home/dev/data/targets/7KR0"
SCORER = "/home/dev/workspace/scripts/verify/indep_rfree.py"
SCORER_SHA = "c6a4a73973b6574703713e4ea4692c3c1acd860c752385c30471aae6177cf32b"  # == scripts/indep_rfree.py in the release
UNTANGLER = "/home/dev/tools/Untangler"
for d in ("models", "scores", "trajectories", "_work"):
    os.makedirs(os.path.join(OUT, d), exist_ok=True)
LOG = open(os.path.join(STAGE, "stage_representations.log"), "a")


def log(*a):
    s = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()) + " " + " ".join(str(x) for x in a)
    print(s, flush=True); LOG.write(s + "\n"); LOG.flush()


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""): h.update(c)
    return h.hexdigest()


def cp(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copy2(src, dst); return dst


assert sha(SCORER) == SCORER_SHA, "independent scorer changed on the pod"

# ---------- which models ----------
def endpoints(stage_dir):
    r = json.load(open(f"{E}/{stage_dir}/result.json"))
    out = []
    for rep, arms in sorted((r.get("endpoints") or {}).items()):
        v = arms.get("T")
        if v: out.append((rep, v))
    return out

REP_ARM = {"1": "T", "2": "T_r2", "3": "T_r3"}
rows = []  # id, stage, arm, what, model, mtz, freeze
rows.append(dict(id="ref_44PS", stage="reference", arm="", what="44PS as deposited (Passmore et al. 2026), six conformations",
                 model="/home/dev/data/raw/44PS/44PS.cif", mtz=None, freeze=False))
cur = json.load(open("/home/dev/state/current/7KR0.json"))
rows.append(dict(id="ctx_7KR0_deposited", stage="context", arm="", what="7KR0 as deposited (qFit multiconformer, single model)",
                 model="/home/dev/data/raw/7KR0/7KR0.cif", mtz=None, freeze=False))
rows.append(dict(id="ctx_7KR0_deliverable", stage="context", arm="", what="7KR0 standing single-model deliverable (targets/7KR0)",
                 model=cur["model"], mtz=None, freeze=False))
for rep, v in endpoints("e035_untangler"):
    arm = REP_ARM[rep]
    rows.append(dict(id=f"E035_{arm}_loop{v['loop']}", stage="E035", arm=arm,
                     what=f"stage 1 connectivity loop, endpoint by the pre-registered rule (loop {v['loop']}{', provisional' if v.get('provisional') else ''})",
                     model=v["model"], mtz=None, freeze=False))
for rep, v in endpoints("e035f_stage2p"):
    arm = REP_ARM[rep]; k = v["loop"]
    rows.append(dict(id=f"E035f_{arm}_k{k}", stage="E035f", arm=arm,
                     what=f"stage 2 with the harness picker, endpoint by the pre-registered rule (slot {k}{', provisional' if v.get('provisional') else ''})",
                     model=v["model"], mtz=None, freeze=False))
for arm in ("T", "T_r2", "T_r3"):
    o = f"{E}/e035c2_stage3/arms/{arm}/Untangler/output"
    assert sha(f"{o}/7KR0_6conf_B0_current8.pdb") == sha(f"{o}/7KR0_6conf_B0_loopEnd7.pdb")
    rows.append(dict(id=f"E035c2_{arm}_cycle3", stage="E035c", arm=arm,
                     what="automated stage-3 cycle, cycle 3 (converged; N = 3)",
                     model=f"{o}/7KR0_6conf_B0_current8.pdb", mtz=f"{o}/7KR0_6conf_B0_loopEnd7-1.mtz", freeze=True))
for arm in ("T", "T_r2", "T_r3"):
    rows.append(dict(id=f"E035d_{arm}_aniso", stage="E035d", arm=arm,
                     what="anisotropic-B finish on the E035c cycle-3 model (convert, 10 mc B only)",
                     model=f"{E}/e035d_aniso/aniso/{arm}_aniso/aniso_final.pdb",
                     mtz=f"{E}/e035d_aniso/arms/{arm}_aniso/Untangler/output/aniso_{arm}_aniso.mtz", freeze=True))
# E041 line R (replication from 7KR0: conformation-aware per-copy waters, anisotropic waters, weight stack, clash cleanup).
# Occupancies already 0.1667 x4 + 0.1666 x2 in these files (E041 environment note 1), freeze=True copies the files into the release.
E41 = f"{E}/e041_44ps/phaseA"
for rid, what in (("R4_S", "line R best R-free: H2_T r1s7 loop + weight stack (wc 0.3, -u 0.25), 10 mc; clashscore 26.7"),
                  ("CJ_R4_p2", "line R after two clash-cleanup passes on R4_S (water copies on own-conformer H removed, 6 mc each); clashscore 4.5"),
                  ("CJ_R4_polish", "CJ_R4_p2 after a 10 mc polish at wc 0.5, -u 0.25; clashscore 4.4")):
    p = f"{E41}/{rid}/e041_{rid}.pdb"
    if os.path.exists(p):
        rows.append(dict(id=f"E041_{rid}", stage="E041", arm="R", what=what, model=p, mtz=None, freeze=True))
for arm in ("T", "T_r2", "T_r3"):
    o = f"{E}/e035d_post/arms/{arm}/Untangler/output"
    if os.path.exists(f"{o}/7KR0_6conf_B0_loopEnd4.pdb"):
        rows.append(dict(id=f"E035d_post_{arm}_loopEnd4", stage="E035d step 2", arm=arm,
                         what="two stage-3 cycles after the anisotropic finish (last closing loop)",
                         model=f"{o}/7KR0_6conf_B0_loopEnd4.pdb", mtz=None, freeze=False))

# E048 / E049 (2026-10-09): blind replications of line R from the deposited 7KR0 qFit model, no reference (44PS never an input).
# E048 = the E044 harness driver; E049 = scripts/portable/sixcopy_waters.py (one phenix.python file). Both runs were still
# going when staged; the rows are the model in force at staging time, labelled with the round. freeze=True copies the files.
E49 = f"{E}/e049_portable/steps"
for rid, p, what in (("E049_r1_aniso_water", f"{E49}/r1_aniso_water/cand_s2.pdb", "portable script, end of round 1 (3 sigma pick 224 sites + anisotropic waters); clashscore 4.7, rotamers 1.3 %"),
                     ("E049_r2_aniso_water", f"{E49}/r2_aniso_water/cand_s1.pdb", "portable script, end of round 2 (2.5 sigma pick + clash cleanup, anisotropic waters); clashscore 4.5, rotamers 1.3 %"),
                     ("E049_r3_pick_cleanup", f"{E49}/r3_pick_cleanup/cand_s2.pdb", "portable script, end of round 3 (2.5 sigma pick + clash cleanup; aniso refused); clashscore 4.6, rotamers 1.2 %"),
                     ("E049_r4_pick", f"{E49}/r4_pick/cand_s2.pdb", "portable script, end of round 4 (2.5 sigma pick, 99 sites; aniso refused), run still going; clashscore 4.9, rotamers 1.2 %")):
    if os.path.exists(p):
        rows.append(dict(id=rid, stage="E049", arm="portable", what=what, model=p, mtz=None, freeze=True))
E48 = f"{E}/e048_autosix/shaken_s02_dep/steps"
for rid, p, what in (("E048_r2_aniso_water", f"{E48}/r2_aniso_water/cand_s3.pdb", "E044 driver, end of round 2 (cleanup, 2.5 sigma pick, anisotropic waters; connectivity loop refused), run still going; clashscore 4.6"),):
    if os.path.exists(p):
        rows.append(dict(id=rid, stage="E048", arm="driver", what=what, model=p, mtz=None, freeze=True))

# E049 final (round 5): the all-data endpoint of the portable script, scored on the same basis as the rows above (data.mtz, 8 712 free).
for rid, p, what in (("E049_r5_pick", f"{E}/e049_portable/models/r5_pick.pdb", "portable script, final model (end of round 5, 2.5 sigma pick; run ended at three rounds without an adoption after it); maps included the free reflections (D582); clashscore 4.9, rotamers 1.2 %"),):
    if os.path.exists(p):
        rows.append(dict(id=rid, stage="E049", arm="portable", what=what, model=p, mtz=None, freeze=True))

# Clean reruns of the portable script (2026-10-11/12; D582 work-only decision maps, D584/D585 no sleep reflection in any program's
# input, D587 bunker = 2 % of the work reflections held outside every working file). These runs were judged on the portable script's
# own select / report / sleep thirds (sixcopy_waters.py split_seed; NOT the harness's split_v2 partition, D605). They are scored here
# on the run's own no-sleep working file — e063_single/prep/data_flags.mtz (172 020 rows: FP, SIGFP, R-free-flags; sleep and bunker
# rows absent) as data and flags, with split.mtz restricted to those rows (score_clean_runsplit/split_nosleep.mtz: SPLIT 1 and 2 only).
# "R-free full" for these rows is therefore R over the select + report thirds (5 808 reflections); the sleep-third value quoted in the
# row text is the run's one logged read (run.json sleep_consultations). The sleep third is never scored here.
CLEAN = dict(data=f"{E}/e063_single/prep/data_flags.mtz", flags=f"{E}/e063_single/prep/data_flags.mtz",
             split=f"{E}/score_clean_runsplit/split_nosleep.mtz")
for rid, p, what in (
    ("E051b_final", f"{E}/e051b_workonly/models/final.pdb",
     "clean rerun (work-only maps, sleep third withheld), end of round 3: 4 sigma picks of 121 and 90 sites + anisotropic waters, every 3 sigma pick refused on the R-gap bound; R-free here = select + report thirds (5 808); sleep third 0.0850 (one logged read); clashscore 4.7, rotamers 1.4 %"),
    ("E059_final", f"{E}/e059_bunker/models/final.pdb",
     "clean rerun with the bunker, end of round 1 (4 sigma pick of 121 sites + anisotropic waters; the round-3 pick refused under a three-seed sigma, D594); R-free here = select + report thirds; sleep third 0.0886, bunker R 0.0946 (one logged read); clashscore 4.0, rotamers 1.2 %"),
    ("E062_final", f"{E}/e062_halfmap/models/final.pdb",
     "clean rerun with the bunker, six light copies per peak with a site-occupancy cap, end of round 3 (3 sigma picks; the 2.5 sigma composite pick + clash cleanup refused at z -1.3); R-free here = select + report thirds; sleep third 0.0837, bunker R 0.0902 (one logged read); clashscore 4.9, rotamers 1.3 %"),
    ("E063_final", f"{E}/e063_single/models/final.pdb",
     "clean rerun with the bunker, one labelled water per peak, end of round 2 (3 sigma pick of 235 waters on the E059 round-1 model; every later rung refused: 2.5 sigma, a second 3 sigma pass, 4 sigma, at start occupancy 0.33 and 0.10); R-free here = select + report thirds; sleep third 0.0856, bunker R 0.0874 (one logged read); clashscore 4.6, rotamers 1.2 %; the record until D607"),
    ("E066_final", f"{E}/e066_mc20/models/final.pdb",
     "clean rerun with the bunker: E063's round-2 model with anisotropic waters refined for twenty macro-cycles per arm (the same step refused at ten cycles, z -1.9; adopted at twenty, z -2.7), end of round 3 (a 4 sigma pick at twenty cycles refused, z -0.2; stopped after three rounds without adoption); R-free here = select + report thirds; sleep third 0.0824, bunker R 0.0836 (one logged read, 2026-10-12T11:05Z); clashscore 5.0, rotamers 1.2 % - the clean record (D607)"),
    ("E049_r5_pick_clean_basis", f"{E}/e049_portable/models/r5_pick.pdb",
     "the E049 final model (same file as E049_r5_pick) scored on the clean rows' reflections (select + report thirds, 5 808) for the like-for-like: the all-data maps' advantage on identical reflections"),
):
    if os.path.exists(p):
        rows.append(dict(id=rid, stage="clean" if rid != "E049_r5_pick_clean_basis" else "E049", arm="portable", what=what,
                         model=p, mtz=None, freeze=(rid != "E049_r5_pick_clean_basis"), **CLEAN))

# ---------- composition helper (phenix.python) ----------
COMP_PY = r'''
import json, sys, collections
import iotbx.pdb
p, out = sys.argv[1:3]
inp = iotbx.pdb.input(file_name=p)
h = inp.construct_hierarchy()
W = ("HOH", "WAT", "DOD")
n_wat = 0; occ_wat = 0.0; n_aniso = 0; n_atoms = 0; n_h = 0
occ_by_alt = collections.defaultdict(list); site_sum = collections.defaultdict(float)
for rg in h.residue_groups():
    for ag in rg.atom_groups():
        water = ag.resname.strip() in W
        for a in ag.atoms():
            n_atoms += 1
            el = a.element.strip().upper()
            if a.uij_is_defined(): n_aniso += 1
            if el in ("H", "D"): n_h += 1; continue
            if water:
                n_wat += 1; occ_wat += a.occ
            else:
                occ_by_alt[ag.altloc.strip() or "_"].append(a.occ)
                site_sum[(rg.parent().id, rg.resseq, rg.icode, a.name.strip())] += a.occ
sums = list(site_sum.values())
res = {"model": p, "n_atoms": n_atoms, "n_hydrogen": n_h, "n_anisou": n_aniso,
       "altlocs": sorted(k for k in occ_by_alt if k != "_"),
       "n_water_atoms": n_wat, "water_occupancy_sum": round(occ_wat, 3),
       "protein_occupancy_per_copy": {k: round(sum(v) / len(v), 4) for k, v in sorted(occ_by_alt.items())},
       "protein_site_occupancy_sum_min": round(min(sums), 3) if sums else None,
       "protein_site_occupancy_sum_max": round(max(sums), 3) if sums else None}
json.dump(res, open(out, "w"), indent=1); print(json.dumps(res))
'''
MTZ_PY = r'''
import json, sys
from iotbx import mtz
o = mtz.object(sys.argv[1])
print(json.dumps({"columns": [c.label() for c in o.columns()], "n_reflections": o.n_reflections()}))
'''
open(os.path.join(OUT, "_work", "composition.py"), "w").write(COMP_PY)
open(os.path.join(OUT, "_work", "mtz_columns.py"), "w").write(MTZ_PY)

def run(argv, logpath):
    with open(logpath, "w") as lf:
        lf.write("# " + " ".join(argv) + "\n"); lf.flush()
        return subprocess.run(argv, stdout=lf, stderr=subprocess.STDOUT).returncode

table = []
for r in rows:
    log("scoring", r["id"], r["model"])
    src_sha = sha(r["model"])
    sj = os.path.join(OUT, "scores", r["id"] + ".json")
    data, flags, split = r.get("data", f"{T}/data.mtz"), r.get("flags", f"{T}/flags.mtz"), r.get("split", f"{T}/split.mtz")
    rc = run(["phenix.python", SCORER, r["model"], data, flags, split, sj],
             os.path.join(OUT, "_work", r["id"] + ".indep.log"))
    if rc != 0: raise SystemExit(f"scorer failed on {r['model']}")
    cj = os.path.join(OUT, "scores", r["id"] + ".composition.json")
    rc = run(["phenix.python", os.path.join(OUT, "_work", "composition.py"), r["model"], cj],
             os.path.join(OUT, "_work", r["id"] + ".comp.log"))
    if rc != 0: raise SystemExit(f"composition failed on {r['model']}")
    entry = dict(r, model_sha256=src_sha, model_bytes=os.path.getsize(r["model"]),
                 score_json=f"scores/{r['id']}.json", composition_json=f"scores/{r['id']}.composition.json",
                 scored_on={"data": data, "flags": flags, "split": split,
                            "basis": "run thirds, sleep withheld (5 808 free)" if "data" in r else "frozen target files (8 712 free)"})
    if r["freeze"]:
        ext = os.path.splitext(r["model"])[1]
        dst = os.path.join(OUT, "models", r["id"] + ext); cp(r["model"], dst)
        assert sha(dst) == src_sha
        entry["frozen_model"] = f"models/{r['id']}{ext}"
        if r["mtz"] and os.path.exists(r["mtz"]):
            dm = os.path.join(OUT, "models", r["id"] + "_map_coeffs.mtz"); cp(r["mtz"], dm)
            entry["frozen_mtz"] = f"models/{r['id']}_map_coeffs.mtz"; entry["mtz_sha256"] = sha(r["mtz"])
            entry["mtz_bytes"] = os.path.getsize(r["mtz"])
            cols = subprocess.run(["phenix.python", os.path.join(OUT, "_work", "mtz_columns.py"), r["mtz"]],
                                  capture_output=True, text=True).stdout.strip().splitlines()[-1]
            entry["mtz_columns"] = json.loads(cols)
    table.append(entry)

# the 44PS score recorded on 2026-10-03 (E041 registration), kept verbatim next to the fresh one
cp(f"{E}/score_44PS/44PS_on_our_flags.json", os.path.join(OUT, "scores", "ref_44PS.e041_20261003.json"))

# ---------- trajectories ----------
TR = os.path.join(OUT, "trajectories")
for stage, files in {
    "e035_untangler": ["TRAJECTORY.md", "result.json", "PROVENANCE.txt"],
    "e035b_stage2": ["TRAJECTORY.md", "result.json"],
    "e035f_stage2p": ["TRAJECTORY.md", "result.json"],
    "e035c_stage3": ["TRAJECTORY.md", "result.json"],
    "e035c2_stage3": ["README.txt", "logs/cycle3_scores.txt"],
    "e035d_aniso": ["README.txt", "logs/aniso_scores.txt", "aniso/T_aniso/command.txt"],
    "e035d_post": ["README.txt"],
    "e049_portable": ["TRAJECTORY.md", "launch.log", "run.json", "scripts/sixcopy_waters.py", "verify/r2_pick_cleanup_s1.summary.txt"],
    "e048_autosix/shaken_s02_dep": ["TRAJECTORY.md", "DECISIONS.md", "state.json"],
    "e051b_workonly": ["TRAJECTORY.md", "launch.log", "launch.out", "run.json", "scripts/sixcopy_waters.py"],
    "e059_bunker": ["TRAJECTORY.md", "launch.log", "launch.out", "run.json", "scripts/sixcopy_waters.py", "vault/bunker.json"],
    "e062_halfmap": ["TRAJECTORY.md", "launch.out", "run.json", "scripts/sixcopy_waters.py", "vault/bunker.json"],
    "e063_single": ["TRAJECTORY.md", "launch.out", "run.json", "run.json.e059b_snapshot", "scripts/sixcopy_waters.py", "vault/bunker.json"],
    "e066_mc20": ["TRAJECTORY.md", "launch.out", "run.json", "scripts/sixcopy_waters.py", "vault/bunker.json"],
}.items():
    for f in files:
        p = f"{E}/{stage}/{f}"
        if os.path.exists(p): cp(p, os.path.join(TR, stage, f.replace("/", "__")))
        else: log("missing trajectory file", p)

# ---------- provenance ----------
def out(argv, cwd=None):
    try: return subprocess.run(argv, capture_output=True, text=True, cwd=cwd).stdout.strip()
    except Exception as e: return str(e)
patches = {}
for p in sorted(glob.glob(f"{E}/e035*/scripts/untangler_patch.sh")) + ["/home/dev/workspace/scripts/experiments/untangler_patch.sh"]:
    patches[p] = sha(p)
shutil.rmtree(os.path.join(OUT, "_work"), ignore_errors=True)
files = []
for root, _, fs in os.walk(OUT):
    for f in fs:
        p = os.path.join(root, f)
        files.append({"file": os.path.relpath(p, OUT), "sha256": sha(p), "bytes": os.path.getsize(p)})
files.sort(key=lambda m: m["file"])
prov = {
    "exported_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "pod_hostname": os.uname().nodename,
    "phenix_version": " ".join(l.strip() for l in out(["phenix.version"]).splitlines() if "Version" in l or "Release" in l),
    "untangler": {"path": UNTANGLER, "remote": out(["git", "remote", "get-url", "origin"], UNTANGLER),
                  "branch": "conformational_tree", "commit": out(["git", "rev-parse", "HEAD"], UNTANGLER)},
    "untangler_patch_scripts_sha256": patches,
    "independent_scorer": {"path": SCORER, "sha256": SCORER_SHA, "argv": "phenix.python indep_rfree.py <model> data.mtz flags.mtz split.mtz <out.json>"},
    "frozen_data": {n: {"path": f"{T}/{n}", "sha256": sha(f"{T}/{n}")} for n in ("data.mtz", "flags.mtz", "split.mtz")},
    "clean_rows_scoring_inputs": {k: {"path": v, "sha256": sha(v)} for k, v in CLEAN.items() if os.path.exists(v)},
    "merged_data_flags_mtz_used_by_untangler": {"path": f"{E}/e035_untangler/data/7KR0_data_flags.mtz",
                                                 "sha256": sha(f"{E}/e035_untangler/data/7KR0_data_flags.mtz")},
    "rows": table,
    "files": files,
}
json.dump(prov, open(os.path.join(OUT, "provenance_pod.json"), "w"), indent=1)
tar = STAGE.rstrip("/") + ".tar.gz"
with tarfile.open(tar, "w:gz") as t:
    t.add(os.path.join(STAGE, "representations"), arcname="agrp_rep/representations")
log("TARBALL", tar, os.path.getsize(tar), sha(tar))
print("DONE", sha(tar))
