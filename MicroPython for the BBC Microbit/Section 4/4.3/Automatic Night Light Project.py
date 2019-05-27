from microbit import *

while True:
    lightLvl = display.read_light_level()
    if lightLvl < 10:
        pin8.write_digital(0)
        sleep(250)
    else:
       pin8.write_digital(1)
       sleep(250)

   