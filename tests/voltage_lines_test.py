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


VBUS = PINS.AIN6.value
VEHICLE = PINS.AIN2.value
BATTERY = PINS.AIN0.value
lines = [VBUS, VEHICLE, BATTERY]
line_dict = {
    VBUS: 'VBUS',
    VEHICLE: 'VEHICLE',
    BATTERY: 'BATTERY'
}
print("VBUS on pin: {}".format(VBUS))
print("VEHICLE on pin: {}".format(VEHICLE))
print("BATTERY on pin: {}".format(BATTERY))
input('\nCheck that pins are correct, then hit enter to continue...')

ADC.setup()
print('Reading 5 voltage sensor values:\n')
for i in range(5):
    time.sleep(0.5)
    for line in lines:
        value = ADC.read(line)
        voltage = value * 1.8 # 1.8V
        raw = ADC.read_raw(line)
        print('{} read_val: {} voltage: {} raw: {}'.format(
            line_dict[line],
            round(value, 2),
            round(voltage, 2),
            raw)
        )
    print()
