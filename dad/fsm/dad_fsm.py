# Python Packages
import time
from statemachine import StateMachine


class DADFSM(StateMachine):
    """ Base finite state machine for DAD device. Allows one to easily create new state machines
    by implementing the interface.

    .. _Python State Machine
        https://python-statemachine.readthedocs.io/en/latest/readme.html

    """

    def __init__(self):
        super().__init__()
        self._RUNNING = True

    def run(self, transition_frequency=2):
        """ Defines the state machine loop. State machine will call on methods in this sequence
        for as long as the state machine is running:

            fetch_input -> handle_transitions -> handle_state action -> cleanup

        Args:
            transition_frequency (int): Frequency that inputs will be checked at, in seconds.

        """
        start_time = time.time()
        while self._RUNNING:
            time.sleep(0.01)  # minimum sleep time to prevent FSM from hogging CPU
            try:
                if time.time() > start_time + transition_frequency:
                    input = self.fetch_input()
                    self.handle_transitions(input)
                    start_time = time.time()
                self.handle_state_action()
            except Exception as e:
                logging.error(e)
                self._RUNNING = False
            finally:
                self.cleanup()

    def fetch_input(self):
        """ Return value is passed to the handle_transitions method.

        Returns:
            (:obj:): Input for handling transitions.

        """
        raise NotImplementedError("Method fetch_input needs to be defined in all subclasses.")

    def handle_transitions(self, input):
        """ Handles transitions based on the supplied input.

        Args:
            input (:obj:): Input to be used in state transition.

        """
        raise NotImplementedError("Method handle_transitions needs to be defined in all subclasses.")

    def handle_state_action(self):
        """ Handles the state action. Should sleep in this method if there is no time consuming operations,
        to prevent FSM from hogging the CPU.

        """
        raise NotImplementedError("Method handle_state_action needs to be defined in all subclasses.")

    def cleanup(self):
        """ Perform any necessary cleanup in the case of an unexpected error.

        """
        pass
