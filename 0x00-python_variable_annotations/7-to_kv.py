#!/usr/bin/env python3
"""This module contains fcn to_kv
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function to return anotated tuple
    Returns a tuple
    """
    return (k, v ** 2)
