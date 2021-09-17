import gpiozero


power_supply = gpiozero.DigitalOutputDevice(4)
actuator_reversal_one = gpiozero.DigitalOutputDevice(17)
actuator_reversal_two = gpiozero.DigitalOutputDevice(27)
pir_sensor_one = gpiozero.MotionSensor(23)
pir_sensor_two = gpiozero.MotionSensor(24)
button_inside = gpiozero.Button(25)
button_outside = gpiozero.Button(18)