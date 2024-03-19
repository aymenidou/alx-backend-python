#!/usr/bin/env python3
'''0x01. Python - Async'''
from asyncio import wait, create_task, FIRST_COMPLETED
# import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''wait_n should return the list of all the delays (float values).
      The list of the delays should be in ascending order without using
        sort() because of concurrency.'''

    tasks = [create_task(wait_random(max_delay))
             for i in range(n)]  # Spawn tasks
    delays = []
    while tasks:
        # Efficiently complete tasks and append delays in order
        done, pending = await wait(tasks, return_when=FIRST_COMPLETED)
        for task in done:
            delay = task.result()
            delays.append(delay)
            tasks.remove(task)
    return (delays)
