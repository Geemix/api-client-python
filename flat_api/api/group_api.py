# coding: utf-8

"""
    Flat API

    The Flat API allows you to easily extend the abilities of the [Flat Platform](https://flat.io), with a wide range of use cases including the following:  * Creating and importing new music scores using MusicXML or MIDI files * Browsing, updating, copying, exporting the user's scores (for example in MP3, WAV or MIDI) * Managing educational resources with Flat for Education: creating & updating the organization accounts, the classes, rosters and assignments.  The Flat API is built on HTTP. Our API is RESTful It has predictable resource URLs. It returns HTTP response codes to indicate errors. It also accepts and returns JSON in the HTTP body. The [schema](/swagger.yaml) of this API follows the [OpenAPI Initiative (OAI) specification](https://www.openapis.org/), you can use and work with [compatible Swagger tools](http://swagger.io/open-source-integrations/). This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/).  You can use your favorite HTTP/REST library for your programming language to use Flat's API. This specification and reference is [available on Github](https://github.com/FlatIO/api-reference).  Getting Started and learn more:  * [API Overview and interoduction](https://flat.io/developers/docs/api/) * [Authentication (Personal Access Tokens or OAuth2)](https://flat.io/developers/docs/api/authentication.html) * [SDKs](https://flat.io/developers/docs/api/sdks.html) * [Rate Limits](https://flat.io/developers/docs/api/rate-limits.html) * [Changelog](https://flat.io/developers/docs/api/changelog.html)   # noqa: E501

    OpenAPI spec version: 2.6.0
    Contact: developers@flat.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from flat_api.api_client import ApiClient


class GroupApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_group_details(self, group, **kwargs):  # noqa: E501
        """Get group information  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_group_details(group, async=True)
        >>> result = thread.get()

        :param async bool
        :param str group: Unique identifier of a Flat group  (required)
        :return: GroupDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_group_details_with_http_info(group, **kwargs)  # noqa: E501
        else:
            (data) = self.get_group_details_with_http_info(group, **kwargs)  # noqa: E501
            return data

    def get_group_details_with_http_info(self, group, **kwargs):  # noqa: E501
        """Get group information  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_group_details_with_http_info(group, async=True)
        >>> result = thread.get()

        :param async bool
        :param str group: Unique identifier of a Flat group  (required)
        :return: GroupDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_group_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group' is set
        if ('group' not in params or
                params['group'] is None):
            raise ValueError("Missing the required parameter `group` when calling `get_group_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group' in params:
            path_params['group'] = params['group']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{group}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GroupDetails',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_group_scores(self, group, **kwargs):  # noqa: E501
        """List group&#39;s scores  # noqa: E501

        Get the list of scores shared with a group.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_group_scores(group, async=True)
        >>> result = thread.get()

        :param async bool
        :param str group: Unique identifier of a Flat group  (required)
        :param str parent: Filter the score forked from the score id `parent`
        :return: list[ScoreDetails]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_group_scores_with_http_info(group, **kwargs)  # noqa: E501
        else:
            (data) = self.get_group_scores_with_http_info(group, **kwargs)  # noqa: E501
            return data

    def get_group_scores_with_http_info(self, group, **kwargs):  # noqa: E501
        """List group&#39;s scores  # noqa: E501

        Get the list of scores shared with a group.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_group_scores_with_http_info(group, async=True)
        >>> result = thread.get()

        :param async bool
        :param str group: Unique identifier of a Flat group  (required)
        :param str parent: Filter the score forked from the score id `parent`
        :return: list[ScoreDetails]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group', 'parent']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_group_scores" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group' is set
        if ('group' not in params or
                params['group'] is None):
            raise ValueError("Missing the required parameter `group` when calling `get_group_scores`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group' in params:
            path_params['group'] = params['group']  # noqa: E501

        query_params = []
        if 'parent' in params:
            query_params.append(('parent', params['parent']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{group}/scores', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ScoreDetails]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_group_users(self, group, **kwargs):  # noqa: E501
        """List group&#39;s users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_group_users(group, async=True)
        >>> result = thread.get()

        :param async bool
        :param str group: Unique identifier of a Flat group  (required)
        :return: list[UserPublic]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_group_users_with_http_info(group, **kwargs)  # noqa: E501
        else:
            (data) = self.list_group_users_with_http_info(group, **kwargs)  # noqa: E501
            return data

    def list_group_users_with_http_info(self, group, **kwargs):  # noqa: E501
        """List group&#39;s users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_group_users_with_http_info(group, async=True)
        >>> result = thread.get()

        :param async bool
        :param str group: Unique identifier of a Flat group  (required)
        :return: list[UserPublic]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_group_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group' is set
        if ('group' not in params or
                params['group'] is None):
            raise ValueError("Missing the required parameter `group` when calling `list_group_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group' in params:
            path_params['group'] = params['group']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{group}/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[UserPublic]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
