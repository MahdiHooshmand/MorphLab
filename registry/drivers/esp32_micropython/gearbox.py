# MorphLab - Gearbox
# Simple fixed-ratio reduction between a motor's shaft and an output shaft.
# Shared by DC joints (25GA-370's built-in gearbox) and the stepper joint
# (stepper -> pan axis, single intermediate gearbox).


class Gearbox:
    def __init__(self, ratio, name="gearbox"):
        self.name = name
        self.ratio = ratio  # motor revolutions per 1 output revolution

    def output_revolutions(self, motor_revolutions):
        return motor_revolutions / self.ratio

    def motor_revolutions(self, output_revolutions):
        return output_revolutions * self.ratio
