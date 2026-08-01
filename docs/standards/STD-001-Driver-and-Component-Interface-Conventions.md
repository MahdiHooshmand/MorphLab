# STD-001: Driver and Component Interface Conventions

| Field         | Value                                              |
| ------------- | --------------------------------------------------- |
| STD           | STD-001                                              |
| Title         | Driver and Component Interface Conventions           |
| Project       | MorphLab                                             |
| Status        | Draft — describes current Tier 1 practice            |
| Date          | 2026-08-01                                           |
| Authors       | Mahdi Hooshmand                                      |
| References    | ADR-004, ADR-006, RFC-002                            |

---

# 1. Purpose

ADR-004 mandates code standards for the Asset Registry but does not fix concrete
interface signatures. This document records the conventions that emerged from
Project 001's first Drivers and Components, as the baseline a Tier 1 asset must
follow, and the gaps a Tier 2 ("Standardized", RFC-002 §6) asset must close.

---

# 2. Current conventions (Tier 1)

## 2.1 Constructors

- **Drivers** (`registry/drivers/<platform>/`): hardware pin(s) are required,
  positional, first argument(s). `name` is an optional keyword with a generic
  default (e.g. `Potentiometer(adc_pin, name="potentiometer")`), since a single
  driver instance's identity rarely matters on its own.
- **Components** (`registry/components/`) and mechanism-level assemblies: `name`
  is a required, positional, first argument, since these represent a specific,
  named degree of freedom or sub-assembly in a mechanism (e.g.
  `DCJoint("motor_1", ...)`).

## 2.2 Reading a sensor

- `Potentiometer.read_raw()` — returns the raw ADC integer.
- `QuadratureEncoder.position` (public attribute) + `.revolutions()` (derived).

*Known gap:* these two sensors expose different read patterns (`read_raw()` vs.
attribute + method). Tier 2 should converge on one pattern — either both expose a
plain `.read()` returning raw units, or both expose `.value` as a property.

## 2.3 Driving an actuator

- `-1.0` to `1.0` continuous drive: `.drive(speed)` (`L298NDriver` channel),
  `.set_speed(speed)` (`DCJoint`, delegates to its channel).
- `+1`/`-1` discrete step: `.step(direction)` (`StepperDriver`, `StepperJoint`).
- `.stop()` present on every actuator-driving object (channel, `DCJoint`); mechanism-
  level `.stop_all()` stops every actuator it owns.

## 2.4 Composition

- Components expose their constituent Drivers as public attributes (`.encoder`,
  `.motor`, `.driver`, `.gearbox`, `.driver_channel`) rather than hiding them —
  intentional, so raw values stay inspectable for debugging and Serial streaming
  (per the platform's test-first, visual-feedback-first workflow) even once a
  higher-level method exists.
- Unit conversion between motor-shaft and output-shaft (`Gearbox`) is shared code,
  not duplicated per Component.

## 2.5 Hardware-free logic

Any file whose *logic* does not depend on real electrical behavior (e.g. `Gearbox`
ratio math, `DCMotor`/`StepperMotor` spec values, pulse-counting direction logic)
must remain importable and testable on the host by depending only on `machine.Pin`
/ `machine.ADC` / `machine.PWM`'s public interface — never on ESP32-specific
side effects — so it can run against `tests/mocks/machine.py`. See `tests/README.md`.

---

# 3. Tier 2 promotion checklist (not yet met by any current asset)

To move a Driver or Component from Tier 1 (Experimental) to Tier 2 (Standardized,
RFC-002 §6), it must additionally:

1. Resolve the §2.2 read-pattern gap for its category (sensor vs. actuator).
2. Have host-side unit tests (`tests/`) covering its public interface.
3. Document its constructor arguments and units in its module docstring.
4. Have no experiment-specific values hardcoded (pins, ratios, calibration constants
   all passed in by the caller — already true for every current asset).

---

# 4. Compliance status (Project 001)

| Asset | Tier | Notes |
|---|---|---|
| `Potentiometer`, `QuadratureEncoder` | 1 (Experimental) | Interface matches §2.2; logic covered by host tests, electrical behavior not yet hardware-tested against this mechanism's wiring |
| `L298NDriver` | 1 (Experimental) | Interface matches §2.3; logic covered by host tests, not yet driven on real hardware |
| `StepperDriver` | 1 (Experimental) | Interface matches §2.3; concrete pulse sequence pending its datasheet |
| `DCJoint`, `StepperJoint` | 1 (Experimental) | Interface matches §2.3/§2.4; both fully covered by host tests |

See [`tests/README.md`](../../tests/README.md) for how these are exercised without hardware.
