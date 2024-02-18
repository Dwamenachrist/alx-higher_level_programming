#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific index.

    Args:
        my_list: The list to modify.
        idx: The index where the replacement should occur.
        element: The new element to insert.

    Returns:
        A new list with the replacement made, or the original list if 
        the index is invalid.
    """

    if 0 <= idx < len(my_list):
        new_list = my_list[:]  # Create a copy of the list
        new_list[idx] = element 
        return new_list
    else:
        return my_list  # Return the original list if index is invalid
