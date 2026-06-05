#!/usr/bin/env python3
"""draw the stacked bar chart"""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """draw the stacked bar chart"""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    people = ["Farrah", "Fred", "Felicia"]
    apples = fruit[0]
    bananas = fruit[1]
    oranges = fruit[2]
    peaches = fruit[3]

    fruits_data = [apples, bananas, oranges, peaches]
    colors = ["red", "yellow", "#ff8000", "#ffe5b4"]
    labels = ["apples", "bananas", "oranges", "peaches"]

    current_bottom = np.zeros(3)

    for d, c, l in zip(fruits_data, colors, labels):
        plt.bar(people, d, bottom=current_bottom, color=c, label=l, width=0.5)
        current_bottom += d

    plt.ylabel("Quantity of Fruit")
    plt.yticks(np.arange(0, 81, 10))
    plt.legend()
    plt.title("Number of Fruit per Person")
    plt.savefig("task6")
