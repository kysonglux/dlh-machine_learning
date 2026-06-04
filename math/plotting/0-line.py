#!/usr/bin/env python3
""" draw the line graph """
import numpy as np
import matplotlib.pyplot as plt


def line():

    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))
    x = list(range(11))
    x = np.linspace(0, 10, 2)
    plt.plot(x, y)
    plt.show()