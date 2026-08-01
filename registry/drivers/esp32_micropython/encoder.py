# MorphLab Project 001 - Encoder driver
# Hardware: optical quadrature encoder built into the 25GA-370 gear motor.
#   - 2 channels (A/B), 90-degree phase offset
#   - 400 pulses per revolution (of the motor shaft, per datasheet)
# See docs/datasheets/M25N-encoder-datasheet.pdf

from machine import Pin


class QuadratureEncoder:
    """Interrupt-driven quadrature encoder counter.

    Counts on channel A's rising edge; channel B's level at that instant
    gives direction. This gives 1x resolution (matches the datasheet's
    400 pulses/rev). Can be upgraded to 4x decoding later by also
    triggering on A's falling edge and B's edges, if finer resolution
    is needed.
    """

    def __init__(self, pin_a, pin_b, ppr=400, name="encoder"):
        self.name = name
        self.ppr = ppr
        self.position = 0  # signed pulse count, raw

        self._pin_a = Pin(pin_a, Pin.IN, Pin.PULL_UP)
        self._pin_b = Pin(pin_b, Pin.IN, Pin.PULL_UP)
        self._pin_a.irq(trigger=Pin.IRQ_RISING, handler=self._on_pulse)

    def _on_pulse(self, pin):
        # If B is already high when A rises, we're spinning one way; else the other.
        if self._pin_b.value():
            self.position -= 1
        else:
            self.position += 1

    def revolutions(self):
        return self.position / self.ppr

    def reset(self):
        self.position = 0
