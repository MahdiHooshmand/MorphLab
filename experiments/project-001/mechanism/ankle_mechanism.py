# MorphLab - Ankle mechanism (Project 001)
# Composition root: 3 DOF ankle physiotherapy mechanism.
#   - pan_axis: StepperJoint - direct gearbox, no sensor (open-loop step count)
#   - motor_1, motor_2: DCJoint - each with its own encoder
#   - pot_axis_2, pot_axis_3: Potentiometer - direct on the two coupled axes
#
# No kinematics yet, by design: without it, we simply command raw motor
# movement and read back potentiometer values, streaming both to the laptop.
# The coupled kinematics function (pan/motor_1/motor_2 -> axis_2/axis_3
# angles) is solved on the laptop, not here - see the platform roadmap
# (Step 5/6). Only once this structure + that kinematics exist can specific
# experiments (control strategies, error-correction methods, etc.) be
# defined and run.


class AnkleMechanism:
    def __init__(self, pan_axis, motor_1, motor_2, pot_axis_2, pot_axis_3):
        self.pan_axis = pan_axis
        self.motor_1 = motor_1
        self.motor_2 = motor_2
        self.pot_axis_2 = pot_axis_2
        self.pot_axis_3 = pot_axis_3

    def raw_state(self):
        """Everything currently readable, with no kinematics applied."""
        return {
            "pan_steps": self.pan_axis.driver.step_count,
            "motor_1_encoder": self.motor_1.encoder.position,
            "motor_2_encoder": self.motor_2.encoder.position,
            "pot_axis_2": self.pot_axis_2.read_raw(),
            "pot_axis_3": self.pot_axis_3.read_raw(),
        }

    def stop_all(self):
        self.motor_1.stop()
        self.motor_2.stop()
