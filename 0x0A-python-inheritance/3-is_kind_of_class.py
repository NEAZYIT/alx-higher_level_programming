#!/usr/bin/python3

""" Same class or inherit from """


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherits from, a specified class.


    Args:
        obj: The object to be checked.
        a_class: The class to check against.


    Returns:
           True if obj is an instance of a_class or inherits from it;
           False otherwise.

    """
    return isinstance(obj, a_class)
