from microbit import *
pin1.set_analog_period(5)

while True:
    potValue = pin0.read_analog()
    print(potValue)
    pin1.write_analog(potValue)