#!/usr/bin/python3
""" Create object from a JSON file """

import json


def load_from_json_file(filename):
    """ Function that creates an Object from a “JSON file” """
    try:
        with open(filename, 'r') as f:
            data = f.read()
            return (json.loads(data))
    except FileNotFoundError:
        return (None)
    except json.JSONDecodeError:
        return (None)
