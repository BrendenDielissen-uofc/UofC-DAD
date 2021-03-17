# DAD Packages
from dad.sensors.sensor import Sensor
# Python Packages
from abc import ABC, abstractmethod
import iio
from overrides import overrides


class IIOSensor(Sensor):
    """ This is an interface for exposing the functionality of IIO devices.

    IIOSensor wraps the Python bindings from the pylibiio library such that they are
    more simple to use. Please refer to the library homepage for more information.

    .. _Analog Devices Inc. LibIIO
        https://github.com/analogdevicesinc/libiio

    """

    def __init__(self, device, channel_names):
        """ Constructor for IIOSensor.

        Args:
            device (str): Device name.
            channel_names (:obj:`list` of :obj:`str`): Device channel names.
        """
        super().__init__(device)
        self._ctx = iio.LocalContext()
        self._ctrl = self._ctx.find_device(device)
        self.channels = [self._ctrl.find_channel(channel) for channel in channel_names]

    def get_channel(self, channel_name):
        """ Returns channel from channel name.

        Args:
            channel_name (str): The name of the desired channel.

        Returns:
            (:obj:`iio.Channel`): The channel.
        """
        return next(channel for channel in self.channels if channel.id == channel_name)

    def get_data_dict(self):
        pass

    def get_raw_data_dict(self):
        pass
