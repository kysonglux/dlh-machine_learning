#!/usr/bin/env python3
"""slice function"""


def slice(df):
    """slice function"""
   
    return df[['High', 'Low', 'Close', 'Volume_(BTC)']].iloc[::60]