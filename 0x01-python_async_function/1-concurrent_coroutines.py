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
    for _ in range(n):
        calls = await wait_random(max_delay)
        bisect.insort(listDelays, calls)
    return listDelays
