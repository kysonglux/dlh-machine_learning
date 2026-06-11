#!/usr/bin/env python3
"""Create a class Binomial"""


class Binomial:
    """Create a class Binomial"""
    def __init__(self, data=None, n=1, p=0.5):
        """initiate the class"""
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            if mean == 0 or variance >= mean:
                self.p = 0.5
                self.n = n
            else:
                estimated_p = 1.0 - (variance / mean)
                self.n = int(round(mean / estimated_p))
                self.p = float(mean / self.n)

        else:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p > 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
