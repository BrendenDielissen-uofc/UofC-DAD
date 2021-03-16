IIODEV1 = '/sys/bus/iio/devices/iio:device1'
IIODEV0 = '/sys/bus/iio/devices/iio:device0'
IIODEV2 = '/sys/bus/iio/devices/iio:device2'
try:
    print(IIODEV2 + '/in_pressure_raw')
    in_pressure_raw = subprocess.check_output(['/bin/cat',IIODEV2 + '/in_pressu$
    print(in_pressure_raw.strip().decode('utf-8'))
except Exception as e:
    print(e)
