#!/usr/bin/python3
"""module 9-student.py
Represent a student
"""


class Student:
    """Class that defines a student.
    Public attributes:
        - first_name
        - last_name
        - age
    Public method to_json().
    """
    def __init__(self, first_name, last_name, age):
        """Initialize the student Instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation
        of a Student instance.
        Returns the dictionary representation of the instance
        """
        return self.__dict__
