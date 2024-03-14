#!/usr/bin/python3
"""This module contains sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes mix of ints and floats
    args: mxd_lst - list of floats or ints
    returns: sum of list
    """
    return sum(mxd_lst)
