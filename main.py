""" GPIO pins
7 11 12 13 15 16 18 22 29 31 32 33 35 36 37 38 40
"""

import gpiozero
import door_controller
import gpio_assignments
from signal import pause

gpio_assignments.button_inside.when_pressed = door_controller.open
gpio_assignments.button_outside.when_pressed = door_controller.open
#button_inside.when_held = door_controller.open_forever
#button_outside.when_held = door_controller.open_forever

gpio_assignments.pir_sensor_one.when_motion = door_controller.wait_for_dog
gpio_assignments.pir_sensor_two.when_motion = door_controller.wait_for_dog
            

pause()