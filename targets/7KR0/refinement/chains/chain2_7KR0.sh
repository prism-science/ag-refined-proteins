#!/bin/bash
# 7KR0 ensemble pipeline (protocol.md stages 1, 2c, 2b, 3, 4, 7), one judged step at a time; starts from the model in force
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last() { ls $K/trajectory | grep "^S[0-9]" | sort | tail -1; }
P=$(last); echo "[$(date -u +%FT%TZ)] chain2 start from $P"
phenix.python tools/split_conformations.py build --run $K --parent $P --source shake --nproc 3 --mc 20
P=$(last); echo "[$(date -u +%FT%TZ)] after split: $P"
phenix.python tools/water_addition.py pick --run $K --parent $P --sigma 4.0 --nproc 6 --tag ens_pick_4.0
P=$(last); echo "[$(date -u +%FT%TZ)] after ens pick 4.0: $P"
phenix.python tools/conn_optim.py relabel --run $K --parent $P --nproc 6 --effort-min 10 --threads 8 --tag ens_relabel_10
P=$(last); echo "[$(date -u +%FT%TZ)] after relabel: $P"
phenix.python tools/water_addition.py pick --run $K --parent $P --sigma 3.0 --nproc 6 --tag ens_pick_3.0
P=$(last); echo "[$(date -u +%FT%TZ)] after ens pick 3.0: $P"
phenix.python tools/refine_step.py aniso-water --run $K --parent $P --nproc 6 --tag ens_aniso_water
P=$(last); echo "[$(date -u +%FT%TZ)] after aniso-water: $P"
phenix.python tools/merge_conformations.py build --run $K --parent $P --nproc 6
P=$(last); echo "[$(date -u +%FT%TZ)] after merge: $P"
phenix.python tools/score_model.py final --run $K --reason "7KR0 pipeline: split, picks, relabel, aniso water, merge"
echo "[$(date -u +%FT%TZ)] chain2 end; model in force $(last)"
