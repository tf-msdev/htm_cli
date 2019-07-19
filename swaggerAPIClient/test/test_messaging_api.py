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
from api.messaging_api import MessagingApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMessagingApi(unittest.TestCase):
    """MessagingApi unit test stubs"""

    def setUp(self):
        self.api = api.messaging_api.MessagingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_admin_project_project_id_message_all_post(self):
        """Test case for api_v1_admin_project_project_id_message_all_post

        Send message to all contributors to a project  # noqa: E501
        """
        pass

    def test_api_v1_messages_delete_multiple_delete(self):
        """Test case for api_v1_messages_delete_multiple_delete

        Delete specified messages for logged in user  # noqa: E501
        """
        pass

    def test_api_v1_messages_get_all_messages_get(self):
        """Test case for api_v1_messages_get_all_messages_get

        Get all messages for logged in user  # noqa: E501
        """
        pass

    def test_api_v1_messages_has_new_messages_get(self):
        """Test case for api_v1_messages_has_new_messages_get

        Gets count of unread messages  # noqa: E501
        """
        pass

    def test_api_v1_messages_message_id_delete(self):
        """Test case for api_v1_messages_message_id_delete

        Deletes the specified message  # noqa: E501
        """
        pass

    def test_api_v1_messages_message_id_get(self):
        """Test case for api_v1_messages_message_id_get

        Gets the specified message  # noqa: E501
        """
        pass

    def test_api_v1_messages_resend_email_verification_post(self):
        """Test case for api_v1_messages_resend_email_verification_post

        Resends the validation user to the logged in user  # noqa: E501
        """
        pass

    def test_api_v1_project_project_id_chat_get(self):
        """Test case for api_v1_project_project_id_chat_get

        Get all chat messages for project  # noqa: E501
        """
        pass

    def test_api_v1_project_project_id_chat_put(self):
        """Test case for api_v1_project_project_id_chat_put

        Add a message to project chat  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()