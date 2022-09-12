"""
This program displays the sum of two variables provided by the user
"""

# declare first variable with initial value 0
number1 = 0

# declare second variable with initial value 6
number2 = 0

number1 = int(input("What is the value of the first value? "))

number2 = int(input("What is the value of the second value? "))

# print the sum of the values
print("The sum of the two provided values {0}".format(number1),"and {0}".format(number2)," is {0}".format(number1+number2))

# another way to display the same message
print("The sum of the two provided values {0} and {1} is {2}".format(number1,number2,number1+number2))