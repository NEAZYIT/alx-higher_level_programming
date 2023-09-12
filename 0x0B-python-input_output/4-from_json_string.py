#!/usr/bin/python3

""" From JSON string to Object """
import json


def from_json_string(my_str):
    """
    Deserialize a JSON string to a Python object.

    Args:
        my_str (str): JSON string to be deserialized.

    Returns:
        object: Python data structure representing the JSON object.
    """
    return (json.loads(my_str))
