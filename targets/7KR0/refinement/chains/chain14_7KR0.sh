#!/bin/bash
# after chain13: stage 2d on the ensemble, Coot auto-fit rotamers on the RSCC worklist (chapi), repeated while accepted
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last_ens() { for s in $(ls $K/trajectory | grep "^S[0-9]" | sort -r); do f=$K/trajectory/$s/model.pdb; [ $(grep -c "^ATOM" $f) -gt 10000 ] && { echo $s; return; }; done; }
while ! grep -q "chain18 end" /home/dev/runs/hr/chain18_7KR0.log 2>/dev/null; do sleep 60; done
for i in 1 2 3; do
  P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain14 coot rotamers $i from $P"
  phenix.python tools/coot_fix.py rotamers --run $K --parent $P --from-peaks --peak-sigma 4.0 --max-changes 12 --nproc 6 --tag ens_coot_rotamers_$i
  Q=$(last_ens); [ "$Q" = "$P" ] && break
done
echo "[$(date -u +%FT%TZ)] chain14 end; ensemble in force $(last_ens)"
