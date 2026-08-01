# MorphLab - DC joint
# Combines Encoder + DCMotor + one L298N channel + Gearbox into "one degree
# of freedom": drive it with set_speed(), read it back via the encoder.

from encoder import QuadratureEncoder


class DCJoint:
    def __init__(self, name, motor, driver_channel, gearbox,
                 encoder_pin_a, encoder_pin_b, encoder_ppr=400):
        self.name = name
        self.motor = motor                    # DCMotor - spec only
        self.driver_channel = driver_channel  # L298NDriver.channel_a / channel_b
        self.gearbox = gearbox
        self.encoder = QuadratureEncoder(
            pin_a=encoder_pin_a, pin_b=encoder_pin_b,
            ppr=encoder_ppr, name=name + "_encoder",
        )

    def set_speed(self, speed):
        """speed: -1.0 to 1.0"""
        self.driver_channel.drive(speed)

    def stop(self):
        self.driver_channel.stop()

    def motor_revolutions(self):
        return self.encoder.revolutions()

    def output_revolutions(self):
        return self.gearbox.output_revolutions(self.encoder.revolutions())
