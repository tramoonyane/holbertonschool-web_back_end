#!/usr/bin/env python3

"""
This module defines an asynchronous generator coroutine
that yields random numbers between 0 and 10.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator coroutine that yields
    random numbers between 0 and 10.

    Yields:
        float: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def main():
    async for number in async_generator():
        print(number)


if __name__ == "__main__":
    asyncio.run(main())
