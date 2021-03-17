# Python Packages
import Adafruit_BBIO.ADC as ADC
import time
from enum import Enum


class PINS(Enum):
    """BeagleBone Black pins enum."""
    # GPIO
    GPIO1_13 = 'GPIO1_13'
    GPIO1_12 = 'GPIO1_12'
    GPIO0_26 = 'GPIO0_26'
    GPIO1_15 = 'GPIO1_15'
    GPIO1_14 = 'GPIO1_14'
    GPIO0_27 = 'GPIO0_27'
    GPIO2_1 = 'GPIO2_1'
    GPIO1_29 = 'GPIO1_29'
    GPIO1_28 = 'GPIO1_28'
    GPIO1_16 = 'GPIO1_16'
    GPIO1_17 = 'GPIO1_17'
    GPIO3_21 = 'GPIO3_21'
    GPIO3_19 = 'GPIO3_19'
    GPIO0_7 = 'GPIO0_7'
    # ADC
    AIN4 = 'AIN4'
    AIN6 = 'AIN6'
    AIN5 = 'AIN5'
    AIN2 = 'AIN2'
    AIN3 = 'AIN3'
    AIN0 = 'AIN0'
    AIN1 = 'AIN1'

TEMP_SENS = PINS.AIN4.value
print("TEMP_SENS on pin: {}".format(TEMP_SENS))
input('\nCheck that pin is correct, then hit enter to continue...')

ADC.setup()
print('Reading 20 temperature sensor values:\n')
for i in range(20):
    time.sleep(0.5)
    value = ADC.read(TEMP_SENS)
    voltage = value * 1.8 # 1.8V
    temperature = (voltage - 0.5) / 0.01
    raw = ADC.read_raw(TEMP_SENS)
    print('read_val: {} voltage: {} raw: {} temperature: {}'.format(
        round(value, 2),
        round(voltage, 2),
        raw, round(temperature, 1))
    )
