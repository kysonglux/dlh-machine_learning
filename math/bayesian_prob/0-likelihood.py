#!/usr/bin/env python3
"""Calculates the likelihood"""


def likelihood(x, n, P):
    """Calculates the likelihood"""
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if x < 0:
        raise ValueError("x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.dnim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if P >= 0 and P <= 1:
        raise ValueError("All values in P must be in the range [0, 1]")
    
    coefficient = n!/(x!(n-x)!)
    successes = P **x
    failures = (1 - P) **(n - x)
    return coefficient * successes * failures
