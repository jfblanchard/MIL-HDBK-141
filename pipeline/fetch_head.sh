#!/usr/bin/env bash
# Pipeline helper: print the short HEAD and require the validator have read THIS commit.
# Usage: bash pipeline/fetch_head.sh          -> prints "PIN <short-sha> <date>"
#        bash pipeline/fetch_head.sh --check  -> writes .pipeline_last_validate_sha and
#                                                exits 0 only if current HEAD == pinned
cd "$(dirname "$0")/.." 2>/dev/null || exit 1
if [ "$1" = "--check" ]; then
  PIN_FILE=.pipeline_last_validate_sha
  [ -f "$PIN_FILE" ] || { echo "NO PIN on record"; exit 3; }
  PIN=$(cat "$PIN_FILE"); CUR=$(git rev-parse --short HEAD)
  if [ "$PIN" = "$CUR" ]; then echo "OK: HEAD still $CUR"; exit 0
  else echo "MISMATCH: validated $PIN, HEAD now $CUR"; exit 4; fi
else
  CUR=$(git rev-parse --short HEAD); DATE=$(git log -1 --format=%cd --date=short)
  echo "PIN $CUR $DATE"
fi
