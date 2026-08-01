# MorphLab Project 001 firmware - host-side setup (Windows / PowerShell)
$ErrorActionPreference = "Stop"

Set-Location (Join-Path $PSScriptRoot "..")

Write-Host "== MorphLab firmware setup (Windows) =="

$python = Get-Command py -ErrorAction SilentlyContinue
if (-not $python) {
    $python = Get-Command python -ErrorAction SilentlyContinue
}
if (-not $python) {
    Write-Error "Python not found. Install Python 3 from https://www.python.org/downloads/ (check 'Add to PATH')."
    exit 1
}

if (-not (Test-Path ".venv")) {
    Write-Host "-- creating virtual environment (.venv)"
    & $python.Source -m venv .venv
}

Write-Host "-- installing host tooling (esptool, mpremote)"
& .\.venv\Scripts\python.exe -m pip install --upgrade pip | Out-Null
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt

Write-Host ""
Write-Host "== Setup complete =="
Write-Host "Next steps:"
Write-Host "  1. .\.venv\Scripts\Activate.ps1"
Write-Host "  2. Plug in the ESP32 over USB and find its port in Device Manager (e.g. COM5)"
Write-Host "  3. Download a MicroPython .bin for ESP32 (classic) from https://micropython.org/download/ESP32_GENERIC/"
Write-Host "  4. Flash it:"
Write-Host "       scripts\flash_micropython.ps1 COM5 path\to\firmware.bin"
Write-Host "  5. Run:"
Write-Host "       scripts\run.ps1 COM5"
