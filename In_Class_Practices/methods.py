def firstMethod():
    """
    This method prints a simple message
    :return:
    """
    print("You are in the first method")


def secondMethod():
    """
    This method returns a message
    :return: Message confirming something
    """
    message = "You are in the second method"
    return message


def thirdMethod(data):
    """
    This method accepts a word and reverse it
    :param data: The word to reverse. Comes from the outside.
    :return: The reversed data
    """
    reversedData = data[::-1]
    return reversedData


def fourthMethod(cat):
    """
    This method prints out the name of the cat passed
    :param cat: The cat name
    :return: N/A
    """
    print("You provided me with a kittie name ", format(cat))
