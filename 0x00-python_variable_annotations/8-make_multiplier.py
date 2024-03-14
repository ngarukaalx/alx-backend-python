#!/usr/bin/env python3
"""This module contains fnc make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ takes a float multiplier as argument
    and returns a function that multiplies a
    float by multiplier.
    """
    def mul(f: float) -> float:
        return f * multiplier
    return mul
