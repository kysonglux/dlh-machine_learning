#!/usr/bin/env python3
"""sorts dataframe descending order"""

import pandas as pd


def high(df):
    """sorts dataframe descending order"""
    return df.sort_values(['High'], ascending=False)
