#!/usr/bin/env python3
"""sorts dataframe descending order"""


def high(df):
    """sorts dataframe descending order"""
    return df.sort_values(['High'], ascending=False)
