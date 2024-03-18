#!/usr/bin/env python3
"""
This module contains func measure_time
"""
from time import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures runtime"""
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()
    time_taken = end - start

    return time_taken / n
