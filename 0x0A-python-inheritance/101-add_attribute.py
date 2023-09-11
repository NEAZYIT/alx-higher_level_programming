#!/usr/bin/python3
""" Function that adds a new attribute to an object if it’s possible """


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute will be added.
        attribute: The name of the attribute to add.
        value: The value to assign to the attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.

    """
    if (
        hasattr(obj, '__dict__') or
        hasattr(obj, '__slots__') or
        hasattr(obj, '__class__')
    ):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
