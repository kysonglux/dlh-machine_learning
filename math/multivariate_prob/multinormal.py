#!/usr/bin/env python3
"""Multivariate Normal distribution"""
import numpy as np


class MultiNormal:
    """Nultivariate Normal distribution"""
    def __init__(self, data):
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)

        X_centered = data - self.mean
        self.cov = (X_centered @ X_centered.T) / (n - 1)

        self.cov_inv = np.linalg.inv(self.cov)
        self.cov_det = np.linalg.det(self.cov)
        self.d = d

    def pdf(self, x):
        """calculates the PDF at a data point"""
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        if x.shape != (self.d, 1):
            raise ValueError(f"x must have the shape ({self.d}, 1)")

        diff = x - self.mean
        exponent = -0.5 * (diff.T @ self.cov_inv @ diff)
        exponent = exponent[0, 0]

        norm_const = 1 / np.sqrt(((2 * np.pi) ** self.d) * self.cov_det)
        return norm_const * np.exp(exponent)
