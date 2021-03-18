# DAD Packages
from dad.sensors.iio.iio_sensor import IIOSensor


class MPU6050(IIOSensor):
    """ The MPU-6050 device combine a 3-axis gyroscope and a 3-axis accelerometer on the same silicon die, together
    with an onboard Digital Motion Processor™ (DMP™), which processes complex 6-axis MotionFusion algorithms. It is
    built into the BeagleBone Black Enhanced and accessible as a Linux IIO device.

    .. _MPU-6050 MEMS Gyro + Accelerometer:
        https://invensense.tdk.com/products/motion-tracking/6-axis/mpu-6050/
    """

    def __init__(self):
        super().__init__(
            'mpu6050',
            ['accel_x', 'accel_y', 'accel_z',
             'anglvel_x', 'anglvel_y', 'anglvel_y',
             'gyro', 'temp'])
        self._accel_x_chan = self.get_channel('accel_x')
        self._accel_y_chan = self.get_channel('accel_y')
        self._accel_z_chan = self.get_channel('accel_z')
        self._anglvel_x_chan = self.get_channel('anglvel_x')
        self._anglvel_y_chan = self.get_channel('anglvel_y')
        self._anglvel_z_chan = self.get_channel('anglvel_z')
        self._gyro_chan = self.get_channel('gyro')
        self._temp_chan = self.get_channel('temp')

    def get_accel_vector(self):
        """ Gets a vector of the current acceleration values.

        Returns:
            (:obj:`list` of :obj:`double`): Acceleration vector (g) as per [x, y, z].
        """
        pass

    def get_angle_vector(self):
        """ Gets a vector of the current angle values.

        Returns:
            (:obj:`list` of :obj:`double`): Angle vector (deg) as per ...
        """
        pass

    def get_raw_accel_values(self):
        """ Gets a vector of the current raw acceleration values.

        Returns:
            (:obj:`list` of :obj:`double`): Angle vector (deg) as per
        """
        pass

    def get_raw_angle_values(self):
        """ Gets a vector of the current raw angle values.

        Returns:
            (:obj:`list` of :obj:`double`): Angle vector (deg) as per ...
        """
        pass

    def get_data_dict(self):
        accel_x, accel_y, accel_z = self.get_accel_vector()
        anglvel_x, anglvel_y, anglvel_z = self.get_angle_vector()
        return {
            'acceleration': {
                'accel_x': accel_x,
                'accel_y': accel_y,
                'accel_z': accel_z
            },
            'angle': {
                'anglvel_x': anglvel_x,
                'anglvel_y': anglvel_y,
                'anglvel_z': anglvel_z
            }
        }

    def get_raw_data_dict(self):
        return {
            'acceleration': {
                'accel_x': {
                    'calibbias': None,
                    'matrix': None,
                    'mount_matrix': None,
                    'raw': None,
                    'scale': None,
                    'scale_available': None
                },
                'accel_y': {
                    'calibbias': None,
                    'matrix': None,
                    'mount_matrix': None,
                    'raw': None,
                    'scale': None,
                    'scale_available': None
                },
                'accel_z': {
                    'calibbias': None,
                    'matrix': None,
                    'mount_matrix': None,
                    'raw': None,
                    'scale': None,
                    'scale_available': None
                }
            },
            'anglvel': {
                'anglvel_x': {
                    'calibbias': None,
                    'mount_matrix': None,
                    'raw': None,
                    'scale': None,
                    'scale_available': None
                },
                'anglvel_y': {
                    'calibbias': None,
                    'mount_matrix': None,
                    'raw': None,
                    'scale': None,
                    'scale_available': None
                },
                'anglvel_z': {
                    'calibbias': None,
                    'mount_matrix': None,
                    'raw': None,
                    'scale': None,
                    'scale_available': None
                }
            },
            'gyro': {
                'matrix': None
            },
            'temp': {
                'offset': None,
                'raw': None,
                'scale': None
            }
        }
