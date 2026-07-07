#!/usr/bin/env python3

import pandas as pd


def from_numpy(array):
    """creates dataframe with columns index"""
    cols = array.shape[1]
    columns = [chr(ord('A') + i) for i in range(cols)]
    df = pd.DataFrame(array, columns=columns)
    return df
