# swagger_client.ValidationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_project_project_id_lock_for_validation_post**](ValidationApi.md#api_v1_project_project_id_lock_for_validation_post) | **POST** /api/v1/project/{project_id}/lock-for-validation | Lock tasks for validation
[**api_v1_project_project_id_mapped_tasks_by_user_get**](ValidationApi.md#api_v1_project_project_id_mapped_tasks_by_user_get) | **GET** /api/v1/project/{project_id}/mapped-tasks-by-user | Get mapped tasks grouped by user
[**api_v1_project_project_id_stop_validating_post**](ValidationApi.md#api_v1_project_project_id_stop_validating_post) | **POST** /api/v1/project/{project_id}/stop-validating | Unlock tasks that are locked for validation resetting them to their last status
[**api_v1_project_project_id_unlock_after_validation_post**](ValidationApi.md#api_v1_project_project_id_unlock_after_validation_post) | **POST** /api/v1/project/{project_id}/unlock-after-validation | Unlocks tasks after validation completed
[**api_v1_user_username_invalidated_tasks_get**](ValidationApi.md#api_v1_user_username_invalidated_tasks_get) | **GET** /api/v1/user/{username}/invalidated-tasks | Get invalidated tasks either mapped by user or invalidated by user

# **api_v1_project_project_id_lock_for_validation_post**
> api_v1_project_project_id_lock_for_validation_post(body, authorization, accept_language, project_id)

Lock tasks for validation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ValidationApi()
body = NULL # object | JSON object for locking task(s)
authorization = 'authorization_example' # str | Base64 encoded session token
accept_language = 'accept_language_example' # str | Language user is requesting
project_id = 56 # int | The ID of the project the tasks are associated with

try:
    # Lock tasks for validation
    api_instance.api_v1_project_project_id_lock_for_validation_post(body, authorization, accept_language, project_id)
except ApiException as e:
    print("Exception when calling ValidationApi->api_v1_project_project_id_lock_for_validation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON object for locking task(s) | 
 **authorization** | **str**| Base64 encoded session token | 
 **accept_language** | **str**| Language user is requesting | 
 **project_id** | **int**| The ID of the project the tasks are associated with | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_mapped_tasks_by_user_get**
> api_v1_project_project_id_mapped_tasks_by_user_get(project_id)

Get mapped tasks grouped by user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ValidationApi()
project_id = 56 # int | The ID of the project the task is associated with

try:
    # Get mapped tasks grouped by user
    api_instance.api_v1_project_project_id_mapped_tasks_by_user_get(project_id)
except ApiException as e:
    print("Exception when calling ValidationApi->api_v1_project_project_id_mapped_tasks_by_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The ID of the project the task is associated with | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_stop_validating_post**
> api_v1_project_project_id_stop_validating_post(body, authorization, accept_language, project_id)

Unlock tasks that are locked for validation resetting them to their last status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ValidationApi()
body = NULL # object | JSON object for unlocking a task
authorization = 'authorization_example' # str | Base64 encoded session token
accept_language = 'accept_language_example' # str | Language user is requesting
project_id = 56 # int | The ID of the project the task is associated with

try:
    # Unlock tasks that are locked for validation resetting them to their last status
    api_instance.api_v1_project_project_id_stop_validating_post(body, authorization, accept_language, project_id)
except ApiException as e:
    print("Exception when calling ValidationApi->api_v1_project_project_id_stop_validating_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON object for unlocking a task | 
 **authorization** | **str**| Base64 encoded session token | 
 **accept_language** | **str**| Language user is requesting | 
 **project_id** | **int**| The ID of the project the task is associated with | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_unlock_after_validation_post**
> api_v1_project_project_id_unlock_after_validation_post(body, authorization, accept_language, project_id)

Unlocks tasks after validation completed

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ValidationApi()
body = NULL # object | JSON object for unlocking a task
authorization = 'authorization_example' # str | Base64 encoded session token
accept_language = 'accept_language_example' # str | Language user is requesting
project_id = 56 # int | The ID of the project the task is associated with

try:
    # Unlocks tasks after validation completed
    api_instance.api_v1_project_project_id_unlock_after_validation_post(body, authorization, accept_language, project_id)
except ApiException as e:
    print("Exception when calling ValidationApi->api_v1_project_project_id_unlock_after_validation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON object for unlocking a task | 
 **authorization** | **str**| Base64 encoded session token | 
 **accept_language** | **str**| Language user is requesting | 
 **project_id** | **int**| The ID of the project the task is associated with | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_user_username_invalidated_tasks_get**
> api_v1_user_username_invalidated_tasks_get(authorization, accept_language, username, as_validator=as_validator, sort_by=sort_by, sort_direction=sort_direction, page=page, page_size=page_size, project=project, closed=closed)

Get invalidated tasks either mapped by user or invalidated by user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ValidationApi()
authorization = 'authorization_example' # str | Base64 encoded session token
accept_language = 'accept_language_example' # str | Language user is requesting
username = 'username_example' # str | The users username
as_validator = 'as_validator_example' # str | treats user as validator, rather than mapper, if true (optional)
sort_by = 'sort_by_example' # str | field to sort by, defaults to action_date (optional)
sort_direction = 'sort_direction_example' # str | direction of sort, defaults to desc (optional)
page = 56 # int | Page of results user requested (optional)
page_size = 56 # int | Size of page, defaults to 10 (optional)
project = 56 # int | Optional project filter (optional)
closed = true # bool | Optional filter for open/closed invalidations (optional)

try:
    # Get invalidated tasks either mapped by user or invalidated by user
    api_instance.api_v1_user_username_invalidated_tasks_get(authorization, accept_language, username, as_validator=as_validator, sort_by=sort_by, sort_direction=sort_direction, page=page, page_size=page_size, project=project, closed=closed)
except ApiException as e:
    print("Exception when calling ValidationApi->api_v1_user_username_invalidated_tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **accept_language** | **str**| Language user is requesting | 
 **username** | **str**| The users username | 
 **as_validator** | **str**| treats user as validator, rather than mapper, if true | [optional] 
 **sort_by** | **str**| field to sort by, defaults to action_date | [optional] 
 **sort_direction** | **str**| direction of sort, defaults to desc | [optional] 
 **page** | **int**| Page of results user requested | [optional] 
 **page_size** | **int**| Size of page, defaults to 10 | [optional] 
 **project** | **int**| Optional project filter | [optional] 
 **closed** | **bool**| Optional filter for open/closed invalidations | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

