#!/usr/bin/python3
""" This module contains a function add_integer(a, b)
    that adds 2 integers.
"""


def add_integer(a, b=98):
    """"Return the addition of a and b.

        Args:
        a(int or float): first parameter
        b(int or float): second parameter

        Return:
        int: sum of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
