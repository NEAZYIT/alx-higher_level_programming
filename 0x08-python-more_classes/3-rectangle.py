#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    
    """ WIDTH """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    """ HEIGHT """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    """ Rectangle area """
    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height
    
    """ Rectangle perimeter """
    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    
    """ Returns printable string representation
    of an instance
    """
    def __str__(self):
        """Return a string representation of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a formal string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"
