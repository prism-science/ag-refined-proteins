#!/bin/bash
# scripts/chain_after.sh RUN NPROC PID NAME TOOL ARGS...: one lever (NAME, from the best model, repeated while accepted, 3
# at most) after the process PID (a chain before it) has ended; PID 0 runs at once. For a lever that a running chain
# lacks (a running chain script is never edited; docs/POD.md). Same rules as scripts/chain_target.sh.
set -u
K=${1:?run directory}
NP=${2:?processes}
WAIT=${3:?pid to wait for, or 0}
NAME=${4:?step name}
source "$(dirname "$0")/chain_lib.sh"   # re-executes this script with the same arguments inside the namespace: shift after it
shift 4
if [ "$WAIT" != "0" ]; then
  say "chain_after ($NAME) waits for pid $WAIT"
  while [ -d "/proc/$WAIT" ]; do sleep 120; done
fi
say "chain_after start on $K: $NAME = $*"
repeat "$NAME" "$@"
say "chain_after end on $K ($NAME); best model $(best)"
