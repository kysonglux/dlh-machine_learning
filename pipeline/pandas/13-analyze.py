#!/usr/bin/env python3
"""compute statistics"""


def analyze(df):
    """compute statistics"""
    return df.drop(columns=["Timestamp"], errors="ignore").describe()
