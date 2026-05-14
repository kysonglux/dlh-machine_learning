#!/usr/bin/env python3
"""concatenates matrices """


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """ concatenates matrices with a specific axis"""
    return np.concatenate((mat1, mat2), axis=axis)
