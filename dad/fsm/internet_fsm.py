# Python Packages
import time
import logging
import speedtest
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
    strong = State('Strong')
    good = State('Good')
    weak = State('Weak')
    off = State('Off', initial=True)

    # Define state transitions
    strong_to_good = strong.to(good)
    good_to_strong = good.to(strong)
    good_to_weak = good.to(weak)
    weak_to_good = weak.to(good)
    weak_to_off = weak.to(off)
    off_to_weak = off.to(weak)

    def __init__(self):
        super().__init__('/home/dad003/logging/internet_status.log')
        self._led = LedFSM(LedFSM.INTERNET_STATUS_LED_PIN)
        self._speed_test = speedtest.Speedtest()
        self._speed_test.get_best_server()

    def on_strong_to_good(self):
        """ State transition action, automatically called on strong to good transition.

        """
        logging.warning("Internet connection reduction (strong to good connection).")

    def on_good_to_strong(self):
        """ State transition action, automatically called on good to strong transition.

        """
        logging.warning("Internet connection improvement (good to strong connection).")

    def on_good_to_weak(self):
        """ State transition action, automatically called on good to weak transition.

        """
        logging.warning("Internet connection reduction (good to weak connection).")

    def on_weak_to_good(self):
        """ State transition action, automatically called on weak to good transition.

        """
        logging.warning("Internet connection improvement (weak to good connection).")

    def on_weak_to_off(self):
        """ State transition action, automatically called on weak to off transition.

        """
        logging.warning("Internet connection reduction (Weak to no connection).")

    def on_off_to_weak(self):
        """ State transition action, automatically called on weak to off transition.

        """
        logging.warning("Internet connection improvement (no connection to weak).")

    def run(self, transition_frequency=2):
        logging.info("Starting Internet FSM...")
        super().run()

    def fetch_input(self):
        try:
            internet_speed = self._speed_test.download(threads=1)  # internet speed in bit/s
        except Exception as e:
            logging.error(e)
            internet_speed = 0
        return internet_speed

    def handle_transitions(self, input):
        if self.is_strong and input <= 25000:
            self.strong_to_good()
        elif self.is_good:
            if input >= 25000:
                self.good_to_strong()
            elif input <= 9000:
                self.good_to_weak()
        elif self.is_weak:
            if input >= 9000:
                self.weak_to_good()
            elif input == 0:
                self.weak_to_off()
        elif self.is_off and input >= 0:
            self.off_to_weak()

    def handle_state_action(self):
        if self.is_strong:
            if self._led.is_low:
                self._led.low_to_high()
            time.sleep(2)
        elif self.is_good:
            self._led.toggle()
            time.sleep(1)
        elif self.is_weak:
            self._led.toggle()
            time.sleep(2)
        elif self.is_off:
            if self._led.is_high:
                self._led.high_to_low()
            time.sleep(2)

    def cleanup(self):
        try:
            if self._led.is_high:
                self._led.high_to_low()
        except Exception as e:
            logging.error(e)


if __name__ == '__main__':
    internet_indicator = InternetFSM()
    internet_indicator.run()
