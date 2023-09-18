#!/usr/bin/python3
""" Square Module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Override the __str__ method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update attributes with provided arguments or keyword arguments"""
        if args:
            arg_count = len(args)
            if arg_count >= 1:
                self.id = args[0]
            if arg_count >= 2:
                self.size = args[1]
            if arg_count >= 3:
                self.x = args[2]
            if arg_count >= 4:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Return a dictionary representation of the Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
