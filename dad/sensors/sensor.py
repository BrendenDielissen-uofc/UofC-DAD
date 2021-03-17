# Python Packages
from abc import abstractmethod, ABC


class Sensor(ABC):
    def __init__(self, device):
        self.device = device

    @abstractmethod
    def get_dict(self):
        """ Gets the current sensor data in a dictionary format.

        Return:
            (dict): The raw sensor data in dictionary format.
        """
        pass

    @abstractmethod
    def get_dict_raw(self):
        """ Gets the current raw sensor data in a dictionary format.

        Return:
            (dict): The raw sensor data in dictionary format.
        """
        pass
