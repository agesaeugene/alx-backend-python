#!/usr/bin/env python3
"""
    Description: Create a new function, task_wait_n, 
    by modifying the wait_n code. The code is virtually
    identical to wait_n, except that task_wait_random 
    is called.
    Arguments: n: int, max_delay: int = 10
"""
import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
   """
   Execute task_wait_random and returns sorted list of delay
   """
   spawn_ls = []
   delay_ls = []
   for i in range(n):
       delayed_task = task_wait_random(max_delay)
       delayed_task.add_done_callback(lambda x: delay_ls.append(x.result()))
       spawn_ls.append(delayed_task)

   for spawn in spawn_ls:
       await spawn

   return delay_ls
