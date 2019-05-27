from microbit import *

while True:
    result = accelerometer.get_values()
    print("x, y, z:", result)
    sleep(500)