#!/usr/bin/env python3
""" calculates the derivative of a polynomial """


def poly_derivative(poly):
    """ calculates the derivative of a polynomial """
    total = 0
    for porwer, coeff in enumerate(poly):
        total += coeff * (x ** power)
