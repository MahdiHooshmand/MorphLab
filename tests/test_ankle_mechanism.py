import unittest
import _paths
from dc_motor import DCMotor
from l298n_driver import L298NDriver
from gearbox import Gearbox
from dc_joint import DCJoint
from stepper_motor import StepperMotor
from stepper_driver import StepperDriver
from stepper_joint import StepperJoint
from potentiometer import Potentiometer
from ankle_mechanism import AnkleMechanism


def _build_mechanism():
    driver = L298NDriver(25, 26, 27, 14, 12, 13)
    gearbox = Gearbox(ratio=21)
    motor_1 = DCJoint("motor_1", DCMotor("motor_1"), driver.channel_a, gearbox, 18, 19)
    motor_2 = DCJoint("motor_2", DCMotor("motor_2"), driver.channel_b, gearbox, 32, 33)
    pan_axis = StepperJoint("pan", StepperMotor("pan_stepper"), StepperDriver(), Gearbox(ratio=5))
    pot_axis_2 = Potentiometer(adc_pin=34)
    pot_axis_3 = Potentiometer(adc_pin=35)
    return AnkleMechanism(pan_axis, motor_1, motor_2, pot_axis_2, pot_axis_3), driver


class TestAnkleMechanism(unittest.TestCase):
    def test_raw_state_has_all_five_readings(self):
        mech, _ = _build_mechanism()
        mech.pot_axis_2._adc.set_value(1000)
        mech.pot_axis_3._adc.set_value(3000)
        state = mech.raw_state()
        self.assertEqual(
            set(state.keys()),
            {"pan_steps", "motor_1_encoder", "motor_2_encoder", "pot_axis_2", "pot_axis_3"},
        )
        self.assertEqual(state["pot_axis_2"], 1000)
        self.assertEqual(state["pot_axis_3"], 3000)

    def test_stop_all_stops_both_dc_motors(self):
        mech, driver = _build_mechanism()
        mech.motor_1.set_speed(1.0)
        mech.motor_2.set_speed(-1.0)
        mech.stop_all()
        self.assertEqual(driver.channel_a._en._duty, 0)
        self.assertEqual(driver.channel_b._en._duty, 0)


if __name__ == "__main__":
    unittest.main()
