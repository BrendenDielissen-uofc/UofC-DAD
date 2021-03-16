# DAD Packages

# Python Packages
import datetime
import time
import daemon


class LoggerDaemon:

    def __init__(self):
        self._RUNNING = True

    def kill(self):
        # kills the logging daemon
        pass

    def logging_proc(self):
        while self._RUNNING:
            # do logging procedure
            # if errors, stop running, log to logger
            with open('/mnt/sd/logging/sensors.txt', 'a') as log:
                log.write('{}: whatever needs to be written'.format(datetime.datetime.now()))
            time.sleep(5)


with daemon.DaemonContext():
    loggerd = LoggerDaemon()
    loggerd.logging_proc()
