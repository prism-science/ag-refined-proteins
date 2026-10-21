#!/bin/bash
# scripts/chain_six.sh RUN [NPROC] [COPIES]: the split into COPIES (default 6) copies from shake from the best model,
# then the ensemble levers on it when it is the best model. chain_target.sh gives two copies at 1.3-1.5 A; on 3TC7
# at 1.5 A the six-copy shake split read 0.167 from 0.186 on the first day (2026-10-14), so the six-copy form is
# tried too. The tighter weights come first (2026-10-20): at 1.5-1.7 A an ensemble's gap sits above the run's cap
# (1LZ8: 0.086 against 0.071; 3TC7 day one: 0.060 against 0.049) and the tighter weights are the lever that lowers
# R-free and narrows the gap at the same time (1LZ8 S0048: -11.8 sigma, gap -0.005); the looser pair of 7KR0 comes
# last. Same rules as scripts/chain_target.sh.
set -u
K=${1:?run directory}
NP=${2:-6}
C=${3:-6}
source "$(dirname "$0")/chain_lib.sh"
B0=$(best)
say "chain_six start on $K from $B0: $C copies from shake"
split "$C"
if [ "$(best)" != "$B0" ]; then
  ladder weights_tight_s "1.0 1.0" "2.0 2.0" "3.0 3.0"
  for s in 4.0 3.0 2.5; do repeat "pick_${s}_s" water_addition.py pick --sigma "$s"; done
  repeat aniso_water_s refine_step.py aniso-water
  repeat converge_s refine_step.py converge
  once occupancies_s refine_step.py occupancies
  repeat coot_rotamers_s coot_fix.py rotamers --from-peaks --peak-sigma 4.0 --near 4.5 --max-changes 12
  once reletter_s water_addition.py reletter
  repeat copy_vote_s copy_vote.py vote --peak-sigma 4.0 --max-changes 12
  ladder weights_loose_s "0.3 0.25"
  repeat converge_t refine_step.py converge
fi
say "chain_six end on $K; best model $(best)"
