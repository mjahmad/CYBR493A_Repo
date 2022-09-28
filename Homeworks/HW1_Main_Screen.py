"""
MJ Ahmad
HW1 main screen.
"""

import In_Class_Activities as Activities
import In_Class_Practices
from Homeworks import Homework1


def main():
    """
    Main method to call and run Homework #1.
    :return: N/A
    """

    # Ask user which program to run
    response = int(input(
        "Which program do you want to run? (1) Password Checker, (2) Simple Calculator, (3) Fancy Calculator \n "
        "Provide a number or a name"))

    # If statement to determine which program to call based on user input

    if response == 1 or response == "Password Checker":
        # Accept password from user
        password = (input("Please enter a password: "))
        if Homework1.CorrectPasswordResponse(password):
            print("Valid Password")
        else:
            print("Invalid password")
    elif response == 2 or response == "Simple Calculator":
        In_Class_Practices.SimpleCalculator.SimpleCalculator()
    elif response == 3 or response == "Fancy Calculator":
        In_Class_Practices.FancyCalculator.FancyCalculator()


# Required to run main method
if __name__ == "__main__":
    main()
