import gpiozero
import door_controller
import gpio_assignments
from signal import pause


#gpio_assignments.pir_sensor_one.when_motion = door_controller.wait_for_dog
#gpio_assignments.pir_sensor_two.when_motion = door_controller.wait_for_dog

gpio_assignments.button_inside.when_pressed = door_controller.open
gpio_assignments.button_outside.when_pressed = door_controller.open
             

pause()