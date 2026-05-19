#!/usr/bin/env python3
""" adds two matrices element-wise """


def add_matrices(mat1, mat2):
    """Adds two matrices element-wise """
    if isinstance(mat1, int) and isinstance(mat2, int):
        return mat1 + mat2
    if isinstance(mat1, list) and isinstance(mat2, list):
        if len(mat1) != len(mat2):
            return None
        result = []
        for m1, m2 in zip(mat1, mat2):
            added = add_matrices(m1, m2)
            if added is None:
                return None
            result.append(added)
        return result

    return None
