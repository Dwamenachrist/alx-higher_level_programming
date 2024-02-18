#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints all integers of a list.

    Args:
        my_list: The list of integers to print. Defaults to an empty list.
    """
    for value in my_list:
        print("{:d}".format(value))