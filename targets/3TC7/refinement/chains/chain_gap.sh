#!/bin/bash
# scripts/chain_gap.sh RUN [NPROC]: the ensemble levers on a fork whose one-step gap bound is loosened (3TC7's
# T431c8e_gap, 2026-10-20: gap_widen_max 0.010, gap_abs_max 0.12, its own metaparameters). On the two-copy model of the
# main run every solvent lever lowered R-free by 0.002 to 0.006 and was refused for widening the gap by 0.005; in the
# fork R-free and geometry decide, and the operator judges the fork's gap with the vault at the end. The tight weights
# first (they narrow the gap), then fewer ADP parameters for six copies at 1.5 A (isotropic protein ADPs, one group B
# factor for each residue, TLS), the solvent ladder down to 2.0 sigma, convergence, occupancies, the Coot and population
# levers, the loose pair last. Same rules as scripts/chain_target.sh.
set -u
K=${1:?run directory}
NP=${2:-6}
source "$(dirname "$0")/chain_lib.sh"
say "chain_gap start on $K from $(best), standing weights $(standing_weights), $(grep -o 'gap_widen_max: [0-9.]*' "$K/metaparams.yaml")"
ladder weights_tight_g "1.0 1.0" "2.0 2.0" "3.0 3.0"
once iso_protein_g refine_step.py iso-protein
once group_adp_g1 refine_step.py group-adp --groups 1
once tls_g refine_step.py tls
for s in 4.0 3.0 2.5 2.0; do repeat "pick_${s}_g" water_addition.py pick --sigma "$s"; done
repeat aniso_water_g refine_step.py aniso-water
repeat converge_g refine_step.py converge
once occupancies_g refine_step.py occupancies
repeat pick_2.5_h water_addition.py pick --sigma 2.5
repeat coot_rotamers_g coot_fix.py rotamers --from-peaks --peak-sigma 4.0 --near 4.5 --max-changes 12
once reletter_g water_addition.py reletter
repeat copy_vote_g copy_vote.py vote --peak-sigma 4.0 --max-changes 12
ladder weights_loose_g "0.3 0.25"
repeat converge_h refine_step.py converge
say "chain_gap end on $K; best model $(best)"
