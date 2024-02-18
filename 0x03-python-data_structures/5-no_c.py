#!/usr/bin/python3
def no_c(my_string):
    """Removes all 'c' and 'C' characters from a string.

    Args:
        my_string: The input string.

    Returns:
        A new string with 'c' and 'C' characters removed.
    """

    new_string = ""  # Initialize an empty string to store the result
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char

    return new_string
