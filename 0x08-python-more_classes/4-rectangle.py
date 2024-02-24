#!/usr/bin/python3
class Rectangle:
    """Represents a rectangle with width, height, and string representations."""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance with optional width and height (default 0)."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the value of the private 'width' attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of the private 'width' attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the value of the private 'height' attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of the private 'height' attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the rectangle's perimeter, accounting for 0 dimensions."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a 'user-friendly' printable string representation of a rectangle using '#'. """
        output = ""
        if self.__width == 0 or self.__height == 0:
            return output
        for _ in range(self.__height):
            output += "#" * self.__width + "\n"
        return output[:-1]  # Remove the trailing newline 

    def __repr__(self):
        """Returns a developer-focused string representation allowing object recreation."""
        class_name = self.__class__.__name__
        return f"{class_name}({self.__width}, {self.__height})" 
