#!/usr/bin/python3
"""
A python class tha represents a class.
"""


class Square:
    """Represent a square.
    Private instance attributes: size
       -property def size(self)
       -property setter def size(self, value)
    Instantiation with optional size.
    Public instance method: def area(self).
    """
    def __init__(self, size=0):
        """Initialize the data."""
        self.__size = size

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size to value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculate the area of a square."""
        return self.__size ** 2
