#!/usr/bin/env python3
""" slice a matrix along specified axes """


def np_slice(matrix, axes={}):
    """Slice a matrix along specified axes."""
    if axes is None:
        axes = {}
    slices = [slice(None)] * matrix.ndim

    for axis, sl in axes.items():
        if isinstance(sl, tuple):
            slices[axis] = slice(*sl)
        else:
            slices[axis] = sl

    return matrix[tuple(slices)]
