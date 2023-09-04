#!/usr/bin/python3
"""Defines a function that prints a name."""


def say_my_name(first_name, last_name=""):
    """
    Print the name in the format "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str): The last name (optional).

    Raises:
        TypeError: If either `first_name` or `last_name` is not a string.

    Example:
        >>> say_my_name("John", "Smith")
        My name is John Smith

        >>> say_my_name("Walter", "White")
        My name is Walter White

        >>> say_my_name("Bob")
        My name is Bob

        >>> say_my_name(12, "White")
        Traceback (most recent call last):
        TypeError: first_name must be a string or last_name must be a string

        >>> say_my_name("John", 42)
        Traceback (most recent call last):
        TypeError: first_name must be a string or last_name must be a string
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
