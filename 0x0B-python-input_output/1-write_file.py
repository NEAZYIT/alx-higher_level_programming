#!/usr/bin/python3

""" Write to a file """


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8)
    and return the number of characters written."""
    with open(filename, 'w', encoding='utf-8') as file:
        num_characters_written = file.write(text)
    return (num_characters_written)
