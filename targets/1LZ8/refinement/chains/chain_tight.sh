#!/bin/bash
# scripts/chain_tight.sh RUN [NPROC]: the tighter weights ladder on an ensemble whose gap sits above the run's cap, under
# the control clause of the gap cap (2026-10-20): 1LZ8's two-copy ensemble (S0035, gap 0.086 against the cap 0.071) had
# wc 1.0 / wu 1.0 refused at -11.8 sigma with a narrower gap (S0048) on the cap alone. The ladder 1.0/1.0, 2.0/2.0,
# 3.0/3.0, then the solvent, ADP, convergence and occupancy levers on the new best model. Same rules as
# scripts/chain_target.sh (cached arms replay).
set -u
K=${1:?run directory}
NP=${2:-6}
source "$(dirname "$0")/chain_lib.sh"
say "chain_tight start on $K from $(best), standing weights $(standing_weights)"
B0=$(best)
ladder weights_tight_t "1.0 1.0" "2.0 2.0" "3.0 3.0"
if [ "$(best)" != "$B0" ]; then
  for s in 4.0 3.0 2.5; do repeat "pick_${s}_t" water_addition.py pick --sigma "$s"; done
  repeat aniso_water_t refine_step.py aniso-water
  once occupancies_t refine_step.py occupancies
  once mask_t refine_step.py mask
  repeat converge_t2 refine_step.py converge
fi
say "chain_tight end on $K; best model $(best)"
