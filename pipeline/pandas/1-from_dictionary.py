#!/usr/bin/env python3
"""create dataframe from a dictionary"""

import pandas as pd


array = {'First': [0.0, 0.5, 1.0, 1.5],
         'Second': ["one", "two", "three", "four"]}
df = pd.DataFrame(array)
df.index = [chr(ord('A') + i) for i in range(len(df))]
