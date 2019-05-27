from microbit import *

while True:
    LDRvalue = pin0.read_analog()
    PIRvalue = pin5.read_digital()
    if LDRvalue < 800:
        if PIRvalue == 1:
            display.show(Image.NO)
        else:
            display.clear()
    else:
        display.clear()
    sleep(250)
    