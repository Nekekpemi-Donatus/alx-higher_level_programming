#!/usr/bin/python3
"""module 3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """Determine if obj is an instance of a_class
    Args:
       obj: instance of a_class
       a_class: class to make instance of
    Return:
      True if obj is instance of a_class other wise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
