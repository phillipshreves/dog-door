import gpiozero
import door_controller
import gpio_assignments
from signal import pause


gpio_assignments.button_inside.when_pressed = door_controller.open
             

pause()
