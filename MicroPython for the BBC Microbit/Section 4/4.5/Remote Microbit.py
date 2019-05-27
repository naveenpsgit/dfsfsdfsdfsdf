from microbit import *
import radio

radio.on()

while True:
    if button_a.is_pressed():
        radio.send("A")
        sleep(250)
    if button_b.is_pressed():
        radio.send("B")
        sleep(250)
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send("Reset")
        sleep(250)

    