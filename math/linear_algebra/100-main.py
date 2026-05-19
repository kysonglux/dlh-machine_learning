#!/usr/bin/env python3

import numpy as np
import importlib.util
from pathlib import Path

# Load module from filename (handles names with digits or hyphens)
helper_path = Path(__file__).parent / '100-slice_like_a_ninja.py'
spec = importlib.util.spec_from_file_location('slice_like_a_ninja', str(helper_path))
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
np_slice = helper.np_slice

mat1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np_slice(mat1, axes={1: (1, 3)}))
print(mat1)
mat2 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
                 [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],
                 [[21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]])
print(np_slice(mat2, axes={0: (2,), 2: (None, None, -2)}))
print(mat2)
