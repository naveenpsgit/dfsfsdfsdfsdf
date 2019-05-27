from microbit import *
import speech

while True:
    lightLvl = display.read_light_level()
    PIR = pin12.read_digital()
    if lightLvl < 10:
        pin8.write_digital(0)
        if PIR == 1:
            speech.say("Stop, Do not Enter")
        sleep(250)
    else:
       pin8.write_digital(1)
       sleep(250)

    
    
   
    