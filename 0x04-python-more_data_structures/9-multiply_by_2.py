#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Creates a new dictionary with values multiplied by 2.

    Args:
        a_dictionary (dict): The input dictionary.

    Returns:
        dict: A new dictionary with values multiplied by 2.
    """

    new_dictionary = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dictionary