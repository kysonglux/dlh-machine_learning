#!/usr/bin/env python3
""" Create Poisson distribution"""


def __init__(self, data=None, lambtha=1.):
    """ Create Poisson distribution """
    if not isinstance(data, list):
        raise TypeError ("data must be a list")
    if count(data) < 2:
        raise ValueError("data must contain multiple values")
    if data == None:
        data = lambtha
    if lambtha < 0 or lambtha == 0:
        raise ValueError(("lambtha must be a positive value"))
    else:
        return (e^(-lambtha)*(lambtha^data)/(data!))

