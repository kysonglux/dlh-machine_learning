#!/usr/bin/env python3
"""function with remove entries"""


def prune(df):
    """function with remove entries"""
    return df[df['Close'].notna()]
