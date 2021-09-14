import gpiozero
import time

power_supply = gpiozero.DigitalOutputDevice(7)
actuator_reversal = gpiozero.DigitalOutputDevice(13)
pir_sensor = gpiozero.MotionSensor(18)


def wait_for_dog():
    if actuator_reversal.value == 0 and power_supply.value == 1:
        power_supply.off()
        time.sleep(1)
        pir_sensor.wait_for_no_motion()
        power_supply.on()


def close():
    print("Door closing")
    pir_sensor.wait_for_no_motion()
    power_supply.on()
    for wait_time in range(120):
        if pir_sensor.motion_detected:
            wait_for_dog()
        time.sleep(0.5)


def open():
    print("Door opening")
    actuator_reversal.on()
    power_supply.on()
    time.sleep(10)
    power_supply.off()
    actuator_reversal.off
    time.sleep(3)
    close()
