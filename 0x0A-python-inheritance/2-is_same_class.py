#!/usr/bin/python3
"""module 2-is_same_class.py
"""


def is_same_class(obj, a_class):
    """Determine if an obj is an instance of a class.
    Args:
         obj:instance of the class a_class
         a_class:class to make instance of
    Return:
         True if obj is instance of a_class otherwise
         False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
