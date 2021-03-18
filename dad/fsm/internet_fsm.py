# Python Packages
import time
import speedtest
import logging
from statemachine import State
# DAD Packages
from dad.fsm.dad_fsm import DADFSM
from dad.fsm.led_fsm import LedFSM


class InternetFSM(DADFSM):
    """ State machine for handling the internet speed indicator LED (red). LED will be solid when there is a strong internet
    download speed, slowly blinking when the internet speed is good, really slowly blinking when the internet speed is bad, and
    off when there is no internet available.

    .. _Speedtest-Cli
        https://github.com/sivel/speedtest-cli/wiki

    """

    # Define states
    # Example: weak = State('Strong', initial=True)

    # Define state transitions
    # Example: weak_to_good = weak.to(good)

    def __init__(self):
        super().__init__()
        logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s',
                            filename='/tmp/logging/internet_status.log',
                            level=logging.WARNING)
        self._led = LedFSM(LedFSM.INTERNET_STATUS_LED_PIN)
        self._speed_test = speedtest.Speedtest()

    # Example state transition action
    # def on_weak_to_good(self):
    #     """ State transition action, automatically called on weak to good transition.
    #
    #     """
    #     logging.info("Internet connection improvement.")

    def fetch_input(self):
        try:
            internet_speed = self._speed_test.download()  # internet speed in bit/s
        except Exception as e:
            logging.warning(e)
            internet_speed = 0
        return internet_speed

    def handle_transitions(self, input):
        # Handling transitions between states
        pass

    def handle_state_action(self):
        # Blink LED's according to specific state
        pass

    def cleanup(self):
        try:
            if self._led.is_high:
                self._led.high_to_low()
        except Exception as e:
            logging.error(e)


if __name__ == '__main__':
    internet_indicator = InternetFSM()
    internet_indicator.run()
