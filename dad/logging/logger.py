# DAD Packages
from dad.sensors.iio.lps331ap import LPS331AP
from dad.sensors.iio.mpu6050 import MPU6050
from dad.sensors.gpio.proto_board import ProtoBoard
# Python Packages
import datetime
import time
import json
import logging


class Logger:
    """ Logs sensor data from all sensors available to the DAD device. Sensors must follow the
    Sensor interface defined in dad.sensors.sensor.

    """

    def __init__(self):
        logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s',
                            filename='/tmp/logging/sensors.log',
                            level=logging.INFO)
        self.sensors = [LPS331AP(), ProtoBoard()]  # MPU6050()]
        self._RUNNING = True

    def logging_proc(self, raw=False):
        logging.info("Sensor logging started.")
        while self._RUNNING:
            try:
                for sensor in self.sensors:
                    filename = '/tmp/logging/{}_raw.txt'.format(sensor.device) if raw else \
                        '/tmp/logging/{}.txt'.format(sensor.device)
                    data = {
                        'time': str(datetime.datetime.now()),
                        'data': sensor.get_dict_raw() if raw else sensor.get_dict()
                    }
                    with open(filename, 'a') as log:
                        log.write(json.dumps(data))
                time.sleep(5)
            except Exception as e:
                logging.error(e)
                self._RUNNING = False


if __name__ == '__main__':
    logger = Logger()
    logger.logging_proc()
