#!/usr/bin/env python3
"""
Description: Wait_random is an asynchronous coroutine that
             accepts an integer input (max_delay, with a default 
             value of 10) and waits for a random delay between 0 
             and max_delay (including float value) seconds before 
             returning it.

Arguments: max_delay: int = 10
"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    '''Wait up to max_delay seconds, then return the length of the delay.
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time

