#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set from a dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file and return a list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**obj_dict) for obj_dict in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of instances to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([
                        obj.id,
                        obj.width,
                        obj.height,
                        obj.x,
                        obj.y
                        ])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Load instances from a CSV file and return a list of instances."""
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    row = [int(val) for val in row]
                    if cls.__name__ == "Rectangle":
                        instance = cls(row[1], row[2], row[3], row[4], row[0])
                    elif cls.__name__ == "Square":
                        instance = cls(row[1], row[2], row[3], row[0])
                    instances.append(instance)
            return instances
        except FileNotFoundError:
            return []
