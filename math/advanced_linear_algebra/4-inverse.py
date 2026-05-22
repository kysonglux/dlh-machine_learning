#!/usr/bin/env python3
"""calculates the inverse of a matrix"""


def determinant(matrix):
    """calculates the determinant of a matrix"""
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    for col in range(len(matrix)):
        new = []
        for r in range(1, len(matrix)):
            sub = []
            for c in range(len(matrix)):
                if c == col:
                    continue
                sub.append(matrix[r][c])
            new.append(sub)
        det += (-1) ** (col) * matrix[0][col] * determinant(new)
    return det


def inverse(matrix):
    """calculates the inverse of a matrix"""
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
        return [[1/matrix[0][0]]]
    cofactor = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            sub = []
            for r in range(len(matrix)):
                if r == i:
                    continue
                new_row = []
                for c in range(len(matrix)):
                    if c == j:
                        continue
                    new_row.append(matrix[r][c])
                sub.append(new_row)
            sign = (-1)**(i + j)
            row.append(determinant(sub) * sign)
        cofactor.append(row)
    adjugate = []
    for row in zip(*cofactor):
        adjugate.append(list(row))
    new_matrix = []
    det = determinant(matrix)
    if det == 0:
        return None
    else:
        for row in adjugate:
            new_row = []
            for val in row:
                new_row.append(val / det)
            new_matrix.append(new_row)
    return new_matrix
