#!/bin/bash
# after chain7: connectivity on the protein only (the view that converges), repeated while accepted, then waters again
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last_ens() { for s in $(ls $K/trajectory | grep "^S[0-9]" | sort -r); do f=$K/trajectory/$s/model.pdb; grep -q "^ATOM.\{10\}[A-Z]" $f && [ $(grep -c "^ATOM" $f) -gt 10000 ] && { echo $s; return; }; done; }
while ! grep -q "chain7 end" /home/dev/runs/hr/chain7_7KR0.log 2>/dev/null; do sleep 60; done
for i in 1 2 3; do
  P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain8 relabel $i from $P"
  phenix.python tools/conn_optim.py relabel --run $K --parent $P --nproc 6 --effort-min 10 --threads 8 --tag ens_relabel_prot_$i
  Q=$(last_ens); [ "$Q" = "$P" ] && break
done
P=$(last_ens); echo "[$(date -u +%FT%TZ)] after relabels: $P"
phenix.python tools/refine_step.py aniso-water --run $K --parent $P --nproc 6 --tag ens_aniso_water_d
P=$(last_ens); phenix.python tools/water_addition.py pick --run $K --parent $P --sigma 2.5 --nproc 6 --tag ens_pick_2.5_c
echo "[$(date -u +%FT%TZ)] chain8 end; ensemble in force $(last_ens)"
