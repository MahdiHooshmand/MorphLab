# Driver Library — ESP32 / MicroPython

Reusable, hardware-abstraction drivers (RFC-002 "Driver", RFC-005 §2.4) for devices used
across MorphLab experiments. Nothing here is specific to a single experiment's pin
assignment — pin numbers are passed in by the experiment that uses them.

**Certification tier:** Tier 1 — Experimental (RFC-002 §Certification Tiers).

## Contents

| File | Provides |
|---|---|
| `potentiometer.py` | `Potentiometer` — raw ADC position read |
| `encoder.py` | `QuadratureEncoder` — interrupt-driven 2-channel pulse counting |
| `dc_motor.py` | `DCMotor` — 25GA-370 electrical/mechanical spec (no actuation itself) |
| `l298n_driver.py` | `L298NDriver` — one physical module, 2 independent channels (A/B) |
| `gearbox.py` | `Gearbox` — fixed-ratio reduction, shared by DC and stepper joints |
| `stepper_motor.py` | `StepperMotor` — steps-per-revolution spec |
| `stepper_driver.py` | `StepperDriver` — placeholder step-count tracker; concrete half-step pulse sequence pending the driver's datasheet |
| `motor.py` | *Superseded* by `dc_motor.py` + [`registry/components/dc_joint.py`](../../components/dc_joint.py). Left in place only so the already-validated Step 1 test keeps working. |

See [`registry/components/`](../../components/) for how these combine into a `DCJoint` /
`StepperJoint`, and [`experiments/project-001/mechanism/`](../../../experiments/project-001/mechanism/)
for how those combine into the full mechanism.

## Adding a new driver

1. One file per device capability (RFC-005 §2.4 — abstract by capability, e.g.
   `PositionSensor`, `VoltageActuator` — not by specific part number where avoidable).
2. Accept pin numbers and calibration constants as constructor arguments; never hardcode
   an experiment's wiring inside a driver.
3. No experiment-specific logic (control loops, JSON framing, WebSocket code) belongs here
   — only the hardware read/write itself.
4. Reference this file from the consuming experiment's docs.
