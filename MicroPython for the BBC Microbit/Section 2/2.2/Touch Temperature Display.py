from microbit import *

while True:
    if pin0.is_touched():
        display.scroll(temperature())
    elif pin1.is_touched():
        tempF = ((9/5)*temperature()) + 32
        display.scroll(tempF)