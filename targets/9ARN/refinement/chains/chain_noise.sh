#!/bin/bash
# scripts/chain_noise.sh RUN [NPROC]: fewer or tighter parameters on a run whose data lose their signal well inside the
# nominal resolution (9ARN, 2026-10-20: every refinement under the recipe raises R-free by 0.01 while R-work falls; the
# deposited model stays the best). Each pair from the best model one time (not a ladder: the first rung was refused
# there): wc/wu 2, 3 and 5 together, wu 3 and 5 alone, one and two group B factors for each residue, the
# secondary-structure and Ramachandran restraints, phenix's rotamer fixing, convergence. Same rules as
# scripts/chain_target.sh.
set -u
K=${1:?run directory}
NP=${2:-6}
source "$(dirname "$0")/chain_lib.sh"
say "chain_noise start on $K from $(best), standing weights $(standing_weights)"
once weights_2_2 refine_step.py weights --wc 2.0 --wu 2.0
once weights_3_3 refine_step.py weights --wc 3.0 --wu 3.0
once weights_5_5 refine_step.py weights --wc 5.0 --wu 5.0
once weights_0.5_3 refine_step.py weights --wc 0.5 --wu 3.0
once weights_0.5_5 refine_step.py weights --wc 0.5 --wu 5.0
once group_adp_n1 refine_step.py group-adp --groups 1
once group_adp_n2 refine_step.py group-adp --groups 2
once restraints_n refine_step.py restraints --ss --rama
once fix_rotamers_n refine_step.py fix-rotamers
repeat converge_n refine_step.py converge
say "chain_noise end on $K; best model $(best)"
