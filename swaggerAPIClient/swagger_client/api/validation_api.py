# coding: utf-8

"""
    HOT Tasking Manager API

    API endpoints for the HOT tasking manager  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ValidationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v1_project_project_id_lock_for_validation_post(self, body, authorization, accept_language, project_id, **kwargs):  # noqa: E501
        """Lock tasks for validation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_project_project_id_lock_for_validation_post(body, authorization, accept_language, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: JSON object for locking task(s) (required)
        :param str authorization: Base64 encoded session token (required)
        :param str accept_language: Language user is requesting (required)
        :param int project_id: The ID of the project the tasks are associated with (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_project_project_id_lock_for_validation_post_with_http_info(body, authorization, accept_language, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_project_project_id_lock_for_validation_post_with_http_info(body, authorization, accept_language, project_id, **kwargs)  # noqa: E501
            return data

    def api_v1_project_project_id_lock_for_validation_post_with_http_info(self, body, authorization, accept_language, project_id, **kwargs):  # noqa: E501
        """Lock tasks for validation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_project_project_id_lock_for_validation_post_with_http_info(body, authorization, accept_language, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: JSON object for locking task(s) (required)
        :param str authorization: Base64 encoded session token (required)
        :param str accept_language: Language user is requesting (required)
        :param int project_id: The ID of the project the tasks are associated with (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization', 'accept_language', 'project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_project_project_id_lock_for_validation_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_v1_project_project_id_lock_for_validation_post`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `api_v1_project_project_id_lock_for_validation_post`")  # noqa: E501
        # verify the required parameter 'accept_language' is set
        if ('accept_language' not in params or
                params['accept_language'] is None):
            raise ValueError("Missing the required parameter `accept_language` when calling `api_v1_project_project_id_lock_for_validation_post`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `api_v1_project_project_id_lock_for_validation_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['project_id'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/project/{project_id}/lock-for-validation', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_project_project_id_mapped_tasks_by_user_get(self, project_id, **kwargs):  # noqa: E501
        """Get mapped tasks grouped by user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_project_project_id_mapped_tasks_by_user_get(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: The ID of the project the task is associated with (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_project_project_id_mapped_tasks_by_user_get_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_project_project_id_mapped_tasks_by_user_get_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def api_v1_project_project_id_mapped_tasks_by_user_get_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """Get mapped tasks grouped by user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_project_project_id_mapped_tasks_by_user_get_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: The ID of the project the task is associated with (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_project_project_id_mapped_tasks_by_user_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `api_v1_project_project_id_mapped_tasks_by_user_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['project_id'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/project/{project_id}/mapped-tasks-by-user', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_project_project_id_stop_validating_post(self, body, authorization, accept_language, project_id, **kwargs):  # noqa: E501
        """Unlock tasks that are locked for validation resetting them to their last status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_project_project_id_stop_validating_post(body, authorization, accept_language, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: JSON object for unlocking a task (required)
        :param str authorization: Base64 encoded session token (required)
        :param str accept_language: Language user is requesting (required)
        :param int project_id: The ID of the project the task is associated with (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_project_project_id_stop_validating_post_with_http_info(body, authorization, accept_language, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_project_project_id_stop_validating_post_with_http_info(body, authorization, accept_language, project_id, **kwargs)  # noqa: E501
            return data

    def api_v1_project_project_id_stop_validating_post_with_http_info(self, body, authorization, accept_language, project_id, **kwargs):  # noqa: E501
        """Unlock tasks that are locked for validation resetting them to their last status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_project_project_id_stop_validating_post_with_http_info(body, authorization, accept_language, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: JSON object for unlocking a task (required)
        :param str authorization: Base64 encoded session token (required)
        :param str accept_language: Language user is requesting (required)
        :param int project_id: The ID of the project the task is associated with (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization', 'accept_language', 'project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_project_project_id_stop_validating_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_v1_project_project_id_stop_validating_post`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `api_v1_project_project_id_stop_validating_post`")  # noqa: E501
        # verify the required parameter 'accept_language' is set
        if ('accept_language' not in params or
                params['accept_language'] is None):
            raise ValueError("Missing the required parameter `accept_language` when calling `api_v1_project_project_id_stop_validating_post`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `api_v1_project_project_id_stop_validating_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['project_id'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/project/{project_id}/stop-validating', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_project_project_id_unlock_after_validation_post(self, body, authorization, accept_language, project_id, **kwargs):  # noqa: E501
        """Unlocks tasks after validation completed  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_project_project_id_unlock_after_validation_post(body, authorization, accept_language, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: JSON object for unlocking a task (required)
        :param str authorization: Base64 encoded session token (required)
        :param str accept_language: Language user is requesting (required)
        :param int project_id: The ID of the project the task is associated with (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_project_project_id_unlock_after_validation_post_with_http_info(body, authorization, accept_language, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_project_project_id_unlock_after_validation_post_with_http_info(body, authorization, accept_language, project_id, **kwargs)  # noqa: E501
            return data

    def api_v1_project_project_id_unlock_after_validation_post_with_http_info(self, body, authorization, accept_language, project_id, **kwargs):  # noqa: E501
        """Unlocks tasks after validation completed  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_project_project_id_unlock_after_validation_post_with_http_info(body, authorization, accept_language, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: JSON object for unlocking a task (required)
        :param str authorization: Base64 encoded session token (required)
        :param str accept_language: Language user is requesting (required)
        :param int project_id: The ID of the project the task is associated with (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization', 'accept_language', 'project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_project_project_id_unlock_after_validation_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_v1_project_project_id_unlock_after_validation_post`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `api_v1_project_project_id_unlock_after_validation_post`")  # noqa: E501
        # verify the required parameter 'accept_language' is set
        if ('accept_language' not in params or
                params['accept_language'] is None):
            raise ValueError("Missing the required parameter `accept_language` when calling `api_v1_project_project_id_unlock_after_validation_post`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `api_v1_project_project_id_unlock_after_validation_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['project_id'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/project/{project_id}/unlock-after-validation', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v1_user_username_invalidated_tasks_get(self, authorization, accept_language, username, **kwargs):  # noqa: E501
        """Get invalidated tasks either mapped by user or invalidated by user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_user_username_invalidated_tasks_get(authorization, accept_language, username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Base64 encoded session token (required)
        :param str accept_language: Language user is requesting (required)
        :param str username: The users username (required)
        :param str as_validator: treats user as validator, rather than mapper, if true
        :param str sort_by: field to sort by, defaults to action_date
        :param str sort_direction: direction of sort, defaults to desc
        :param int page: Page of results user requested
        :param int page_size: Size of page, defaults to 10
        :param int project: Optional project filter
        :param bool closed: Optional filter for open/closed invalidations
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_user_username_invalidated_tasks_get_with_http_info(authorization, accept_language, username, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_user_username_invalidated_tasks_get_with_http_info(authorization, accept_language, username, **kwargs)  # noqa: E501
            return data

    def api_v1_user_username_invalidated_tasks_get_with_http_info(self, authorization, accept_language, username, **kwargs):  # noqa: E501
        """Get invalidated tasks either mapped by user or invalidated by user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_user_username_invalidated_tasks_get_with_http_info(authorization, accept_language, username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Base64 encoded session token (required)
        :param str accept_language: Language user is requesting (required)
        :param str username: The users username (required)
        :param str as_validator: treats user as validator, rather than mapper, if true
        :param str sort_by: field to sort by, defaults to action_date
        :param str sort_direction: direction of sort, defaults to desc
        :param int page: Page of results user requested
        :param int page_size: Size of page, defaults to 10
        :param int project: Optional project filter
        :param bool closed: Optional filter for open/closed invalidations
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'accept_language', 'username', 'as_validator', 'sort_by', 'sort_direction', 'page', 'page_size', 'project', 'closed']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_user_username_invalidated_tasks_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `api_v1_user_username_invalidated_tasks_get`")  # noqa: E501
        # verify the required parameter 'accept_language' is set
        if ('accept_language' not in params or
                params['accept_language'] is None):
            raise ValueError("Missing the required parameter `accept_language` when calling `api_v1_user_username_invalidated_tasks_get`")  # noqa: E501
        # verify the required parameter 'username' is set
        if ('username' not in params or
                params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `api_v1_user_username_invalidated_tasks_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']  # noqa: E501

        query_params = []
        if 'as_validator' in params:
            query_params.append(('asValidator', params['as_validator']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sortBy', params['sort_by']))  # noqa: E501
        if 'sort_direction' in params:
            query_params.append(('sortDirection', params['sort_direction']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'project' in params:
            query_params.append(('project', params['project']))  # noqa: E501
        if 'closed' in params:
            query_params.append(('closed', params['closed']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/user/{username}/invalidated-tasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)