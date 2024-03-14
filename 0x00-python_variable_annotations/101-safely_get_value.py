#!/usr/bin/env python3
"""This module contains func safely_get_value"""
from typing import Any, Union, TypeVar, Mapping
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,  key: Any, default: Union[T, None]) -> Union[Any, T]:
    """Fuction typed"""
    if key in dct:
        return dct[key]
    else:
        return default
