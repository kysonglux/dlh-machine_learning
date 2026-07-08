#!/usr/bin/env python3
"""compute statistics"""

import pandas as pd


def analyze(df):
    """compute statistics"""
    return df.drop(columns=["Timestamp"], errors="ignore").describe()
