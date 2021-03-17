# DAD Packages
from dad.sensors.sensor import Sensor
from dad.sensors.gpio.pins import PINS
# Python Packages
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC


class ProtoBoard(Sensor):

    def __init__(self):
        super().__init__('proto_board')

    def get_dict(self):
        pass

    def get_dict_raw(self):
        pass
