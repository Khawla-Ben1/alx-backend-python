#!/usr/bin/env python3
"""The basics of async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Takes an integer argument and returns a float value"""

    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
