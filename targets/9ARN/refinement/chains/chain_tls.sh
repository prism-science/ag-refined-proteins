#!/bin/bash
# scripts/chain_tls.sh RUN [NPROC]: the deposited TLS groups restored with an isotropic residual, then the levers
# that depend on it, on a run whose chain ran before the lever existed (9ARN, 9D5Y, 7DVR, 5MR8; 2026-10-19). The
# anonymiser removes the TLS matrices with the REMARK records; a deposited ANISOU set that is a TLS total U then
# refines as free anisotropic ADPs. Same rules as scripts/chain_target.sh; the log is RUN/chain_target.log.
set -u
K=${1:?run directory}
NP=${2:-6}
source "$(dirname "$0")/chain_lib.sh"
say "chain_tls start on $K from $(best)"
floor
once tls_deposited_a refine_step.py tls --groups deposited --iso
repeat settle_c refine_step.py settle
once add_hydrogens_b refine_step.py add-hydrogens
ladder weights_tight "1.0 1.0" "2.0 2.0"
ladder weights_loose "0.3 0.25" "0.2 0.25"
repeat aniso_water_c refine_step.py aniso-water
repeat converge_d refine_step.py converge
say "chain_tls end on $K; best model $(best)"
