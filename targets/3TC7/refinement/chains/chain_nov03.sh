#!/bin/bash
# scripts/chain_nov03.sh FORK PARENT [NPROC]: the levers of docs/NOV03_PLAN.md §3 on a fork that already carries the
# gate of 2026-10-28 plus `sanity_clash_tol` (the `<run>_nqh` forks of 2026-11-03). Waits for a running nqh step of the
# fork to end, then runs from the line's model in force, in this order: nonbonded 300 (L2), share-waters 0.5 and 1.0
# (L3), prune 0.5 and 0.75 (L4), b-to-occ 2.0 (L5), Untangler (L8), nonbonded 1000 (L2). A lever with nothing to change
# records a skip. The parent of each step is the last ACCEPT or BUILD from PARENT on.
set -u
K=${1:?fork directory}
PARENT=${2:?the model in force when the line starts}
NP=${3:-6}
source "$(dirname "$0")/chain_lib.sh"
FORK_FROM=$PARENT
export FORK_FROM
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
step_() { local name=$1; shift; local P; P=$(latest); say "$name from $P"; run "$@" --parent "$P" --tag "$name"; }
untangle_() { local P; P=$(latest); say "$1 from $P: Untangler low_compute_clash_resolution"; run conn_optim.py relabel --parent "$P" --tag "$1" --effort-min 10 --untangler lcr; }
scan_line() { phenix.python tools/coot_repair.py scan --model "$K/trajectory/$(latest)/model.pdb" 2>&1 | head -1 | tee -a "$LOG"; }
say "chain_nov03 start on $K from $PARENT"
while pgrep -f "refine_step.py nqh --run $K" >/dev/null 2>&1; do sleep 60; done
say "the nqh step of $K has ended; the model in force is $(latest)"
scan_line
step_ nonbonded_300 refine_step.py nonbonded --weight 300
step_ share_0.5 ensemble_edit.py share-waters --tol 0.5
step_ share_1.0 ensemble_edit.py share-waters --tol 1.0
step_ prune_0.5 ensemble_edit.py prune --rmsd 0.5
step_ prune_0.75 ensemble_edit.py prune --rmsd 0.75
step_ b_to_occ_2 ensemble_edit.py b-to-occ --ratio 2.0
untangle_ untangle_n
step_ nonbonded_1000 refine_step.py nonbonded --weight 1000
scan_line
say "chain_nov03 end on $K; the line's last model $(latest) (from $PARENT)"
