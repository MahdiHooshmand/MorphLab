import unittest
import _paths
from dc_motor import DCMotor


class TestDCMotor(unittest.TestCase):
    def test_defaults_match_datasheet(self):
        m = DCMotor("motor_1")
        self.assertEqual(m.rated_voltage, 12)
        self.assertEqual(m.no_load_rpm, 330)
        self.assertEqual(m.stall_torque_kgcm, 1.0)
        self.assertEqual(m.rated_current_a, 2.8)


if __name__ == "__main__":
    unittest.main()
