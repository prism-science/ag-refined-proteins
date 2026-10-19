#!/bin/bash
# 7KR0 chain: a sparse water pick (4 sigma), then anisotropic water ADPs, each a judged step
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last() { ls $K/trajectory | grep "^S[0-9]" | sort | tail -1; }
P=$(last); echo "[$(date -u +%FT%TZ)] 7KR0 chain start from $P"
phenix.python tools/water_addition.py pick --run $K --parent $P --sigma 4.0 --nproc 6 --tag water_pick_4.0
P=$(last); echo "[$(date -u +%FT%TZ)] after pick 4.0: $P"
phenix.python tools/refine_step.py aniso-water --run $K --parent $P --nproc 6
P=$(last); echo "[$(date -u +%FT%TZ)] after aniso-water: $P"
phenix.python tools/refine_step.py converge --run $K --parent $P --nproc 6
echo "[$(date -u +%FT%TZ)] 7KR0 chain end; model in force $(last)"
