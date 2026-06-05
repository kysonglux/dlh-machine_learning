#!/usr/bin/env python3
""" draw line graph while chaning scale"""
import numpy as np
import matplotlib.pyplot as plt


def change_scale():

    """ draw line graph while chaning scale"""
    x = np.arange(0, 28651, 5730)
    r = np.log(0.5)
    t = 5730
    y = np.exp((r / t) * x)
    plt.figure(figsize=(6.4, 4.8))

    plt.plot(x, y, color="blue")
    plt.yscale("log")
    plt.ylim(0, 1)
    plt.xlim(0, 28650)
    plt.margins(x=0, y=0)
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")
    plt.title("Exponential Decay of C-14")
    plt.savefig("exponential.png")
