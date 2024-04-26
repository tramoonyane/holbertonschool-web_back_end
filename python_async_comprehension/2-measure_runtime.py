#!/usr/bin/env python3
"""  write a measure_runtime coroutine that will
execute async_comprehension four times in parallel
using asyncio.gather"""

import time
from typing import List, Generator
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime should measure the
    total runtime and return it"""
    start = time.time()
    await asyncio.gather(async_comprehension())
    end = time.time()
    total = end - start
    return total
