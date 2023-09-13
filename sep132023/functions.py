#!/usr/bin/env python3
"""
This module contains the two functions we want to test
"""


def add_ints(a, b):
    """
    Function to add together two integers
    """
    if type(a) is not int or type(b) != int:
        raise TypeError('a and b must be ints')
    return sum((a, b))


def circle_area(d):
    """
    Function to calculate the area of a circle, given the circle's diameter
    """
    import math
    return ((math.pi * d**2) / 4)
