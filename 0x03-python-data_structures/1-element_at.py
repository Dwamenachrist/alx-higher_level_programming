#!/usr/bin/python3
def element_at(my_list, idx):
    """Safely retrieves an element from a list.

    Args:
        my_list: The list to access.
        idx: The index of the desired element.

    Returns:
        The element at the specified index, or None if the index is invalid.
    """

    if 0 <= idx < len(my_list):  # Check for valid index
        return my_list[idx]
    else:
        return None