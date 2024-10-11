#!/usr/bin/env python3
"""
    accepts a string k and an integer OR float v as parameters 
    and returns a tuple. The tuple's first element is the 
    string k.

"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple containing k and the square of v.
    """
    return (k, float(v**2))
