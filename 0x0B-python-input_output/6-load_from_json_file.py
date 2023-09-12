#!/usr/bin/python3
""" Create object from a JSON file """

import json


def load_from_json_file(new_filename):
    """ Function that creates an Object from a “JSON file” """
    with open(new_filename, 'r') as new_file:
        return (json.load(new_file))
