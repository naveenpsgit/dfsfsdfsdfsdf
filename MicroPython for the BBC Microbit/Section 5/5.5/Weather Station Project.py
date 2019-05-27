from microbit import *
import BMP180_lib
import I2CLCD_Microbit_lib


l = I2CLCD_Microbit_lib.LCD1620()
b = BMP180_lib.BMP180()


while True:
    lightLvl = str(display.read_light_level())
    t = str(int(b.Temperature()))
    p = str(int(b.Pressure()))
    a = str(int(b.Altitude()))
    
    l.puts(t,0,0)
    l.puts("C",3,0)
    
    l.puts(p,5,0)
    l.puts("hPa",12,0)
    
    l.puts(a,0,1)
    l.puts("m",3,1)
    
    l.puts(lightLvl,5,1)
    l.puts("LightLvl",8,1)
    
    sleep(500)
    
   
    