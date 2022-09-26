"""
Functions are also known as method.

"""


def SimpleCalculator():
    """
    Example of a non-return method of our simple calculator
    :return:
    """
    print(" Hello user, this is  a simple calculator")

    # Ask user for input and store it in val1 as an integer, value with no decimal places
    val1 = int(input("Provide the first input"))

    # Ask user for operation and store it in op. No cast is needed here, the operation is treated as string
    op = input("Provide the operation input")
    # print(op)

    # Ask user for input and store it in val2 as an integer, value with no decimal places

    val2 = int(input("Provide the last input"))

    # print(val2)
    # Now test the operator and printout the result
    if op == '+':
        print(val1 + val2)
    elif op == '-':
        print(val1 - val2)
    elif op == '/':
        print(val1 / val2)
    else:
        print(val1 * val2)


def FancyCalculator():
    """
     Example of a non-return method of our fancy calculator
    :return:
    """
    # Display a message to user.
    print(" Hello user, this is  a fancy calculator")

    # Accept usre input as one equation
    equation = input("Provide me with an equation")

    # split up the user input using space and get the first item of the split list
    val1 = equation.split(' ')[0]
    # print(val1)

    # split up the user input using space and get the second item of the split list
    op = equation.split(' ')[1]
    # print(op)

    # split up the user input using space and get the third item of the split list
    val2 = equation.split(' ')[2]

    # print(val2)
    # Now test the operator and printout the result
    if op == '+':
        print(val1 + val2)
    elif op == '-':
        print(val1 - val2)
    elif op == '/':
        print(val1 / val2)
    else:
        print(val1 * val2)


def SimpleCalculatorWithRetun() -> int:
    """
       Example of a non-return method of our simple calculator
       :return:
       """
    print(" Hello user, this is  a simple calculator")

    # Ask user for input and store it in val1 as an integer, value with no decimal places
    val1 = int(input("Provide the first input"))

    # Ask user for operation and store it in op. No cast is needed here, the operation is treated as string
    op = input("Provide the operation input")
    # print(op)

    # Ask user for input and store it in val2 as an integer, value with no decimal places

    val2 = int(input("Provide the last input"))

    # print(val2)
    # Now test the operator and RETURN the result
    if op == '+':
        return val1 + val2
    elif op == '-':
        return val1 - val2
    elif op == '/':
        return val1 / val2
    else:
        return val1 * val2


def CompareTwoNumbers():
    # declare first variable with initial value 12
    number1 = 6

    # declare second variable with initial value 6
    number2 = 4

    # compare the two
    if number1 > number2:
        print("The value of the first number {0} ".format(number1),
              "is greater than the value of the second number {0}".format(number2))

    elif number1 < number2:
        print("The value of the first number {0} ".format(number1),
              "is less than the value of the second number {0}".format(number2))

    else:
        print("Values are equal")
        # print("The value of the second number is less than the value of the first number")
