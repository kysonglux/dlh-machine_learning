#!/usr/bin/env python3
""" draw the line graph """
import numpy as np
import matplotlib.pyplot as plt


def line():
    """ draw the line graph"""

    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))
    x = np.arange(0, 11)
    plt.plot(y, color="red")

    plt.xlim(0, 10)
    plt.savefig("line_plot.png")
