# DAD Packages
from dad.sensors.pins import PINS
# Python Packages
import Adafruit_BBIO.GPIO as GPIO


class Indicator:

    def __init__(self, pin, setup=GPIO.OUT):
        self.pin = pin
        GPIO.setup(pin, setup)
