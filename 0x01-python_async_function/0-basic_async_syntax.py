#!/usr/bin/env python3
"""
This module contains an asyn func
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous corootine
    args: max_delay - int
    """
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
