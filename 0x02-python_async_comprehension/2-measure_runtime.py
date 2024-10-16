#!/usr/bin/env python3
"""
Description: Import async_comprehension from the previous file and 
             create a measure_runtime coroutine to execute it four 
             times in parallel using asyncio.gather.

             measure_runtime should calculate the overall runtime 
             and return it


"""
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Calculate the runtime of async_comprehension performed four times 
    in parallel.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
