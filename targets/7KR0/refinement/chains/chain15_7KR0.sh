#!/bin/bash
# after the running 2.5 sigma pick (S0039): waters per copy. The copies step (lettered waters above their share get their copies), repeated while accepted; picks in copies mode at 2.5 then 2.0 sigma; convergence; anisotropic waters
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last_ens() { for s in $(ls $K/trajectory | grep "^S[0-9]" | sort -r); do f=$K/trajectory/$s/model.pdb; [ $(grep -c "^ATOM" $f) -gt 10000 ] && { echo $s; return; }; done; }
while ! grep -q "^S0039" $K/trajectory/score_history.txt 2>/dev/null; do sleep 60; done
sleep 30
for i in 1 2 3; do
  P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain15 water copies $i from $P"
  phenix.python tools/water_addition.py copies --run $K --parent $P --nproc 6 --tag ens_water_copies_$i
  Q=$(last_ens); [ "$Q" = "$P" ] && break
done
for i in 1 2 3; do
  P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain15 pick copies 2.5 ($i) from $P"
  phenix.python tools/water_addition.py pick --run $K --parent $P --sigma 2.5 --mode copies --nproc 6 --tag ens_pick_copies_2.5_$i
  Q=$(last_ens); [ "$Q" = "$P" ] && break
done
P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain15 pick copies 2.0 from $P"
phenix.python tools/water_addition.py pick --run $K --parent $P --sigma 2.0 --mode copies --nproc 6 --tag ens_pick_copies_2.0
P=$(last_ens); phenix.python tools/refine_step.py converge --run $K --parent $P --nproc 6 --tag ens_converge_20_e
P=$(last_ens); phenix.python tools/refine_step.py aniso-water --run $K --parent $P --nproc 6 --tag ens_aniso_water_g
echo "[$(date -u +%FT%TZ)] chain15 end; ensemble in force $(last_ens)"
