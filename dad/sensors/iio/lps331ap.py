# DAD Packages
from dad.sensors.iio.iio_sensor import IIOSensor
# Python Packages
from overrides import overrides


class LPS331AP(IIOSensor):
    """ The LPS331AP is a MEMS sensor which measures absolute pressure and temperature.
    It is built into the BeagleBone Black Enhanced and accessible as a Linux IIO device.

    .. _LPS331AP MEMS Pressure Sensor:
        https://www.st.com/en/mems-and-sensors/lps331ap.html#:~:text=The%20LPS331AP%20is%20available%20in,to%20reach%20the%20sensing%20element.
    """

    def __init__(self):
        super().__init__('lps331ap', ['pressure', 'temp'])
        self._temp_chan = self.get_channel('temp')
        self._pressure_chan = self.get_channel('pressure')

    def get_temperature(self, rounding=2):
        """ Gets the current internal temperature in Celcius.
        Returns:
            (float): The current internal temperature reading.
        """
        raw_temp, offset, scale = self.get_raw_temperature_values()
        return round((offset + raw_temp) * (scale / 1000), rounding)

    def get_pressure(self, rounding=2):
        """ Gets the current internal pressure reading in millibars.
        Returns:
            (float): The current internal pressure reading.
        """
        raw_pressure, scale = self.get_raw_pressure_values()
        return round((raw_pressure * scale) / 100, rounding)

    def get_raw_temperature_values(self):
        """ Gets the current raw temperature values.

        Return:
             (:obj:`tuple` of :obj:`float`): Tuple of raw temperature values.
                Formatted as: (raw, offset, scale).
        """
        raw_temp = float(self._temp_chan.attrs['raw'].value)
        offset = float(self._temp_chan.attrs['offset'].value)
        scale = float(self._temp_chan.attrs['scale'].value)
        return raw_temp, offset, scale

    def get_raw_pressure_values(self):
        """ Gets the current raw pressure values.

        Returns:
            (:obj:`tuple` of :obj:`float`): Tuple of raw pressure values.
                Formatted as: (raw, scale).
        """
        raw_pressure = float(self._pressure_chan.attrs['raw'].value)
        scale = float(self._pressure_chan.attrs['scale'].value)
        return raw_pressure, scale

    def get_data_dict(self):
        return {
            'temperature': self.get_temperature(),
            'pressure': self.get_pressure()
        }

    def get_raw_data_dict(self):
        raw_temp, offset, temp_scale = self.get_raw_temperature_values()
        raw_pressure, pressure_scale = self.get_raw_pressure_values()
        return {
            'temperature': {
                'raw': raw_temp,
                'offset': offset,
                'scale': temp_scale
            },
            'pressure': {
                'raw': raw_pressure,
                'scale': pressure_scale
            }
        }
