#!/bin/bash
# after chain21: the population step again, the strongest peaks only and the side chain copied without shake
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last_ens() { for s in $(ls $K/trajectory | grep "^S[0-9]" | sort -r); do f=$K/trajectory/$s/model.pdb; [ $(grep -c "^ATOM" $f) -gt 10000 ] && { echo $s; return; }; done; }
while ! grep -q "chain21 end" /home/dev/runs/hr/chain21_7KR0.log 2>/dev/null; do sleep 60; done
for i in 1 2; do
  P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain22 copy vote, exact, 5 sigma ($i) from $P"
  phenix.python tools/copy_vote.py vote --run $K --parent $P --peak-sigma 5.0 --max-changes 8 --shake 0 --nproc 6 --tag ens_copy_vote_exact_$i
  Q=$(last_ens); [ "$Q" = "$P" ] && break
done
echo "[$(date -u +%FT%TZ)] chain22 end; ensemble in force $(last_ens)"
