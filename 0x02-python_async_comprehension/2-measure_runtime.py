#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    coroutine that will execute async_comprehension four times in parallel
    """
    beginning = perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = perf_counter()
    return end - beginning
