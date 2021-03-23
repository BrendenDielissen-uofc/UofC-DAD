# Python Packages
import time
import logging
from statemachine import State
# DAD Packages
from dad.fsm.dad_fsm import DADFSM
from dad.fsm.led_fsm import LedFSM
from dad.sensors.gpio.proto_board import ProtoBoard


class PowerFSM(DADFSM):
    """ State machine for handling the power indicator LED (green). LED will be solid when there is full vehicle power
    available, and slowly blinking when the DAD is running off of battery power.

    """

    # Define states
    full = State('Full', initial=True)
    battery = State('Battery')

    # Define state transitions
    full_to_battery = full.to(battery)
    battery_to_full = battery.to(full)

    def __init__(self):
        super().__init__('/home/dad003/logging/power_status.log')
        self._proto_board = ProtoBoard()
        self._led = LedFSM(LedFSM.POWER_LED_PIN)

    def on_full_to_battery(self):
        """ State transition action, automatically called on full to battery transition.

        """
        logging.warning("Power status transitioning to battery.")

    def on_battery_to_full(self):
        """ State transition action, automatically called on battery to full transition.

        """
        logging.warning("Power status transitioning to fully powered.")

    def run(self, transition_frequency=2):
        logging.info("Starting Power FSM...")
        super().run()

    def fetch_input(self):
        voltage_values = self._proto_board.get_raw_sense_line_voltages()
        vehicle = voltage_values['vehicle']['scaled']
        return vehicle

    def handle_transitions(self, input):
        if self.is_full and input <= 0.6:
            self.full_to_battery()
        elif self.is_battery and input > 0.6:
            self.battery_to_full()

    def handle_state_action(self):
        if self.is_full:
            if self._led.is_low:
                self._led.low_to_high()
            time.sleep(2)
        else:
            self._led.toggle()
            time.sleep(1)

    def cleanup(self):
        try:
            if self._led.is_high:
                self._led.high_to_low()
        except Exception as e:
            logging.error(e)


if __name__ == '__main__':
    power_indicator = PowerFSM()
    power_indicator.run()
