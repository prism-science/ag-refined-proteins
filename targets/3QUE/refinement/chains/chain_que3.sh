#!/bin/bash
# scripts/chain_que3.sh RUN [NPROC]: 3QUE after the reference-model restraints were accepted (S0057, 2026-10-21: R-free
# 0.2685 -> 0.2642, rotamer outliers 8.3 % -> 3.6 %, the gap 0.020 narrower). The levers refused under the old recipe,
# again under the new one: the Coot fits of the remaining rotamer outliers, the water picks at 4 and 3 sigma, riding
# hydrogens, the mask, settle and convergence. Same rules as scripts/chain_target.sh.
set -u
K=${1:?run directory}
NP=${2:-6}
source "$(dirname "$0")/chain_lib.sh"
say "chain_que3 start on $K from $(best), standing weights $(standing_weights)"
repeat coot_outliers_r coot_fix.py rotamers --from-outliers --min-cc-gain 0.0 --max-changes 12
repeat pick_4.0_r water_addition.py pick --sigma 4.0
repeat pick_3.0_r water_addition.py pick --sigma 3.0
once add_hydrogens_r refine_step.py add-hydrogens
once mask_r refine_step.py mask
repeat settle_s refine_step.py settle
once converge_s refine_step.py converge
say "chain_que3 end on $K; best model $(best)"
