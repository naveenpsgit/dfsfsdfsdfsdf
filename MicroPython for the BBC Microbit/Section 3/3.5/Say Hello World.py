from microbit import *
import speech

while True:
    if button_a.is_pressed():
        speech.say("Hello World", speed=120, pitch=100, throat=100, mouth=200)
        pin16.write_digital