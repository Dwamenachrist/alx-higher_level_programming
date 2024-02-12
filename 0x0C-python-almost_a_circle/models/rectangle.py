#!/usr/bin/python3
from base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width   # Calls the setter with validation
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:  # Validation changed for non-negativity
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:  # Validation changed for non-negativity
            raise ValueError("y must be >= 0")
        self.__y = value
        
    def area(self):
        """Calculates and returns the area of the Rectangle."""
        return self.width * self.height  # Accessing width/height via getters

    def display(self):
        """Prints the Rectangle instance with '#' characters to stdout."""
        for row in range(self.height):  # Iterate through the rows
            for col in range(self.width):  # Iterate through the columns
                print("#", end="")  # Print '#' without a newline
            print()  # Move to the next line after each row

