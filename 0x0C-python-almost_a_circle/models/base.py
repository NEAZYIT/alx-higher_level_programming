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

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a JSON file."""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_dicts))
