#!/bin/bash
# after chain5: the merge back to conformers (a BUILD step, the single-model deliverable)
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last() { ls $K/trajectory | grep "^S[0-9]" | sort | tail -1; }
while ! grep -q "chain5 end" /home/dev/runs/hr/chain5_7KR0.log 2>/dev/null; do sleep 60; done
P=$(last); echo "[$(date -u +%FT%TZ)] chain6: merge from $P"
phenix.python tools/merge_conformations.py build --run $K --parent $P --nproc 6 --tag merge_conformers_b
echo "[$(date -u +%FT%TZ)] chain6 end; model in force $(last)"
