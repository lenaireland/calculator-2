"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import add

def calculator():

    while True:

        user_input = input(" > ")
        tokens = user_input.split(" ")
        tokens[1] = float(tokens[1])
        tokens[2] = float(tokens[2])

        if tokens[0] == "q":
            # quit()
            return
        else:
            if tokens[0] == "+":
                print(add(tokens[1], tokens[2]))



calculator()
# Your code goes here
