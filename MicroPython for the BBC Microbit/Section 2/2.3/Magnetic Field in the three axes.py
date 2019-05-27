from microbit import *

while True:
    x = compass.get_x()
    y = compass.get_y()
    z = compass.get_z()
    print("x reading: ", x, ", y reading: ", y, "z reading: ", z)
    sleep(500)