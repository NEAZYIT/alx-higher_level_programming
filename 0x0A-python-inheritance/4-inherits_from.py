#!/usr/bin/python3

"""Module for inherits_from function."""

def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherits from a_class.

    Agrs:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
           True if obj is an instance of a class that inherits from a_class,
           False otherwise.

    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
