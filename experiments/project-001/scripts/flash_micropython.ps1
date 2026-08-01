# Erase and flash a MicroPython .bin onto an ESP32 DevKit (classic)
# Usage: scripts\flash_micropython.ps1 COM5 path\to\firmware.bin
param(
    [Parameter(Mandatory=$true)][string]$Port,
    [Parameter(Mandatory=$true)][string]$Firmware
)
$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")

$esptool = ".\.venv\Scripts\esptool.py"
if (-not (Test-Path $esptool)) {
    Write-Error "esptool not found. Run scripts\setup_windows.ps1 first."
    exit 1
}

Write-Host "== Erasing flash on $Port =="
& .\.venv\Scripts\python.exe $esptool --chip esp32 --port $Port erase_flash

Write-Host "== Writing $Firmware to $Port =="
& .\.venv\Scripts\python.exe $esptool --chip esp32 --port $Port --baud 460800 write_flash -z 0x1000 $Firmware

Write-Host "== Done. Reconnect/power-cycle the board, then run scripts\run.ps1 $Port =="
