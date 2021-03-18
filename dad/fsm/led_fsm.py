# Python Package
import Adafruit_BBIO.GPIO as GPIO
from statemachine import StateMachine, State
# DAD Package
from dad.sensors.gpio.pins import PINS


class LedFSM(StateMachine):
    """ Finite state machine for managing the DAD LED indicators.

    .. _Python State Machine
        https://python-statemachine.readthedocs.io/en/latest/readme.html

    """
    # Default pin values
    POWER_LED_PIN = PINS.GPIO0_26.value
    INTERNET_STATUS_LED_PIN = PINS.GPIO1_13.value

    # Define states
    low = State('Low', initial=True)
    high = State('High')

    # Define state transitions
    high_to_low = high.to(low)
    low_to_high = low.to(high)

    def __init__(self, pin):
        """ Constructor for LedFSM.

        Args:
             pin (str): GPIO pin name corresponding to the LED.
        """
        super().__init__()
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)

    def on_high_to_low(self):
        """ State transition action, automatically called on a high to low state transition.
        """
        GPIO.output(self.pin, GPIO.LOW)

    def on_low_to_high(self):
        """ State transition action, automatically called on a low to high state transition.
        """
        GPIO.output(self.pin, GPIO.HIGH)

    def toggle(self):
        """ Helper function for toggling the state.
        """
        if self.is_low:
            self.low_to_high()
        else:
            self.high_to_low()
