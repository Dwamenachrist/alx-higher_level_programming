#!/usr/bin/python3
"""Provides the blueprint for creating rectangle objects."""

class Rectangle:
    """Defines the characteristics and actions of a rectangle.

    Attributes:
        number_of_instances (int): Counts the total Rectangle objects in existence.
        print_symbol (any):  The character used to display the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Creates a new Rectangle instance.

        Args:
            width (int): The desired width of the rectangle.
            height (int): The desired height of the rectangle.
        """
        Rectangle.number_of_instances += 1  # Increment Rectangle count
        self.width = width
        self.height = height

    @property
    def width(self):
        """Allows retrieval and modification of the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Updates the width, ensuring it's an integer and not negative.""" 
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Allows retrieval and modification of the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Updates the height, ensuring it's an integer and not negative.""" 
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the total space within the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the distance around the rectangle's border.

        Note: Returns 0 if either width or height is zero.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles and returns the one with the larger (or equal) area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

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

    def __str__(self):
        """Provides a user-friendly visual representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_string = ""
        for _ in range(self.__height):
            rectangle_string += (self.print_symbol * self.__width) + "\n"
        return rectangle_string[:-1] 

    def __repr__(self):
        """Provides a string form suitable for recreating the Rectangle instance."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a farewell message when a Rectangle is deleted and manages instances."""
        Rectangle.number_of_instances -= 1 
        print("Bye rectangle...")
