#!/usr/bin/env python3
"""concatenate two dataframes"""

import pandas as pd


def hierarchy(df1, df2):
    """concatenate two dataframes"""
    index = __import__('10-index').index
    df1 = index(df1)
    df2 = index(df2)
    df2 = df2.loc[1417411980:1417417980]
    new_dataset = pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])
    return new_dataset.sort_index()
