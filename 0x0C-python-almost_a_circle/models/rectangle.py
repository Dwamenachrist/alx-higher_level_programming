#!/usr/bin/python3

from base import Base

class Rectangle(Base):
    """
    Represents a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
		
		# Inherited from the class Base. 
		# Initializes a Rectangle object.

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle (add validation here if needed)."""
        self.__width = value 

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle (add validation here if needed)."""
        self.__height = value 

    @property
    def x(self):
        """Gets the x-coordinate of the top-left corner."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x-coordinate of the top-left corner (add validation here if needed)."""
        self.__x = value

    @property
    def y(self):
        """Gets the y-coordinate of the top-left corner."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y-coordinate of the top-left corner (add validation here if needed)."""
        self.__y = value

if __name__ == "__main__":
    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

