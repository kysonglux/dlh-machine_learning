#!/usr/bin/env python3
"""advanced linear algebra"""


def determinant(matrix):
    """ calculate determinant """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    elif len(matrix) != len(matrix[0]):        
        raise ValueError("matrix must be a square matrix")
    elif len(matrix) == []:
        return []
    elif len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
        det = 0
        for col in range(len(matrix))
            minor = []
            for i in range (1, len(matrix))
                row = []
                for 