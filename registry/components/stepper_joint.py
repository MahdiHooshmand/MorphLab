# MorphLab - Stepper joint
# Combines StepperMotor + StepperDriver + Gearbox. Drives the pan axis
# directly through a single gearbox - no separate kinematics needed.
# No feedback sensor: position is tracked open-loop from commanded steps.


class StepperJoint:
    def __init__(self, name, motor, driver, gearbox):
        self.name = name
        self.motor = motor
        self.driver = driver
        self.gearbox = gearbox

    def step(self, direction):
        self.driver.step(direction)

    def motor_revolutions(self):
        return self.driver.step_count / self.motor.steps_per_rev

    def output_revolutions(self):
        return self.gearbox.output_revolutions(self.motor_revolutions())
