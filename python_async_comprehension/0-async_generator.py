#!/usr/bin/env python3

"""
This module defines an asynchronous generator coroutine
that yields random numbers between 0 and 10.
"""

from asyncio import sleep
from random import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """
    Asynchronous generator coroutine that yields
    random numbers between 0 and 10.

    Yields:
        float: Random number between 0 and 10.
    """
    for _ in range(10):
        await sleep(1)
        yield 10 * random()
