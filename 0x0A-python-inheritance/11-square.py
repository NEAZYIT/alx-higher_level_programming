#!/usr/bin/python3
""" New class """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Class square inherist from rectangle """
    def __init__(self, size: int) -> None:
        self.__size = size
        super().__init__(self._validate_size(size), self._validate_size(size))

    @staticmethod
    def _validate_size(size: int) -> int:
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size <= 0:
            raise ValueError("Size must be a positive integer")
        return size

    def __str__(self) -> str:
        return f"[Square] {self.__size}/{self.__size}"
