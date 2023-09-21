#!/usr/bin/python3
"""
Rotate Matrix
"""


def rotate_2d_matrix(matrix):
    """
    A function that rotates a matrix
    by 90 degrees
    """

    n = len(matrix)

    # Reverse each row of the matrix.
    for i in range(n // 2):
        for j in range(n):
            matrix[i][j], matrix[n - 1 - i][j] =\
                matrix[n - 1 - i][j], matrix[i][j]

    # Transpose the matrix.
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
