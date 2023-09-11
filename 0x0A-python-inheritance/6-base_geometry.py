#!/usr/bin/python3

""" New class Geometry module """


class BaseGeometry:
    """
    BaseGeometry class is the base class for geometry-related operations.

    Methods:
           area(self): Raises an Exception with the message
           'area() is not implemented'.

    """
    def area(self):
        """
        Placeholder method for calculating the area of a geometric shape.


        Raises:
              Exception: Always raises an Exception with the message
              'area() is not implemented'.

        """
        raise Exception("area() is not implemented")
