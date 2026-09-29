"""Independent R-free check. NOT the harness code path (no extract_xtal_data, no outlier rejection):
read data.mtz (FP,SIGFP; or IMEAN,SIGIMEAN via French-Wilson), flags.mtz (R-free-flags, 0 = free), split.mtz (SPLIT 1=select 2=report),
build fmodel on ALL common reflections, update scales, report R on work/free/select/report with a
manual R computation. Usage: phenix.python indep_rfree.py <model> <data.mtz> <flags.mtz> <split.mtz> <out.json>
"""
import json
import sys
import time

import iotbx.pdb
import mmtbx.f_model
import mmtbx.model
from cctbx.array_family import flex
from iotbx.reflection_file_reader import any_reflection_file
from libtbx.utils import null_out


def find(path, want):
    for ma in any_reflection_file(path).as_miller_arrays():
        ls = ma.info().label_string()
        if ls == want or ls.split(",")[0] == want or want in ma.info().labels:
            return ma
    return None


def arr(path, want):
    ma = find(path, want)
    if ma is None:
        have = [m.info().label_string() for m in any_reflection_file(path).as_miller_arrays()]
        raise SystemExit(f"no {want} in {path} (have {have})")
    return ma

def manual_r(fo, fc, sel):
    fo_s, fc_s = fo.select(sel), fc.select(sel)
    return float(flex.sum(flex.abs(fo_s - fc_s)) / flex.sum(fo_s))

t0 = time.time()
model_path, data_mtz, flags_mtz, split_mtz, out_path = sys.argv[1:6]
fobs = find(data_mtz, "FP")
data_kind, n_fw_dropped = "amplitudes (FP,SIGFP)", 0
if fobs is None:
    # phase-2 targets frozen as merged intensities (4QO4, 6UDY, 7DVR, 9D5U, 9D5Y): convert with cctbx's French-Wilson,
    # the same treatment phenix.refine / phenix.model_vs_data apply to intensity input. A few very weak or negative
    # intensities may be rejected by the conversion; their count is recorded and the flag/split sets are intersected.
    from cctbx import french_wilson
    iobs = arr(data_mtz, "IMEAN")
    fobs = french_wilson.french_wilson_scale(miller_array=iobs, log=null_out())
    n_fw_dropped = iobs.size() - fobs.size()
    data_kind = "intensities (IMEAN,SIGIMEAN) -> French-Wilson amplitudes (cctbx.french_wilson)"
fobs = fobs.map_to_asu()
flags = arr(flags_mtz, "R-free-flags").map_to_asu()
split = arr(split_mtz, "SPLIT").map_to_asu()
n_data, n_flags = fobs.size(), flags.size()
fobs, flags = fobs.common_sets(flags)
if n_fw_dropped == 0:
    assert fobs.size() == n_data == n_flags, (fobs.size(), n_data, n_flags)
else:
    assert fobs.size() == n_data <= n_flags, (fobs.size(), n_data, n_flags)
free = flags.customized_copy(data=(flags.data() == 0))
fobs, split = fobs.common_sets(split); free, split = free.common_sets(split)
assert fobs.size() == n_data
code = split.data()
sel_free = free.data()
sel_select = sel_free & (code == 1)
sel_report = sel_free & (code == 2)
assert (sel_free & (code == 0)).count(True) == 0, "free reflections marked work in split"
assert (~sel_free & (code != 0)).count(True) == 0, "work reflections marked select/report in split"

pdb_inp = iotbx.pdb.input(file_name=model_path)
model = mmtbx.model.manager(model_input=pdb_inp, crystal_symmetry=fobs.crystal_symmetry(), log=null_out())
model.setup_scattering_dictionaries(scattering_table="n_gaussian")
xrs = model.get_xray_structure()
h = model.get_hierarchy()
n_h = sum(1 for a in h.atoms() if a.element.strip().upper() in ("H", "D"))
altlocs = sorted({a.parent().altloc for a in h.atoms() if a.parent().altloc.strip()})
n_water = sum(1 for rg in h.residue_groups() if any(ag.resname.strip() in ("HOH", "WAT", "DOD") for ag in rg.atom_groups()))
fmodel = mmtbx.f_model.manager(f_obs=fobs, r_free_flags=free, xray_structure=xrs)
fmodel.update_all_scales(remove_outliers=False, log=null_out())
fo = fmodel.f_obs().data()
fc = flex.abs(fmodel.f_model_scaled_with_k1().data())
work_sel = ~fmodel.r_free_flags().data()
res = {
    "model": model_path, "data": data_kind, "n_dropped_french_wilson": n_fw_dropped,
    "n_atoms": xrs.scatterers().size(), "n_hydrogen": n_h, "altlocs": altlocs,
    "n_water_residues": n_water,
    "n_reflections": fobs.size(), "n_free": sel_free.count(True), "n_select": sel_select.count(True),
    "n_report": sel_report.count(True), "n_work": work_sel.count(True),
    "d_min": fobs.d_min(),
    "r_work_fmodel": fmodel.r_work(), "r_free_fmodel": fmodel.r_free(),
    "r_work_manual": manual_r(fo, fc, work_sel), "r_free_manual": manual_r(fo, fc, sel_free),
    "r_free_select_manual": manual_r(fo, fc, sel_select), "r_free_report_manual": manual_r(fo, fc, sel_report),
    "wall_s": round(time.time() - t0, 1),
}
with open(out_path, "w") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res))
