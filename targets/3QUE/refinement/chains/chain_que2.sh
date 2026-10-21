#!/bin/bash
# scripts/chain_que2.sh RUN [NPROC]: 3QUE after chain_lowres (2026-10-20: best S0041 at 0.2705 under wc 2 / wu 2 and TLS
# with 3 groups). Riding hydrogens under the tight weights (refused at +0.016 under wc 0.5, where phenix.ready_set's
# model drifted to a bond RMSD of 0.023 A), then the levers that were refused by a thousandth, from the new model when
# the hydrogens are accepted: the two restraint sets (-0.0023 against the control, S0037), the Coot fits of the rotamer
# outliers (-0.0011, S0042), settle, convergence. Same rules as scripts/chain_target.sh.
set -u
K=${1:?run directory}
NP=${2:-6}
source "$(dirname "$0")/chain_lib.sh"
say "chain_que2 start on $K from $(best), standing weights $(standing_weights)"
once add_hydrogens_q refine_step.py add-hydrogens
once restraints_q refine_step.py restraints --ss --rama
repeat coot_outliers_q coot_fix.py rotamers --from-outliers --min-cc-gain 0.0 --max-changes 12
repeat settle_q refine_step.py settle
once converge_q refine_step.py converge
say "chain_que2 end on $K; best model $(best)"
