#!/usr/bin/env bash
# MorphLab Project 001 firmware - host-side setup (Ubuntu/Linux)
set -euo pipefail

cd "$(dirname "$0")/.."

echo "== MorphLab firmware setup (Ubuntu) =="

if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 not found. Install it first: sudo apt install python3 python3-venv" >&2
  exit 1
fi

if ! python3 -c "import venv" >/dev/null 2>&1; then
  echo "ERROR: python3-venv missing. Run: sudo apt install python3-venv" >&2
  exit 1
fi

if [ ! -d ".venv" ]; then
  echo "-- creating virtual environment (.venv)"
  python3 -m venv .venv
fi

echo "-- installing host tooling (esptool, mpremote)"
./.venv/bin/pip install --upgrade pip >/dev/null
./.venv/bin/pip install -r requirements.txt

echo "-- checking serial (dialout) permissions"
if groups "$USER" | grep -q '\bdialout\b'; then
  echo "   OK: $USER is already in the 'dialout' group."
else
  echo "   WARNING: $USER is NOT in the 'dialout' group."
  echo "   Without this, /dev/ttyUSB0 access will fail with a permission error."
  echo "   Fix with:  sudo usermod -aG dialout $USER   (then log out/in)"
fi

cat <<'EOF'

== Setup complete ==
Next steps:
  1. source .venv/bin/activate
  2. Plug in the ESP32 over USB and find its port:
       ls /dev/ttyUSB*   (or /dev/ttyACM*)
  3. Download a MicroPython .bin for ESP32 (classic) from https://micropython.org/download/ESP32_GENERIC/
  4. Flash it:
       scripts/flash_micropython.sh /dev/ttyUSB0 path/to/firmware.bin
  5. Run:
       scripts/run.sh /dev/ttyUSB0
EOF
