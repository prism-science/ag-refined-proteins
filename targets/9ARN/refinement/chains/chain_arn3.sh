#!/bin/bash
# scripts/chain_arn3.sh RUN [NPROC] [PID]: the third set on 9ARN (2026-10-20, after chain_arn2 took it from 0.2934 to
# 0.2770 with anisotropic waters and TLS under wc 2 / wu 2 and the restraints): protein ADPs isotropic under the standing
# TLS (the deposited anisotropic set is a TLS total U; isotropic was refused under the loose recipe), settle while
# accepted, wc 1 / wu 1 as a check in the looser direction, the 4 sigma pick while accepted, the deposited TLS groups
# with an isotropic residual against the standing groups, convergence. Same rules as scripts/chain_target.sh. With PID
# the chain waits until that process has ended.
set -u
K=${1:?run directory}
NP=${2:-6}
WAIT=${3:-}
source "$(dirname "$0")/chain_lib.sh"
if [ -n "$WAIT" ]; then
  say "chain_arn3 waits for pid $WAIT"
  while [ -d "/proc/$WAIT" ]; do sleep 120; done
fi
say "chain_arn3 start on $K from $(best), standing weights $(standing_weights)"
once iso_protein_b refine_step.py iso-protein
repeat settle_arn refine_step.py settle
once weights_1_1_check refine_step.py weights --wc 1.0 --wu 1.0
repeat pick_4.0_arn water_addition.py pick --sigma 4.0
once tls_deposited_iso_b refine_step.py tls --groups deposited --iso --replace
repeat converge_arn refine_step.py converge
say "chain_arn3 end on $K; best model $(best)"
