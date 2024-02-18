#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer in a list.

    Args:
        my_list: The list of integers (defaults to an empty list).

    Returns:
        The maximum integer in the list, or None if the list is empty.
    """

    if not my_list:  # Handle an empty list directly
        return None

    max_value = my_list[0]  # Initialize max_value with the first element
    for num in my_list:
        if num > max_value:
            max_value = num

    return max_value
