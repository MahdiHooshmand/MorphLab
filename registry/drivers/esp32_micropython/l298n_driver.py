# MorphLab - L298N dual H-bridge driver
# ONE physical L298N module, 2 independent channels (A and B) - drives both
# DC motors from a single module (confirmed: only one L298N on this mechanism).

from machine import Pin, PWM


class _Channel:
    """One of the L298N's two independent H-bridge outputs."""

    def __init__(self, en_pin, in1_pin, in2_pin, pwm_freq=1000):
        self._en = PWM(Pin(en_pin))
        self._en.freq(pwm_freq)
        self._in1 = Pin(in1_pin, Pin.OUT)
        self._in2 = Pin(in2_pin, Pin.OUT)
        self.stop()

    def drive(self, speed):
        """speed: -1.0 (full reverse) to 1.0 (full forward)."""
        speed = max(-1.0, min(1.0, speed))
        duty = int(abs(speed) * 65535)
        self._en.duty_u16(duty)
        if speed > 0:
            self._in1.value(1)
            self._in2.value(0)
        elif speed < 0:
            self._in1.value(0)
            self._in2.value(1)
        else:
            self._in1.value(0)
            self._in2.value(0)

    def stop(self):
        self.drive(0)


class L298NDriver:
    def __init__(self, ena_pin, in1_pin, in2_pin, enb_pin, in3_pin, in4_pin, name="l298n"):
        self.name = name
        self.channel_a = _Channel(ena_pin, in1_pin, in2_pin)
        self.channel_b = _Channel(enb_pin, in3_pin, in4_pin)

    def stop_all(self):
        self.channel_a.stop()
        self.channel_b.stop()
