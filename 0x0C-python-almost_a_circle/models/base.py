#!/usr/bin/python3
"""Defines a base model class."""
import json


class Base:
    """Base class for managing id attribute in other classes."""

    __nb_objects = 0  # Private class attribute

    def __init__(self, id=None):
        """Initialize the Base instance."""
        if id is not None:
            self.id = id  # Assign id if provided
        else:
            Base.__nb_objects += 1  # Increment the private attribute
            self.id = Base.__nb_objects  # Assign the new value to id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
