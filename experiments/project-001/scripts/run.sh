#!/usr/bin/env bash
# Upload registry drivers + this experiment's firmware/*.py to the ESP32
# (flattened - MicroPython's device filesystem has no local repo folders)
# and open a live REPL.
# Usage: scripts/run.sh /dev/ttyUSB0
set -euo pipefail

cd "$(dirname "$0")/.."

PORT="${1:?Usage: $0 <serial-port>}"
MPREMOTE="./.venv/bin/mpremote"
command -v "$MPREMOTE" >/dev/null 2>&1 || MPREMOTE="mpremote"
REGISTRY_DRIVERS="../../registry/drivers/esp32_micropython"
REGISTRY_COMPONENTS="../../registry/components"

echo "== Uploading registry + mechanism + firmware/*.py to $PORT =="
for f in "$REGISTRY_DRIVERS"/*.py "$REGISTRY_COMPONENTS"/*.py mechanism/*.py firmware/*.py; do
  "$MPREMOTE" connect "$PORT" fs cp "$f" ":$(basename "$f")"
done

echo "== Resetting board and opening REPL (Ctrl+] to exit) =="
"$MPREMOTE" connect "$PORT" reset
"$MPREMOTE" connect "$PORT" repl
