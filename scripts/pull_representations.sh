#!/usr/bin/env bash
# Refresh representations/7KR0/ (the E035 Untangler line, PROTOCOL §18) from the campaign pod. Run from the repository root.
#   1. stage on the pod (scripts/stage_representations_on_pod.py: copy the frozen six-copy models and map coefficients,
#      re-score every table row with the independent scorer, record composition, copy trajectories, hash, tar)
#   2. transfer the tarball as line-wrapped base64 in 100 000-line chunks, each verified by SHA-256
#   3. replace models/, scores/, trajectories/ and provenance_pod.json under representations/7KR0/ (README.md is kept),
#      then rebuild the table, provenance.json and MANIFEST.sha256
# The model list is in the staging script; edit it there when a stage produces a new frozen model.
set -euo pipefail
cd "$(dirname "$0")/.."
POD=(actl pod exec autoresearch -n diffuse --)
STAGE=/home/dev/runs/agrp_export_$(date -u +%Y%m%dT%H%MZ)_rep
TMP=$(mktemp -d)
filter() { grep -v -e 'Unable to use a TTY' -e 'newer actl' -e 'actl update' || true; }

echo "staging on pod: $STAGE"
"${POD[@]}" bash -lc "mkdir -p $STAGE && cat > $STAGE/stage_representations_on_pod.py" < scripts/stage_representations_on_pod.py 2>/dev/null | filter
"${POD[@]}" bash -lc "source /opt/phenix/phenix_env.sh && cd $STAGE && python3 stage_representations_on_pod.py $STAGE > driver.log 2>&1; tail -1 driver.log" 2>/dev/null | filter | tee "$TMP/done.txt"
TAR_SHA=$(grep -E '^DONE [0-9a-f]{64}$' "$TMP/done.txt" | cut -d' ' -f2) || { echo "staging failed; see $STAGE/driver.log on the pod" >&2; exit 1; }

echo "transferring"
B64=/home/dev/runs/agrp_rep_b64
"${POD[@]}" bash -lc "rm -rf $B64 && mkdir $B64 && base64 -w 76 $STAGE.tar.gz > $B64/all.b64 && cd $B64 && split -l 40000 -d -a 3 all.b64 part_ && sha256sum part_*" 2>/dev/null | filter > "$TMP/parts.txt"
while read -r want name; do
  for try in 1 2 3; do
    "${POD[@]}" bash -lc "cat $B64/$name" < /dev/null 2>/dev/null | grep -E '^[A-Za-z0-9+/=]+$' > "$TMP/$name" || true
    got=$(shasum -a 256 "$TMP/$name" | cut -d' ' -f1)
    [[ "$got" == "$want" ]] && break
    [[ $try == 3 ]] && { echo "chunk $name failed three times" >&2; exit 1; }
  done
done < "$TMP/parts.txt"
cat "$TMP"/part_* | base64 -d > "$TMP/rep.tar.gz"
LOCAL_SHA=$(shasum -a 256 "$TMP/rep.tar.gz" | cut -d' ' -f1)
[[ "$LOCAL_SHA" == "$TAR_SHA" ]] || { echo "tarball sha mismatch: pod $TAR_SHA local $LOCAL_SHA" >&2; exit 1; }
"${POD[@]}" bash -lc "rm -rf $B64" 2>/dev/null | filter

echo "extracting"
tar xzf "$TMP/rep.tar.gz" -C "$TMP"
SRC="$TMP/agrp_rep/representations/7KR0"
DST=representations/7KR0
mkdir -p "$DST"
rm -rf "$DST/models" "$DST/scores" "$DST/trajectories"
cp -R "$SRC/models" "$SRC/scores" "$SRC/trajectories" "$DST/"
cp "$SRC/provenance_pod.json" "$DST/provenance_pod.json"
python3 - "$DST" <<'PY'
import hashlib, json, os, sys
d = sys.argv[1]
man = json.load(open(os.path.join(d, "provenance_pod.json")))["files"]
for m in man:
    if m["file"] == "provenance_pod.json": continue
    assert hashlib.sha256(open(os.path.join(d, m["file"]), "rb").read()).hexdigest() == m["sha256"], m["file"]
print(f"verified {len(man)} files against the pod manifest")
PY
python3 scripts/build_representations.py
python3 scripts/build_index.py
rm -rf "$TMP"
echo "done: review git status, add a CHANGELOG.md line, commit"
