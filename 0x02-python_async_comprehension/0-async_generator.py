#!/usr/bin/env python3
'''0x02-python_async_comprehension.'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that yields 10 random numbers between 0 and 10,
    waiting 1 second between each yield.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
