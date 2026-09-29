"""Coordinate-level diff of deposited vs released model for every staged target (gemmi). Usage: python model_diff.py <STAGE>"""
import glob, json, os, sys
import gemmi
STAGE = sys.argv[1]
def summarize(path):
    st = gemmi.read_structure(path); st.setup_entities()
    m = st[0]
    waters, resid_alt, nonwater, n_atoms, n_h, occ = set(), {}, set(), 0, 0, {}
    for ch in m:
        for res in ch:
            key = f"{ch.name} {res.seqid.num}{res.seqid.icode.strip()}"
            if res.name == "HOH" or res.is_water():
                waters.add(key)
            else:
                nonwater.add(f"{key} {res.name}")
                alts = {a.altloc for a in res if a.altloc != "\0"}
                resid_alt[f"{key} {res.name}"] = "".join(sorted(alts))
            for a in res:
                n_atoms += 1
                if a.element.name in ("H", "D"): n_h += 1
    return {"n_atoms": n_atoms, "n_hydrogen": n_h, "n_waters": len(waters),
            "n_nonwater_residues": len(nonwater), "n_residues_with_altlocs": sum(1 for v in resid_alt.values() if v),
            "_waters": waters, "_nonwater": nonwater, "_alt": resid_alt}
out = {}
for d in sorted(glob.glob(f"{STAGE}/targets/*")):
    T = os.path.basename(d)
    dep = summarize(f"{d}/deposited/{T}.cif"); rel = summarize(f"{d}/model/{T}_refined.cif")
    alt_changes = []
    for k in sorted(set(dep["_alt"]) & set(rel["_alt"])):
        if dep["_alt"][k] != rel["_alt"][k]:
            alt_changes.append({"residue": k, "before": dep["_alt"][k] or "-", "after": rel["_alt"][k] or "-"})
    out[T] = {"target": T,
              "deposited": {k: v for k, v in dep.items() if not k.startswith("_")},
              "released": {k: v for k, v in rel.items() if not k.startswith("_")},
              "waters_added": sorted(rel["_waters"] - dep["_waters"]), "waters_removed": sorted(dep["_waters"] - rel["_waters"]),
              "nonwater_residues_added": sorted(rel["_nonwater"] - dep["_nonwater"]),
              "nonwater_residues_removed": sorted(dep["_nonwater"] - rel["_nonwater"]),
              "altloc_changes": alt_changes,
              "hydrogens_delta": rel["n_hydrogen"] - dep["n_hydrogen"]}
    with open(f"{d}/validation/release/model_diff.json", "w") as f: json.dump(out[T], f, indent=1)
print(json.dumps(out))
