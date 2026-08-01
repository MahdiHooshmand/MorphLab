# Step 1: Sensor Interfacing (Potentiometer + Encoder)

**Goal:** Read the mechanism's potentiometer and the motor's built-in quadrature encoder,
and stream raw values over Serial. No JSON framing yet (that's ADR-001 / Step 4), no
actuation yet (that's Step 2) — just proving the sensors are wired correctly and readable.

## Hardware in this step

- ESP32 DevKit (classic)
- Potentiometer mounted on the mechanism
- 25GA-370 DC gear motor (12V, 330RPM) with built-in optical quadrature encoder
  (400 pulses/rev, 2-channel A/B, 90° phase) — see `docs/datasheets/`

## Wiring

| Signal | ESP32 Pin | Notes |
|---|---|---|
| Potentiometer wiper | GPIO34 | ADC1, input-only — no WiFi/boot conflicts |
| Potentiometer outer legs | 3V3 and GND | either orientation; swapping reverses direction sense |
| Encoder Channel A | GPIO18 | digital in, internal pull-up enabled in code |
| Encoder Channel B | GPIO19 | digital in, internal pull-up enabled in code |
| Encoder VCC | 3V3 | confirm against the datasheet if your module needs 5V instead |
| Encoder GND / Motor GND | GND | common ground with the ESP32 |

> The motor's power leads (+/-) are **not** connected yet — Step 1 is read-only.
> If your wiring uses different pins, just edit the constants at the top of
> `firmware/main.py` (`POT_ADC_PIN`, `ENCODER_PIN_A`, `ENCODER_PIN_B`).

## New files

- `firmware/potentiometer.py` — `Potentiometer` class, raw ADC read (0-4095).
- `firmware/encoder.py` — `QuadratureEncoder` class, interrupt-driven pulse counting with direction.
- `firmware/motor.py` — `Motor` class; wraps an `Encoder` instance (PWM/driver pins added in Step 2).
- `firmware/main.py` — instantiates both and prints raw values every 200 ms.

## Run it

**Ubuntu:** `scripts/run.sh /dev/ttyUSB0`
**Windows:** `scripts\run.ps1 COM5`

(This uploads every `.py` file in `firmware/` to the board, resets it, and opens the REPL.)

## Expected output

```
MorphLab Step 1 - raw sensor stream starting
pot_raw: 0-4095 | encoder_pos: signed pulse count | encoder_rev: position/PPR
pot_raw=2048  encoder_pos=0  encoder_rev=0.000
pot_raw=2051  encoder_pos=0  encoder_rev=0.000
...
```

**Verification checklist:**
1. Slowly turn the potentiometer shaft → `pot_raw` should move smoothly between roughly
   0 and 4095 (no jumps, no stuck value).
2. Manually rotate the motor's output shaft by hand, one direction → `encoder_pos`
   should count steadily upward (or downward — see note below).
3. Rotate it the other way → the sign should flip.
4. Rotate exactly one full revolution of the **motor shaft** (not the gearbox output
   shaft) → `encoder_pos` should read close to 400 and `encoder_rev` close to 1.000.

If direction feels backwards, swap encoder channels A and B in the wiring (or in
`ENCODER_PIN_A` / `ENCODER_PIN_B`) — this is expected and not a bug.

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| `pot_raw` stuck at 0 or 4095 | Wiper wired to a rail instead of the middle pin, or pot at end of travel |
| `pot_raw` noisy/jittery | Loose wiring, or pot at a mechanical dead zone — moves are fine to smooth later |
| `encoder_pos` never changes | Check A/B wiring, and that encoder VCC is actually powered |
| `encoder_pos` jumps by more than 1 per pulse randomly | Debounce/wiring noise — usually a loose connection, not code |

---
Next: **Step 2 — Actuator Control** (extend the `Motor` class with PWM/driver pins).
