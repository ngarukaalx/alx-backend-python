#!/usr/bin/env python3
"""Import async_comprehension from the previous file and write a
measure_runtime
"""
from asyncio import gather
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure run time of pararell excution
    measure_runtime should measure the total runtime and return it.
    """
    start = time()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    end = time()
    return end - start
