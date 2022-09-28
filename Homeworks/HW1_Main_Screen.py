"""
MJ Ahmad
HW1 main screen.
"""

import In_Class_Activities as Activities




def main():

    """
    Main method to call and run Homework #1.
    :return: N/A
    """

    # Ask user which program to run
    response = int(input("Which program do you want to run? (1) Password Checker, (2) Simple Calculator, (3) Fancy Calculator \n Provide a number or a name"))

    # If stetement to detemine which program to call based on user input

    if response == 1 or response == "Password Checker":
        # Accept password from user
        password = str(input("Please enter a password: "))
        print(CorrectPasswordResponse(str(input("Please enter a password: "))))


# Required to run main method
if __name__ == "__main__":
    main()
