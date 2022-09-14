"""
This program calculates different things related to circles
"""
# Import the library mth, we need it to obtain the value of PI
import math

def CircleArea(diameter):
    """
    This method calculates the area of a circle, given the circle's diameter
    :param diameter: passed value of the circle's diameter
    :return: the area of the circle
    """
    # The area is radius (square) * pie
    # Let us calculate radius:
    radius = 0.5 * diameter

    # Let us calculate area
    area = radius * math.pi
    return area


def ShowCircleArea():
    """
    This method calculates the area of a circle, by asking use for a diameter
    :return: N/A
    """
    diameter = float(input("What is the diameter of the cirlce?"))
    # The area is radius (square) * pie
    # Let us calculate radius:
    radius = 0.5 * diameter

    # Let us calculate area
    area = radius * math.pi
    print("The area of a circle of {0}".format(diameter), " is {0}".format(area))
