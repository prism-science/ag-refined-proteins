#!/bin/bash
# scripts/chain_oct28.sh SRC FORK PARENT [NPROC]: the trials of 2026-10-28 (operator; docs/OCT28_TRIALS.md) on a fork of
# SRC from PARENT. The fork's metaparameters, set before its first step, gate on Holton's wE (quality_we_rel), the tallest
# mFo-DFc peak (quality_peak_tol), the waters in the range of motion (sanity_envelope_tol) and the residues next to
# positive peaks (sanity_peaks_tol), with the count tolerances scaled by the square root of the count (sanity_count_k).
# The steps, each from the line's last accepted model:
#   1. coot_repair.py peaks: the strongest difference peaks (6 sigma and up): a lettered water under a peak made a water
#      of every copy, a peak in open solvent a new water of every copy; peaks in the range of motion go to step 4
#   2. Untangler (conn_optim.py relabel), when the model's clashscore is above CLASH_HIGH (10)
#   3. coot_repair.py envelope: the waters in the range of motion deleted
#   4. coot_repair.py density: the Coot refit of each copy (omit maps) of the residues in or next to difference density
#   5. coot_repair.py bfactors: copy B-factors more than 3 times apart reset to the copy median
#   6. picks at 3.0 and 2.5 sigma with --envelope 2.6 (no new water in the range of motion)
#   7. anisotropic waters, settle
#   8. peaks again, Untangler again when the clashscore is above CLASH_HIGH, the copy-B reset again
set -u
SRC=${1:?the run to fork}
K=${2:?fork directory}
PARENT=${3:?the first model of the line}
NP=${4:-6}
CLASH_HIGH=${CLASH_HIGH:-10}
if [ ! -d "$K" ]; then bash "$(dirname "$0")/fork_run.sh" "$SRC" "$K" || exit 1; fi
source "$(dirname "$0")/chain_lib.sh"
if [ -s "$K/oct28_line_from.txt" ]; then FORK_FROM=$(cat "$K/oct28_line_from.txt"); else
FORK_FROM=$(phenix.python - "$K" <<"PY"
import json, sys
last = 0
for ln in open(sys.argv[1] + "/trajectory/score_history.jsonl"):
    last = max(last, int(json.loads(ln)["step"][1:]))
print("S%04d" % (last + 1))
PY
)
echo "$FORK_FROM" > "$K/oct28_line_from.txt"; fi
export FORK_FROM
phenix.python - "$K/metaparams.yaml" <<"PY"
import sys
p = sys.argv[1]
t = open(p).read()
add = [("sanity_gate", "true", "the Coot checks in the gate"),
       ("sanity_water_tol", "3", "waters in protein density a step may add"),
       ("sanity_copyb_tol", "5", "copy-B outliers a step may add"),
       ("sanity_density_tol", "2", "residues beyond +-3.5 sigma a step may add"),
       ("sanity_peaks_tol", "2", "residues next to positive peaks a step may add"),
       ("sanity_envelope_tol", "3", "waters in the range of motion a step may add"),
       ("sanity_count_k", "2", "each count tolerance at least 2 x sqrt(the control's count)"),
       ("sanity_drop", "0.1", "a repair lowers one check by this share and by more than its tolerance,"),
       ("sanity_gap_drop", "0.002", "or narrows the gap by this much,"),
       ("sanity_rfree_k", "2.0", "with R-free not worse than this many sigma"),
       ("holton_we", "true", "Holton's weighted energy on each judged model"),
       ("quality_we_rel", "0.05", "a step may raise wE by this share of the control's"),
       ("quality_we_drop", "0.10", "a repair: wE lower by this share"),
       ("quality_peak_tol", "1.0", "a step may raise the tallest mFo-DFc peak by this many sigma"),
       ("quality_peak_drop", "1.5", "a repair: the tallest peak lower by this many sigma")]
keys = [k for k, _, _ in add]
lines = [ln for ln in t.splitlines() if ln.split(":")[0].strip() not in keys]
for k, v, c in add:
    lines.append("%-27s # %s (scripts/chain_oct28.sh, set before the fork's first step)" % ("%s: %s" % (k, v), c))
open(p, "w").write("\n".join(lines) + "\n")
print("metaparams: the trials of 2026-10-28 on")
PY
latest() {   # the line's model in force: the last ACCEPT or BUILD from FORK_FROM on, else PARENT
  phenix.python - "$K" "$FORK_FROM" "$PARENT" <<"PY"
import json, sys
last = sys.argv[3]
for ln in open(sys.argv[1] + "/trajectory/score_history.jsonl"):
    r = json.loads(ln)
    if r["step"] >= sys.argv[2] and r.get("verdict") in ("ACCEPT", "BUILD"):
        last = r["step"]
print(last)
PY
}
clash_of() {   # the recorded clashscore of a step (its score cache), or 0
  phenix.python - "$K" "$1" <<"PY"
import json, sys
sys.path.insert(0, ".")
from tools.lib import hr
run = hr.RunDir(sys.argv[1])
try:
    m = str(run.model_of(sys.argv[2]))
    rec = json.load(open(run.scores / (hr.sha256_file(m) + ".json")))
    print(rec.get("clashscore") or 0)
except Exception:
    print(0)
PY
}
step_() { local name=$1; shift; local P; P=$(latest); say "$name from $P"; run "$@" --parent "$P" --tag "$name"; }
untangle_if_high() {
  local P; P=$(latest); local c; c=$(clash_of "$P")
  if phenix.python -c "import sys; sys.exit(0 if float(sys.argv[1]) > float(sys.argv[2]) else 1)" "$c" "$CLASH_HIGH"; then
    say "$1: clashscore $c of $P above $CLASH_HIGH: Untangler"
    run conn_optim.py relabel --parent "$P" --tag "$1" --effort-min 10
  else
    say "$1: clashscore $c of $P not above $CLASH_HIGH"
  fi
}
scan_line() { phenix.python tools/coot_repair.py scan --model "$K/trajectory/$(latest)/model.pdb" 2>&1 | head -1 | tee -a "$LOG"; }
say "chain_oct28 start on $K from $PARENT (fork of $SRC; the fork's steps start at $FORK_FROM)"
scan_line
step_ peaks_q coot_repair.py peaks --sigma 6.0
untangle_if_high untangle_q
step_ envelope_q coot_repair.py envelope
step_ density_q coot_repair.py density
step_ bfactors_q coot_repair.py bfactors
step_ pick_3.0_q water_addition.py pick --sigma 3.0 --envelope 2.6
step_ pick_2.5_q water_addition.py pick --sigma 2.5 --envelope 2.6
step_ aniso_water_q refine_step.py aniso-water
step_ settle_q refine_step.py settle
step_ peaks_q2 coot_repair.py peaks --sigma 6.0
untangle_if_high untangle_q2
step_ bfactors_q2 coot_repair.py bfactors
scan_line
say "chain_oct28 end on $K; the line's last model $(latest) (from $PARENT)"
