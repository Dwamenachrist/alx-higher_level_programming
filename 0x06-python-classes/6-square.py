#!/usr/bin/python3
class Square:
    """Represents a square with size, validation, area calculation, printing, and positioning."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size  
        self.position = position  

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(n, int) and n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' characters, respecting its position."""
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):  # Print empty lines for vertical position
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")  # Horizontal spaces 
                print("#" * self.__size)                