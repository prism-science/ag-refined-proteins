#!/bin/bash
# scripts/fork_gap_after.sh RUN PID [NPROC]: wait for PID (the chain on RUN) to end, then fork RUN into RUN_gap with the
# looser one-step gap bound (gap_widen_max 0.010, gap_abs_max 0.12, its own metaparameters, a note in run.json; the
# bounds of the 3TC7 fork T431c8e_gap, 2026-10-20) and run scripts/chain_gap.sh on the fork. For the sub-angstrom
# targets 7R2H and 8C5N, whose picks on the ensemble lose accepted gains to the gap rule (2026-10-21). PID 0 forks at
# once. The main run keeps the standing bounds; the operator judges the fork's gap with the vault at the end.
set -u
K=${1:?run directory}
WAIT=${2:?pid to wait for, or 0}
NP=${3:-6}
DST=${K}_gap
cd "$(dirname "$0")/.."
if [ "$WAIT" != "0" ]; then
  echo "[$(date -u +%FT%TZ)] fork_gap_after waits for pid $WAIT on $K"
  while [ -d "/proc/$WAIT" ]; do sleep 120; done
fi
if [ -e "$DST" ]; then echo "[$(date -u +%FT%TZ)] $DST exists: nothing done"; exit 1; fi
bash scripts/fork_run.sh "$K" "$DST" | tail -1
rsync -a --chmod=u+rwX "$K/refine_cache/" "$DST/refine_cache/" 2>/dev/null || true
python3 - "$DST" <<'PY'
import json, sys
d = sys.argv[1]
p = d + "/metaparams.yaml"
t = open(p).read()
assert "gap_widen_max: 0.002" in t
t = t.replace("gap_widen_max: 0.002", "gap_widen_max: 0.010        # the gap fork: the bound of 0.002 refused accepted-size gains of the picks on the ensemble; the operator judges the fork's gap with the vault at the end")
t = t.replace("gap_abs_max: 0.03", "gap_abs_max: 0.12           # the gap fork: the cap does not bind; R-free and geometry decide") if "gap_abs_max: 0.03" in t else t + "gap_abs_max: 0.12           # the gap fork: the cap does not bind\n"
open(p, "w").write(t)
r = json.load(open(d + "/run.json"))
r["gap_max"] = 0.12
r.setdefault("notes", []).append({"utc": __import__("datetime").datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                                  "what": "gap fork of %s: gap_widen_max 0.010 and gap_abs_max 0.12 (gap_max 0.12); the main run keeps the standing bounds" % d.split("/")[-1].replace("_gap", "")})
json.dump(r, open(d + "/run.json", "w"), indent=1, sort_keys=True)
print(d.split("/")[-1], "gap_max", r["gap_max"], "standing", {k: v for k, v in (r.get("standing") or {}).items() if k in ("wc", "wu", "adp", "tls", "mask")})
PY
echo "[$(date -u +%FT%TZ)] chain_gap starts on $DST"
exec bash scripts/chain_gap.sh "$DST" "$NP"
