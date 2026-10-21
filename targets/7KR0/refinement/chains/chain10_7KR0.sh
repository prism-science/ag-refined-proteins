#!/bin/bash
# in parallel with the ensemble chains: the merged single model S0017 (clashscore 24.8) gets its water clash cleanup and hygiene, each a judged step
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last_single() { for s in $(ls $K/trajectory | grep "^S[0-9]" | sort -r); do f=$K/trajectory/$s/model.pdb; n=$(grep -c "^ATOM" $f); [ $n -lt 10000 ] && [ $n -gt 5000 ] && { echo $s; return; }; done; }
P=$(last_single); echo "[$(date -u +%FT%TZ)] chain10 start from the merged model $P"
for i in 1 2 3; do
  P=$(last_single); phenix.python tools/water_addition.py cleanup --run $K --parent $P --nproc 6 --tag single_cleanup_$i
  Q=$(last_single); [ "$Q" = "$P" ] && break
done
P=$(last_single); phenix.python tools/water_addition.py hygiene --run $K --parent $P --nproc 6 --tag single_hygiene
P=$(last_single); phenix.python tools/refine_step.py converge --run $K --parent $P --nproc 6 --tag single_converge
echo "[$(date -u +%FT%TZ)] chain10 end; single model in force $(last_single)"
