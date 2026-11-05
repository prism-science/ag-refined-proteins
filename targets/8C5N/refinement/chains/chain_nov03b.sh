#!/bin/bash
# scripts/chain_nov03b.sh FORK PARENT [NPROC]: the second chain of docs/NOV03_PLAN.md on a fork that carries the gate
# with `sanity_clash_tol`: the clashscore without moving heavy atoms off their density. From the line's model in force:
# hydrogens refined individually (a repair on the clashscore; sub-angstrom data only, else the lever skips), the
# nonbonded term at 32, 64 and 128 (repairs; the ladder below the 300 that cost 7KR0 +6 sigma and 7R2H +17 sigma),
# Untangler at 30 minutes of effort (a geometry step). Waits for a running chain_nov03.sh or its waiters on the fork.
set -u
K=${1:?fork directory}
PARENT=${2:?the model in force when the line starts}
NP=${3:-6}
source "$(dirname "$0")/chain_lib.sh"
FORK_FROM=$PARENT
export FORK_FROM
latest() {
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
step_() { local name=$1; shift; local P; P=$(latest); say "$name from $P"; run "$@" --parent "$P" --tag "$name"; }
untangle_() { local P; P=$(latest); say "$1 from $P: Untangler low_compute_clash_resolution, 30 min"; run conn_optim.py relabel --parent "$P" --tag "$1" --effort-min 30 --untangler lcr; }
scan_line() { phenix.python tools/coot_repair.py scan --model "$K/trajectory/$(latest)/model.pdb" 2>&1 | head -1 | tee -a "$LOG"; }
say "chain_nov03b start on $K from $PARENT"
while pgrep -f "chain_nov03.sh $K" >/dev/null 2>&1 || pgrep -f "wait_clash_$(basename "$K").sh" >/dev/null 2>&1 || pgrep -f "wait_rotamer_7r2h.sh" >/dev/null 2>&1 && [ "$(basename "$K")" = "Ta4f3f9_nqh" ]; do sleep 300; done
say "the first chain of $K has ended; the model in force is $(latest)"
scan_line
step_ hydrogens_r refine_step.py hydrogens --kind sanity
step_ nonbonded_32 refine_step.py nonbonded --weight 32
step_ nonbonded_64 refine_step.py nonbonded --weight 64
step_ nonbonded_128 refine_step.py nonbonded --weight 128
untangle_ untangle_30
scan_line
say "chain_nov03b end on $K; the line's last model $(latest) (from $PARENT)"
