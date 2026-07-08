#!/usr/bin/env python3
"""using column as an index"""


def index(df):
    """using column as an index"""
    return df.set_index("Timestamp")
