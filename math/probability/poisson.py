#!/usr/bin/env python3
""" Create Poisson distribution"""


class Poisson:
    """create Poisson distribution"""
    def __init__(self, data=None, lambtha=1.):
        """Initialize Poisson distribution"""
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = sum(data) / len(data)
        else:
            if lambtha <= 0:
                raise ValueError(("lambtha must be a positive value"))
            self.lambtha = lambtha

    def pmf(self, k):
        """ Calculate Probability Mass Function"""
        k = int(k)
        if k < 0:
            return 0
        else:
            e = 2.7182818285
            factorial = 1
            for i in range(1, k + 1):
                factorial *= i
            result = e ** (-self.lambtha) * (self.lambtha ** k)/factorial
            return result

    def cdf(self, k):
        """Calculate Cumulative Distribution Function"""
        k = int(k)
        if k < 0:
            return 0
        result = 0
        for i in range(k + 1):
            result += self.pmf(i)
        return result
