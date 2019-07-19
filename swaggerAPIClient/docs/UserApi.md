# swagger_client.UserApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_stats_user_username_get**](UserApi.md#api_v1_stats_user_username_get) | **GET** /api/v1/stats/user/{username} | Get detailed stats about user
[**api_v1_user_accept_license_license_id_post**](UserApi.md#api_v1_user_accept_license_license_id_post) | **POST** /api/v1/user/accept-license/{license_id} | Post to indicate user has accepted license terms
[**api_v1_user_id_userid_get**](UserApi.md#api_v1_user_id_userid_get) | **GET** /api/v1/user-id/{userid} | Gets user information by id
[**api_v1_user_search_all_get**](UserApi.md#api_v1_user_search_all_get) | **GET** /api/v1/user/search-all | Gets paged list of all usernames
[**api_v1_user_search_filter_username_get**](UserApi.md#api_v1_user_search_filter_username_get) | **GET** /api/v1/user/search/filter/{username} | Gets paged lists of users matching username filter
[**api_v1_user_set_expert_mode_is_expert_post**](UserApi.md#api_v1_user_set_expert_mode_is_expert_post) | **POST** /api/v1/user/set-expert-mode/{is_expert} | Allows user to enable or disable expert mode
[**api_v1_user_update_details_post**](UserApi.md#api_v1_user_update_details_post) | **POST** /api/v1/user/update-details | Updates user info
[**api_v1_user_username_get**](UserApi.md#api_v1_user_username_get) | **GET** /api/v1/user/{username} | Gets user information
[**api_v1_user_username_mapped_projects_get**](UserApi.md#api_v1_user_username_mapped_projects_get) | **GET** /api/v1/user/{username}/mapped-projects | Gets projects user has mapped
[**api_v1_user_username_osm_details_get**](UserApi.md#api_v1_user_username_osm_details_get) | **GET** /api/v1/user/{username}/osm-details | Gets details from OSM for the specified username
[**api_v1_user_username_set_level_level_post**](UserApi.md#api_v1_user_username_set_level_level_post) | **POST** /api/v1/user/{username}/set-level/{level} | Allows PMs to set a users mapping level
[**api_v1_user_username_set_role_role_post**](UserApi.md#api_v1_user_username_set_role_role_post) | **POST** /api/v1/user/{username}/set-role/{role} | Allows PMs to set the users role

# **api_v1_stats_user_username_get**
> api_v1_stats_user_username_get(username)

Get detailed stats about user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
username = 'username_example' # str | The users username

try:
    # Get detailed stats about user
    api_instance.api_v1_stats_user_username_get(username)
except ApiException as e:
    print("Exception when calling UserApi->api_v1_stats_user_username_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The users username | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_user_accept_license_license_id_post**
> api_v1_user_accept_license_license_id_post(authorization, license_id)

Post to indicate user has accepted license terms

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
authorization = 'authorization_example' # str | Base64 encoded session token
license_id = 56 # int | ID of license terms have been accepted for

try:
    # Post to indicate user has accepted license terms
    api_instance.api_v1_user_accept_license_license_id_post(authorization, license_id)
except ApiException as e:
    print("Exception when calling UserApi->api_v1_user_accept_license_license_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **license_id** | **int**| ID of license terms have been accepted for | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_user_id_userid_get**
> api_v1_user_id_userid_get(authorization, userid)

Gets user information by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
authorization = 'authorization_example' # str | Base64 encoded sesesion token
userid = 56 # int | The users user id

try:
    # Gets user information by id
    api_instance.api_v1_user_id_userid_get(authorization, userid)
except ApiException as e:
    print("Exception when calling UserApi->api_v1_user_id_userid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded sesesion token | 
 **userid** | **int**| The users user id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_user_search_all_get**
> api_v1_user_search_all_get(page=page, username=username, role=role, level=level)

Gets paged list of all usernames

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
page = 56 # int | Page of results user requested (optional)
username = 56 # int | Full or part username (optional)
role = 'role_example' # str | Role of User, eg ADMIN, PROJECT_MANAGER (optional)
level = 'level_example' # str | Level of User, eg BEGINNER (optional)

try:
    # Gets paged list of all usernames
    api_instance.api_v1_user_search_all_get(page=page, username=username, role=role, level=level)
except ApiException as e:
    print("Exception when calling UserApi->api_v1_user_search_all_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page of results user requested | [optional] 
 **username** | **int**| Full or part username | [optional] 
 **role** | **str**| Role of User, eg ADMIN, PROJECT_MANAGER | [optional] 
 **level** | **str**| Level of User, eg BEGINNER | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_user_search_filter_username_get**
> api_v1_user_search_filter_username_get(username, page=page, project_id=project_id)

Gets paged lists of users matching username filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
username = 'username_example' # str | Partial or full username
page = 56 # int | Page of results user requested (optional)
project_id = 56 # int | Optional, promote project participants to head of results (optional)

try:
    # Gets paged lists of users matching username filter
    api_instance.api_v1_user_search_filter_username_get(username, page=page, project_id=project_id)
except ApiException as e:
    print("Exception when calling UserApi->api_v1_user_search_filter_username_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Partial or full username | 
 **page** | **int**| Page of results user requested | [optional] 
 **project_id** | **int**| Optional, promote project participants to head of results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_user_set_expert_mode_is_expert_post**
> api_v1_user_set_expert_mode_is_expert_post(authorization, is_expert)

Allows user to enable or disable expert mode

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
authorization = 'authorization_example' # str | Base64 encoded session token
is_expert = 'is_expert_example' # str | true to enable expert mode, false to disable

try:
    # Allows user to enable or disable expert mode
    api_instance.api_v1_user_set_expert_mode_is_expert_post(authorization, is_expert)
except ApiException as e:
    print("Exception when calling UserApi->api_v1_user_set_expert_mode_is_expert_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **is_expert** | **str**| true to enable expert mode, false to disable | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_user_update_details_post**
> api_v1_user_update_details_post(body, authorization)

Updates user info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
body = NULL # object | JSON object for creating draft project
authorization = 'authorization_example' # str | Base64 encoded session token

try:
    # Updates user info
    api_instance.api_v1_user_update_details_post(body, authorization)
except ApiException as e:
    print("Exception when calling UserApi->api_v1_user_update_details_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON object for creating draft project | 
 **authorization** | **str**| Base64 encoded session token | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_user_username_get**
> api_v1_user_username_get(authorization, username)

Gets user information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
authorization = 'authorization_example' # str | Base64 encoded session token
username = 'username_example' # str | The users username

try:
    # Gets user information
    api_instance.api_v1_user_username_get(authorization, username)
except ApiException as e:
    print("Exception when calling UserApi->api_v1_user_username_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **username** | **str**| The users username | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_user_username_mapped_projects_get**
> api_v1_user_username_mapped_projects_get(accept_language, username)

Gets projects user has mapped

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
accept_language = 'accept_language_example' # str | Language user is requesting
username = 'username_example' # str | The users username

try:
    # Gets projects user has mapped
    api_instance.api_v1_user_username_mapped_projects_get(accept_language, username)
except ApiException as e:
    print("Exception when calling UserApi->api_v1_user_username_mapped_projects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language user is requesting | 
 **username** | **str**| The users username | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_user_username_osm_details_get**
> api_v1_user_username_osm_details_get(username)

Gets details from OSM for the specified username

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
username = 'username_example' # str | The users username

try:
    # Gets details from OSM for the specified username
    api_instance.api_v1_user_username_osm_details_get(username)
except ApiException as e:
    print("Exception when calling UserApi->api_v1_user_username_osm_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The users username | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_user_username_set_level_level_post**
> api_v1_user_username_set_level_level_post(authorization, username, level)

Allows PMs to set a users mapping level

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
authorization = 'authorization_example' # str | Base64 encoded session token
username = 'username_example' # str | The users username
level = 'level_example' # str | The mapping level that should be set

try:
    # Allows PMs to set a users mapping level
    api_instance.api_v1_user_username_set_level_level_post(authorization, username, level)
except ApiException as e:
    print("Exception when calling UserApi->api_v1_user_username_set_level_level_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **username** | **str**| The users username | 
 **level** | **str**| The mapping level that should be set | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_user_username_set_role_role_post**
> api_v1_user_username_set_role_role_post(authorization, username, role)

Allows PMs to set the users role

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
authorization = 'authorization_example' # str | Base64 encoded session token
username = 'username_example' # str | The users username
role = 'role_example' # str | The role to add

try:
    # Allows PMs to set the users role
    api_instance.api_v1_user_username_set_role_role_post(authorization, username, role)
except ApiException as e:
    print("Exception when calling UserApi->api_v1_user_username_set_role_role_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **username** | **str**| The users username | 
 **role** | **str**| The role to add | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

