#!/bin/bash
# scripts/chain_ions.sh RUN [NPROC] [RESNAME] [SIGMA]: ions of the crystallisation condition at the strong difference
# peaks (tools/place_ions.py), repeated while accepted; then settle, the 4 sigma water pick and convergence from the
# best model. 4QO4 (2026-10-20): crystals from 1.9 to 2.4 M ammonium sulfate; peaks of 5.5 to 9 sigma next to LYS51,
# GLN18, HIS96, ARG97, ARG29 and GLU95 that waters did not explain (S0003). Same rules as scripts/chain_target.sh.
set -u
K=${1:?run directory}
NP=${2:-6}
RES=${3:-SO4}
SIG=${4:-5.0}
source "$(dirname "$0")/chain_lib.sh"
say "chain_ions start on $K from $(best): $RES at $SIG sigma"
repeat "ions_${RES}" place_ions.py place --resname "$RES" --peak-sigma "$SIG" --max-ions 6
repeat settle_i refine_step.py settle
repeat pick_4.0_i water_addition.py pick --sigma 4.0
repeat converge_i refine_step.py converge
say "chain_ions end on $K; best model $(best)"
