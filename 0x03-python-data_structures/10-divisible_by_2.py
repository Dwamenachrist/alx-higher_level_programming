#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finds multiples of 2 in a list and indicates their divisibility status.

    Args:
        my_list: The input list.

    Returns:
        A new list containing True for elements divisible by 2, False otherwise.
    """

    result_list = []
    for num in my_list:
        if num % 2 == 0:  # Check for divisibility by 2
            result_list.append(True)
        else:
            result_list.append(False)

    return result_list
