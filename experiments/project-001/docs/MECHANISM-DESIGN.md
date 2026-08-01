# Project 001 — Mechanism Design: Ankle Physiotherapy Device

> Detailed engineering notes. The versioned, platform-level summary is
> [SPEC-001](../../../docs/specifications/SPEC-001-Project-001-Ankle-Mechanism.md).
> The `registry/drivers/` vs `registry/components/` split follows
> [ADR-006](../../../docs/adrs/ADR-006-Reusable-Component-Layer.md); interface
> conventions follow [STD-001](../../../docs/standards/STD-001-Driver-and-Component-Interface-Conventions.md).

## Overview

A 3-DOF ankle physiotherapy mechanism.

| Axis | Actuator(s) | Kinematics | Feedback |
|---|---|---|---|
| pan | 1x stepper motor, through a single gearbox | Direct (fixed gear ratio only) | Step count (open-loop, no sensor) |
| axis 2 | motor_1 + motor_2 + stepper (coupled) | Complex, function of all 3 actuators — to be solved on the laptop | pot_axis_2 (direct on shaft) |
| axis 3 | motor_1 + motor_2 + stepper (coupled) | Complex, function of all 3 actuators — to be solved on the laptop | pot_axis_3 (direct on shaft) |

**Actuators:**
- 1x stepper motor — half-step driver, spec not received yet.
- 2x [25GA-370 DC gear motor](datasheets/25GA-370-motor-datasheet.pdf) with built-in
  [optical quadrature encoder](datasheets/M25N-encoder-datasheet.pdf) (400 PPR).
- **1x L298N module, 2 independent channels** — confirmed: not two separate modules.
  Channel A drives motor_1, channel B drives motor_2.

**Sensors:**
- 2x built-in motor encoders (one per DC motor, on the motor shaft, before the gearbox).
- 2x potentiometer, mounted **directly** on the axis 2 / axis 3 output shafts (no gearbox).

## Object composition (bottom-up)

Matches the "small objects combine into bigger objects" pattern requested for this
project: primitives live in the reusable driver registry, reusable joint compositions
in `registry/components/`, and the mechanism-specific assembly in the experiment.

**Level 0 — primitives** (`registry/drivers/esp32_micropython/`, reusable, no
mechanism-specific config):
- `Encoder` (`encoder.py`) — quadrature pulse counting.
- `Potentiometer` (`potentiometer.py`) — raw ADC read.
- `DCMotor` (`dc_motor.py`) — 25GA-370 electrical/mechanical spec only.
- `L298NDriver` (`l298n_driver.py`) — one module, `.channel_a` / `.channel_b`.
- `Gearbox` (`gearbox.py`) — fixed-ratio reduction, shared by DC and stepper joints.
- `StepperMotor` (`stepper_motor.py`) — steps-per-revolution spec.
- `StepperDriver` (`stepper_driver.py`) — **placeholder** step-count tracker only,
  pending the actual driver's datasheet.

**Level 1 — joints** (`registry/components/`, reusable across future experiments —
pins/ratios/instances are passed in, nothing here is ankle-specific):
- `DCJoint` (`dc_joint.py`) — composes `Encoder` + `DCMotor` + one `L298NDriver`
  channel + `Gearbox` into one drivable, readable degree of freedom.
- `StepperJoint` (`stepper_joint.py`) — composes `StepperMotor` + `StepperDriver` +
  `Gearbox`. Directly drives the pan axis; no separate kinematics needed since it's
  a single fixed-ratio gearbox.

**Level 2 — the mechanism** (`experiments/project-001/mechanism/ankle_mechanism.py`):
- `AnkleMechanism` — composes `pan_axis` (`StepperJoint`) + `motor_1`, `motor_2`
  (`DCJoint`) + `pot_axis_2`, `pot_axis_3` (`Potentiometer`). **No kinematics here
  by design** — for now it only commands raw motor movement and reads back
  potentiometer/encoder values (`raw_state()`), streamed to the laptop as-is.

## Where kinematics and comparison happen

Per the confirmed plan: the ESP32 side stays deliberately dumb (raw commands out,
raw sensor values in). The **laptop** is where it gets interesting, once this
structure exists:
- Solve the coupled kinematics for axis 2 / axis 3 from (pan, motor_1, motor_2).
- Compare theoretical (kinematics-derived) values against the measured
  potentiometer values.
- Separately, compare potentiometer values against a mobile phone's IMU, connected
  to the laptop (Step 5 — WebSocket / network integration).
- Only once this full loop exists can specific experiments be defined and run:
  comparing control strategies, error-correction methods, etc.

## Open items (needed before Step 2 can drive real hardware)

1. **Stepper driver datasheet** — control scheme (STEP/DIR vs. direct coil
   sequencing) determines the concrete `StepperDriver` implementation.
2. **Gear ratio** for the two 25GA-370 motors and the stepper's gearbox — which row
   of the datasheet table (e.g. 1:21, 1:15.5, ...) matches the actual units in hand.
3. **Pin assignments** — L298N ENA/IN1/IN2/ENB/IN3/IN4, stepper control pins,
   potentiometer ADC pins for axis 2/3. Not needed for this structural design, but
   required to instantiate these objects in `firmware/main.py` for Step 2.

## Status

Structure only — these classes are not yet wired into `firmware/main.py` or tested
on hardware. Step 1 (`firmware/main.py`) still uses the simpler `Encoder` /
`Potentiometer` reads directly via the (now superseded) `Motor` class. Step 2 will
introduce `firmware/main.py` changes that instantiate this composition once items
1–3 above are resolved.
