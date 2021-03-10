# Python Packages
from enum import Enum


class PINS(Enum):
    """BeagleBone Black pins enum."""
    # GPIO pins
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
    # ADC pins
    AIN4 = "AIN4"
    AIN6 = "AIN6"
    AIN5 = "AIN5"
    AIN2 = "AIN2"
    AIN3 = "AIN3"
    AIN0 = "AIN0"
    AIN1 = "AIN1"
