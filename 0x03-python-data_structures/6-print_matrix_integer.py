#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers.

    Args:
        matrix: A list of lists representing the matrix (defaults to an empty matrix).
    """

    for row in matrix:
        for i, item in enumerate(row):
            print("{:d}".format(item), end="")  
            if i != len(row) - 1:  # No space after the last element in a row
                print(" ", end="")
        print()  # Newline after each row
