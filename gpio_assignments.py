import gpiozero


power_supply = gpiozero.DigitalOutputDevice(25)
actuator_reversal = gpiozero.DigitalOutputDevice(18)
pir_sensor = gpiozero.MotionSensor(23)
button_inside = gpiozero.Button(24)
