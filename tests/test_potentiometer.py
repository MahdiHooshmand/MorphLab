import unittest
import _paths
from potentiometer import Potentiometer


class TestPotentiometer(unittest.TestCase):
    def test_read_raw(self):
        pot = Potentiometer(adc_pin=34)
        pot._adc.set_value(2048)
        self.assertEqual(pot.read_raw(), 2048)


if __name__ == "__main__":
    unittest.main()
