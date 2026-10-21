#!/bin/bash
# scripts/chain_lib.sh: the functions of the chain scripts (chain_target.sh, chain_followup.sh). Source it after
# K (the run directory) and NP (processes for each step) are set. The parent of every step is the best recorded
# model: the step (INIT, ACCEPT or BUILD) with the lowest R-free. The log is K/chain_target.log.
export HR_RUNS=$(dirname "$K") HR_NPROC=${NP:-6}
# docs/SANDBOX.md: the whole script runs in a network namespace with no interface
if [ "${HR_NONET:-}" != "1" ] && command -v unshare >/dev/null 2>&1 && unshare -rn true 2>/dev/null; then
  exec unshare -rn env HR_NONET=1 bash "$0" "$@"
fi
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd "$(dirname "${BASH_SOURCE[0]}")/.."
LOG=$K/chain_target.log
say() { echo "[$(date -u +%FT%TZ)] $*" | tee -a "$LOG"; }
best() {   # the recorded step with the lowest R-free among INIT, ACCEPT and BUILD (ties: the latest)
  phenix.python - "$K" <<"PY"
import json, sys
best = None
for ln in open(sys.argv[1] + "/trajectory/score_history.jsonl"):
    r = json.loads(ln)
    if r.get("verdict") not in ("INIT", "ACCEPT", "BUILD"):
        continue
    rf = (r.get("metrics") or {}).get("r_free")
    if rf is None:
        continue
    if best is None or rf <= best[1]:
        best = (r["step"], rf)
print(best[0] if best else "S0001")
PY
}
dmin() { phenix.python -c "import json,sys; print(json.load(open(sys.argv[1] + '/run.json')).get('d_min', 9))" "$K"; }
below() { phenix.python -c "import sys; sys.exit(0 if float(sys.argv[1]) <= float(sys.argv[2]) else 1)" "$(dmin)" "$1"; }
standing_weights() { phenix.python -c "import json,sys; s=json.load(open(sys.argv[1] + '/run.json')).get('standing') or {}; print('%g %g' % (float(s.get('wc', 0.5)), float(s.get('wu', 1.0))))" "$K"; }
run() { local tool=$1; shift; phenix.python "tools/$tool" "$@" --run "$K" --nproc "$HR_NPROC" 2>&1 | tee -a "$LOG" | grep "^S00" | cut -c1-240; }
repeat() {   # repeat NAME TOOL ARGS...: run the lever from the best model while it is accepted, 3 times at most
  local name=$1; shift
  for i in 1 2 3; do
    local P; P=$(best); say "$name ($i) from $P"
    run "$@" --parent "$P" --tag "${name}_$i"
    [ "$(best)" = "$P" ] && break
  done
}
once() {   # once NAME TOOL ARGS...: the lever one time from the best model
  local name=$1; shift
  local P; P=$(best); say "$name from $P"
  run "$@" --parent "$P" --tag "$name"
}
ladder() {   # ladder NAME "wc wu" ...: each weight pair from the best model while the pair before was accepted
  local name=$1; shift; local i=0
  for pair in "$@"; do
    i=$((i + 1))
    local wc=${pair% *} wu=${pair#* }
    if [ "$(standing_weights)" = "$wc $wu" ]; then say "$name ($i): the standing weights are $wc $wu already"; continue; fi
    local P; P=$(best); say "$name ($i) wc $wc wu $wu from $P"
    run refine_step.py weights --parent "$P" --wc "$wc" --wu "$wu" --tag "${name}_$i"
    [ "$(best)" = "$P" ] && break
  done
}
floor() {   # the noise floor of a judged step: the common recipe from the best model, when run.json has none of that recipe
  if phenix.python -c "import json,sys; nf=json.load(open(sys.argv[1] + '/run.json')).get('noise_floor') or {}; sys.exit(0 if nf.get('recipe') == 'common' else 1)" "$K"; then
    say "noise floor: measured with the common recipe already"; return; fi
  local P; P=$(best); say "noise floor from $P"
  phenix.python tools/noise_floor.py measure --parent "$P" --run "$K" --nproc "$HR_NPROC" --tag "noise_floor_$P" 2>&1 | tee -a "$LOG" | grep "noise floor" | cut -c1-200
}
split() {   # split COPIES: the representation change; the best-model rule leaves a worse BUILD behind
  local P; P=$(best); say "split $1 copies from $P"
  run split_conformations.py build --parent "$P" --source shake --copies "$1" --mc 20 --tag "split_shake_$1"
  say "after the split the best model is $(best)"
}
