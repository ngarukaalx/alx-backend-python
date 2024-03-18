#!/usr/bin/env python3
"""This module contains func wai_n
"""
import asyncio
from typing import List
import bisect
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """multiple coroutines at the same time"""
    listDelays = []
    waits = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        task.add_done_callback(lambda i: listDelays.append(i.result()))
        waits.append(task)
    for wait in waits:
        await wait
    return listDelays
