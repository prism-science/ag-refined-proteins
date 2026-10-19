#!/bin/bash
# after the first 7KR0 chain: re-judge the anisotropic-water arms of S0004 under the clash cap of 15, then the ensemble pipeline
source /opt/phenix/phenix_env.sh >/dev/null 2>&1
cd /home/dev/hr
K=/home/dev/runs/hr/Tff1b3f
export HR_RUNS=/home/dev/runs/hr HR_NPROC=6
last() { ls $K/trajectory | grep "^S[0-9]" | sort | tail -1; }
while ! grep -q "chain end" /home/dev/runs/hr/chain_7KR0.log 2>/dev/null; do sleep 60; done
echo "[$(date -u +%FT%TZ)] chain4: re-judge S0004 (anisotropic water ADPs) under clash cap 15"
rm -rf $K/pending/aniso_water_rejudge; cp -r $K/trajectory/rejected/S0004/arms $K/pending/aniso_water_rejudge
python3 - <<"PY"
import json
K = "/home/dev/runs/hr/Tff1b3f"
p = K + "/pending/aniso_water_rejudge/refine.json"
d = json.load(open(p))
for arm in d["arms"].values():
    for r in arm:
        for key in ("model", "workdir", "log"):
            if r.get(key):
                r[key] = r[key].replace("/pending/aniso-water/", "/pending/aniso_water_rejudge/")
json.dump(d, open(p, "w"), indent=1)
print("arms re-pointed:", {k: len(v) for k, v in d["arms"].items()})
PY
phenix.python tools/score_model.py judge --run $K --pending aniso_water_rejudge --parent S0001 --worker refinement --tool refine_step --kind improving --stage refinement --description "water ADPs anisotropic (the arms of S0004, re-judged under the clash cap of 15; operator 2026-10-15)"
P=$(last); echo "[$(date -u +%FT%TZ)] after the re-judge: $P"
bash /home/dev/runs/hr/chain2_7KR0.sh
