#!/bin/bash
# after S0041 (the copies-mode pick): the single-mode ladder on the model in force (2.5 sigma while accepted, 2.0 once), convergence, anisotropic waters
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last_ens() { for s in $(ls $K/trajectory | grep "^S[0-9]" | sort -r); do f=$K/trajectory/$s/model.pdb; [ $(grep -c "^ATOM" $f) -gt 10000 ] && { echo $s; return; }; done; }
while ! grep -q "^S0041" $K/trajectory/score_history.txt 2>/dev/null; do sleep 60; done
sleep 30
for i in 1 2 3; do
  P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain16 pick 2.5 ($i) from $P"
  phenix.python tools/water_addition.py pick --run $K --parent $P --sigma 2.5 --nproc 6 --tag ens_pick_2.5_e$i
  Q=$(last_ens); [ "$Q" = "$P" ] && break
done
P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain16 pick 2.0 from $P"
phenix.python tools/water_addition.py pick --run $K --parent $P --sigma 2.0 --nproc 6 --tag ens_pick_2.0_c
P=$(last_ens); phenix.python tools/refine_step.py converge --run $K --parent $P --nproc 6 --tag ens_converge_20_f
P=$(last_ens); phenix.python tools/refine_step.py aniso-water --run $K --parent $P --nproc 6 --tag ens_aniso_water_h
echo "[$(date -u +%FT%TZ)] chain16 end; ensemble in force $(last_ens)"
