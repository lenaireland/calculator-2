"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculator():

    while True:

        user_input = input(" > ")
        tokens = user_input.split(" ")

        new_tokens = tokens_to_floats(tokens)

            # new_tokens.append(float(item))
        # if len(tokens) > 1:
        #     tokens[1] = float(tokens[1])
        # if len(tokens) > 2:
        #     tokens[2] = float(tokens[2])

        if new_tokens != False:

            if tokens[0] == "q":
                quit()
                # return
            else:
                if tokens[0] == "+":
                    print(add(new_tokens))
                elif tokens[0] == "-":
                    print(subtract(new_tokens))
                elif tokens[0] == "*":
                    print(multiply(new_tokens[0], new_tokens[1]))
                elif tokens[0] == "/":
                    print(divide(new_tokens[0], new_tokens[1]))
                elif tokens[0] == "square":
                    print(square(new_tokens[0]))
                elif tokens[0] == "cube":
                    print(cube(new_tokens[0]))
                elif tokens[0] == "pow":
                    print(power(new_tokens[0], new_tokens[1]))
                elif tokens[0] == "mod":
                    print(mod(new_tokens[0], new_tokens[1]))
                else:
                    print("That command does not exist")


def tokens_to_floats(tokens):
    new_tokens = []
    for item in tokens[1:]:
        try:
            new_tokens.append(float(item))
        except ValueError:
            print("Error - expected a number!")
            return False
    return new_tokens

calculator()
# Your code goes here
