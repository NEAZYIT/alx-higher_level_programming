#!/usr/bin/python3
"""Module containing the Square class"""


class Square:
    """The Square class"""

    def __init__(self, size: int = 0, position: tuple[int, int] = (0, 0)):
        """Initializing an instance of Square.

        Args:
            size (int): The size of the Square instance. Default value is 0.
            position (tuple[int, int]): x, y coordinate offset when printing
            the square.
        """
        self.size = size
        self.position = position

    def __str__(self) -> str:
        """Returns a string representation of the square made with hashtags.

        Uses 'size' to determine the size of the square and
        'position' to offset the printing.

        Returns:
            str: A string representing the square made of hashtags.
        """
        square_str = ""
        if self.size != 0:
            for _ in range(self.position[1]):
                square_str += '\n'
            for _ in range(self.size):
                square_str += ' ' * self.position[0] + '#' * self.size
                if _ != self.size - 1:
                    square_str += '\n'
        return square_str

    @property
    def size(self) -> int:
        """int: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self) -> tuple[int, int]:
        """tuple[int, int]: The x, y coordinate offset of the square."""
        return self.__position

    @position.setter
    def position(self, value: tuple[int, int]) -> None:
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self) -> int:
        """Returns the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self) -> None:
        """Prints the square using hashtags.

        The printing starts from the specified position
        and the size of the square.
        """
        if self.size != 0:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
        else:
            print()
