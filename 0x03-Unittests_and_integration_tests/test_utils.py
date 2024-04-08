#!/usr/bin/env python3
"""Test module for utils.access_nested_map"""

from utils import access_nested_map, get_json
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Dict
from unittest.mock import patch, Mock


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping,
            path: Sequence) -> None:
        """Test that KeyError is raised"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class for testing get_json"""
    @parameterized.expand([
        (("http://example.com"), {"payload": True}),
        (("http://holberton.io"), {"payload": False})
        ])
    @patch('utils.requests.get')
    def test_get_json(
            self, test_usr: str,
            test_payload: Dict, mock_get: Mock) -> Dict:
        """Test that utils.get_json returns expected results"""
        # create a mock obj with a json method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_usr)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_usr)


if __name__ == "__main__":
    """run with unittest module"""
    unittest.main()
