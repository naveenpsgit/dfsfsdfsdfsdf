from microbit import *

while True:
    potValue = pin0.read_analog()
    print(potValue)
    sleep(500)
    