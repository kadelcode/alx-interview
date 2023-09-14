#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """
    A fuction that rotates an n x n matrix
    by 90 degrees.
    """

    # Transpose the matrix
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print(transposed_matrix)

    # Reverse each row of the transposed matrix.
    for i in transposed_matrix:
        i.reverse()

    # Return the rotated matrix.
    # return transposed_matrix
