import gpiozero
import door_controller
import gpio_assignments
from signal import pause


gpio_assignments.pir_sensor_one.when_motion = door_controller.wait_for_dog
gpio_assignments.pir_sensor_two.when_motion = door_controller.wait_for_dog
            

pause()