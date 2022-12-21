#!/usr/bin/python3
"""
A square class with a private instance size
"""


class Square:
    """Represent a square.
    Private instance attribute: size.
    Instantiation with size (no type/value verification).
    """

    def __init__(self, size):
        """Initialize the attributes."""
        self.__size = size
