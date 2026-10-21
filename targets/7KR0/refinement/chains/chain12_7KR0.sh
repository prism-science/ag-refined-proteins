#!/bin/bash
# after chain8: the relabel with the waters following their copies (S0028 reused while S0025 is in force), repeated while accepted; then hydrogens; then occupancies
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last_ens() { for s in $(ls $K/trajectory | grep "^S[0-9]" | sort -r); do f=$K/trajectory/$s/model.pdb; [ $(grep -c "^ATOM" $f) -gt 10000 ] && { echo $s; return; }; done; }
while ! grep -q "chain8 end" /home/dev/runs/hr/chain11_7KR0.log 2>/dev/null; do sleep 60; done
P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain12 relabel, waters follow, from $P"
if [ "$P" = "S0025" ]; then
  phenix.python tools/conn_optim.py relabel --run $K --parent S0025 --from-relabel S0028 --nproc 6 --tag ens_relabel_prot_1w
else
  phenix.python tools/conn_optim.py relabel --run $K --parent $P --nproc 6 --effort-min 10 --threads 8 --tag ens_relabel_prot_2
fi
for i in 2 3; do
  Q=$(last_ens); [ "$Q" = "$P" ] && break
  P=$Q; echo "[$(date -u +%FT%TZ)] chain12 relabel $i from $P"
  phenix.python tools/conn_optim.py relabel --run $K --parent $P --nproc 6 --effort-min 10 --threads 8 --tag ens_relabel_prot_${i}w
done
P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain12 hydrogens from $P"
phenix.python tools/refine_step.py hydrogens --run $K --parent $P --nproc 6 --tag ens_hydrogens_1
P=$(last_ens); echo "[$(date -u +%FT%TZ)] chain12 occupancies from $P"
phenix.python tools/refine_step.py occupancies --run $K --parent $P --nproc 6 --tag ens_occupancies_b
echo "[$(date -u +%FT%TZ)] chain12 end; ensemble in force $(last_ens)"
