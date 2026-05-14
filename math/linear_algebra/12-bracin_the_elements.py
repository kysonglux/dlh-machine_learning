#!/usr/bin/env python3
"""element-wise addition, subtraction, mul, division"""


def np_elementwise(mat1, mat2):
    """element-wise add, sub, mul, div"""
    add = mat1 + mat2
    sub = mat1 - mat2
    mul = mat1 * mat2
    div = mat1 / mat2
    return add, sub, mul, div
