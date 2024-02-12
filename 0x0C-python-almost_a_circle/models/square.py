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