# DAD Packages
import dad.sensors.iio.iio_sensor.IIOSensor
# Python Packages


class LPS331AP(IIOSensor):
    """ The LPS331AP is a MEMS sensor which measures absolute pressure and temperature.
    It is built into the BeagleBone Black Enhanced and accessible as a Linux IIO device.

    .. _LPS331AP MEMS Pressure Sensor:
        https://www.st.com/en/mems-and-sensors/lps331ap.html#:~:text=The%20LPS331AP%20is%20available%20in,to%20reach%20the%20sensing%20element.
    """

    def __init__(self):
        super().__init__('lps331ap', ['pressure', 'temp'])

    def get_temperature(self):
        """ Gets the current internal temperature in Celcius.

        Returns:
            (double): The current internal temperature reading.
        """
        pass

    def get_pressure(self):
        """ Gets the current internal pressure reading in millibars.

        Returns:
            (double): The current internal pressure reading.
        """
        pass