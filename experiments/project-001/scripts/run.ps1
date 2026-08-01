# Upload registry drivers + this experiment's firmware\*.py to the ESP32
# (flattened - MicroPython's device filesystem has no local repo folders)
# and open a live REPL.
# Usage: scripts\run.ps1 COM5
param(
    [Parameter(Mandatory=$true)][string]$Port
)
$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")

$mpremote = ".\.venv\Scripts\mpremote.exe"
if (-not (Test-Path $mpremote)) { $mpremote = "mpremote" }
$registryDrivers = "..\..\registry\drivers\esp32_micropython"
$registryComponents = "..\..\registry\components"

Write-Host "== Uploading registry + mechanism + firmware\*.py to $Port =="
Get-ChildItem -Path "$registryDrivers\*.py", "$registryComponents\*.py", "mechanism\*.py", "firmware\*.py" | ForEach-Object {
    & $mpremote connect $Port fs cp $_.FullName (":" + $_.Name)
}

Write-Host "== Resetting board and opening REPL (Ctrl+] to exit) =="
& $mpremote connect $Port reset
& $mpremote connect $Port repl
