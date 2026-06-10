#!/usr/bin/env python3
"""Create a class Normal"""


class Normal:
    """Create a class Normal"""
    def __init__(self, data=None, mean=0., stddev=1.):
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            result = 0
            for i in data:
                result += (i - self.mean)**2
            self.stddev = (result / len(data))**0.5

        else:
            if stddev < 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
