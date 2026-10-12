#!/usr/bin/env bash
# Refresh this release from the campaign pod. Run from the repository root with an `actl` login that can exec into the pod.
#   1. stage on the pod (scripts/stage_on_pod.py: copy every standing deliverable with its data, records and ledger rows;
#      run the release-time validation; hash; tar)
#   2. transfer the tarball as line-wrapped base64 in 100 000-line chunks, each verified by SHA-256 (a single
#      `actl pod exec` stream truncates large outputs)
#   3. replace targets/ and provenance.json, rebuild the cards, index.json and MANIFEST.sha256
set -euo pipefail
cd "$(dirname "$0")/.."
POD=(actl pod exec autoresearch -n diffuse --)
STAGE=/home/dev/runs/agrp_export_$(date -u +%Y%m%dT%H%MZ)
TMP=$(mktemp -d)
filter() { grep -v -e 'Unable to use a TTY' -e 'newer actl' -e 'actl update' || true; }

echo "staging on pod: $STAGE"
"${POD[@]}" bash -lc "mkdir -p $STAGE && cat > $STAGE/stage_on_pod.py" < scripts/stage_on_pod.py 2>/dev/null | filter
"${POD[@]}" bash -lc "cat > $STAGE/model_diff_on_pod.py" < scripts/model_diff_on_pod.py 2>/dev/null | filter
# Release the targets already in targets/ unless AGRP_TARGETS names others (state/current holds unreleased targets too).
TARGETS=${AGRP_TARGETS:-$(ls targets | tr '\n' ' ')}
echo "targets: $TARGETS"
"${POD[@]}" bash -lc "source /opt/phenix/phenix_env.sh && cd $STAGE && AGRP_TARGETS='$TARGETS' AGRP_WORKERS=8 python3 stage_on_pod.py $STAGE > driver.log 2>&1; tail -1 driver.log" 2>/dev/null | filter | tee "$TMP/done.txt"
TAR_SHA=$(grep -E '^DONE [0-9a-f]{64}$' "$TMP/done.txt" | cut -d' ' -f2) || { echo "staging failed; see $STAGE/driver.log on the pod" >&2; exit 1; }

echo "transferring"
"${POD[@]}" bash -lc "cd /home/dev/runs && rm -rf agrp_b64 && mkdir agrp_b64 && base64 -w 76 $STAGE.tar.gz > agrp_b64/all.b64 && cd agrp_b64 && split -l 40000 -d -a 3 all.b64 part_ && sha256sum part_*" 2>/dev/null | filter > "$TMP/parts.txt"
while read -r want name; do
  for try in 1 2 3; do
    "${POD[@]}" bash -lc "cat /home/dev/runs/agrp_b64/$name" < /dev/null 2>/dev/null | grep -E '^[A-Za-z0-9+/=]+$' > "$TMP/$name" || true
    got=$(shasum -a 256 "$TMP/$name" | cut -d' ' -f1)
    [[ "$got" == "$want" ]] && break
    [[ $try == 3 ]] && { echo "chunk $name failed three times" >&2; exit 1; }
  done
done < "$TMP/parts.txt"
cat "$TMP"/part_* | base64 -d > "$TMP/agrp.tar.gz"
LOCAL_SHA=$(shasum -a 256 "$TMP/agrp.tar.gz" | cut -d' ' -f1)
[[ "$LOCAL_SHA" == "$TAR_SHA" ]] || { echo "tarball sha mismatch: pod $TAR_SHA local $LOCAL_SHA" >&2; exit 1; }
"${POD[@]}" bash -lc "rm -rf /home/dev/runs/agrp_b64" 2>/dev/null | filter

echo "extracting"
tar xzf "$TMP/agrp.tar.gz" -C "$TMP"
rm -rf targets && mkdir targets && cp -R "$TMP/agrp/targets/." targets/ && cp "$TMP/agrp/provenance.json" provenance.json
python3 - "$TMP/agrp/manifest.json" <<'PY'
import hashlib, json, sys
man = json.load(open(sys.argv[1]))
for m in man:
    assert hashlib.sha256(open(m["file"], "rb").read()).hexdigest() == m["sha256"], m["file"]
print(f"verified {len(man)} files against the pod manifest")
PY
python3 scripts/build_index.py
rm -rf "$TMP"
echo "done: review git status, add a CHANGELOG.md line with the export timestamp from provenance.json, commit"
