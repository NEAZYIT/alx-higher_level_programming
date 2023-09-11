#!/usr/bin/python3
""" New class """


class MyInt(int):
    """MyInt class that inherits from int but inverts == and != operators."""

    def __eq__(self, other):
        """Override == (equals) operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != (not equals) operator."""
        return super().__eq__(other)
