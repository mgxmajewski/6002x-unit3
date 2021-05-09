import math
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
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    list_of_str = L
    len_of_list = len(list_of_str)
    if len_of_list == 0:
        return float('NaN')
    else:
        return 0
    
print(std_dev_of_lengths([]))