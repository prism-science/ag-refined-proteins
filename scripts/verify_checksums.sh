#!/usr/bin/env bash
# Verify every released file against MANIFEST.sha256. Run from the repository root.
set -euo pipefail
cd "$(dirname "$0")/.."
if command -v sha256sum >/dev/null 2>&1; then sha256sum -c --quiet MANIFEST.sha256; else shasum -a 256 -c MANIFEST.sha256 --quiet; fi
echo "all files match MANIFEST.sha256"
