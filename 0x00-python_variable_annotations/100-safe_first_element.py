#!/usr/bin/env python3
"""
    Description: Complete the following code with the appropriate 
    duck-typed annotations.

"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ 
    If lst contains any elements, return the first one;
    else, return None.
    """
    if lst:
        return lst[0]
    else:
        return None
