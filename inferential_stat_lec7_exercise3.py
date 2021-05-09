import math
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np


def std_dev_of_lengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """