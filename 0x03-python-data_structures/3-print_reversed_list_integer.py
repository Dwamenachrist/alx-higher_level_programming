#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints a list of integers in reverse order.

    Args:
        my_list: The list of integers (defaults to an empty list).
    """

    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))
