#!/usr/bin/env python3
"""concatenates two dataframe"""

import pandas as pd


def concat(df1, df2):
    """concatenates two dataframe"""
    index = __import__('10-index').index
    df1 = index(df1)
    df2 = index(df2)
    df2 = df2.loc[:1417411920]
    return pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])
