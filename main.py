""" GPIO pins
7 11 12 13 15 16 18 22 29 31 32 33 35 36 37 38 40
"""

import gpiozero
import door_controller
from signal import pause


button_inside = gpiozero.Button(17)
button_outside = gpiozero.Button(18)
pir_sensor_one = gpiozero.MotionSensor(23)
pir_sensor_two = gpiozero.MotionSensor(24)


button_inside.when_pressed = door_controller.open
button_outside.when_pressed = door_controller.open
#button_inside.when_held = door_controller.open_forever
#button_outside.when_held = door_controller.open_forever

pir_sensor_one.motion_detected = door_controller.wait_for_dog
pir_sensor_two.motion_detected = door_controller.wait_for_dog
            

pause()
