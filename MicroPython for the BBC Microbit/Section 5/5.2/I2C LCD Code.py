from microbit import *
import I2CLCD_Microbit_lib

l = I2CLCD_Microbit_lib.LCD1620()
l.puts("Hello, My name is Naveen PS")

while True:
    l.setcmd(0x18)
    sleep(250)