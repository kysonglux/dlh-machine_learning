#!/usr/bin/env python3
"""calculates the minor of a matrix"""


def determinant(matrix):
    """"calculates the determinant of a matrix"""
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    for j in range(len(matrix)):
        new_sub = []
        for r in range(1, len(matrix)):
            new_row = []
            for c in range(len(matrix)):
                if c == j:
                    continue
                new_row.append(matrix[r][c])
            new_sub.append(new_row)
        det += (-1)**j * matrix[0][j] * determinant(new_sub)
    return det


def minor(matrix):
    """determinant of the smaller matrix left over when cross out """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    if matrix == []:
        raise TypeError("matrix must be a list of lists")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) == 1:
        return [[1]]
    minor_matrix = []
    for col in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            sub = []
            for i in range(len(matrix)):
                if i == col:
                    continue
                new_row = []
                for k in range(len(matrix)):
                    if k == j:
                        continue
                    new_row.append(matrix[i][k])
                sub.append(new_row)
            row.append(determinant(sub))
        minor_matrix.append(row)
    return minor_matrix
