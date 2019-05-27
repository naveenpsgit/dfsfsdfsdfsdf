from microbit import *
import radio
radio.on()

while True: 
    incoming = radio.receive()
    if incoming is not None:
        display.scroll(incoming)
    sleep(500)
    