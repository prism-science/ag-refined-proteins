#!/bin/bash
# scripts/chain_more.sh RUN [NPROC]: the levers not yet tried on 1LZ8, 4QO4 and 9ARN after their first chains
# (2026-10-19 15:20Z): waters below 1 sigma pruned, the water clash cleanup, TLS with phenix.find_tls_groups against
# the standing groups, three more weight pairs, settle, the two-copy split from qFit conformers with the solvent
# and convergence levers on it when it is the best model, convergence. Same rules as scripts/chain_target.sh.
set -u
K=${1:?run directory}
NP=${2:-6}
source "$(dirname "$0")/chain_lib.sh"
split_from() {   # split_from SOURCE COPIES
  local P; P=$(best); say "split $2 copies from $P, source $1"
  run split_conformations.py build --parent "$P" --source "$1" --copies "$2" --mc 20 --tag "split_$1_$2"
  say "after the split the best model is $(best)"
}
say "chain_more start on $K from $(best), d_min $(dmin), standing weights $(standing_weights)"
once prune_a water_addition.py prune --sigma 1.0
once cleanup_a water_addition.py cleanup
once tls_find_a refine_step.py tls --groups find --replace
once weights_0.5_0.5 refine_step.py weights --wc 0.5 --wu 0.5
once weights_0.5_2.0 refine_step.py weights --wc 0.5 --wu 2.0
once weights_0.4_1.0 refine_step.py weights --wc 0.4 --wu 1.0
repeat settle_d refine_step.py settle
B0=$(best)
split_from qfit 2
if [ "$(best)" != "$B0" ]; then
  for s in 4.0 3.0 2.5; do repeat "pick_${s}_q" water_addition.py pick --sigma "$s"; done
  repeat aniso_water_q refine_step.py aniso-water
  repeat converge_q refine_step.py converge
  once occupancies_q refine_step.py occupancies
  once reletter_q water_addition.py reletter
  repeat copy_vote_q copy_vote.py vote --peak-sigma 4.0 --max-changes 12
fi
repeat converge_e refine_step.py converge
say "chain_more end on $K; best model $(best)"
