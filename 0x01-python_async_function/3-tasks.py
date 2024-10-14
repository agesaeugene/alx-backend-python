#!/usr/bin/env python3
"""
    Description: Create a function using standard syntax,
    not async. The task_wait_random function accepts an 
    integer max_delay and returns an asyncio.Task.
    Arguments: max_delay: int
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Asynchronous task for wait_random is created and
    Task object is returned.
    """
    return asyncio.create_task(wait_random(max_delay))
