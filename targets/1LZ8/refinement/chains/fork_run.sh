#!/bin/bash
# scripts/fork_run.sh RUN NEW: a copy of a run directory for a fork (the same working data, flags, sealed vault and
# step record; the arms of the steps, the pending directories and the refinement cache are left out).
set -eu
SRC=${1:?run directory}
DST=${2:?new run directory}
[ -e "$DST" ] && { echo "$DST exists"; exit 1; }
# --chmod=u+rwX: the sealed vault directory is read-only, and rsync makes its temporary files inside the copy (2026-10-20)
rsync -a --chmod=u+rwX --exclude 'pending/' --exclude 'refine_cache/' --exclude 'arms/' --exclude 'vault/_source/' --exclude 'vault/bunker*' --exclude 'vault/identity.json' "$SRC/" "$DST/"
chmod -R u+w "$DST/vault" 2>/dev/null || true
echo "forked $SRC -> $DST ($(du -sh "$DST" | cut -f1))"
