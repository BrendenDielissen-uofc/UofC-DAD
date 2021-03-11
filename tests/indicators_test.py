# Python Packages
import Adafruit_BBIO.GPIO as GPIO
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


LED1 = PINS.GPIO0_26.value
LED2 = PINS.GPIO1_29.value
print("LED1 on pin: {}".format(LED1))
print("LED2 on pin: {}".format(LED2))
input('\nCheck that pins are correct, then hit enter to continue...')

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

print('Flashing both LED\' 10 times:')
for i in range(10):
    print('Flash {}'.format(i + 1))
    GPIO.output(LED1, GPIO.HIGH)
    GPIO.output(LED2, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED1, GPIO.LOW)
    GPIO.output(LED2, GPIO.LOW)
    time.sleep(1)