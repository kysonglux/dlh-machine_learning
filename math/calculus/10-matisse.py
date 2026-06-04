#!/usr/bin/env python3
""" calculates the derivative of a polynomial """


def poly_derivative(poly):
    """ calculates the derivative of a polynomial """
    if not isinstance(poly, list) or poly == []:
        return None

    derivative = []
    if len(poly) == 1:
        return [0]
    for i in range(1, len(poly)):
        derivative.append(i * poly[i])
    return derivative
