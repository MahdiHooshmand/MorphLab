# MorphLab - Stepper motor spec
# Generic step-count-based position tracking. No driver interface here -
# see stepper_driver.py.


class StepperMotor:
    def __init__(self, name, steps_per_rev=200):
        self.name = name
        self.steps_per_rev = steps_per_rev
