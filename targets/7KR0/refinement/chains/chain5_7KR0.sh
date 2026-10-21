#!/bin/bash
# after chain2 on the 7KR0 ensemble: the second lever set, each a judged step from the model in force
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last() { ls $K/trajectory | grep "^S[0-9]" | sort | tail -1; }
while ! grep -q "chain2 end" /home/dev/runs/hr/chain4_7KR0.log 2>/dev/null; do sleep 60; done
P=$(last); echo "[$(date -u +%FT%TZ)] chain5 start from $P"
phenix.python tools/refine_step.py weights --run $K --parent $P --wc 0.3 --wu 0.25 --nproc 6 --tag ens_weights_03_025
P=$(last); echo "[$(date -u +%FT%TZ)] after weights: $P"
phenix.python tools/conn_optim.py relabel --run $K --parent $P --nproc 6 --effort-min 20 --threads 8 --tag ens_relabel_20
P=$(last); echo "[$(date -u +%FT%TZ)] after relabel 20: $P"
phenix.python tools/water_addition.py pick --run $K --parent $P --sigma 3.0 --nproc 6 --tag ens_pick_3.0_b
P=$(last); echo "[$(date -u +%FT%TZ)] after pick 3.0: $P"
phenix.python tools/water_addition.py pick --run $K --parent $P --sigma 2.5 --nproc 6 --tag ens_pick_2.5
P=$(last); echo "[$(date -u +%FT%TZ)] after pick 2.5: $P"
phenix.python tools/refine_step.py converge --run $K --parent $P --nproc 6 --tag ens_converge_20
P=$(last); echo "[$(date -u +%FT%TZ)] after converge: $P"
phenix.python tools/score_model.py final --run $K --reason "7KR0 pipeline, second lever set: weights, relabel 20 min, picks 3.0 and 2.5, converge" --force
echo "[$(date -u +%FT%TZ)] chain5 end; model in force $(last)"
