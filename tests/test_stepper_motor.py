import unittest
import _paths
from stepper_motor import StepperMotor


class TestStepperMotor(unittest.TestCase):
    def test_defaults(self):
        m = StepperMotor("pan_stepper", steps_per_rev=200)
        self.assertEqual(m.steps_per_rev, 200)


if __name__ == "__main__":
    unittest.main()
