#!/bin/bash
# scripts/chain_weights.sh RUN [NPROC]: the tighter weights ladder (wc 1.0 / wu 1.0, then 2.0 / 2.0, each rung while
# the one before is accepted) on a run whose chain ran before the ladder existed (2026-10-19). Same rules as
# scripts/chain_target.sh; the log is RUN/chain_target.log.
set -u
K=${1:?run directory}
NP=${2:-6}
source "$(dirname "$0")/chain_lib.sh"
say "chain_weights start on $K from $(best), standing weights $(standing_weights)"
ladder weights_tight "1.0 1.0" "2.0 2.0"
say "chain_weights end on $K; best model $(best)"
