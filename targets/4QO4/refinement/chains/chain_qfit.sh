#!/bin/bash
# scripts/chain_qfit.sh RUN [NPROC] [COPIES] [PARENT]: the split into COPIES (default 2) copies from qFit conformers (the
# systematic multiconformer builder on the work-only 2mFo-DFc map), then the solvent, ADP, convergence, occupancy,
# reletter and copy-vote levers on it when it is the best model, then convergence. Same rules as
# scripts/chain_target.sh (the best recorded model is the parent; a worse BUILD is left behind).
set -u
K=${1:?run directory}
NP=${2:-6}
C=${3:-2}
PARENT=${4:-}
source "$(dirname "$0")/chain_lib.sh"
B0=$(best)
P=${PARENT:-$B0}
say "chain_qfit start on $K: $C copies from qFit, parent $P (best $B0)"
say "split $C copies from $P, source qfit"
run split_conformations.py build --parent "$P" --source qfit --copies "$C" --mc 20 --tag "split_qfit_$C"
say "after the split the best model is $(best)"
if [ "$(best)" != "$B0" ]; then
  for s in 4.0 3.0 2.5; do repeat "pick_${s}_q" water_addition.py pick --sigma "$s"; done
  repeat aniso_water_q refine_step.py aniso-water
  repeat converge_q refine_step.py converge
  once occupancies_q refine_step.py occupancies
  once reletter_q water_addition.py reletter
  repeat copy_vote_q copy_vote.py vote --peak-sigma 4.0 --max-changes 12
  repeat converge_r refine_step.py converge
fi
say "chain_qfit end on $K; best model $(best)"
