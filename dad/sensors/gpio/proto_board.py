# Python Packages
import Adafruit_BBIO.ADC as ADC
# DAD Packages
from dad.sensors.sensor import Sensor
from dad.sensors.gpio.pins import PINS


class ProtoBoard(Sensor):
    """ The ProtoBoard consists of a TMP36 temperature sensor for external environment temperature readings,
    as well as 3 sense lines for the vehicle, battery, and vbus voltages, which are all read into the BeagleBone Black
    Enchanced's on-board ADC's. The AdaFruit BBIO library provides an interface for accessing the ADC values.

    .. _TMP36 Temperature Sensor:
        https://www.analog.com/media/en/technical-documentation/data-sheets/TMP35_36_37.pdf
    .. _Adafruit BBIO Library:
        https://github.com/adafruit/adafruit-beaglebone-io-python

    """
    # Storage of pin names, offsets, and scale factors for each sensor.
    SENSORS = {
        'temperature': {
            'pin': PINS.AIN4.value,
            'offset': -50,
            'scale_factor': 100
        },
        'vbus': {
            'pin': PINS.AIN6.value,
            'offset': 0,
            'scale_factor': 7.9 / 1.1
        },
        'vehicle': {
            'pin': PINS.AIN2.value,
            'offset': 0,
            'scale_factor': 9.87
        },
        'battery': {
            'pin': PINS.AIN0.value,
            'offset': 0,
            'scale_factor': 7.9 / 1.1
        }
    }

    def __init__(self):
        super().__init__('proto_board')
        ADC.setup()
        self._sense_lines = ['vbus', 'vehicle', 'battery']

    def get_temperature(self, rounding=2):
        """ Gets the current temperature reading from TMP36.

        Args:
            rounding (int): Specifies the amount of decimal place digits to round return values to.
        Returns:
             (float): Temperature value in Celcius.
        """
        temperature_raw_values = self.get_raw_temperature()
        temp_offset, temp_scaling_factor = self._get_sensor_scaling_values('temperature')
        temperature_voltage_value = temperature_raw_values['scaled']
        
        # Nick & Juj - This is completed.
        # Equation follows a simple y = mx + b formula.
        current_temperature = temp_scaling_factor * temperature_voltage_value + temp_offset

        return round(current_temperature, rounding)

    def get_sense_line_voltages(self, rounding=2):
        """ Gets the current sense line voltage readings from ADC dividers.

        Args:
            rounding (int): Specifies the amount of decimal place digits to round return values to.
        Returns:
             (dict): Sense line voltage readings.
                Formatted as:
                {
                    'vbus': ...,
                    'vehicle': ...,
                    'battery': ...
                }
        """
        raw_sense_line_readings = self.get_raw_sense_line_voltages()
        vbus_raw_values = raw_sense_line_readings['vbus']
        vbus_offset, vbus_scale_factor = self._get_sensor_scaling_values('vbus')
        vbus_voltage_value = vbus_raw_values['scaled']

        vehicle_raw_values = raw_sense_line_readings['vehicle']
        vehicle_offset, vehicle_scale_factor = self._get_sensor_scaling_values('vehicle')
        vehicle_voltage_value = vehicle_raw_values['scaled']

        battery_raw_values = raw_sense_line_readings['battery']
        battery_offset, battery_scale_factor = self._get_sensor_scaling_values('battery')
        battery_voltage_value = battery_raw_values['scaled']

        # Nick & Juj -> This is complete.
        # y = mx + b (although b in this case is always = 0)

        vbus = vbus_scale_factor * vbus_voltage_value + vbus_offset
        vehicle = vehicle_scale_factor * vehicle_voltage_value + vehicle_offset
        battery = battery_scale_factor * battery_voltage_value + battery_offset
        
        return {
            'vbus': vbus,
            'vehicle': vehicle,
            'battery': battery
        }

    def get_raw_sense_line_voltages(self):
        """ Gets the current raw sense line ADC voltages.

        Returns:
             (dict): Dict of raw sense line ADC readings.
                Formatted as:
                {
                    ...,
                    sensor: {
                        'value': ...,
                        'scaled': ...,
                        'raw': ...
                    }
                }
        """
        return {sensor: self._get_raw_adc_data(sensor) for sensor in self._sense_lines}

    def get_raw_temperature(self):
        """ Gets the current raw TMP36 ADC readings.

        Returns:
             (dict): Dict of raw TMP36 ADC readings.
                Formatted as:
                {
                    'temperature': {
                        'value': ...,
                        'scaled': ...,
                        'raw': ...
                    }
                }
        """
        return {'temperature': self._get_raw_adc_data('temperature')}

    @classmethod
    def _get_raw_adc_data(cls, sensor):
        raw_data = {
            'value': None,
            'scaled': None,
            'raw': None,
        }
        pin = cls.SENSORS[sensor]['pin']
        raw_data['value'] = ADC.read(pin)  # ADC value between 0 - 1.0
        raw_data['scaled'] = raw_data['value'] * 1.8  # ADC values scaled to 1.8V
        raw_data['raw'] = ADC.read_raw(pin)  # raw ADC value
        return raw_data

    @classmethod
    def _get_sensor_scaling_values(cls, sensor):
        return cls.SENSORS[sensor]['offset'], cls.SENSORS[sensor]['scale_factor']

    def get_data_dict(self):
        return {
            'temperature': self.get_temperature(),
            'sense_lines': self.get_sense_line_voltages()
        }

    def get_raw_data_dict(self):
        return {
            'temperature': self.get_raw_temperature()['temperature'],
            'sense_lines': self.get_raw_sense_line_voltages()
        }
