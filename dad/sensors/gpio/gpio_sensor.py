
class GPIOSensor:

    def __init__(self, pin, setup):
        self.pin = pin
        setup = GPIO.OUT if setup == 'IN' else GPIO.IN
        GPIO.setup(pin, setup)