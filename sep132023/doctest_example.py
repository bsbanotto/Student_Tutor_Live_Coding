#!/usr/bin/env python3
"""
This is the "example" module.

The example module supplies one function, make_int_list().  For example,

>>> make_int_list(5, 10)
[5, 6, 7, 8, 9, 10]
"""

def make_int_list(start, end):
    """Returns a list of integers from start to end, inclusive.

    Make sure it returns a list
    >>> type(make_int_list(2, 6))
    <class 'list'>

    Test for normal usage, starting at 0
    >>> make_int_list(0, 5)
    [0, 1, 2, 3, 4, 5]

    Make sure it works backwards
    >>> make_int_list(9, 4)
    [9, 8, 7, 6, 5, 4]

    Make sure it'll go from negative to positive
    >>> make_int_list(-3, 2)
    [-3, -2, -1, 0, 1, 2]

    Make sure it -won't create a list of floats
    >>> make_int_list(0.6, 4.1)
    Traceback (most recent call last):
    ...
    ValueError: start and end must be exact integer
    """
    if type(start) is not int or type(end) is not int:
        raise ValueError('start and end must be exact integer')
    if end < start:
        return [num for num in range(start, end - 1, -1)]
    else:
        return [num for num in range(start, end + 1)]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
