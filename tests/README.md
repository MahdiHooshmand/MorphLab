# Host-side logic tests

Pure-`python3` unit tests for the registry/experiment code that has **no hardware
dependency in its logic** — Gearbox math, DCMotor/StepperMotor spec values, and
the pulse-counting/direction logic inside Encoder, L298NDriver, DCJoint, and
StepperJoint. `tests/mocks/machine.py` stubs MicroPython's `machine` module
(Pin/ADC/PWM) so the exact same device source files can be imported and exercised
here, with no ESP32 attached.

**What this does NOT test:** electrical correctness (voltage levels, PWM
frequency response, actual motor behavior) or the still-open items (stepper
driver pulse sequence, real gear ratios, real pin assignments). It tests that the
Python logic is correct *given* whatever the hardware reports.

## Run

```bash
cd MorphLab
python3 -m unittest discover -s tests -p "test_*.py" -v
```

Expected: `Ran 17 tests ... OK`, no failures.

## Coverage

| Test file | Covers |
|---|---|
| `test_gearbox.py` | `Gearbox` ratio math |
| `test_dc_motor.py` | `DCMotor` spec values match the 25GA-370 datasheet |
| `test_stepper_motor.py` | `StepperMotor` spec values |
| `test_encoder.py` | `QuadratureEncoder` pulse counting + direction |
| `test_potentiometer.py` | `Potentiometer` raw ADC read |
| `test_l298n_driver.py` | `L298NDriver` — both channels drive independently, `stop_all()` |
| `test_joints.py` | `DCJoint` (encoder → gearbox → output revolutions, `set_speed`/`stop`), `StepperJoint` (step count → gearbox → output revolutions, direction sign) |
| `test_ankle_mechanism.py` | `AnkleMechanism.raw_state()` shape, `stop_all()` reaches both DC joints |
