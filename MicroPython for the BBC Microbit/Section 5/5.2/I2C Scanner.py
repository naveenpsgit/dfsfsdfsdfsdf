from microbit import*

i2c.init(freq=100000, sda=pin20, scl=pin19)
AllDevices=i2c.scan()
NumberOfDevices=(len(AllDevices))
print("No of devices inluding accelerometer and compass :", NumberOfDevices)
print("Address of all devices in decimal:", AllDevices)

print("Address of all devices in hexadecimal:") 
for i in range(0,NumberOfDevices,1):
    print(hex(AllDevices[i])) 