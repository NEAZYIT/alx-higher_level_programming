#!/usr/bin/python3

""" To JSON string """
import json


def to_json_string(my_obj):
    """
    Convert a Python object to its JSON representation as a string.

    Args:
        my_obj: The Python object to be converted to JSON.

    Returns:
        A JSON string representation of the object.
    """
    return (json.dumps(my_obj))
