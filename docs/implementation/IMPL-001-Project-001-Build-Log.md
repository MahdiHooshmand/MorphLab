# IMPL-001: Project 001 — Implementation Log & Test Procedure

| Field | Value |
|---|---|
| IMPL | IMPL-001 |
| Title | Project 001 — Implementation Log & Test Procedure |
| Project | MorphLab |
| Status | Living document — updated as each step is implemented |
| Date | 2026-08-01 |
| Authors | Mahdi Hooshmand |
| References | ADR-004, ADR-006, STD-001, SPEC-001 |

---

# 1. Purpose

RFCs and ADRs record *decisions*; STD records *interface contracts*; SPEC records the
*current design snapshot*. This document records what has actually been **built and
verified**, in the order it should be (re-)verified, so at any point it's possible to
answer "which parts are currently known to work?" without re-reading every commit.

---

# 2. Ordered test procedure

Run these in order. Each depends on the previous one having passed — if a later test
fails, the first suspect is whatever the immediately preceding step touched.

## 2.1 Host-side logic tests (no hardware required)

```bash
cd MorphLab
python3 -m unittest discover -s tests -p "test_*.py" -v
```

**Expected:** `Ran 17 tests ... OK`.

Covers every Driver/Component's *logic* (Gearbox math, spec values, pulse-counting/
direction, channel independence, composition, `AnkleMechanism.raw_state()` shape)
against `tests/mocks/machine.py`, with no ESP32 attached. See `tests/README.md` for
the full coverage table. **Run this first, and after every code change** — it takes
under a second and catches logic errors before they reach hardware.

## 2.2 Step 0 — Dev environment (hardware)

Procedure: `experiments/project-001/docs/STEP-00-ENV-SETUP.md`.
**Expected:** Serial REPL prints `MorphLab OK - tick 0`, `tick 1`, ... once per second.
Confirms the flash → upload → live-Serial toolchain works end to end.

## 2.3 Step 1 — Sensor interfacing (hardware)

Procedure: `experiments/project-001/docs/STEP-01-SENSOR-INTERFACING.md`.
**Expected:** `pot_raw` moves smoothly 0–4095 as the potentiometer turns;
`encoder_pos` counts ~400 per full motor-shaft revolution, sign flips with direction.
Confirms the physical potentiometer and one motor's encoder are wired correctly.

## 2.4 Step 2 — Actuator control (hardware) — **blocked**

Not yet runnable. Blocked on:
1. Stepper driver datasheet.
2. Gear ratios (both DC motors, stepper gearbox).
3. Pin assignments (L298N x6, stepper control pins, pot_axis_2/3 ADC pins).

Once unblocked: wire `DCJoint` / `StepperJoint` / `AnkleMechanism` into
`firmware/main.py`, and the test procedure will be added to
`experiments/project-001/docs/STEP-02-ACTUATOR-CONTROL.md`.

---

# 3. Status summary

| Layer | Status |
|---|---|
| `registry/drivers/esp32_micropython/` | All 7 modules implemented; logic passes host tests (§2.1); `Encoder`/`Potentiometer` additionally hardware-verified (§2.3). `L298NDriver`/`StepperDriver` not yet hardware-verified. |
| `registry/components/` (`DCJoint`, `StepperJoint`) | Implemented; logic passes host tests. Not yet hardware-verified (needs §2.4's open items). |
| `experiments/project-001/mechanism/` (`AnkleMechanism`) | Implemented; `raw_state()`/`stop_all()` logic passes host tests. No kinematics yet, by design (see SPEC-001 §6). |
| `experiments/project-001/firmware/main.py` | Still Step 1 only (raw pot + single encoder via the superseded `Motor` class). Not yet updated to use `DCJoint`/`StepperJoint`/`AnkleMechanism` — waiting on §2.4. |

---

# 4. Deviations from earlier design notes

- Originally assumed 2x separate L298N modules (one per DC motor); corrected to
  **1 module, 2 channels** (`L298NDriver.channel_a` / `.channel_b`).
- Originally gave the stepper joint its own "simple kinematics" abstraction;
  corrected to a **plain `Gearbox`**, shared with the DC joints — the stepper→pan
  link is a single fixed-ratio gearbox, not a separate kinematics concept.
- `AnkleMechanism` deliberately has **no kinematics method** yet. Coupled
  forward/inverse kinematics for axis 2 / axis 3 will be solved on the laptop
  (platform roadmap Step 5/6), not on the ESP32.
