# MorphLab - Stepper driver (half-step)
# PLACEHOLDER: the concrete half-step driver module's datasheet is not
# available yet, so this only tracks the commanded step count. This lets
# StepperJoint and AnkleMechanism be built and tested logically now; replace
# `step()` with the real pulse sequence once the driver spec arrives.


class StepperDriver:
    def __init__(self, name="stepper_driver"):
        self.name = name
        self.step_count = 0  # signed, +1 per step forward, -1 per step backward

    def step(self, direction):
        """direction: +1 or -1."""
        self.step_count += 1 if direction >= 0 else -1
