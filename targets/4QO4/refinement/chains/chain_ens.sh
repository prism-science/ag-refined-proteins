#!/bin/bash
# scripts/chain_ens.sh RUN [NPROC]: the levers not yet tried on the best models of 1LZ8 and 4QO4 (2026-10-19 22:30Z):
# the bulk-solvent mask radii optimised (refine_step.py mask), the tighter weights ladder 1.0/1.0 and 2.0/2.0 and the
# looser 0.3/0.25 on the model in force (on 1LZ8 the ladder ran on the single model only; its two-copy ensemble has the
# default weights), the altloc occupancies again (refused at -1.7 sigma on 1LZ8's ensemble), settle, convergence. Same
# rules as scripts/chain_target.sh; a rung equal to the standing weights is skipped; cached arms replay.
set -u
K=${1:?run directory}
NP=${2:-6}
source "$(dirname "$0")/chain_lib.sh"
say "chain_ens start on $K from $(best), standing weights $(standing_weights)"
once mask_e refine_step.py mask
ladder weights_tight_e "1.0 1.0" "2.0 2.0"
ladder weights_loose_e "0.3 0.25"
repeat occupancies_e refine_step.py occupancies
repeat settle_e refine_step.py settle
repeat converge_e2 refine_step.py converge
say "chain_ens end on $K; best model $(best)"
