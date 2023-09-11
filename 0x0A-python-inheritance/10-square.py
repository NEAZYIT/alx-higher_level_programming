#!/usr/bin/python3
""" New class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class square inheriting from rectangle
    """
    def __init__(self, size):
        """
        Initialize a Square instance.
        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Compute and return the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return a string representation of the square.
        Returns:
            str: The string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
