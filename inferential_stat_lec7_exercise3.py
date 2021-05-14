import os
import numpy as np
os.environ["OPENBLAS_NUM_THREADS"] = "1"


def variance(L):
    """
   :param L: list of strings
   :return: variance of L
   """
    mean = sum(L)/len(L)
    tot = 0.0
    for x in L:
        tot += (x - mean)**2
    return tot/len(L)


def std_dev_of_lengths(L):
    """
    :param L: a list of strings
    :return: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    list_of_str = L
    array_of_str = np.array([len(x) for x in list_of_str])
    if len(array_of_str) == 0:
        return float('NaN')
    else:
        return variance(array_of_str)**.5


print(variance([10, 4, 12, 15, 20, 5])**.5/11)