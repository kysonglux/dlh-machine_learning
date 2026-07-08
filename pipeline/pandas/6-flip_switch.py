#!/usr/bin/env python3
"""function that reverse order, sorted"""


def flip_switch(df):
    """function that reverse order, sorted"""
    data = df.iloc[::-1]
    return data.T
