#!/bin/bash
# scripts/chain_peaks.sh RUN [NPROC] [NEAR]: Coot auto-fit rotamers on the residues whose side chains sit next to the
# strongest work-only difference peaks (the peak worklist with a credit radius of NEAR A, 4.5 by default: 4QO4 S0017
# has 9.0, 8.4 and 8.1 sigma peaks 3.3 to 3.6 A from GLU95, LYS51 and GLN18, out of the default 1.6 A reach),
# repeated while accepted, then convergence. Same rules as scripts/chain_target.sh.
set -u
K=${1:?run directory}
NP=${2:-6}
NEAR=${3:-4.5}
source "$(dirname "$0")/chain_lib.sh"
say "chain_peaks start on $K from $(best), credit radius $NEAR A"
repeat coot_rotamers_near coot_fix.py rotamers --from-peaks --peak-sigma 4.0 --near "$NEAR" --max-changes 12
repeat converge_p refine_step.py converge
say "chain_peaks end on $K; best model $(best)"
