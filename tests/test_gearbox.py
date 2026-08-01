import unittest
import _paths
from gearbox import Gearbox


class TestGearbox(unittest.TestCase):
    def test_output_revolutions(self):
        g = Gearbox(ratio=21)
        self.assertAlmostEqual(g.output_revolutions(21), 1.0)

    def test_motor_revolutions(self):
        g = Gearbox(ratio=21)
        self.assertAlmostEqual(g.motor_revolutions(1.0), 21)


if __name__ == "__main__":
    unittest.main()
