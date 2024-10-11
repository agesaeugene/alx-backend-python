#!/usr/bin/env python3
"""
    Description: Annotate the following function's parameters 
    and return values with the proper types.

"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
       Return a collection of tuples, each containing the
       element and its length.
    """
    return [(i, len(i)) for i in lst]
