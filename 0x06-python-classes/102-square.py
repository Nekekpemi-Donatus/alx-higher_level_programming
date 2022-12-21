#!/usr/bin/python3
"""
A python class that defines a square.
"""


class Square:
    """Representnt a square.
    Private instance attribute: size:
     -property def size(self): to retrieve it
     -property setter def size(self, value): to set it:
    Instantiation with size: def __init__(self, size=0):
    Public instance method: def area(self):
    """
    def __init__(self, size=0):
        """Initialize the data."""
        self.__size = size

    def __eq__(self, other):
        """Equal."""
        if hasattr(other, 'size'):
            return self.__size == other.__size
        return self.__size == other

    def __ne__(self, other):
        """Not equal."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Less than."""
        if hasattr(other, 'size'):
            return self.__size < other.__size
        return self.__size < other

    def __le__(self, other):
        """Less than or equal."""
        if hasattr(other, 'size'):
            return self.__size <= other.__size
        return self.__size <= other

    @property
    def size(self):
        """return the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size to value."""
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

        def area(self):
            """calculate the area of the square."""
            return self.__size ** 2
