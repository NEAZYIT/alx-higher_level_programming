#!/usr/bin/python3
""" Base Geometry module """


class BaseGeometry:

    """ Base Geometry """

    def area(self):
        """ Area method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Integer validator method """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ Initialize a Rectangle instance """
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """ Calculate the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ String representation of the rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
