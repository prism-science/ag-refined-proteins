"""Stage the ag-refined-proteins release on the pod.

For every standing deliverable (state/current/<ID>.json): copy the model, map coefficients, frozen data and flags,
deposited model, refinement record, campaign validation and per-target ledger rows into STAGE/targets/<ID>/; run a
uniform release-time validation (independent scorer, phenix.model_vs_data, phenix.molprobity) on the deposited and
refined model of every target; hash everything; tar. Usage (pod, phenix env sourced): python3 agrp_stage.py <STAGE>
"""
import csv, glob, hashlib, json, os, re, shutil, sqlite3, subprocess, sys, tarfile, time
from concurrent.futures import ThreadPoolExecutor

STAGE = sys.argv[1]
CUR = "/home/dev/state/current"; RUNS = "/home/dev/runs"; DATA = "/home/dev/data"; STATE = "/home/dev/state"
VERIFY_DIRS = sorted(glob.glob(f"{RUNS}/verify_*"))
os.makedirs(STAGE, exist_ok=True)
LOG = open(os.path.join(STAGE, "stage.log"), "a")
def log(*a):
    s = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()) + " " + " ".join(str(x) for x in a)
    print(s, flush=True); LOG.write(s + "\n"); LOG.flush()

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""): h.update(c)
    return h.hexdigest()

def cp(src, dst, required=True):
    if not os.path.exists(src):
        if required: raise SystemExit(f"MISSING {src}")
        return None
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst); return dst

def run(argv, cwd, logpath, timeout=3600):
    with open(logpath, "w") as lf:
        lf.write("# " + " ".join(argv) + "\n"); lf.flush()
        r = subprocess.run(argv, cwd=cwd, stdout=lf, stderr=subprocess.STDOUT, timeout=timeout)
    return r.returncode

# ---------- helpers written for phenix.python ----------
MERGE_PY = r'''
import sys
from iotbx.reflection_file_reader import any_reflection_file
data_mtz, flags_mtz, out = sys.argv[1:4]
arrs = any_reflection_file(data_mtz).as_miller_arrays()
obs = next((m for m in arrs if m.info().label_string().startswith("FP")), None)
root = "FP"
if obs is None:
    obs = next(m for m in arrs if m.info().label_string().startswith("IMEAN")); root = "IMEAN"
flags = next(m for m in any_reflection_file(flags_mtz).as_miller_arrays() if "R-free-flags" in m.info().labels)
obs, flags = obs.common_sets(flags)
ds = obs.as_mtz_dataset(column_root_label=root)
ds.add_miller_array(flags, column_root_label="R-free-flags")
ds.mtz_object().write(out)
print("wrote", out, root, obs.size(), "reflections;", (flags.data() == 0).count(True), "free")
'''
INDEP_PY = open("/home/dev/runs/verify_20260917/indep_rfree.py").read()   # the campaign's independent scorer, verbatim
HELPERS = os.path.join(STAGE, "_helpers"); os.makedirs(HELPERS, exist_ok=True)
open(os.path.join(HELPERS, "merge_mtz.py"), "w").write(MERGE_PY)
open(os.path.join(HELPERS, "indep_rfree.py"), "w").write(INDEP_PY)

# ---------- ledger ----------
con = sqlite3.connect(f"{STATE}/ledger.sqlite"); con.row_factory = sqlite3.Row
def export(table, where, args, dst):
    rows = [dict(r) for r in con.execute(f"select * from {table} where {where}", args)]
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    cols = [d[1] for d in con.execute(f"pragma table_info({table})")]
    with open(dst, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
        for r in rows: w.writerow(r)
    return len(rows)

# ---------- per-target staging ----------
targets = sorted(os.path.basename(p)[:-5] for p in glob.glob(f"{CUR}/*.json"))
records = {}
for T in targets:
    rec = json.load(open(f"{CUR}/{T}.json")); records[T] = rec
    model = rec["model"]; mdir = os.path.dirname(model)
    D = os.path.join(STAGE, "targets", T)
    log(T, "staging from", mdir)
    # model
    cp(model, f"{D}/model/{T}_refined.cif")
    cp(model[:-4] + ".pdb", f"{D}/model/{T}_refined.pdb")
    # map coefficients
    maps = rec.get("maps_mtz") or (model[:-4] + ".mtz")
    cp(maps, f"{D}/maps/{T}_refined_map_coeffs.mtz")
    # frozen data
    for name in ("data.mtz", "flags.mtz", "split.mtz"):
        cp(f"{DATA}/targets/{T}/{name}", f"{D}/data/{T}_{name}")
    for name in ("split.json", "prep.json"):
        cp(f"{DATA}/targets/{T}/{name}", f"{D}/data/{name}")
    # deposited
    cp(f"{DATA}/raw/{T}/{T}.cif", f"{D}/deposited/{T}.cif")
    cp(f"{DATA}/raw/{T}/{T}.fasta", f"{D}/deposited/{T}.fasta", required=False)
    cp(f"{DATA}/raw/{T}/rcsb_entry.json", f"{D}/deposited/rcsb_entry.json")
    cp(f"{DATA}/raw/{T}/FETCHED", f"{D}/deposited/FETCHED", required=False)
    cp(f"{DATA}/raw/{T}/MANIFEST.sha256", f"{D}/deposited/fetch_manifest.sha256", required=False)
    # refinement record
    cp(f"{CUR}/{T}.json", f"{D}/refinement/current.json")
    for name in ("command.txt", "refine_001.eff", "refine_001.log", "refine_decisions.json", "refine_result.json"):
        cp(f"{mdir}/{name}", f"{D}/refinement/{name}", required=(name != "refine_001.eff"))
    cp(f"{mdir}/model_vs_data/model_vs_data.stdout.log", f"{D}/refinement/model_vs_data.campaign.log", required=False)
    cp(f"{mdir}/cycle_row.json", f"{D}/validation/campaign/cycle_row.json", required=False)
    for name in ("molprobity.out", "molprobity_result.json", "clash_altloc.json", "clashscore.json"):
        cp(f"{mdir}/{name}", f"{D}/validation/campaign/{name}", required=False)
    # experiment records for the phase-1 deliverables (the run dir's parent holds them)
    for up in (os.path.dirname(mdir), os.path.dirname(os.path.dirname(mdir))):
        for name in ("result.json", "header.json", "paired_cycle.json"):
            p = os.path.join(up, name)
            if os.path.exists(p): cp(p, f"{D}/refinement/experiment_{name}")
    # campaign validation
    cp(f"{RUNS}/{T}/c000/noise_floor/noise_floor.json", f"{D}/validation/campaign/noise_floor.json")
    for extra in glob.glob(f"{RUNS}/{T}/c000/noise_floor_*/noise_floor.json"):
        tag = os.path.basename(os.path.dirname(extra))
        cp(extra, f"{D}/validation/campaign/{tag}.json")
    for v in VERIFY_DIRS:
        for p in glob.glob(f"{v}/{T}_*.json"):
            cp(p, f"{D}/validation/campaign/{os.path.basename(v)}/{os.path.basename(p)}")
    for g in glob.glob(f"{STATE}/checks/G3_{T}*.json") + glob.glob(f"{STATE}/checks/fetch_{T}.json"):
        cp(g, f"{D}/validation/campaign/checks/{os.path.basename(g)}")
    cp(f"{STATE}/dossier/{T}.json", f"{D}/validation/campaign/dossier.json", required=False)
    # ledger rows
    L = f"{D}/ledger"
    n = {}
    for table in ("cycles", "changes", "bisections", "noise_floor", "checks", "rfree_consultations", "defects", "solvent_disagreements"):
        n[table] = export(table, "target = ?", (T,), f"{L}/{table}.csv")
    n["deviations"] = export("deviations", "target = ? or description like ?", (T, f"%{T}%"), f"{L}/deviations.csv")
    for dm in sorted(glob.glob(f"{RUNS}/{T}/runs/*/DECISIONS.md")):
        rid = os.path.basename(os.path.dirname(dm)); cp(dm, f"{L}/runs/{rid}/DECISIONS.md")
        cp(os.path.join(os.path.dirname(dm), "run_summary.json"), f"{L}/runs/{rid}/run_summary.json", required=False)
    log(T, "ledger rows", n)

# ---------- release-time validation (uniform across targets, deposited vs refined) ----------
def mp_parse(path):
    txt = open(path, errors="replace").read() if os.path.exists(path) else ""
    def g(pat):
        m = re.search(pat, txt); return float(m.group(1)) if m else None
    return {"ramachandran_outliers_pct": g(r"Ramachandran outliers\s*=\s*([\d.]+)\s*%"),
            "ramachandran_favored_pct": g(r"favored\s*=\s*([\d.]+)\s*%"),
            "rotamer_outliers_pct": g(r"Rotamer outliers\s*=\s*([\d.]+)\s*%"),
            "cbeta_deviations": g(r"C-beta deviations\s*=\s*([\d.]+)"),
            "clashscore": g(r"Clashscore\s*=\s*([\d.]+)"),
            "rms_bonds": g(r"RMS\(bonds\)\s*=\s*([\d.]+)"),
            "rms_angles": g(r"RMS\(angles\)\s*=\s*([\d.]+)"),
            "molprobity_score": g(r"MolProbity score\s*=\s*([\d.]+)")}
def mvd_parse(path):
    txt = open(path, errors="replace").read() if os.path.exists(path) else ""
    m1 = re.search(r"^\s*r_work:\s*([\d.]+)", txt, re.M); m2 = re.search(r"^\s*r_free:\s*([\d.]+)", txt, re.M)
    return {"r_work": float(m1.group(1)) if m1 else None, "r_free": float(m2.group(1)) if m2 else None}

def validate(T):
    D = os.path.join(STAGE, "targets", T); V = f"{D}/validation/release"; os.makedirs(V, exist_ok=True)
    W = os.path.join(STAGE, "_work", T); os.makedirs(W, exist_ok=True)
    data, flags, split = (f"{D}/data/{T}_{n}" for n in ("data.mtz", "flags.mtz", "split.mtz"))
    merged = f"{W}/merged.mtz"
    rc = run(["phenix.python", f"{HELPERS}/merge_mtz.py", data, flags, merged], W, f"{V}/merge_mtz.log")
    out = {"target": T, "merge_exit": rc, "models": {}}
    for which, model in (("deposited", f"{D}/deposited/{T}.cif"), ("refined", f"{D}/model/{T}_refined.cif")):
        m = {"model_sha256": sha(model)}
        rc = run(["phenix.python", f"{HELPERS}/indep_rfree.py", model, data, flags, split, f"{V}/rfree_indep.{which}.json"], W, f"{V}/rfree_indep.{which}.log")
        m["indep_exit"] = rc
        if os.path.exists(f"{V}/rfree_indep.{which}.json"): m["indep"] = json.load(open(f"{V}/rfree_indep.{which}.json"))
        wd = f"{W}/mvd_{which}"; os.makedirs(wd, exist_ok=True)
        rc = run(["phenix.model_vs_data", model, merged], wd, f"{V}/model_vs_data.{which}.log")
        m["model_vs_data_exit"] = rc; m["model_vs_data"] = mvd_parse(f"{V}/model_vs_data.{which}.log")
        wd = f"{W}/mp_{which}"; os.makedirs(wd, exist_ok=True)
        rc = run(["phenix.molprobity", model, "output.prefix=mp"], wd, f"{V}/molprobity.{which}.log")
        m["molprobity_exit"] = rc
        if os.path.exists(f"{wd}/mp.out"): shutil.copy2(f"{wd}/mp.out", f"{V}/molprobity.{which}.out")
        m["molprobity"] = mp_parse(f"{V}/molprobity.{which}.out")
        out["models"][which] = m
        log(T, which, "indep", rc if False else m["indep_exit"], "mvd", m["model_vs_data"], "mp", m["molprobity"])
    json.dump(out, open(f"{V}/summary.json", "w"), indent=1)
    return T

t0 = time.time()
with ThreadPoolExecutor(max_workers=int(os.environ.get("AGRP_WORKERS", "8"))) as ex:
    for T in ex.map(validate, targets): log("validated", T, round(time.time() - t0), "s")
shutil.rmtree(os.path.join(STAGE, "_work"), ignore_errors=True)

# ---------- coordinate-level diff deposited vs released (gemmi, autoref venv) ----------
diff_py = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model_diff_on_pod.py")
if os.path.exists(diff_py):
    rc = run(["/home/dev/envs/autoref/bin/python", diff_py, STAGE], STAGE, os.path.join(STAGE, "model_diff.log"))
    log("model_diff exit", rc)
else:
    log("model_diff_on_pod.py not found next to this script; skipped")

# ---------- provenance + manifest + tar ----------
try:
    pv = subprocess.run(["phenix.version"], capture_output=True, text=True).stdout
except Exception as e:
    pv = str(e)
prov = {"exported_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "pod_hostname": os.uname().nodename,
        "phenix_version": " ".join(l.strip() for l in pv.splitlines() if "Version" in l or "Release" in l),
        "ledger_sqlite_sha256": sha(f"{STATE}/ledger.sqlite"),
        "ledger_counts": {t: con.execute(f"select count(*) from {t}").fetchone()[0] for t in ("cycles", "changes", "jobs", "deviations", "noise_floor", "checks", "bisections", "defects")},
        "state_current": records, "verify_dirs": VERIFY_DIRS, "targets": targets,
        "molprobity_invocation": "phenix.molprobity <model> output.prefix=mp (defaults)",
        "model_vs_data_invocation": "phenix.model_vs_data <model> <merged data+flags mtz>",
        "indep_rfree_source": "/home/dev/runs/verify_20260917/indep_rfree.py (== scripts/verify/indep_rfree.py)"}
json.dump(prov, open(os.path.join(STAGE, "provenance.json"), "w"), indent=1)
man = []
for root, _, files in os.walk(os.path.join(STAGE, "targets")):
    for f in files:
        p = os.path.join(root, f); rel = os.path.relpath(p, STAGE)
        man.append({"file": rel, "sha256": sha(p), "bytes": os.path.getsize(p)})
man.sort(key=lambda m: m["file"])
json.dump(man, open(os.path.join(STAGE, "manifest.json"), "w"), indent=1)
log("manifest", len(man), "files", sum(m["bytes"] for m in man), "bytes")
tar = STAGE.rstrip("/") + ".tar.gz"
with tarfile.open(tar, "w:gz") as t:
    for name in ("targets", "manifest.json", "provenance.json", "stage.log"):
        t.add(os.path.join(STAGE, name), arcname=os.path.join("agrp", name))
log("TARBALL", tar, os.path.getsize(tar), sha(tar))
print("DONE", sha(tar))
