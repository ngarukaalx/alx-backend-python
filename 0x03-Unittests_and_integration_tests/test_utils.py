#!/usr/bin/env python3
"""Test module for utils.access_nested_map"""

import utils
from utils import access_nested_map, get_json, memoize
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


class TestMemoize(unittest.TestCase):
    """class for testing memoize"""
    def test_memoize(self):
        """function"""
        class TestClass:
            """test class"""
            def a_method(self):
                """returns 42"""
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # path a_method
        with patch.object(
                TestClass,
                'a_method', return_value=42) as mocked_mtd:
            # create instance of TestClass
            class_test = TestClass()

            # call a_property twice
            first = class_test.a_property
            second = class_test.a_property

            # checked a_method was called only once
            mocked_mtd.assert_called_once()

            # Asssert result are correct
            self.assertEqual(first, 42)
            self.assertEqual(second, 42)


if __name__ == "__main__":
    """run with unittest module"""
    unittest.main()
