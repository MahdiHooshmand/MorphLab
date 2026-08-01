import unittest
import _paths
from dc_motor import DCMotor
from l298n_driver import L298NDriver
from gearbox import Gearbox
from dc_joint import DCJoint
from stepper_motor import StepperMotor
from stepper_driver import StepperDriver
from stepper_joint import StepperJoint


class TestDCJoint(unittest.TestCase):
    def _make_joint(self):
        motor = DCMotor("motor_1")
        driver = L298NDriver(25, 26, 27, 14, 12, 13)
        gearbox = Gearbox(ratio=21)
        joint = DCJoint("joint_1", motor, driver.channel_a, gearbox,
                         encoder_pin_a=18, encoder_pin_b=19, encoder_ppr=400)
        return joint, driver

    def test_output_revolutions_after_gearbox(self):
        joint, _ = self._make_joint()
        joint.encoder._pin_b.value(0)
        for _ in range(400 * 21):  # one full output-shaft revolution
            joint.encoder._pin_a.simulate_pulse()
        self.assertAlmostEqual(joint.output_revolutions(), 1.0)

    def test_set_speed_drives_its_channel(self):
        joint, driver = self._make_joint()
        joint.set_speed(0.5)
        self.assertEqual(driver.channel_a._in1.value(), 1)
        self.assertGreater(driver.channel_a._en._duty, 0)

    def test_stop(self):
        joint, driver = self._make_joint()
        joint.set_speed(1.0)
        joint.stop()
        self.assertEqual(driver.channel_a._en._duty, 0)


class TestStepperJoint(unittest.TestCase):
    def test_pan_revolutions_after_gearbox(self):
        motor = StepperMotor("pan_stepper", steps_per_rev=200)
        driver = StepperDriver()
        gearbox = Gearbox(ratio=5)
        joint = StepperJoint("pan_joint", motor, driver, gearbox)
        for _ in range(200 * 5):  # one full pan-axis revolution
            joint.step(1)
        self.assertAlmostEqual(joint.output_revolutions(), 1.0)

    def test_direction_sign(self):
        motor = StepperMotor("pan_stepper", steps_per_rev=200)
        driver = StepperDriver()
        joint = StepperJoint("pan_joint", motor, driver, Gearbox(ratio=1))
        joint.step(1)
        joint.step(-1)
        joint.step(-1)
        self.assertEqual(driver.step_count, -1)


if __name__ == "__main__":
    unittest.main()
