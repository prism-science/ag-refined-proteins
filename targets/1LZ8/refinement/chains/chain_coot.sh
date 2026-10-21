#!/bin/bash
# scripts/chain_coot.sh RUN [NPROC] [N]: Coot zone refinement of the N (default 3) worst-fitting protein residues of
# the best model (the RSCC worklist on the work-only 2mFo-DFc map), each as one judged step (the residue and its two
# neighbours), then convergence. Same rules as scripts/chain_target.sh.
set -u
K=${1:?run directory}
NP=${2:-6}
N=${3:-3}
source "$(dirname "$0")/chain_lib.sh"
say "chain_coot start on $K from $(best)"
P=$(best)
phenix.python tools/worklist.py --run "$K" --parent "$P" 2>&1 | tee -a "$LOG" | tail -n 1 | cut -c1-200
ZONES=$(phenix.python - "$K" "$P" "$N" <<"PY"
import json, os, sys
k, p, n = sys.argv[1], sys.argv[2], int(sys.argv[3])
f = "%s/trajectory/WORKLIST_%s.json" % (k, p)
wl = json.load(open(f))["worklist"] if os.path.exists(f) else []
seen = set()
out = []
for r in wl:
    key = (r["chain"], r["resseq"])
    if key in seen or r["resname"] in ("HOH", "WAT", "DOD"):
        continue
    seen.add(key)
    out.append("%s:%d" % (r["chain"], r["resseq"]))
    if len(out) >= n:
        break
print(" ".join(out))
PY
)
say "zones: ${ZONES:-none}"
for z in $ZONES; do
  c=${z%%:*}; r=${z##*:}
  P=$(best); say "coot zone $c $((r-1))-$((r+1)) from $P"
  run coot_fix.py zone --parent "$P" --chain "$c" --start $((r-1)) --end $((r+1)) --tag "coot_zone_${c}${r}"
done
repeat converge_z refine_step.py converge
say "chain_coot end on $K; best model $(best)"
