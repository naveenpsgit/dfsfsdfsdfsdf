from microbit import *

while True:
    if button_a.is_pressed():
        display.scroll(temperature())
    elif button_b.is_pressed():
        tempF = ((9/5)*temperature()) + 32
        display.scroll(tempF)