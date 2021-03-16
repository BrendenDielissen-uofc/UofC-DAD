import time, iio


class IIOSensor:
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
        self.device = device
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


class LPS331AP(IIOSensor):
    """ The LPS331AP is a MEMS sensor which measures absolute pressure and temperature.
    It is built into the BeagleBone Black Enhanced and accessible as a Linux IIO device.
    .. _LPS331AP MEMS Pressure Sensor:
        https://www.st.com/en/mems-and-sensors/lps331ap.html#:~:text=The%20LPS331AP%20is%20available%20in,to%20reach%20the%20sensing%20element.
    """

    def __init__(self, device, channel_names):
        super().__init__('lps331ap', ['pressure', 'temp'])

    def get_temperature(self):
        """ Gets the current internal temperature in Celcius.
        Returns:
            (double): The current internal temperature reading.
        """
        chan = self.get_channel('temp')
        raw_temp = float(chan.attrs['raw'].value)
        offset = float(chan.attrs['offset'].value)
        scale = float(chan.attrs['scale'].value)
        temp = (offset + raw_temp) * (scale / 1000)
        return temp

    def get_pressure(self):
        """ Gets the current internal pressure reading in millibars.
        Returns:
            (double): The current internal pressure reading.
        """
        chan = self.get_channel('pressure')
        raw_pressure = float(chan.attrs['raw'].value)
        scale = float(chan.attrs['scale'].value)
        pressure = (raw_pressure * scale) / 100
        return pressure


#Non-class functions for reference (testing)
# def get_pressure():
#     ctx = iio.LocalContext()
#     ctrl = ctx.find_device('lps331ap')
#
#     chan = ctrl.find_channel('pressure')
#     raw_pressure = float(chan.attrs['raw'].value)
#     scale = float(chan.attrs['scale'].value)
#     scaled_pressure = (raw_pressure * scale) / 100
#     print('Pressure: {} bar'.format(round(scaled_pressure, 3)))
#     return scaled_pressure
#
#
# def get_temperature():
#     ctx = iio.LocalContext()
#     ctrl = ctx.find_device('lps331ap')
#
#     chan = ctrl.find_channel('temp')
#     raw_temp = float(chan.attrs['raw'].value)
#     offset = float(chan.attrs['offset'].value)
#     scale = float(chan.attrs['scale'].value)
#     temp = (offset + raw_temp) * (scale / 1000)
#     print('Temperature: {} C'.format(round(temp, 2)))
#     return temp
