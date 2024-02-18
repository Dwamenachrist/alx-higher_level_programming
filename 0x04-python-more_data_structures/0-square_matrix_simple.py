#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a 2D list")

    new_matrix = [[element**2 for element in row] for row in matrix]

    return new_matrix

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)  # Original matrix remains unchanged
