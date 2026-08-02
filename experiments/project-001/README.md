# Experiment: Project 001

MicroPython firmware + host tooling for MorphLab's first experiment, running on an
**ESP32 DevKit (classic)**. This is the *Experiment* layer (RFC-003 Domain Model): it binds
pins to reusable drivers from [`registry/drivers/`](../../registry/drivers/) and will later
add the control loop, JSON messaging, and networking specific to this mechanism.

Certification tier: **Tier 1 — Experimental**.

## Contents

- `firmware/` — the code that runs *on* the ESP32 (`boot.py`, `main.py`). Imports drivers
  from `registry/drivers/esp32_micropython/` at upload time (see `scripts/run.sh`).
- `mechanism/` — this experiment's composition root (`ankle_mechanism.py`), combining
  reusable joints from `registry/components/`.
- `scripts/` — cross-platform (Ubuntu + Windows) setup/flash/run scripts.
- `docs/` — step-by-step build log (setup, test procedure, expected output) and hardware
  datasheets for this experiment's mechanism.

> Editor config (`.vscode/`) lives at the **repo root** (`MorphLab/.vscode/`), not here —
> open `MorphLab` itself in VS Code, not this subfolder. See `docs/STEP-00-ENV-SETUP.md`.

## Mechanism

This experiment is a 3-DOF ankle physiotherapy mechanism. See
[`docs/MECHANISM-DESIGN.md`](docs/MECHANISM-DESIGN.md) for the full design: axes,
actuators/sensors, and the object composition hierarchy (drivers → joints → mechanism).

## Roadmap position

- [x] Step 0 — Dev environment & repo scaffolding
- [x] Step 1 — Sensor Interfacing (potentiometer + encoder → raw Serial stream)
- [ ] Step 2 — Actuator Control
- [ ] Step 3 — Local Control Loop (PID)
- [ ] Step 4 — MorphLab JSON Messaging (ADR-001)
- [ ] Step 5 — WebSocket / Network Integration
- [ ] Step 6 — System Integration & Spec Extraction

## Quick start

See [`docs/STEP-00-ENV-SETUP.md`](docs/STEP-00-ENV-SETUP.md), then
[`docs/STEP-01-SENSOR-INTERFACING.md`](docs/STEP-01-SENSOR-INTERFACING.md).
