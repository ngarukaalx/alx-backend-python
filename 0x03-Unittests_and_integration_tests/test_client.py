#!/usr/bin/env python3
"""Test client.GithubbOrgClient"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, MagicMock, PropertyMock
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """class to test GithubOrgClient"""
    @parameterized.expand([
        ("google",),
        ("abc",)
        ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json) -> None:
        """test that GithubOrgClient.org returns the correct value"""
        # mock response from get_json
        mock_get_json.return_value = "fine"

        # instance of GithubOrgClient
        instance = GithubOrgClient(org_name)

        # call org
        result = instance.org

        mock_get_json.assert_called_once_with(
                GithubOrgClient.ORG_URL.format(org=org_name))
        self.assertEqual(result, "fine")

    def test_public_repos_url(self) -> None:
        """unit test _pupblic_repos_url"""
        expected_value = {"repos_url": "https://api.github.com/repos"}
        with patch.object(GithubOrgClient, 'org',
                          PropertyMock(return_value=expected_value)):
            instance = GithubOrgClient("org_name")
            result = instance._public_repos_url

            # test result is expected payload
            self.assertEqual(result, expected_value['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json) -> None:
        """Test public_repos """
        hiram = {"name": "exhausted", "license": {"key": "v"}}
        girlfriend = {"name": "searching"}
        money = {"name": "scanning"}

        mock_get_json.return_value = [hiram, girlfriend, money]

        with patch.object(GithubOrgClient, '_public_repos_url',
                          PropertyMock(return_value="wwwww")) as rep:
            instance = GithubOrgClient("org_name")
            result = instance.public_repos()
            self.assertEqual(result, ['exhausted', 'searching', 'scanning'])
            mock_get_json.assert_called_once()
            rep.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo: Dict[str, Dict],
                         license_key: str, licence) -> None:
        """test has_license"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         licence)


if __name__ == "__main__":
    """run tests"""
    unittest.main()
