"""
This is a facny-ish calculator\
This accepts one user inout, the equation
prints out the output.
"""
import re
# Display a message to user.
def FancyCalculator():

    """
    This is the fancy calculator
    :return:
    """
    print(" Hello user, this is  a fancy calculator")

    # Accept usre input as one equation
    equation = input("Provide me with an equation")
    
    # split up the user input using space and get the first item of the split list
    val1 = equation.split(' ')[0]
    #print(val1)

    # split up the user input using space and get the second item of the split list
    op = equation.split(' ')[1]
    #print(op)

    # split up the user input using space and get the third item of the split list
    val2 = equation.split(' ')[2]

    #print(val2)
    # Now test the operator and printout the result
    if op=='+':
        print(val1+val2)
    elif op=='-':
        print(val1-val2)
    elif op == '/':
        print(val1 / val2)
    else:
        print(val1 * val2)
