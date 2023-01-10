#!/usr/bin/python3
"""module 6-base_geometry.py
"""


class BaseGeometry:
    """Represent the Geometry
    Attributes:
    None
    method(public): def area(self): that raises an Exception with
       the message area() is not implemented
    Public instance method: def integer_validator(self, name, value):
       that validates value
    """
    def area(self):
        """Raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
