#!/bin/bash
# after chain9: the water ladder again on the converged model (2.5 sigma repeated while accepted, then 2.0 sigma one time), convergence, anisotropic waters
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last_ens() { for s in $(ls $K/trajectory | grep "^S[0-9]" | sort -r); do f=$K/trajectory/$s/model.pdb; [ $(grep -c "^ATOM" $f) -gt 10000 ] && { echo $s; return; }; done; }
while ! grep -q "chain9 end" /home/dev/runs/hr/chain9_7KR0.log 2>/dev/null; do sleep 60; done
P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain13 start from $P"
for i in 1 2 3; do
  P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain13 pick 2.5 ($i) from $P"
  phenix.python tools/water_addition.py pick --run $K --parent $P --sigma 2.5 --nproc 6 --tag ens_pick_2.5_d$i
  Q=$(last_ens); [ "$Q" = "$P" ] && break
done
P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain13 pick 2.0 from $P"
phenix.python tools/water_addition.py pick --run $K --parent $P --sigma 2.0 --nproc 6 --tag ens_pick_2.0_b
P=$(last_ens); phenix.python tools/refine_step.py converge --run $K --parent $P --nproc 6 --tag ens_converge_20_d
P=$(last_ens); phenix.python tools/refine_step.py aniso-water --run $K --parent $P --nproc 6 --tag ens_aniso_water_f
echo "[$(date -u +%FT%TZ)] chain13 end; ensemble in force $(last_ens)"
