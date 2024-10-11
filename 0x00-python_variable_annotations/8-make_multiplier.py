#!/usr/bin/env python3
"""
    Description: accepts a float multiplier as input 
    and returns a function that multiplies a float by
    multiplier.
    
    Arguments: multiplier: float
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return the function that multiplies a float by'multiplier'. """
    return lambda x: x * multiplier
