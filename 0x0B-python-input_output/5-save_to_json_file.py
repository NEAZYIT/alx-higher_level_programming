#!/usr/bin/python3
""" Save Object to a file """
import json


def save_to_json_file(my_obj, filename):
    """
    Serialize an object to JSON format and save it to a text file.

    Args:
    - my_obj: The Python object to be serialized.
    - filename: The name of the file to save the JSON data.

    Returns:
    - None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
