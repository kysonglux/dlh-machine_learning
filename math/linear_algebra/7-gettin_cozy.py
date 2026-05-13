#!/usr/bin/env python3
""" concatenates two matrices """


def cat_matrices2D(mat1, mat2, axis=0):
    """"shallow copy vs. deep copy """
    if axis == 0:
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    else:
        new_matrix = []
        for i in range(len(mat1)):
            new_matrix.append(mat1[i][:] + mat2[i][:])
        return new_matrix
