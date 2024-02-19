#!/usr/bin/python3
class Square:
    """A class representing a square with a private size attribute."""
    def __init__(self, size):
        """Initializes the Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
