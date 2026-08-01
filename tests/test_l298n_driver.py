import unittest
import _paths
from l298n_driver import L298NDriver


class TestL298NDriver(unittest.TestCase):
    def test_channels_are_independent(self):
        d = L298NDriver(ena_pin=25, in1_pin=26, in2_pin=27, enb_pin=14, in3_pin=12, in4_pin=13)
        d.channel_a.drive(0.5)
        d.channel_b.drive(-1.0)
        self.assertGreater(d.channel_a._en._duty, 0)
        self.assertEqual(d.channel_b._in1.value(), 0)
        self.assertEqual(d.channel_b._in2.value(), 1)

    def test_stop_all(self):
        d = L298NDriver(25, 26, 27, 14, 12, 13)
        d.channel_a.drive(1.0)
        d.channel_b.drive(-1.0)
        d.stop_all()
        self.assertEqual(d.channel_a._en._duty, 0)
        self.assertEqual(d.channel_b._en._duty, 0)


if __name__ == "__main__":
    unittest.main()
