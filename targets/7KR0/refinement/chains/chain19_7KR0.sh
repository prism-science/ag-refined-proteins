#!/bin/bash
# after chain14 (Coot rotamers): the reference solvent model from our own sites. Every water to ceil(occupancy x 6) copies, refined with each at or below 1/6 (the cap stands when accepted); then picks in copies mode; convergence
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last_ens() { for s in $(ls $K/trajectory | grep "^S[0-9]" | sort -r); do f=$K/trajectory/$s/model.pdb; [ $(grep -c "^ATOM" $f) -gt 10000 ] && { echo $s; return; }; done; }
while ! grep -q "chain14 end" /home/dev/runs/hr/chain14_7KR0.log 2>/dev/null; do sleep 60; done
P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain19 water copies, all, capped, from $P"
phenix.python tools/water_addition.py copies --run $K --parent $P --all --cap --jitter 0 --nproc 6 --tag ens_water_cap_b
Q=$(last_ens)
if [ "$Q" != "$P" ]; then
  for i in 1 2; do
    P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain19 pick copies 2.5 ($i) from $P"
    phenix.python tools/water_addition.py pick --run $K --parent $P --sigma 2.5 --mode copies --nproc 6 --tag ens_pick_copies_cap_$i
    Q=$(last_ens); [ "$Q" = "$P" ] && break
  done
  P=$(last_ens); phenix.python tools/refine_step.py converge --run $K --parent $P --nproc 6 --tag ens_converge_20_h
fi
echo "[$(date -u +%FT%TZ)] chain19 end; ensemble in force $(last_ens)"
