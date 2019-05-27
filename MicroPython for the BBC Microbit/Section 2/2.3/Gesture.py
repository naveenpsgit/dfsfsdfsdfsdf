from microbit import *

while True:
    ges = accelerometer.current_gesture()
    print(ges)
    sleep(100)
  
  