import unittest
import _paths
from encoder import QuadratureEncoder


class TestQuadratureEncoder(unittest.TestCase):
    def test_counts_forward_one_revolution(self):
        enc = QuadratureEncoder(pin_a=18, pin_b=19, ppr=400)
        enc._pin_b.value(0)  # B low while A rises = forward
        for _ in range(400):
            enc._pin_a.simulate_pulse()
        self.assertEqual(enc.position, 400)
        self.assertAlmostEqual(enc.revolutions(), 1.0)

    def test_counts_reverse(self):
        enc = QuadratureEncoder(pin_a=18, pin_b=19, ppr=400)
        enc._pin_b.value(1)  # B high while A rises = reverse
        enc._pin_a.simulate_pulse()
        self.assertEqual(enc.position, -1)

    def test_reset(self):
        enc = QuadratureEncoder(pin_a=18, pin_b=19, ppr=400)
        enc._pin_b.value(0)
        enc._pin_a.simulate_pulse()
        enc.reset()
        self.assertEqual(enc.position, 0)


if __name__ == "__main__":
    unittest.main()
