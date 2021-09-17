import gpiozero
import time
import gpio_assignments


def wait_for_dog():
    if gpio_assignments.actuator_reversal_one.value == 0:
        gpio_assignments.power_supply.off()
        time.sleep(2)
        gpio_assignments.power_supply.on()


def close():
    gpio_assignments.power_supply.on()
    for waiting in range(120):
        gpio_assignments.pir_sensor_one.when_motion = wait_for_dog
        gpio_assignments.pir_sensor_two.when_motion = wait_for_dog
        time.sleep(0.1)
    gpio_assignments.power_supply.off()
    


def open():
    gpio_assignments.actuator_reversal_one.on()
    gpio_assignments.actuator_reversal_two.on()
    gpio_assignments.power_supply.on()
    time.sleep(10)
    gpio_assignments.power_supply.off()
    gpio_assignments.actuator_reversal_one.off()
    gpio_assignments.actuator_reversal_two.off()
    time.sleep(2)
    close()
