#!/usr/bin/python3
""" New class """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Class square inheriting from rectangle """

    def __init__(self, size):
        """ Initializes a Square instance """
        super().__init__(size, size)
        self.size = size

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value
