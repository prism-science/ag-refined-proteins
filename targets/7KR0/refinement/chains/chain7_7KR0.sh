#!/bin/bash
# after chain6 (the merge): the third lever set on the 7KR0 ensemble, from the model in force (an ensemble step)
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last_ens() { for s in $(ls $K/trajectory | grep "^S[0-9]" | sort -r); do f=$K/trajectory/$s/model.pdb; grep -q "^ATOM.\{10\}[A-Z]" $f && [ $(grep -c "^ATOM" $f) -gt 10000 ] && { echo $s; return; }; done; }
while ! grep -q "chain6 end" /home/dev/runs/hr/chain6_7KR0.log 2>/dev/null; do sleep 60; done
P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain7 start from the ensemble in force $P"
phenix.python tools/water_addition.py pick --run $K --parent $P --sigma 2.0 --nproc 6 --tag ens_pick_2.0
P=$(last_ens); echo "[$(date -u +%FT%TZ)] after pick 2.0: $P"
phenix.python tools/refine_step.py aniso-water --run $K --parent $P --nproc 6 --tag ens_aniso_water_b
P=$(last_ens); echo "[$(date -u +%FT%TZ)] after aniso-water b: $P"
phenix.python tools/refine_step.py converge --run $K --parent $P --nproc 6 --tag ens_converge_20_b
P=$(last_ens); echo "[$(date -u +%FT%TZ)] after converge: $P"
phenix.python tools/refine_step.py occupancies --run $K --parent $P --nproc 6 --tag ens_occupancies
P=$(last_ens); echo "[$(date -u +%FT%TZ)] after occupancies: $P"
phenix.python tools/water_addition.py pick --run $K --parent $P --sigma 2.5 --nproc 6 --tag ens_pick_2.5_b
P=$(last_ens); echo "[$(date -u +%FT%TZ)] after pick 2.5 b: $P"
phenix.python tools/refine_step.py aniso-water --run $K --parent $P --nproc 6 --tag ens_aniso_water_c
echo "[$(date -u +%FT%TZ)] chain7 end; ensemble in force $(last_ens)"
