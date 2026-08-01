# MorphLab Project 001 - Potentiometer driver
# Mechanism-mounted potentiometer, read via ESP32 ADC.

from machine import ADC, Pin


class Potentiometer:
    """Raw analog position sensor on a single ADC-capable GPIO."""

    def __init__(self, adc_pin, name="potentiometer"):
        self.name = name
        self._adc = ADC(Pin(adc_pin))
        self._adc.atten(ADC.ATTN_11DB)  # full 0-3.3V input range
        self._adc.width(ADC.WIDTH_12BIT)  # 0-4095 raw reading

    def read_raw(self):
        """Returns the raw 12-bit ADC reading (0-4095)."""
        return self._adc.read()
