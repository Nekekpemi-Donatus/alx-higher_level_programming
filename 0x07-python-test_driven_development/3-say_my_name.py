#!/usr/bin/python3
"""
Module 3-say_my_name
"""


def say_my_name(first_name, last_name=""):
    """Print My name is <first name> <last name>.

       Args:
       first_name(string): first name parameter
       last_name(string):  last name parameter

       Return:
       string: sentence
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
