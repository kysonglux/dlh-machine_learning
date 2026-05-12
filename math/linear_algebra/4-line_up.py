#!/usr/bin/env python3
""" matrix addition """


def add_arrays(arr1, arr2):
    """ matrix addition """
    if len(arr1) != len(arr2):
        return None
    new_arr = []
    for e in range(len(arr1)):
        new_arr.append(arr1[e] + arr2[e])
    return new_arr
