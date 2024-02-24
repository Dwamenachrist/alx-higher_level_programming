#!/usr/bin/python3
"""Provides a blueprint for creating rectangle objects."""

class Rectangle:
    """Models a geometrical rectangle.

    Attributes:
        number_of_instances (int): Tracks the total count of Rectangle objects created.
        print_symbol (any): The character used to visually represent the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Creates a new Rectangle instance.

        Args:
            width (int): The desired width of the rectangle.
            height (int): The desired height of the rectangle.
        """
        Rectangle.number_of_instances += 1  # Increment instance counter
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width, ensuring it's an integer and non-negative."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height, ensuring it's an integer and non-negative."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the rectangle's area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the rectangle's perimeter.
        
        Note: Returns 0 if either width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height) 

    def __str__(self):
        """Provides a printable string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([self.print_symbol * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Provides a developer-friendly representation for creating new instances."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when a Rectangle object is deleted and adjusts instance count."""
        Rectangle.number_of_instances -= 1 
        print("Bye rectangle...")
