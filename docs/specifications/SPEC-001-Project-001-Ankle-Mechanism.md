# SPEC-001: Project 001 — Ankle Physiotherapy Mechanism

| Field         | Value                                          |
| ------------- | ------------------------------------------------ |
| SPEC          | SPEC-001                                          |
| Title         | Project 001 — Ankle Physiotherapy Mechanism        |
| Project       | MorphLab                                          |
| Status        | In progress — structure implemented, not yet run on hardware |
| Date          | 2026-08-01                                        |
| Authors       | Mahdi Hooshmand                                   |
| References    | ADR-004, ADR-006, RFC-002, RFC-003                 |

---

# 1. Summary

A 3-DOF ankle physiotherapy mechanism (Experiment `project-001`), controlled by an
ESP32 DevKit (classic) running MicroPython. Full engineering detail, open items, and
the object composition hierarchy are maintained as a living document at
[`experiments/project-001/docs/MECHANISM-DESIGN.md`](../../experiments/project-001/docs/MECHANISM-DESIGN.md);
this SPEC is the versioned, platform-level summary of that design.

---

# 2. Hardware

| Component | Spec | Quantity | Notes |
|---|---|---|---|
| Controller | ESP32 DevKit (classic), MicroPython | 1 | |
| DC gear motor | 25GA-370, 12V, 330RPM, 2.8A, 1kg·cm, built-in optical quadrature encoder (400 PPR) | 2 | drives motor_1 / motor_2 |
| DC motor driver | L298N module, 2 independent channels | 1 | channel A → motor_1, channel B → motor_2 |
| Stepper motor | TBD | 1 | drives the pan axis directly through a single gearbox |
| Stepper driver | Simple half-step driver | 1 | **datasheet not yet available** |
| Potentiometer | direct-mounted on shaft (no gearbox) | 2 | pot_axis_2, pot_axis_3 |

---

# 3. Axes

| Axis | Actuator(s) | Kinematics | Feedback |
|---|---|---|---|
| pan | stepper (single gearbox) | Direct, fixed ratio | step count only (open-loop) |
| axis 2 | motor_1 + motor_2 + stepper (coupled) | Complex, function of all 3 actuators — solved on the laptop, not the ESP32 | pot_axis_2 |
| axis 3 | motor_1 + motor_2 + stepper (coupled) | Complex, function of all 3 actuators — solved on the laptop, not the ESP32 | pot_axis_3 |

---

# 4. Software module inventory

| Layer | Path | Modules |
|---|---|---|
| Drivers | `registry/drivers/esp32_micropython/` | `encoder.py`, `potentiometer.py`, `dc_motor.py`, `l298n_driver.py`, `gearbox.py`, `stepper_motor.py`, `stepper_driver.py` (placeholder) |
| Components | `registry/components/` | `dc_joint.py` (`DCJoint`), `stepper_joint.py` (`StepperJoint`) |
| Mechanism | `experiments/project-001/mechanism/` | `ankle_mechanism.py` (`AnkleMechanism`) |
| Entry point | `experiments/project-001/firmware/` | `boot.py`, `main.py` (currently Step 1 only) |

See STD-001 for the interface conventions these modules follow, and `tests/README.md`
for how their logic is verified without hardware.

---

# 5. Implementation status

- **Implemented and hardware-tested:** Step 0 (dev environment), Step 1 (raw
  potentiometer + single-motor encoder read via the pre-Component `Motor` class).
- **Implemented, unit-tested on host, not yet hardware-tested:** the full
  Driver → Component → Mechanism stack above (17 passing tests, `tests/`).
- **Not yet implemented:** actual Step 2 wiring in `firmware/main.py` (blocked on
  open items below), any kinematics, JSON messaging (ADR-001), networking.

---

# 6. Open items

1. Stepper driver datasheet (determines `StepperDriver`'s real pulse sequence).
2. Gear ratios for both DC motors and the stepper's gearbox.
3. Pin assignments: L298N (ENA/IN1/IN2/ENB/IN3/IN4), stepper control pins,
   pot_axis_2 / pot_axis_3 ADC pins.
4. Coupled kinematics equations for axis 2 / axis 3 (laptop-side).
