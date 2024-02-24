#!/usr/bin/python3
"""Provides the foundation for creating rectangle objects."""

class Rectangle:
    """Models the properties and behaviors of a rectangular shape.

    Attributes:
        number_of_instances (int): Keeps track of how many Rectangle objects exist.
        print_symbol (any):  The character used to visually represent the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle object.

        Args:
            width (int): The desired width of the rectangle.
            height (int): The desired height of the rectangle.
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets or sets the rectangle's width."""
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
        """Gets or sets the rectangle's height."""
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
        """Calculates and returns the rectangle's total internal space."""
        return self.__width * self.__height

    def perimeter(self):
        """Measures the total length of the rectangle's outer boundary.

        Note: Returns 0 if the rectangle has either zero width or zero height.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles and returns the one with the larger (or equal) area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.

        Raises:
            TypeError: If either input object is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2 

    @classmethod
    def square(cls, size=0):
        """Creates a Rectangle where all sides are equal (a square).

        Args:
            size (int): The desired length of each side of the square.
        """
        return cls(size, size) 

    def __str__(self):
        """Constructs a readable representation of the rectangle using characters."""
        if self.__width == 0 or self.__height == 0:
            return ""  # Represents an empty rectangle
        rectangle_string = ""
        for _ in range(self.__height):
            rectangle_string += (self.print_symbol * self.__width) + "\n"
        return rectangle_string[:-1] 

    def __repr__(self):
        """Creates a string that can be used to recreate the Rectangle object."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when a Rectangle is deleted & updates the instance count."""
        Rectangle.number_of_instances -= 1  
        print("Bye rectangle...")