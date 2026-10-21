#!/bin/bash
# scripts/chain_target.sh RUN [NPROC]: the lever order on one preprocessed run, without an agent.
# RUN is the run directory (/home/dev/runs/hr/<handle>) with S0000 and S0001 in place. Every step is judged by the
# gate; an accepted lever repeats until it is refused (3 at most, SPEC §4.6). The parent of every step is the best
# model so far: the recorded step (INIT, ACCEPT or BUILD) with the lowest R-free, so a BUILD that scores above its
# parent is left behind (a split at 1.7 Å loses 0.05; 2026-10-19).
# The order (2026-10-19, after the first three targets at 1.4-1.7 Å): settle (the first refinement is not converged:
# 1LZ8 had 0.005 left), riding hydrogens (the deposited models have none), protein ADPs isotropic above 1.2 Å (9ARN
# was anisotropic at 1.37 Å and overfit), TLS, the weights ladders (tighter: 1.0/1.0, 2.0/2.0; looser: 0.3/0.25, 0.2/0.25; each rung while the
# one before is accepted; wc 0.5 / wu 1.0 is the recipe), NCS, settle again, then the 7KR0 order: water ADPs
# anisotropic, the split (6 copies at or below 1.3 Å, 2 copies at 1.3-1.5 Å, none above), the water picks, convergence,
# occupancies, Coot rotamers, reletter, copy votes. Levers that need an ensemble skip themselves on a single model.
# The log is RUN/chain_target.log.
set -u
K=${1:?run directory}
NP=${2:-6}
source "$(dirname "$0")/chain_lib.sh"
say "chain_target start on $K from $(best), d_min $(dmin)"
floor
once tls_deposited_a refine_step.py tls --groups deposited --iso
repeat settle_a refine_step.py settle
once add_hydrogens_a refine_step.py add-hydrogens
if below 1.2; then say "no iso-protein: d_min $(dmin) is at or below 1.2 A"; else once iso_protein_a refine_step.py iso-protein; fi
once tls_a refine_step.py tls
ladder weights_tight "1.0 1.0" "2.0 2.0"
ladder weights_loose "0.3 0.25" "0.2 0.25"
once ncs_a refine_step.py ncs
repeat settle_b refine_step.py settle
repeat aniso_water_a refine_step.py aniso-water
if below 1.3; then split 6; elif below 1.5; then split 2; else say "no split: d_min $(dmin) is above 1.5 A"; fi
for s in 4.0 3.0 2.5; do repeat "pick_${s}_a" water_addition.py pick --sigma "$s"; done
repeat aniso_water_b refine_step.py aniso-water
repeat converge_a refine_step.py converge
once occupancies_a refine_step.py occupancies
repeat pick_2.5_b water_addition.py pick --sigma 2.5
repeat coot_rotamers_a coot_fix.py rotamers --from-peaks --peak-sigma 4.0 --max-changes 12
once reletter_a water_addition.py reletter
repeat copy_vote_a copy_vote.py vote --peak-sigma 4.0 --max-changes 12
repeat converge_b refine_step.py converge
say "chain_target end on $K; best model $(best)"
