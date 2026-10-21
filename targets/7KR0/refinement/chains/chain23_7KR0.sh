#!/bin/bash
# the clash fix that deletes nothing: waters in own-copy clashes move to a copy they clear; repeated while accepted
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last_ens() { for s in $(ls $K/trajectory | grep "^S[0-9]" | sort -r); do f=$K/trajectory/$s/model.pdb; [ $(grep -c "^ATOM" $f) -gt 10000 ] && { echo $s; return; }; done; }
for i in 1 2; do
  P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain23 water reletter $i from $P"
  phenix.python tools/water_addition.py reletter --run $K --parent $P --nproc 6 --tag ens_water_reletter_$i
  Q=$(last_ens); [ "$Q" = "$P" ] && break
done
echo "[$(date -u +%FT%TZ)] chain23 end; ensemble in force $(last_ens)"
