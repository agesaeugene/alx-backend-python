#!/usr/bin/env python3
"""
    Description: takes a list mxd_lst of floats and
    integers and returns the total as a float.
    
    Arguments: mxd_lst: List[Union[int, float]]
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the total of the elements in mxd_list. """
    return sum(mxd_lst)
