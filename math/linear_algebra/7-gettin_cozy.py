#!/usr/bin/env python3
""" concatenates two matrices """


def cat_matrices2D(mat1, mat2, axis=0):
    """"shallow copy vs. deep copy """
      # Check if either matrix is empty
       # Check all rows in mat1 have same length
         # Check all rows in mat2 have same length
    if axis == 0:
           # Must have same number of columns
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    else:
         # Must have same number of rows
        if len(mat1) != len(mat2):
            return None
        new_matrix = []
        for i in range(len(mat1)):
            new_matrix.append(mat1[i][:] + mat2[i][:])
        return new_matrix
