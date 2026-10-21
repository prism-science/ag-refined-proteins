#!/bin/bash
# after chain7: convergence first (40 cycles against the standing 10, repeated while accepted), then the connectivity chain (chain8); chain9 follows chain8 on its own
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last_ens() { for s in $(ls $K/trajectory | grep "^S[0-9]" | sort -r); do f=$K/trajectory/$s/model.pdb; [ $(grep -c "^ATOM" $f) -gt 10000 ] && { echo $s; return; }; done; }
while ! grep -q "chain7 end" /home/dev/runs/hr/chain7_7KR0.log 2>/dev/null; do sleep 60; done
for i in 1 2 3; do
  P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain11 converge 40 from $P ($i)"
  phenix.python tools/refine_step.py converge --run $K --parent $P --mc 40 --nproc 6 --tag ens_converge_40_$i
  Q=$(last_ens); [ "$Q" = "$P" ] && break
done
echo "[$(date -u +%FT%TZ)] chain11 end; ensemble in force $(last_ens); starting the connectivity chain"
bash /home/dev/runs/hr/chain8_7KR0.sh
