#!/usr/bin/env python3
"""
    Description: Create a measure_time function that takes two 
    integers as parameters, n and max_delay, and returns 
    total_time / n
    Arguments: n: int, max_delay: int
"""

from time import time
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Return execution time for wait_n given `n` and `max_delay`.
    """
    start_time = time()
    run(wait_n(n, max_delay))
    end_time = time()
    total_time = end_time - start_time
    return total_time / n
