#!/bin/bash
# scripts/after_pid.sh PID SCRIPT ARGS...: wait until the process PID has ended, then run `bash SCRIPT ARGS...` (a chain
# script) in this process. Builds a queue of chains without a shell that holds the whole pipeline in its command line
# (2026-10-20: 3TC7's six-copy chain moved ahead of its qFit split). PID 0 runs at once.
set -u
WAIT=${1:?pid to wait for, or 0}
shift
if [ "$WAIT" != "0" ]; then
  echo "[$(date -u +%FT%TZ)] after_pid waits for pid $WAIT, then: bash $*"
  while [ -d "/proc/$WAIT" ]; do sleep 60; done
fi
echo "[$(date -u +%FT%TZ)] after_pid starts: bash $*"
exec bash "$@"
