#!/usr/bin/python3
class Square:
    """A class representing a square with size attribute, validation, area calculation, and printing."""

    def __init__(self, size=0):
        self.size = size  # Calls the setter method

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2 

    def my_print(self):
        """Prints a representation of the square to stdout using '#' characters.
        """
        if self.__size == 0:
            print()  # Prints an empty line if size is 0
        else:
            for i in range(self.__size):  # Repeat for 'size' rows
                print("#" * self.__size)  # Print a row of '#' symbols 
