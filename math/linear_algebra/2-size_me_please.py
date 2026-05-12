#!/usr/bin/env python3
""" shape of matrix """


def matrix_shape(matrix):
    """calculates the shape of a matrix"""
    shape = []
    element = matrix
    for _ in range(10):
        if isinstance(element, list):
            shape.append(len(element))
            element = element[0]
        else:
            break
    return shape
