#!/usr/bin/python3
from models.base import Base
from collections import OrderedDict

import json

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
        """Prints the Rectangle instance with '#' characters, including 'x' and 'y' offset."""
        for y_offset in range(self.y):  # New: Add 'y' offset
            print()  # Print blank lines for vertical shift

        for row in range(self.height):
            print(" " * self.x, end="")  # Added spaces for 'x' offset
            for col in range(self.width):
                print("#", end="")
            print() 


    def __str__(self):
        """Overrides the default __str__ to return a custom string representation."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )
        

    def update(self, *args, **kwargs):
        """Assigns attributes based on positional or keyword arguments."""

        # 1. Prioritize positional arguments (*args) if present
        if args:  
            attr_names = ["id", "width", "height", "x", "y"] 
            for index, value in enumerate(args[:5]):
                setattr(self, attr_names[index], value)  

        # 2. Handle keyword arguments (**kwargs) 
        for key, value in kwargs.items():
            if hasattr(self, key):  # Safety check:  Does the attribute exist?
                setattr(self, key, value)
                
    def to_dictionary(self):
        """
        Represents a dictionary representation of rectangle
        """
        rec_dict = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
        }

        return rec_dict
    
    @classmethod
    def save_to_file(cls, rectangles):
        """Saves a list of Rectangle objects to a file in JSON format."""
        if rectangles is None:
            data = []
        else:
            data = [obj.to_dictionary() for obj in rectangles]

        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            json.dump(data, f)