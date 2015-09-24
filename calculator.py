"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

def calculator():
    action = True
 

    while action != "q":
        token=raw_input(">").split(" ")
        action = token[0]
        num1 = int(token[1])
        
        if len(token)>=3:
            num2 = int(token[2]) 

        if action == "+":
            print add(num1,num2)


        if action == "-":
            print subtract(num1,num2)

        if action == "*":
            print multiply(num1,num2)

        if action == "/":
            print divide(num1,num2)

        if action == "square":
            print square(num1)

        if action == "cube":
            print cube(num1)

        if action == "pow":
            print power(num1, num2)

        if action == "mod":
            print mod(num1, num2)

        
    return


calculator()