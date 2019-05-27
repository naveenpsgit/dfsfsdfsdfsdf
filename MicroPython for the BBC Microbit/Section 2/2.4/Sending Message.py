from microbit import *
import radio

while True:
    radio.on() # turns the radio on
    message = "Hello, World!"
    radio.send(message)
    sleep(500) 