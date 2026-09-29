"""Join a target's frozen data.mtz (FP,SIGFP or IMEAN,SIGIMEAN) and flags.mtz (R-free-flags, 0 = free) into one MTZ
for programs that want a single reflection file (phenix.model_vs_data, phenix.refine, Coot).
Usage: phenix.python scripts/merge_mtz.py targets/<ID>/data/<ID>_data.mtz targets/<ID>/data/<ID>_flags.mtz out.mtz
"""
import sys

from iotbx.reflection_file_reader import any_reflection_file

data_mtz, flags_mtz, out = sys.argv[1:4]
arrs = any_reflection_file(data_mtz).as_miller_arrays()
obs = next((m for m in arrs if m.info().label_string().startswith("FP")), None)
root = "FP"
if obs is None:
    obs = next(m for m in arrs if m.info().label_string().startswith("IMEAN"))
    root = "IMEAN"
flags = next(m for m in any_reflection_file(flags_mtz).as_miller_arrays() if "R-free-flags" in m.info().labels)
obs, flags = obs.common_sets(flags)
ds = obs.as_mtz_dataset(column_root_label=root)
ds.add_miller_array(flags, column_root_label="R-free-flags")
ds.mtz_object().write(out)
print("wrote", out, root, obs.size(), "reflections;", (flags.data() == 0).count(True), "free")
