#!/usr/bin/env python3
"""Import async_comprehension from the previous file and write a
measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
a
measure_runtime should measure the total runtime and return it.
"""
from time import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure run time of pararell excution
    measure_runtime should measure the total runtime and return it.
    """
    start = time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end = time()
    return end - start
