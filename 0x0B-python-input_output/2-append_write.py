#!/usr/bin/python3
"""module 2-append_write.py
"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file
    and returns the number of characters added"""
    with open(filename, 'a', encoding="utf-8") as f_obj:
        text_added = f_obj.write(text)
    return text_added
