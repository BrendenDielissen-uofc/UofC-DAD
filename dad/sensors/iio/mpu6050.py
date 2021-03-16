# DAD Packages
import dad.sensors.iio.iio_sensor.IIOSensor


# Python Packages


class MPU6050(IIOSensor):
    """ The MPU-6050 devices combine a 3-axis gyroscope and a 3-axis accelerometer on the same silicon die, together
    with an onboard Digital Motion Processor™ (DMP™), which processes complex 6-axis MotionFusion algorithms. It is
    built into the BeagleBone Black Enhanced and accessible as a Linux IIO device.

    .. _MPU-6050 MEMS Gyro + Accelerometer:
        https://invensense.tdk.com/products/motion-tracking/6-axis/mpu-6050/
    """

    def __init__(self):
        self.super(
            'mpu6050',
            ['accel_x', 'accel_y', 'accel_z',
             'anglvel_x', 'anglvel_y', 'anglvel_y',
             'gyro', 'temp'])

    def get_accel_vector(self):
        """ Gets a vector of the current acceleration values.

        Returns:
            (:obj:`list` of :obj:`double`): Acceleration vector (g) as per [x, y, z].
        """
        pass

    def get_angle_vector(self):
        """ Gets a vector of the current angle values.

        Returns:
            (:obj:`list` of :obj:`double`): Angle vector (deg) as per [x, y, z].
        """
        pass
