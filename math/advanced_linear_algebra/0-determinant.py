#!/usr/bin/env python3
"""advanced linear algebra"""


def determinant(matrix):
    """ calculate determinant """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    elif matrix == []:
        raise TypeError("matrix must be a list of lists")
    elif not isinstance(matrix[0], list):
        raise TypeError("matrix must be a list of lists")
    elif matrix == [[]]:
        return 1
    elif any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")
    elif len(matrix) == 1 and len(matrix[0]) == 0:
        return 1
    elif len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for col in range(len(matrix)):
            minor = []
            for i in range(1, len(matrix)):
                row = []
                for j in range(len(matrix)):
                    if j != col:
                        row.append(matrix[i][j])
                minor.append(row)
            det += (-1) ** col * matrix[0][col] * determinant(minor)
        return det
