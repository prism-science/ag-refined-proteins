"""Independent flag identity check (gemmi only): raw SF mmCIF status=='f' set vs flags.mtz free set;
data.mtz FP vs F_meas_au; operator MTZ flags vs ours (7KR0)."""
import sys

import gemmi
import numpy as np

target, sfcif, data_mtz, flags_mtz = sys.argv[1:5]
op_mtz = sys.argv[5] if len(sys.argv) > 5 else None
doc = gemmi.cif.read(sfcif)
blk = next(b for b in doc if b.find_loop("_refln.index_h"))
tab = blk.find("_refln.", ["index_h", "index_k", "index_l", "status", "F_meas_au", "F_meas_sigma_au"])
raw_free, raw_work, raw_other, fmeas = set(), set(), {}, {}
for r in tab:
    hkl = (int(r[0]), int(r[1]), int(r[2]))
    s = r[3]
    if s == "f": raw_free.add(hkl)
    elif s == "o": raw_work.add(hkl)
    else: raw_other[s] = raw_other.get(s, 0) + 1
    if s in ("f", "o"):
        fmeas[hkl] = (float(r[4]), float(r[5]))
m = gemmi.read_mtz_file(flags_mtz)
M = np.array(m, copy=False)
col = m.column_with_label("R-free-flags")
mtz_free, mtz_work = set(), set()
for i in range(m.nreflections):
    hkl = (int(M[i,0]), int(M[i,1]), int(M[i,2]))
    (mtz_free if col.array[i] == 0 else mtz_work).add(hkl)
d = gemmi.read_mtz_file(data_mtz)
DD = np.array(d, copy=False)
fp, sfp = d.column_with_label("FP"), d.column_with_label("SIGFP")
maxdiff, n_cmp = 0.0, 0
for i in range(d.nreflections):
    hkl = (int(DD[i,0]), int(DD[i,1]), int(DD[i,2]))
    if hkl in fmeas:
        n_cmp += 1
        maxdiff = max(maxdiff, abs(fmeas[hkl][0] - fp.array[i]), abs(fmeas[hkl][1] - sfp.array[i]))
print(target, "raw: free", len(raw_free), "work", len(raw_work), "other", raw_other)
print(target, "flags.mtz: free", len(mtz_free), "work", len(mtz_work), "n", m.nreflections)
print(target, "free sets identical:", raw_free == mtz_free, "| work sets identical:", raw_work == mtz_work,
      "| free-only-in-raw", len(raw_free - mtz_free), "free-only-in-mtz", len(mtz_free - raw_free))
print(target, "data.mtz FP/SIGFP vs F_meas_au: compared", n_cmp, "max abs diff", maxdiff)
if op_mtz:
    o = gemmi.read_mtz_file(op_mtz)
    OO = np.array(o, copy=False)
    print(target, "operator mtz columns:", [c.label for c in o.columns], "n", o.nreflections, "sg", o.spacegroup.hm, "cell", o.cell)
    lab = [c.label for c in o.columns if "free" in c.label.lower() or "FreeR" in c.label]
    if lab:
        oc = o.column_with_label(lab[0])
        vals = {}
        for i in range(o.nreflections): vals[oc.array[i]] = vals.get(oc.array[i], 0) + 1
        print(target, "operator flag column", lab[0], "value counts", vals)
        # map both to ASU for comparison
        asu = gemmi.ReciprocalAsu(o.spacegroup)
        ops = o.spacegroup.operations()
        def to_asu(hkl): return tuple(asu.to_asu(hkl, ops)[0])
        op_free = set(); op_all = set()
        for i in range(o.nreflections):
            hkl = to_asu((int(OO[i,0]), int(OO[i,1]), int(OO[i,2])))
            op_all.add(hkl)
            if oc.array[i] == 0: op_free.add(hkl)
        asu2 = gemmi.ReciprocalAsu(m.spacegroup); ops2 = m.spacegroup.operations()
        our_free = {tuple(asu2.to_asu(h, ops2)[0]) for h in mtz_free}
        our_all = our_free | {tuple(asu2.to_asu(h, ops2)[0]) for h in mtz_work}
        common = op_all & our_all
        print(target, "operator vs ours: common refl", len(common), "op free", len(op_free), "our free", len(our_free),
              "free-in-op-not-ours(common)", len((op_free - our_free) & common), "free-in-ours-not-op(common)", len((our_free - op_free) & common),
              "op-only refl", len(op_all - our_all), "ours-only refl", len(our_all - op_all))
