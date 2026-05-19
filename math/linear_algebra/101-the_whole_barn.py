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
            if isinstance(m1, list) and isinstance(m2, list):
                if len(m1) != len(m2):
                    return None
                result.append(add_matrices(m1, m2))
            elif isinstance(m1, int) and isinstance(m2, int):
                result.append(m1 + m2)
            else:
                return None
        return [add_matrices(m1, m2) for m1, m2 in zip(mat1, mat2)]
    return None