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
