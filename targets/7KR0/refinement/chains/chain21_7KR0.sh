#!/bin/bash
# after chain20 (the population votes): when the votes changed the model, the 2.5 sigma rung again (it reopens after a change) and a convergence step
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last_ens() { for s in $(ls $K/trajectory | grep "^S[0-9]" | sort -r); do f=$K/trajectory/$s/model.pdb; [ $(grep -c "^ATOM" $f) -gt 10000 ] && { echo $s; return; }; done; }
while ! grep -q "chain20 end" /home/dev/runs/hr/chain20_7KR0.log 2>/dev/null; do sleep 60; done
P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain21 start from $P"
if [ "$P" != "S0042" ]; then
  for i in 1 2; do
    P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain21 pick 2.5 ($i) from $P"
    phenix.python tools/water_addition.py pick --run $K --parent $P --sigma 2.5 --nproc 6 --tag ens_pick_2.5_f$i
    Q=$(last_ens); [ "$Q" = "$P" ] && break
  done
  P=$(last_ens); phenix.python tools/refine_step.py converge --run $K --parent $P --nproc 6 --tag ens_converge_20_i
else
  echo "[$(date -u +%FT%TZ)] chain21: the votes changed nothing; no pick"
fi
echo "[$(date -u +%FT%TZ)] chain21 end; ensemble in force $(last_ens)"
