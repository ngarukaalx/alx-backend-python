#!/usr/bin/env python3
"""Test module for utils.access_nested_map"""

from utils import access_nested_map
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """class to test access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(
            self, nested_map: Mapping,
            path: Sequence, return_val: Any) -> None:
        """Test access_nested_map"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, return_val)


if __name__ == "__main__":
    """run with unittest module"""
    unittest.main()
