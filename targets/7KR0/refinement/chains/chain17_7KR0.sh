#!/bin/bash
# after S0044 (the 2.0 sigma pick): de-overfit. Water occupancies back to the copy share and held; tighter ADP restraint rungs; convergence
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last_ens() { for s in $(ls $K/trajectory | grep "^S[0-9]" | sort -r); do f=$K/trajectory/$s/model.pdb; [ $(grep -c "^ATOM" $f) -gt 10000 ] && { echo $s; return; }; done; }
while ! grep -q "^S0044" $K/trajectory/score_history.txt 2>/dev/null; do sleep 60; done
sleep 30
P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain17 water-occ from $P"
phenix.python tools/refine_step.py water-occ --run $K --parent $P --nproc 6 --tag ens_water_occ_held
for W in "0.3 0.5" "0.3 1.0"; do
  set -- $W; P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain17 weights $1 $2 from $P"
  phenix.python tools/refine_step.py weights --run $K --parent $P --wc $1 --wu $2 --nproc 6 --tag ens_weights_${1}_${2}_b
done
P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain17 converge from $P"
phenix.python tools/refine_step.py converge --run $K --parent $P --nproc 6 --tag ens_converge_20_g
echo "[$(date -u +%FT%TZ)] chain17 end; ensemble in force $(last_ens)"
