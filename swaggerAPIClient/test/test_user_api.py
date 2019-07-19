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
from api.user_api import UserApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_stats_user_username_get(self):
        """Test case for api_v1_stats_user_username_get

        Get detailed stats about user  # noqa: E501
        """
        pass

    def test_api_v1_user_accept_license_license_id_post(self):
        """Test case for api_v1_user_accept_license_license_id_post

        Post to indicate user has accepted license terms  # noqa: E501
        """
        pass

    def test_api_v1_user_id_userid_get(self):
        """Test case for api_v1_user_id_userid_get

        Gets user information by id  # noqa: E501
        """
        pass

    def test_api_v1_user_search_all_get(self):
        """Test case for api_v1_user_search_all_get

        Gets paged list of all usernames  # noqa: E501
        """
        pass

    def test_api_v1_user_search_filter_username_get(self):
        """Test case for api_v1_user_search_filter_username_get

        Gets paged lists of users matching username filter  # noqa: E501
        """
        pass

    def test_api_v1_user_set_expert_mode_is_expert_post(self):
        """Test case for api_v1_user_set_expert_mode_is_expert_post

        Allows user to enable or disable expert mode  # noqa: E501
        """
        pass

    def test_api_v1_user_update_details_post(self):
        """Test case for api_v1_user_update_details_post

        Updates user info  # noqa: E501
        """
        pass

    def test_api_v1_user_username_get(self):
        """Test case for api_v1_user_username_get

        Gets user information  # noqa: E501
        """
        pass

    def test_api_v1_user_username_mapped_projects_get(self):
        """Test case for api_v1_user_username_mapped_projects_get

        Gets projects user has mapped  # noqa: E501
        """
        pass

    def test_api_v1_user_username_osm_details_get(self):
        """Test case for api_v1_user_username_osm_details_get

        Gets details from OSM for the specified username  # noqa: E501
        """
        pass

    def test_api_v1_user_username_set_level_level_post(self):
        """Test case for api_v1_user_username_set_level_level_post

        Allows PMs to set a users mapping level  # noqa: E501
        """
        pass

    def test_api_v1_user_username_set_role_role_post(self):
        """Test case for api_v1_user_username_set_role_role_post

        Allows PMs to set the users role  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()