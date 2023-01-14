#!/usr/bin/python3
"""module 6-base_geometry.py
"""


class BaseGeometry:
    """Represent the Geometry
    Attributes:
    None
    method(public): def area(self): that raises an Exception with
    the message area() is not implemented
    """
    def area(self):
        """Raise an exception"""
        raise Exception("area() is not implemented")
