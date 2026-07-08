#!/usr/bin/env python3
"""function that takes a dataframe as input"""

import pandas as pd


def rename(df):
    """rename funtion that takes a datafrom as input """
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit="s")
    return df[["Datetime", "Close"]]
