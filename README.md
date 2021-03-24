# UofC-DAD
Repository for Project DAD related scripts/packages and more.

DAD - FSM
- The FSM module within the DAD package contains the state machine implementations that are constantly running in background Cron jobs
on the DAD's BeagleBone Black Enhanced.
- "dad_fsm.py" is the base class that implements the state machine loop within its "run" method, which is described simply in
pseudo-code below: 

    while running:
  
      fetch_input -> handle_transitions -> handle_state action 
    
    cleanup
  
- Both the InternetFSM and PowerFSM, defined in "internet_fsm.py" and "power_fsm.py" respectively, inherit the functionality provided from the DADFSM object defined in "dad_fsm.py", 
but define their own specific states, state transitions, and handling as required. For more detail on the specific purposes of both the
Internet and Power FSM's, please see the "internet_fsm.py" and "power_fsm.py" files for more descriptive documentation.
- The LedFSM, defined in "led_fsm.py", defines a simple state machine for tracking the state of individual LED's which are controlled by the 
BeagleBone's GPIO pins. Essentially, this machine provides a simple interface for interacting with the LED's such that they are always in a known
state. 

DAD - Logging
- The Logger class as defined in the "logger.py" file is a simple class that allows both raw and processed sensor logging from any class that implements the 
Sensor interface as defined in "dad.sensors.sensor.py"
- The intended use for this class is to constantly log the data captured from the DAD's own sensors (i.e. internal enclosure temperature, external temperature, voltages from the vehicle, battery and vbus,
as well as gyroscope and accelerometer data) in a background Cron job as soon as the GPIO pins and IIO devices are online from reboot on the BeagleBone.
- Raw and processed sensor logging options are both provided to allow flexibility of where the sensor data will be processed, i.e. will the sensor data be processed
on the BeagleBone as it is captured, or will it be processed once it is transferred to a remote server. 

DAD - Sensors
- The Sensor module within the DAD package is intended to provide an easy to use interface for the various onboard sensors available to a DAD device.
- The GPIO submodule defines the functionality of any GPIO sensors which were provided by Team DAD on the Protoboard Cape that was defined specifically for the DAD device.
- The IIO submodule defines the functionality of the IIO devices which came installed on the BeagleBone Black Enhanced.
- The Sensor interface, within "sensor.py", is intended to describe a format that the Logger, within "dad.logging.logger.py", will expect to log, and thus allows
future engineers to easily add/customize/remove sensor functionality as necessary. 

