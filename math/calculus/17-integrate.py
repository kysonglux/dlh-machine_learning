#!/usr/bin/env python3
""" calculates the integral of a polynomial """


def poly_integral(poly, C=0):
    """ calculates the integral of a polynomial """
    if not isinstance(poly, list) or poly == []:
       return None 
    if not isinstance(C, int):
        return None
    integral = []
    for i in range(1, len(poly)):
        integral.append( 1 / (poly[i] + 1))
    if len(poly) > 1 and poly == 0:
        integral.pop()
    return integral    
