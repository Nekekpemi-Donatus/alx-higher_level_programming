#!/usr/bin/python3
"""
module Locked_class
"""


class LockedClass:
    """class LockedClass with no class or object attribute,
    that prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name
    """
    __slots__ = ['first_name']

    def __init__(self, first_name=""):
        """Initialize the data"""
        self.first_name = first_name
