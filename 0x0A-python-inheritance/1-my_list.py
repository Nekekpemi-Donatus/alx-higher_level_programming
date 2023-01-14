#!/usr/bin/python3
"""Module 1-my_list.py
"""


class MyList(list):
    """class MyList inherits from list"""

    def print_sorted(self):
        """Print the list in ascending sort."""
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
