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


class MappingIssuesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v1_mapping_issue_categories_get(self, **kwargs):  # noqa: E501
        """Gets all mapping issue categories  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_mapping_issue_categories_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool include_archived: Optional filter to include archived categories
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_mapping_issue_categories_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_mapping_issue_categories_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v1_mapping_issue_categories_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets all mapping issue categories  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_mapping_issue_categories_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool include_archived: Optional filter to include archived categories
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include_archived']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_mapping_issue_categories_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include_archived' in params:
            query_params.append(('includeArchived', params['include_archived']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/mapping-issue-categories', 'GET',
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

    def api_v1_mapping_issue_category_category_id_delete(self, authorization, category_id, **kwargs):  # noqa: E501
        """Delete the specified mapping-issue category. Note that categories can  # noqa: E501

        be deleted only if they have never been associated with a task. To<br/>instead archive a used category that is no longer needed, update the<br/>category with its archived flag set to true.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_mapping_issue_category_category_id_delete(authorization, category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Base64 encoded session token (required)
        :param int category_id: The unique mapping-issue category ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_mapping_issue_category_category_id_delete_with_http_info(authorization, category_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_mapping_issue_category_category_id_delete_with_http_info(authorization, category_id, **kwargs)  # noqa: E501
            return data

    def api_v1_mapping_issue_category_category_id_delete_with_http_info(self, authorization, category_id, **kwargs):  # noqa: E501
        """Delete the specified mapping-issue category. Note that categories can  # noqa: E501

        be deleted only if they have never been associated with a task. To<br/>instead archive a used category that is no longer needed, update the<br/>category with its archived flag set to true.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_mapping_issue_category_category_id_delete_with_http_info(authorization, category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Base64 encoded session token (required)
        :param int category_id: The unique mapping-issue category ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'category_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_mapping_issue_category_category_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `api_v1_mapping_issue_category_category_id_delete`")  # noqa: E501
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params or
                params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `api_v1_mapping_issue_category_category_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'category_id' in params:
            path_params['category_id'] = params['category_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/mapping-issue-category/{category_id}', 'DELETE',
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

    def api_v1_mapping_issue_category_category_id_get(self, category_id, **kwargs):  # noqa: E501
        """Get specified mapping-issue category  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_mapping_issue_category_category_id_get(category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int category_id: The unique mapping-issue category ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_mapping_issue_category_category_id_get_with_http_info(category_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_mapping_issue_category_category_id_get_with_http_info(category_id, **kwargs)  # noqa: E501
            return data

    def api_v1_mapping_issue_category_category_id_get_with_http_info(self, category_id, **kwargs):  # noqa: E501
        """Get specified mapping-issue category  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_mapping_issue_category_category_id_get_with_http_info(category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int category_id: The unique mapping-issue category ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_mapping_issue_category_category_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params or
                params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `api_v1_mapping_issue_category_category_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'category_id' in params:
            path_params['category_id'] = params['category_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/mapping-issue-category/{category_id}', 'GET',
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

    def api_v1_mapping_issue_category_category_id_put(self, body, authorization, category_id, **kwargs):  # noqa: E501
        """Update an existing mapping-issue category  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_mapping_issue_category_category_id_put(body, authorization, category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: JSON object for updating a mapping-issue category (required)
        :param str authorization: Base64 encoded session token (required)
        :param int category_id: The unique mapping-issue category ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_mapping_issue_category_category_id_put_with_http_info(body, authorization, category_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_mapping_issue_category_category_id_put_with_http_info(body, authorization, category_id, **kwargs)  # noqa: E501
            return data

    def api_v1_mapping_issue_category_category_id_put_with_http_info(self, body, authorization, category_id, **kwargs):  # noqa: E501
        """Update an existing mapping-issue category  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_mapping_issue_category_category_id_put_with_http_info(body, authorization, category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: JSON object for updating a mapping-issue category (required)
        :param str authorization: Base64 encoded session token (required)
        :param int category_id: The unique mapping-issue category ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization', 'category_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_mapping_issue_category_category_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_v1_mapping_issue_category_category_id_put`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `api_v1_mapping_issue_category_category_id_put`")  # noqa: E501
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params or
                params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `api_v1_mapping_issue_category_category_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'category_id' in params:
            path_params['category_id'] = params['category_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

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
            '/api/v1/mapping-issue-category/{category_id}', 'PUT',
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

    def api_v1_mapping_issue_category_post(self, body, authorization, **kwargs):  # noqa: E501
        """Creates a new mapping-issue category  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_mapping_issue_category_post(body, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: JSON object for creating a new mapping-issue category (required)
        :param str authorization: Base64 encoded session token (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v1_mapping_issue_category_post_with_http_info(body, authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v1_mapping_issue_category_post_with_http_info(body, authorization, **kwargs)  # noqa: E501
            return data

    def api_v1_mapping_issue_category_post_with_http_info(self, body, authorization, **kwargs):  # noqa: E501
        """Creates a new mapping-issue category  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v1_mapping_issue_category_post_with_http_info(body, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: JSON object for creating a new mapping-issue category (required)
        :param str authorization: Base64 encoded session token (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_mapping_issue_category_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `api_v1_mapping_issue_category_post`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `api_v1_mapping_issue_category_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

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
            '/api/v1/mapping-issue-category', 'POST',
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