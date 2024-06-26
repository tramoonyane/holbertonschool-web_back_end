#!/usr/bin/env python3
"""  alter it into a new function task_wait_n.
The code is nearly identical to wait_n except
task_wait_random is being called """

from typing import List
task_wait_n = __import__('1-concurrent_coroutines').wait_n


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays"""
    delays = []
    for i in range(n):
        delay = await task_wait_random(max_delay)
        delays.append(delay)
        delays = sorted(delays)
    return delays
