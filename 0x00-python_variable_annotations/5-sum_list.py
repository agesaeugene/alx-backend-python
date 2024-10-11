#!/usr/bin/env python3
"""
    Description: This function accepts a list of floats
    as an argument and returns the total as a float.
    Arguments: input_list: List[float]

"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of all entries in the input_list.
    """
    return float(sum(input_list))
