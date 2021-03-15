IIODEV1 = '/sys/bus/iio/devices/iio\:device1'
IIODEV0 = '/sys/bus/iio/devices/iio\:device0'
try:
    in_pressure_raw = open(IIODEV1 + '/in_pressure_raw', 'r')
    print(in_pressure_raw.read())
except:
    print('Test fail')
