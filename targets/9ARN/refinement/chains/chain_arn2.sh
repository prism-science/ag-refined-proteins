#!/bin/bash
# scripts/chain_arn2.sh RUN [NPROC]: the levers of 9ARN again from its first model below the deposited one (S0056,
# 2026-10-20: wc 2 / wu 2 with the secondary-structure and Ramachandran restraints standing). Under the recipe at
# 0.5 / 1.0 the 1 sigma water prune, the anisotropic waters and TLS were accepted against their controls and still
# above the deposited model; from a better base under tighter weights they may pass it. The prune, anisotropic waters
# while accepted, TLS by phenix.find_tls_groups, the mask, annealing. Same rules as scripts/chain_target.sh.
set -u
K=${1:?run directory}
NP=${2:-6}
source "$(dirname "$0")/chain_lib.sh"
say "chain_arn2 start on $K from $(best), standing weights $(standing_weights)"
once prune_b water_addition.py prune --sigma 1.0
repeat aniso_water_b2 refine_step.py aniso-water
once tls_find_b refine_step.py tls --groups find --replace
once mask_b refine_step.py mask
once anneal_b refine_step.py anneal
say "chain_arn2 end on $K; best model $(best)"
