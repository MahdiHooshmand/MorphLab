# Test-only stub of MicroPython's `machine` module, so registry/experiment
# code can be imported and exercised with plain python3 on the host, with
# no ESP32 attached. Not shipped to the device.


class Pin:
    IN = "IN"
    OUT = "OUT"
    PULL_UP = "PULL_UP"
    IRQ_RISING = "IRQ_RISING"
    IRQ_FALLING = "IRQ_FALLING"

    def __init__(self, id, mode=None, pull=None):
        self.id = id
        self.mode = mode
        self.pull = pull
        self._value = 0
        self._irq_handler = None

    def value(self, v=None):
        if v is None:
            return self._value
        self._value = v

    def irq(self, trigger=None, handler=None):
        self._irq_handler = handler

    def simulate_pulse(self):
        """Test helper: fire the registered IRQ handler once."""
        if self._irq_handler:
            self._irq_handler(self)


class ADC:
    ATTN_11DB = "ATTN_11DB"
    WIDTH_12BIT = "WIDTH_12BIT"

    def __init__(self, pin):
        self.pin = pin
        self._value = 0

    def atten(self, v):
        pass

    def width(self, v):
        pass

    def read(self):
        return self._value

    def set_value(self, v):
        """Test helper."""
        self._value = v


class PWM:
    def __init__(self, pin):
        self.pin = pin
        self._freq = 0
        self._duty = 0

    def freq(self, f=None):
        if f is None:
            return self._freq
        self._freq = f

    def duty_u16(self, d=None):
        if d is None:
            return self._duty
        self._duty = d
