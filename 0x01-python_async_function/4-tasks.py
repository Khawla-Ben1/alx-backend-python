#!/usr/bin/env python3
"""task_wait_random"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    A list of n tasks that run the task_wait_random
    Args:
        n: integer represents the number of tasks to create
        max_delay: integer represents the maximum amount of time
    Returns:
        list of floats representing the time each task took to complete
    """

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
