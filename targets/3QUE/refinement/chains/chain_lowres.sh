#!/bin/bash
# scripts/chain_lowres.sh RUN [NPROC] [PID]: the low-resolution levers (2026-10-20, 3QUE at 2.7 A: R-work 0.19 against
# R-free 0.285, rotamer outliers 7.6 % deposited and 12.9 % after the first refinement, every lever of chain_target
# refused). The tighter weights beyond the first rung (wc 2.0 / wu 2.0, 3.0 / 3.0), the ADP weight alone (wu 2, 4),
# secondary-structure and Ramachandran restraints, group B factors (one, then two for each residue), phenix's rotamer
# fixing, Coot auto-fit of the rotamer outliers (a fit kept when the CC does not fall), TLS by phenix.find_tls_groups,
# settle, convergence. Same rules as scripts/chain_target.sh. With PID the chain waits until that process (the
# pipeline before it) has ended.
set -u
K=${1:?run directory}
NP=${2:-6}
WAIT=${3:-}
source "$(dirname "$0")/chain_lib.sh"
if [ -n "$WAIT" ]; then
  say "chain_lowres waits for pid $WAIT"
  while [ -d "/proc/$WAIT" ]; do sleep 120; done
fi
say "chain_lowres start on $K from $(best), standing weights $(standing_weights)"
ladder weights_tight_l "2.0 2.0" "3.0 3.0"
ladder weights_wu_l "0.5 2.0" "0.5 4.0"
once restraints_ss_rama refine_step.py restraints --ss --rama
once group_adp_1 refine_step.py group-adp --groups 1
once group_adp_2 refine_step.py group-adp --groups 2
once fix_rotamers_a refine_step.py fix-rotamers
repeat coot_outliers_a coot_fix.py rotamers --from-outliers --min-cc-gain 0.0 --max-changes 12
once tls_find_l refine_step.py tls --groups find --replace
ladder weights_tight_l2 "1.0 1.0" "2.0 2.0"
repeat settle_l refine_step.py settle
repeat converge_l refine_step.py converge
say "chain_lowres end on $K; best model $(best)"
