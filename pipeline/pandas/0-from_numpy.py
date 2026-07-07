#!/usr/bin/env python3

import pandas as pd
import numpy as np


def from_numpy(array):
    """creates dataframe"""
    data = np.array(array)
    cols = array.shape[1]
    columns = [chr(ord('A') + i) for i in range(cols)]
    df = pd.DataFrame(data, columns=columns)
    return df
