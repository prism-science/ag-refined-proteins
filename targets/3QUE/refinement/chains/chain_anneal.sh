#!/bin/bash
# scripts/chain_anneal.sh RUN [NPROC] [PID]: simulated annealing as a lever (2026-10-20): the candidate's refinement runs
# phenix's Cartesian annealing (main.simulated_annealing) against the recipe without it, from the best model; accepted, the
# annealed model is the model in force and the lever repeats; then torsion-angle annealing one time, then convergence.
# A one-time perturbation of the model, never a standing option. Same rules as scripts/chain_target.sh. With PID the
# chain waits until that process (the chain before it) has ended.
set -u
K=${1:?run directory}
NP=${2:-6}
WAIT=${3:-}
source "$(dirname "$0")/chain_lib.sh"
if [ -n "$WAIT" ]; then
  say "chain_anneal waits for pid $WAIT"
  while [ -d "/proc/$WAIT" ]; do sleep 120; done
fi
say "chain_anneal start on $K from $(best), standing weights $(standing_weights)"
repeat anneal_a refine_step.py anneal
once anneal_torsion_a refine_step.py anneal --torsion
repeat converge_sa refine_step.py converge
say "chain_anneal end on $K; best model $(best)"
