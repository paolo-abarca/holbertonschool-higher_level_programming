#!/usr/bin/python3
"""
Python function
that adds 2 integers
return addition
"""


def add_integer(a, b=98):
    """
    Returns an integer:
    the sum of a and b
    """

    result = 0
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    result = int(a) + int(b)

    return result
