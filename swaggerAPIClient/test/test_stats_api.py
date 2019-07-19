# coding: utf-8

"""
    HOT Tasking Manager API

    API endpoints for the HOT tasking manager  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.stats_api import StatsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestStatsApi(unittest.TestCase):
    """StatsApi unit test stubs"""

    def setUp(self):
        self.api = api.stats_api.StatsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_stats_project_project_id_activity_get(self):
        """Test case for api_v1_stats_project_project_id_activity_get

        Get user actvity on a project  # noqa: E501
        """
        pass

    def test_api_v1_stats_project_project_id_contributions_get(self):
        """Test case for api_v1_stats_project_project_id_contributions_get

        Get all user contributions on a project  # noqa: E501
        """
        pass

    def test_api_v1_stats_project_project_id_get(self):
        """Test case for api_v1_stats_project_project_id_get

        Get Project Stats  # noqa: E501
        """
        pass

    def test_api_v1_stats_summary_get(self):
        """Test case for api_v1_stats_summary_get

        Get HomePage Stats  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
