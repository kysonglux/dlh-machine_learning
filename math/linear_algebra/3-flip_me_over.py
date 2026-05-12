#!/usr/bin/env python3
"""about Transpose"""


def matrix_transpose(matrix):
    """using zip transpose the matrix"""
    return [list(row) for row in zip(*matrix)]
