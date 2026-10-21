#!/bin/bash
# scripts/chain_lz2.sh RUN [NPROC]: fewer ADP parameters and the low-resolution restraints on 1LZ8's two-copy ensemble
# (2026-10-20: best S0060 at 0.2440 with a gap of 0.077 under wc 2 / wu 2, TLS and the mask; every solvent, occupancy,
# convergence and annealing lever refused). The secondary-structure and Ramachandran restraints, one and two group B
# factors for each residue, TLS by phenix.find_tls_groups against the standing group, wc 3 / wu 3, settle, convergence.
# Same rules as scripts/chain_target.sh.
set -u
K=${1:?run directory}
NP=${2:-6}
source "$(dirname "$0")/chain_lib.sh"
say "chain_lz2 start on $K from $(best), standing weights $(standing_weights)"
once restraints_lz refine_step.py restraints --ss --rama
once group_adp_lz1 refine_step.py group-adp --groups 1
once group_adp_lz2 refine_step.py group-adp --groups 2
once tls_find_lz refine_step.py tls --groups find --replace
once weights_3_3_lz refine_step.py weights --wc 3.0 --wu 3.0
repeat settle_lz refine_step.py settle
repeat converge_lz refine_step.py converge
say "chain_lz2 end on $K; best model $(best)"
