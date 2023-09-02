#!/usr/bin/env python3


def add_ints(a, b):
    if type(a) is not int or type(b) is not int:
        raise TypeError
    return a + b

def circle_area(d):
    """
    Calculates the area of a circle given a diameter
    """
    import math
    return (math.pi * d**2) / 4
