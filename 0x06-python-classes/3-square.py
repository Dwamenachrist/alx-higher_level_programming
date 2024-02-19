#!/usr/bin/python3
class Square:
    """A class representing a square with size attribute, validation, and area calculation."""

    def __init__(self, size=0):
        """Initializes the Square instance with size validation

        Args:
          size (int, optional): The size of the square. Defaults to 0.

        Raises
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """ 
        self.size = size  # Calls the setter method

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The private size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square, with validation.

        Args:
            value (int): The updated size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """        
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2 
