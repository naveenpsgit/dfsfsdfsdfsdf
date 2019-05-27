from microbit import *
import music
tune = ["C", "D", "E", "R", "F", "G"]

while True:
    if button_a.is_pressed():
      music.play(tune)