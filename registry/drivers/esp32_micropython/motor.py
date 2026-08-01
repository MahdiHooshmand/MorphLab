# MorphLab Project 001 - Motor object
# 25GA-370 DC gear motor (12V, 330RPM, 2.8A, 1kg.cm) with a built-in
# optical quadrature encoder. See docs/datasheets/25GA-370-motor-datasheet.pdf
#
# SUPERSEDED as of the actuator architecture pass: actuation + driving now
# lives in registry/components/dc_joint.py (DCJoint), which composes this
# same Encoder with DCMotor + an L298NDriver channel + Gearbox. Left in
# place, unmodified, so the already-validated Step 1 sensor test keeps
# working as-is. New work should use DCJoint instead.

from encoder import QuadratureEncoder


class Motor:
    def __init__(self, name, encoder_pin_a, encoder_pin_b, encoder_ppr=400):
        self.name = name
        self.encoder = QuadratureEncoder(
            pin_a=encoder_pin_a,
            pin_b=encoder_pin_b,
            ppr=encoder_ppr,
            name=name + "_encoder",
        )
        # Step 2 will add: self.pwm, self.driver_pins, self.set_speed(), etc.
