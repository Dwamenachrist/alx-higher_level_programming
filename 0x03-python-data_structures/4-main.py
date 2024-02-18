#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Creates a new list with an element replaced at a specified index.

    Args:
        my_list: The original list.
        idx: The index where the replacement will occur.
        element: The new element to insert.

    Returns:
        A new list with the replacement, or a copy of the original list
        if the index is invalid.
    """

    if 0 <= idx < len(my_list):
        new_list = my_list[:]  # Create a copy
        new_list[idx] = element
    else:
        new_list = my_list[:]  # Return a copy if the index is invalid

    return new_list
