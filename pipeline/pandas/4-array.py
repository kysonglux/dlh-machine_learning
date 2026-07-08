#!/usr/bin/env python3
"""Function that takes dataframe as input"""

import pandas as pd


def array(df):
    """Function that takes dataframe as input"""
    array = df[["High", "Close"]].to_numpy()
    return array
