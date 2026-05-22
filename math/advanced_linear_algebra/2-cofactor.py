#!/usr/bin/env python3
"""calculates the cofactor of a matrix"""


def determinant(matrix):
    """calculates the determinant of a matrix"""
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    for col in range(len(matrix)):
        minor = []
        for r in range(1, len(matrix)):
            row = []
            for c in range(len(matrix)):
                if c == col:
                    continue
                row.append(matrix[r][c])
            minor.append(row)
        det += (-1) ** col * matrix[0][col] * determinant(minor)
    return det


def cofactor(matrix):
    """calculates the cofactor of a matrix"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if matrix == []:
        raise TypeError("matrix must be a list of lists")
    if matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) == 1:
        return [[1]]
    cofactor_matrix = []
    for j in range(len(matrix)):
        row = []
        for k in range(len(matrix)):
            sub = []
            for r in range(len(matrix)):
                if r == j:
                    continue
                new_row = []
                for c in range(len(matrix)):
                    if c == k:
                        continue
                    new_row.append(matrix[r][c])
                sub.append(new_row)
            sign = (-1) ** (j + k)
            row.append(sign * determinant(sub))
        cofactor_matrix.append(row)
    return cofactor_matrix
