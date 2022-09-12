"""
A simple calculator program that accepts 3 inputs
Input1 is the first value
Input2 is the operation
Input3 is the last value
"""

import re
# Display a message to user.
print(" Hello user, this is  a simple calculator")

# Ask user for input and store it in val1 as an integer, value with no decimal places
val1 = int(input("Provide the first input"))


# Ask user for operation and store it in op. No cast is needed here, the operation is treated as string
op = input("Provide the operation input")
#print(op)

# Ask user for input and store it in val2 as an integer, value with no decimal places

val2 = int(input("Provide the last input"))

#print(val2)
# Now test the operator and printout the result
if op == '+':
    print(val1+val2)
elif op == '-':
    print(val1-val2)
elif op == '/':
    print(val1 / val2)
else:
    print(val1 * val2)
