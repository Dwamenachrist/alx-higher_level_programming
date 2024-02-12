#!/usr/bin/python3

from rectangle import Rectangle

class Square(Rectangle):
    """Represents a Square"""

    def __init__(self, size, x=0, y=0, id=None):
            """Initializes a Square.
				Args:
					size (int): Size of the square.
					x (int, optional): x-coordinate. Defaults to 0.
					y (int, optional): y-coordinate. Defaults to 0.
					id (int, optional):  Unique identifier. Defaults to None.
				"""
            super().__init__(size, size, x, y, id)  

    def __str__(self):
        """Overrides the __str__ method to return a custom representation."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        """Gets the size of the Square."""
        return self.width  

    @size.setter
    def size(self, value):
        """Sets the size of the Square (alters both width and height)."""
        self.width = value  # Use existing setter with validation
        self.height = value
        
    def update(self, *args, **kwargs):
        """Updates Square attributes using positional or keyword arguments."""

        # 1. Process Positional Arguments (*args)
        if args:
            attr_names = ["id", "size", "x", "y"]
            for index, value in enumerate(args[:4]):  # Limit to 4 attributes
                setattr(self, attr_names[index], value)  

        # 2. Process Keyword Arguments (**kwargs)
        else:  # Skip kwargs processing if *args were provided
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)