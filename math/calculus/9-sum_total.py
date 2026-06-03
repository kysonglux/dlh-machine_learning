#!/usr/bin/env python3
""" summation of i """


def summation_i_squared(n):
    if n <= 0:
        return None
    else:
        return ((n * (n + 1) * (2*n + 1)) // 6)
