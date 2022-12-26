#!/usr/bin/python3
"""
A python class that represent a square.
"""


class Square:
    """Represent a square.
    Private instance attribute.
    Instantiation with optional size.
    """
    def __init__(self, size=0):
        """Initialize the data."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculate the area of a square.

        Args:
        None

        Return:
        int: current square area.
        """
        return self.__size * self.__size
