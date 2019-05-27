from microbit import *

while True:
    x = int(input("Enter the first number:"))
    y = int(input("Enter the second number:"))
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