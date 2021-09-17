import gpiozero
import time
import gpio_assignments


def wait_for_dog():
    print("Motion detected")
    if gpio_assignments.sactuator_reversal.value == 0 and gpio_assignments.power_supply.value == 1:
        gpio_assignments.power_supply.off()
        gpio_assignments.pir_sensor_one.wait_for_no_motion()
        gpio_assignments.pir_sensor_two.wait_for_no_motion()
        print("No Motion Detected")
        gpio_assignments.power_supply.on()


def close():
    print("Door closing")
    gpio_assignments.pir_sensor_one.wait_for_no_motion()
    gpio_assignments.power_supply.on()
    time.sleep(60)
    gpio_assignments.power_supply.off()
    print("Door closed")
    


def open():
    print("Door opening")
    gpio_assignments.actuator_reversal.on()
    gpio_assignments.power_supply.on()
    time.sleep(10)
    gpio_assignments.power_supply.off()
    gpio_assignments.actuator_reversal.off()
    time.sleep(3)
    close()
