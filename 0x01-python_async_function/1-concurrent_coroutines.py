#!/usr/bin/env python3
'''0x01. Python - Async'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''wait_n should return the list of all the delays (float values).
      The list of the delays should be in ascending order without using
        sort() because of concurrency.'''
    delay = []
    for i in range(n):
        delay.append(await wait_random(max_delay))
    return (delay)

