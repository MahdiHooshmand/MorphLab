# MorphLab Project 001 - main.py
# Step 1: Sensor Interfacing
# Reads the mechanism's potentiometer + the motor's built-in encoder,
# and streams raw values over Serial (plain text - ADR-001 JSON framing
# comes in Step 4, not here).

import time
from potentiometer import Potentiometer
from motor import Motor

# --- Pin map (adjust here if your wiring differs) ---
POT_ADC_PIN = 34
ENCODER_PIN_A = 18
ENCODER_PIN_B = 19
ENCODER_PPR = 400

pot = Potentiometer(POT_ADC_PIN, name="joint_potentiometer")
motor = Motor("joint_motor", ENCODER_PIN_A, ENCODER_PIN_B, encoder_ppr=ENCODER_PPR)

print("MorphLab Step 1 - raw sensor stream starting")
print("pot_raw: 0-4095 | encoder_pos: signed pulse count | encoder_rev: position/PPR")

while True:
    pot_raw = pot.read_raw()
    enc_pos = motor.encoder.position
    enc_rev = motor.encoder.revolutions()
    print("pot_raw={}  encoder_pos={}  encoder_rev={:.3f}".format(pot_raw, enc_pos, enc_rev))
    time.sleep_ms(200)
