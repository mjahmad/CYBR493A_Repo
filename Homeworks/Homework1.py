"""
MJ Ahmad
Class for Homework #1, the password checker part

"""
# import modules
import re


def CorrectPasswordResponse(password):
    """
    This verifies whether a provided password is valid or not
    :param password: Argument passed from the main method. Type string
    :return: Ture if password is valid, False otherwise
    """
    # Define a list of symbols
    symbols = ['!', '@', '#', '$', '%']

    # If the password's length is < 8, or has no digit or has no symbols, then return False
    if len(password) < 8:
        print("Length")
        return False
    # if no digit is found, then return False
    elif not any(char.isdigit() for char in password):
        print("Number")
        return False
    # If no symbols found, return False
    elif not any(char in symbols for char in password):
        print("Symbols")
        return False
    # Return True if all IF statements fail (do not return anything)
    return True
