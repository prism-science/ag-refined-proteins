#!/bin/bash
# after chain8: the next restraint-weight rungs on the ensemble (E041 line: looser restraints lowered R-free, the gap bound judges), convergence, anisotropic waters
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last_ens() { for s in $(ls $K/trajectory | grep "^S[0-9]" | sort -r); do f=$K/trajectory/$s/model.pdb; [ $(grep -c "^ATOM" $f) -gt 10000 ] && { echo $s; return; }; done; }
while ! grep -q "chain12 end" /home/dev/runs/hr/chain12_7KR0.log 2>/dev/null; do sleep 60; done
P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain9 start from $P"
for W in "0.3 0.1" "0.2 0.25" "0.2 0.1"; do
  set -- $W; P=$(last_ens)
  phenix.python tools/refine_step.py weights --run $K --parent $P --wc $1 --wu $2 --nproc 6 --tag ens_weights_${1}_${2}
done
P=$(last_ens); phenix.python tools/refine_step.py converge --run $K --parent $P --nproc 6 --tag ens_converge_20_c
P=$(last_ens); phenix.python tools/refine_step.py aniso-water --run $K --parent $P --nproc 6 --tag ens_aniso_water_e
echo "[$(date -u +%FT%TZ)] chain9 end; ensemble in force $(last_ens)"
