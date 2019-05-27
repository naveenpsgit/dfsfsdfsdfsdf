from microbit import *
import radio

radio.on()
while True:
    incoming = radio.receive()
    if incoming == "A":
        pin8.write_digital(0)
        sleep(250)
    if incoming == "B":
        pin12.write_digital(0)
        sleep(250)
    if incoming == "Reset":
        pin8.write_digital(1)
        pin12.write_digital(1)
        sleep(250)