#!/usr/bin/env bash
# Erase and flash a MicroPython .bin onto an ESP32 DevKit (classic)
# Usage: scripts/flash_micropython.sh /dev/ttyUSB0 path/to/firmware.bin
set -euo pipefail

cd "$(dirname "$0")/.."

PORT="${1:?Usage: $0 <serial-port> <firmware.bin>}"
FIRMWARE="${2:?Usage: $0 <serial-port> <firmware.bin>}"
ESPTOOL="./.venv/bin/esptool.py"

if [ ! -x "$ESPTOOL" ] && ! command -v esptool.py >/dev/null 2>&1; then
  echo "ERROR: esptool not found. Run scripts/setup_ubuntu.sh first." >&2
  exit 1
fi
command -v "$ESPTOOL" >/dev/null 2>&1 || ESPTOOL="esptool.py"

echo "== Erasing flash on $PORT =="
"$ESPTOOL" --chip esp32 --port "$PORT" erase_flash

echo "== Writing $FIRMWARE to $PORT =="
"$ESPTOOL" --chip esp32 --port "$PORT" --baud 460800 write_flash -z 0x1000 "$FIRMWARE"

echo "== Done. Reconnect/power-cycle the board, then run scripts/run.sh $PORT =="
