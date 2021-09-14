""" GPIO pins
7 11 12 13 15 16 18 22 29 31 32 33 35 36 37 38 40
"""

import gpiozero
import door_controller
from signal import pause


button_inside = gpiozero.Button(11)
button_outside = gpiozero.Button(12)


button_inside.when_pressed = door_controller.open
button_outside.when_pressed = door_controller.open
button_inside.when_held = door_controller.open_forever
button_outside.when_held = door_controller.open_forever


pause()