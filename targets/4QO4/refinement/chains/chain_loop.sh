#!/bin/bash
# scripts/chain_loop.sh RUN NPROC CHAIN START END SEQFILE: a missing loop built by phenix.fit_loops (tools/build_loop.py)
# as one judged step, then settle, the 4 sigma water pick and convergence from the best model. 4QO4 (2026-10-20):
# residues 69 to 72 of chain A. Same rules as scripts/chain_target.sh.
set -u
K=${1:?run directory}
NP=${2:-6}
CH=${3:?chain}
S=${4:?start}
E=${5:?end}
SEQ=${6:?sequence file}
source "$(dirname "$0")/chain_lib.sh"
say "chain_loop start on $K from $(best): residues $S to $E of chain $CH"
once "loop_${CH}_${S}_${E}" build_loop.py build --chain "$CH" --start "$S" --end "$E" --seq-file "$SEQ"
repeat settle_l refine_step.py settle
repeat pick_4.0_l water_addition.py pick --sigma 4.0
repeat converge_l refine_step.py converge
say "chain_loop end on $K; best model $(best)"
