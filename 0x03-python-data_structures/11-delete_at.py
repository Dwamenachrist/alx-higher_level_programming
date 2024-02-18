#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes an item at a specific index in a list.

    Args:
        my_list: The list to modify.
        idx: The index of the element to delete.

    Returns:
        The updated list with the element removed (if the index was valid).
    """

    if 0 <= idx < len(my_list):  # Check if index is within valid range
        del my_list[idx]  # Delete the element if index is valid
    
    return my_list
