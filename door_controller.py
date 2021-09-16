import gpiozero
import time

power_supply = gpiozero.DigitalOutputDevice(4)
actuator_reversal = gpiozero.DigitalOutputDevice(27)
pir_sensor_one = gpiozero.MotionSensor(23)
pir_sensor_two = gpiozero.MotionSensor(24)


def wait_for_dog():
    print("Motion detected")
    if actuator_reversal.value == 0 and power_supply.value == 1:
        power_supply.off()
        pir_sensor_one.wait_for_no_motion()
        pir_sensor_two.wait_for_no_motion()
        print("No Motion Detected")
        power_supply.on()


def close():
    print("Door closing")
    pir_sensor_one.wait_for_no_motion()
    power_supply.on()
    time.sleep(60)
    power_supply.off()
    print("Door closed")
    


def open():
    print("Door opening")
    actuator_reversal.on()
    power_supply.on()
    time.sleep(10)
    power_supply.off()
    actuator_reversal.off()
    time.sleep(3)
    close()
