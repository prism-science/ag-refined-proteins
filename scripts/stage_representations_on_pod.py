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
SCORER_SHA = "1899241e4e1da2b8281b47fa6e144eabcdc411b4602e9237710c2f4b1e76de46"  # == scripts/indep_rfree.py in the release
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
for arm in ("T", "T_r2", "T_r3"):
    o = f"{E}/e035d_post/arms/{arm}/Untangler/output"
    if os.path.exists(f"{o}/7KR0_6conf_B0_loopEnd4.pdb"):
        rows.append(dict(id=f"E035d_post_{arm}_loopEnd4", stage="E035d step 2", arm=arm,
                         what="two stage-3 cycles after the anisotropic finish (last closing loop)",
                         model=f"{o}/7KR0_6conf_B0_loopEnd4.pdb", mtz=None, freeze=False))

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
    rc = run(["phenix.python", SCORER, r["model"], f"{T}/data.mtz", f"{T}/flags.mtz", f"{T}/split.mtz", sj],
             os.path.join(OUT, "_work", r["id"] + ".indep.log"))
    if rc != 0: raise SystemExit(f"scorer failed on {r['model']}")
    cj = os.path.join(OUT, "scores", r["id"] + ".composition.json")
    rc = run(["phenix.python", os.path.join(OUT, "_work", "composition.py"), r["model"], cj],
             os.path.join(OUT, "_work", r["id"] + ".comp.log"))
    if rc != 0: raise SystemExit(f"composition failed on {r['model']}")
    entry = dict(r, model_sha256=src_sha, model_bytes=os.path.getsize(r["model"]),
                 score_json=f"scores/{r['id']}.json", composition_json=f"scores/{r['id']}.composition.json")
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
