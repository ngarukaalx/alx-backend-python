#!/usr/bin/env python3
"""THis module contains func task_wait_random
"""
import asyncio
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """craeting tasks for async"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
