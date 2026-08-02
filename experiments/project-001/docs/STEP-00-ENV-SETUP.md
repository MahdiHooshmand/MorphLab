# Step 0: Dev Environment & Repo Scaffolding

**Goal:** Get MicroPython running on the ESP32 DevKit and prove the host (Ubuntu or Windows)
can flash it, upload code, and see live Serial output through VS Code. No sensors involved yet.

## Hardware

- ESP32 DevKit (classic) connected to your laptop via USB.

## 0. Open the project

Open **`MorphLab`** (the repo root) in VS Code — not this `experiments/project-001`
subfolder. The workspace's `.vscode/settings.json` lives at the root and is what makes
imports like `from encoder import ...` resolve correctly across `registry/` and
`experiments/`; opening a subfolder as its own workspace skips that config.

All commands below assume a terminal opened at the repo root, so start with:
```bash
cd experiments/project-001
```

## 1. Host setup

**Ubuntu:**
```bash
chmod +x scripts/*.sh
scripts/setup_ubuntu.sh
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
scripts\setup_windows.ps1
.\.venv\Scripts\Activate.ps1
```

## 2. Find the serial port

- Ubuntu: `ls /dev/ttyUSB*` (usually `/dev/ttyUSB0`)
- Windows: Device Manager → Ports (COM & LPT) (usually `COM3`/`COM5`/...)

## 3. Flash MicroPython

Download the **ESP32 (classic, not S3/C3)** generic build from
https://micropython.org/download/ESP32_GENERIC/, then:

**Ubuntu:**
```bash
scripts/flash_micropython.sh /dev/ttyUSB0 ~/Downloads/ESP32_GENERIC-xxxxxxxx.bin
```

**Windows:**
```powershell
scripts\flash_micropython.ps1 COM5 C:\Downloads\ESP32_GENERIC-xxxxxxxx.bin
```

## 4. Upload firmware and open the REPL

**Ubuntu:** `scripts/run.sh /dev/ttyUSB0`
**Windows:** `scripts\run.ps1 COM5`

## Expected output

> **Superseded note:** this is what `firmware/main.py` printed right when Step 0 was
> completed. Since then, Step 1 (see `STEP-01-SENSOR-INTERFACING.md`) **overwrote
> `firmware/main.py`** with the sensor-reading loop — `scripts/run.sh` always uploads
> and runs whatever is *currently* in `firmware/`, so on an up-to-date checkout you'll
> see Step 1's `pot_raw=... encoder_pos=...` stream here instead. That's expected, not
> a regression — it means Step 0's toolchain still works and Step 1's code is what's
> running now. This section is kept for historical reference / for re-verifying the
> toolchain in isolation (e.g. by temporarily reverting `main.py` to the tick counter).

The terminal should print, once per second:

```
MorphLab OK - tick 0
MorphLab OK - tick 1
MorphLab OK - tick 2
...
```

If you see this incrementing counter, the full chain works: **MicroPython flashed → code
uploaded → live Serial stream visible on the host.** Press `Ctrl+]` to leave the REPL.

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| `Permission denied` on `/dev/ttyUSB0` | User not in `dialout` group (see setup script output) |
| Port not found | Wrong cable (some are charge-only) or driver missing (CP2102/CH340) |
| `esptool` timeout / sync error | Hold the `BOOT` button on the DevKit while flashing starts |
| Garbled REPL text | Wrong baud rate — `mpremote` handles this automatically, no config needed |

---
Next: **Step 1 — Sensor Interfacing** (potentiometer + encoder raw reads).
