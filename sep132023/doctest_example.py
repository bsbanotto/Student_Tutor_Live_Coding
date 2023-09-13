#!/usr/bin/env python3
"""
Module to create a list of integers inclusive of start and end

# Create a test here to show doc tests can be at the module level
>>> make_int_list(4, 7)
[4, 5, 6, 7]
"""

def make_int_list(start, end):
    """Returns a list of integers from start to end, inclusive.

    # Create a test here to ensure we are returning a list
    >>> type(make_int_list(1, 6))
    <class 'list'>

    # Create a test here to make sure it works backwards
    >>> make_int_list(6, 2)
    [6, 5, 4, 3, 2]

    # Create a test here to make sure it must me integer
    >>> make_int_list(4.6, 9.3)
    Traceback (most recent call last):
        ...
    TypeError: start and end must be integer
    """
    # Do the actual work of the function here
    if start < end:
        # Do something
        try:
            return [num for num in range(start, end + 1)]
        except:
            raise TypeError("start and end must be integer")
    else:
        # Do something else
        try:
            return [num for num in range(start, end - 1, -1)]
        except:
            raise TypeError("start and end must be integer")
        
    # try:
    #     return [num for num in range(start, end + 1)]
    # except:
    #     raise TypeError("start and end must be integer")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
