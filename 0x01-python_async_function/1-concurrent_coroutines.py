#!/usr/bin/env python3
"""
Description: Create a measure_time function that takes integers
           n and max_delay as inputs and returns total_time / n.

Arguments: n: int, max_delay: int
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return the execution time for wait_n with 'n' and'max_delay'.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
