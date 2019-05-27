from microbit import *

def input2int(inputString):
    output = int(input(inputString))
    return output
    
while True:
    x = input2int("Enter the first number:")
    y = input2int("Enter the second number:")
    operation = input("Add, Subtract, Divide or Multiply? ")
    if operation == "Add":
        print(x+y)
    if operation == "Subtract":
        if x>y: 
            print(x-y)
        else:
            print(y-x)
    if operation == "Divide":
        print(x/y)
    if operation == "Multiply":
        print(x*y)