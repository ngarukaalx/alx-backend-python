#!/usr/bin/env python3
"""This module contains func wai_n
"""
import asyncio
from typing import List
import bisect
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """multiple coroutines at the same time"""
    listDelays = []
    waits = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        task.add_done_callback(lambda i: listDelays.append(i.result()))
        waits.append(task)
    for wait in waits:
        await wait
    return listDelays
