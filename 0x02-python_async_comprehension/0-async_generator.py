#!/usr/bin/env python3
"""
Description: a coroutine called  async_generator that takes no
of arguments

"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Generates a random value between 0 and 10 every second, ten times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
