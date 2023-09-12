#!/usr/bin/python3

""" Append to a file """


def append_write(filename="", text=""):
    """Append a string to the end of a text file (UTF8)
    and return the number of characters added."""
    with open(filename, 'a', encoding='utf-8') as file:
        num_characters_added = file.write(text)
    return (num_characters_added)
