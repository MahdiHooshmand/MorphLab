# Step 0: Dev Environment & Repo Scaffolding

**Goal:** Get MicroPython running on the ESP32 DevKit and prove the host (Ubuntu or Windows)
can flash it, upload code, and see live Serial output through VS Code. No sensors involved yet.

## Hardware

- ESP32 DevKit (classic) connected to your laptop via USB.

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
