#!/usr/bin/python3
"""module 1-write_file.py
"""


def write_file(filename="", text=""):
    """Function that writes to a file
    and return the length of the character within.
    Args:
    filename: name of the file to write to
    text: text to write to file.
    """
    with open(filename, 'w', encoding='utf-8') as f_obj:
        file_content = f_obj.write(text)
    return file_content
