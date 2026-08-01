# Components — reusable joint compositions

Composed, reusable "one degree of freedom" building blocks (RFC-005 §2.4).
Each one wires together a set of atomic drivers from
[`registry/drivers/esp32_micropython/`](../drivers/esp32_micropython/) but is
still generic: pins, ratios, and instances of the atomic parts are passed in
by whichever experiment uses it.

| File | Provides | Composes |
|---|---|---|
| `dc_joint.py` | `DCJoint` | `Encoder` + `DCMotor` + one `L298NDriver` channel + `Gearbox` |
| `stepper_joint.py` | `StepperJoint` | `StepperMotor` + `StepperDriver` + `Gearbox` |

Experiment-specific assemblies (e.g. combining several joints into a full
mechanism, plus that mechanism's kinematics) live in the experiment itself —
see [`experiments/project-001/mechanism/`](../../experiments/project-001/mechanism/).
