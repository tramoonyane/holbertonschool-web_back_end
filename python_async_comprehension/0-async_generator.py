#!/usr/bin/env python3
"""Write a coroutine called async_generator
that takes no arguments."""

import asyncio
import random
from typing import List, Generator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """The coroutine will loop 10 times, each
    time asynchronously wait 1 second, then
    yield a random number between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
