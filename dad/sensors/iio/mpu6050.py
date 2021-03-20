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
        raw_accel_x, raw_accel_y, raw_accel_z = self.get_raw_accel_values()
        accel_x_scale = float(self._accel_x_chan.attrs['scale'].value)
        accel_y_scale = float(self._accel_y_chan.attrs['scale'].value)
        accel_z_scale = float(self._accel_z_chan.attrs['scale'].value)
        accel_vector = [raw_accel_x * accel_x_scale, raw_accel_y * accel_y_scale, raw_accel_z * accel_z_scale]
        return accel_vector

    def get_angle_vector(self):
        """ Gets a vector of the current angle values.

        Returns:
            (:obj:`list` of :obj:`double`): Angle vector (deg) as per ...
        """
        raw_angle_x, raw_angle_y, raw_angle_z = self.get_raw_angle_values()
        angle_x_scale = float(self._anglvel_x_chan.attrs['scale'].value)
        angle_y_scale = float(self._anglvel_y_chan.attrs['scale'].value)
        angle_z_scale = float(self._anglvel_z_chan.attrs['scale'].value)
        angle_vector = [raw_angle_x * angle_x_scale * 57.2958, raw_angle_y * angle_y_scale * 57.2958, raw_angle_z * angle_z_scale * 57.2958]
        return angle_vector

    def get_raw_accel_values(self):
        """ Gets a vector of the current raw acceleration values.

        Returns:
            (:obj:`list` of :obj:`double`): Acceleration values as per ...
        """
        raw_accel_x = float(self._accel_x_chan.attrs['raw'].value)
        raw_accel_y = float(self._accel_y_chan.attrs['raw'].value)
        raw_accel_z = float(self._accel_z_chan.attrs['raw'].value)
        raw_accel_list = [raw_accel_x, raw_accel_y, raw_accel_z]
        return raw_accel_list

    def get_raw_angle_values(self):
        """ Gets a vector of the current raw angle values.

        Returns:
            (:obj:`list` of :obj:`double`): Angle values (rad) as per ...
        """
        raw_angle_x = float(self._anglvel_x_chan.attrs['raw'].value)
        raw_angle_y = float(self._anglvel_y_chan.attrs['raw'].value)
        raw_angle_z = float(self._anglvel_z_chan.attrs['raw'].value)
        raw_angle_list = [raw_angle_x, raw_angle_y, raw_angle_z]
        return raw_angle_list

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

    def _decode_matrix_values(self, matrix_str):
        split = [sub.split(',') for sub in matrix_str.split(';')]
        for i, row in enumerate(split):
            for j, ax in enumerate(row):
                split[i][j] = int(ax.strip())
        return split

    def _decode_scale_available_values(self, scale_available_str):
        return [float(ax) for ax in scale_available_str.split()]

    def get_raw_data_dict(self):
        raw_accel_x, raw_accel_y, raw_accel_z = self.get_raw_accel_values()
        raw_angle_x, raw_angle_y, raw_angle_z = self.get_raw_angle_values()
        return {
            'acceleration': {
                'accel_x': {
                    'calibbias': float(self._accel_x_chan.attrs['calibbias'].value),
                    'matrix': self._decode_matrix_values(self._accel_x_chan.attrs['matrix'].value),
                    'mount_matrix': self._decode_matrix_values(self._accel_x_chan.attrs['mount_matrix'].value),
                    'raw': raw_accel_x,
                    'scale': float(self._accel_x_chan.attrs['scale'].value),
                    'scale_available': self._decode_scale_available_values(self._accel_x_chan.attrs['scale_available'].value)
                },
                'accel_y': {
                    'calibbias': float(self._accel_y_chan.attrs['calibbias'].value),
                    'matrix': self._decode_matrix_values(self._accel_y_chan.attrs['matrix'].value),
                    'mount_matrix': self._decode_matrix_values(self._accel_y_chan.attrs['mount_matrix'].value),
                    'raw': raw_accel_y,
                    'scale': float(self._accel_y_chan.attrs['scale'].value),
                    'scale_available': self._decode_scale_available_values(self._accel_y_chan.attrs['scale_available'].value)
                },
                'accel_z': {
                    'calibbias': float(self._accel_z_chan.attrs['calibbias'].value),
                    'matrix': self._decode_matrix_values(self._accel_z_chan.attrs['matrix'].value),
                    'mount_matrix': self._decode_matrix_values(self._accel_z_chan.attrs['mount_matrix'].value),
                    'raw': raw_accel_z,
                    'scale': float(self._accel_z_chan.attrs['scale'].value),
                    'scale_available': self._decode_scale_available_values(self._accel_z_chan.attrs['scale_available'].value)
                }
            },
            'anglvel': {
                'anglvel_x': {
                    'calibbias': float(self._anglvel_x_chan.attrs['calibbias'].value),
                    'mount_matrix': self._decode_matrix_values(self._anglvel_x_chan.attrs['mount_matrix'].value),
                    'raw': raw_angle_x,
                    'scale': float(self._anglvel_x_chan.attrs['scale'].value),
                    'scale_available': self._decode_scale_available_values(self._anglvel_x_chan.attrs['scale_available'].value)
                },
                'anglvel_y': {
                    'calibbias': float(self._anglvel_y_chan.attrs['calibbias'].value),
                    'mount_matrix': self._decode_matrix_values(self._anglvel_y_chan.attrs['mount_matrix'].value),
                    'raw': raw_angle_y,
                    'scale': float(self._anglvel_y_chan.attrs['scale'].value),
                    'scale_available': self._decode_scale_available_values(self._anglvel_y_chan.attrs['scale_available'].value)
                },
                'anglvel_z': {
                    'calibbias': float(self._anglvel_z_chan.attrs['calibbias'].value),
                    'mount_matrix': self._decode_matrix_values(self._anglvel_z_chan.attrs['mount_matrix'].value),
                    'raw': raw_angle_z,
                    'scale': float(self._anglvel_z_chan.attrs['scale'].value),
                    'scale_available': self._decode_scale_available_values(self._anglvel_z_chan.attrs['scale_available'].value)
                }
            },
            'gyro': {
                'matrix': self._decode_matrix_values(self._gyro_chan.attrs['matrix'].values)
            },
            'temp': {
                'offset': float(self._temp_chan.attrs['offset'].value),
                'raw': float(self._temp_chan.attrs['raw'].value),
                'scale': float(self._temp_chan.attrs['scale'].value)
            }
        }
