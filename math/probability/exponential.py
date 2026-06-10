#!/usr/bin/env python3
""" Create Exponential Class"""


class Exponential:
    """Exponential Class"""
    def __init__(self, data=None, lambtha=1.):
        """initialize the class"""
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = 1/(sum(data) / len(data))
        else:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)

    def pdf(self, x):
        """Calculates the value of PDF"""
        if x < 0:
            return 0
        e = 2.7182818285
        return self.lambtha*e**(-self.lambtha*x)

    def cdf(self, x):
        """Calculates the value of the Cumulative Distribution Function"""
        if x < 0:
            return 0
        e = 2.7182818285
        return 1 - e**(-self.lambtha*x)
