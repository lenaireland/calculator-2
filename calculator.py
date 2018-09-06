"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculator():

    while True:

        user_input = input(" > ")
        tokens = user_input.split(" ")
        if len(tokens) > 1:
            tokens[1] = float(tokens[1])
        if len(tokens) > 2:
            tokens[2] = float(tokens[2])

        if tokens[0] == "q":
            # quit()
            return
        else:
            if tokens[0] == "+":
                print(add(tokens[1], tokens[2]))
            elif tokens[0] == "-":
                print(subtract(tokens[1], tokens[2]))
            elif tokens[0] == "*":
                print(multiply(tokens[1], tokens[2]))
            elif tokens[0] == "/":
                print(divide(tokens[1], tokens[2]))
            elif tokens[0] == "square":
                print(square(tokens[1]))
            elif tokens[0] == "cube":
                print(cube(tokens[1]))
            elif tokens[0] == "pow":
                print(power(tokens[1], tokens[2]))
            elif tokens[0] == "mod":
                print(mod(tokens[1], tokens[2]))

calculator()
# Your code goes here
