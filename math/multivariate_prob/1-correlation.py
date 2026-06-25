#!/usr/bin/env python3
"""calculates a correlation matrix"""
import numpy as np


def correlation(C):
    """calculates a correlation matrix"""
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    d = C.shape[0]

    std = np.sqrt(np.diag(C))

    if np.any(std == 0):
        raise ValueError("zero variance")

    corr = C / (std[:, None] * std[None, :])

    return corr
