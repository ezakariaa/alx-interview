#!/usr/bin/python3
""" Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in place.
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i + 1, n):
            # Swap the elements at (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
