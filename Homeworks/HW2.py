"""
Python file for HW #2. Password checker
This file has some methods which validate different criteria of a given password.
"""

def ValidLength(password):
    """
    A method which validates whether a given password is at least 8 chars long
    :param password: Password to check, passed from main
    :return: True if length is 8 chars or more, otherwise, False
    """
    # Check if length of password is less than 8
    if len(password) < 8:
        # Return false if password is less than 8 chars long
        return False
    # Return True otherwise
    return True


def HasNumber(password):
    """
    A method which validates whether a given password has at least one number
    :param password: Password to check, passed from main
    :return: True if password has at least one number, otherwise, False
    """
    # if no digit is found, then return False
    if not any(char.isdigit() for char in password):
        return False
    return True

    # If no symbols found, return False
def HasSymbol(password):
    """
    A method which validates whether a given password has at least one symbol
    :param password: Password to check, passed from main
    :return: True if one symbol is in password, otherwise False
    """
    # Define a list of symbols
    symbols = ['!', '@', '#', '$', '%']
    if not any(char in symbols for char in password):
        return False
    return True
