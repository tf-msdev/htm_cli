# swagger_client.MappingApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_project_project_id_aoi_get**](MappingApi.md#api_v1_project_project_id_aoi_get) | **GET** /api/v1/project/{project_id}/aoi | Get AOI of Project
[**api_v1_project_project_id_get**](MappingApi.md#api_v1_project_project_id_get) | **GET** /api/v1/project/{project_id} | Get HOT Project for mapping
[**api_v1_project_project_id_has_user_locked_tasks_details_get**](MappingApi.md#api_v1_project_project_id_has_user_locked_tasks_details_get) | **GET** /api/v1/project/{project_id}/has-user-locked-tasks/details | Gets details of any locked task on the project from logged in user
[**api_v1_project_project_id_has_user_locked_tasks_get**](MappingApi.md#api_v1_project_project_id_has_user_locked_tasks_get) | **GET** /api/v1/project/{project_id}/has-user-locked-tasks | Gets any locked task on the project from logged in user
[**api_v1_project_project_id_summary_get**](MappingApi.md#api_v1_project_project_id_summary_get) | **GET** /api/v1/project/{project_id}/summary | Gets project summary
[**api_v1_project_project_id_task_task_id_comment_post**](MappingApi.md#api_v1_project_project_id_task_task_id_comment_post) | **POST** /api/v1/project/{project_id}/task/{task_id}/comment | Adds a comment to the task outside of mapping/validation
[**api_v1_project_project_id_task_task_id_get**](MappingApi.md#api_v1_project_project_id_task_task_id_get) | **GET** /api/v1/project/{project_id}/task/{task_id} | Get task for mapping
[**api_v1_project_project_id_task_task_id_lock_for_mapping_post**](MappingApi.md#api_v1_project_project_id_task_task_id_lock_for_mapping_post) | **POST** /api/v1/project/{project_id}/task/{task_id}/lock-for-mapping | Locks the task for mapping
[**api_v1_project_project_id_task_task_id_stop_mapping_post**](MappingApi.md#api_v1_project_project_id_task_task_id_stop_mapping_post) | **POST** /api/v1/project/{project_id}/task/{task_id}/stop-mapping | Unlock task that is locked for mapping resetting it to it&#x27;s last status
[**api_v1_project_project_id_task_task_id_undo_mapping_post**](MappingApi.md#api_v1_project_project_id_task_task_id_undo_mapping_post) | **POST** /api/v1/project/{project_id}/task/{task_id}/undo-mapping | Get task for mapping
[**api_v1_project_project_id_task_task_id_unlock_after_mapping_post**](MappingApi.md#api_v1_project_project_id_task_task_id_unlock_after_mapping_post) | **POST** /api/v1/project/{project_id}/task/{task_id}/unlock-after-mapping | Unlocks the task after mapping completed
[**api_v1_project_project_id_tasks_as_gpx_get**](MappingApi.md#api_v1_project_project_id_tasks_as_gpx_get) | **GET** /api/v1/project/{project_id}/tasks_as_gpx | Get tasks as GPX
[**api_v1_project_project_id_tasks_as_osm_xml_get**](MappingApi.md#api_v1_project_project_id_tasks_as_osm_xml_get) | **GET** /api/v1/project/{project_id}/tasks-as-osm-xml | Get tasks as OSM XML
[**api_v1_project_project_id_tasks_get**](MappingApi.md#api_v1_project_project_id_tasks_get) | **GET** /api/v1/project/{project_id}/tasks | Get tasks as JSON

# **api_v1_project_project_id_aoi_get**
> api_v1_project_project_id_aoi_get(project_id, as_file=as_file)

Get AOI of Project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingApi()
project_id = 56 # int | The unique project ID
as_file = true # bool | Set to false if file download not preferred (optional)

try:
    # Get AOI of Project
    api_instance.api_v1_project_project_id_aoi_get(project_id, as_file=as_file)
except ApiException as e:
    print("Exception when calling MappingApi->api_v1_project_project_id_aoi_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The unique project ID | 
 **as_file** | **bool**| Set to false if file download not preferred | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_get**
> api_v1_project_project_id_get(accept_language, project_id, as_file=as_file, abbreviated=abbreviated)

Get HOT Project for mapping

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingApi()
accept_language = 'accept_language_example' # str | Language user is requesting
project_id = 56 # int | The unique project ID
as_file = true # bool | Set to true if file download is preferred (optional)
abbreviated = true # bool | Set to true if only state information is desired (optional)

try:
    # Get HOT Project for mapping
    api_instance.api_v1_project_project_id_get(accept_language, project_id, as_file=as_file, abbreviated=abbreviated)
except ApiException as e:
    print("Exception when calling MappingApi->api_v1_project_project_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language user is requesting | 
 **project_id** | **int**| The unique project ID | 
 **as_file** | **bool**| Set to true if file download is preferred | [optional] 
 **abbreviated** | **bool**| Set to true if only state information is desired | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_has_user_locked_tasks_details_get**
> api_v1_project_project_id_has_user_locked_tasks_details_get(authorization, accept_language, project_id)

Gets details of any locked task on the project from logged in user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingApi()
authorization = 'authorization_example' # str | Base64 encoded session token
accept_language = 'accept_language_example' # str | Language user is requesting
project_id = 56 # int | The ID of the project the task is associated with

try:
    # Gets details of any locked task on the project from logged in user
    api_instance.api_v1_project_project_id_has_user_locked_tasks_details_get(authorization, accept_language, project_id)
except ApiException as e:
    print("Exception when calling MappingApi->api_v1_project_project_id_has_user_locked_tasks_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **accept_language** | **str**| Language user is requesting | 
 **project_id** | **int**| The ID of the project the task is associated with | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_has_user_locked_tasks_get**
> api_v1_project_project_id_has_user_locked_tasks_get(authorization, project_id)

Gets any locked task on the project from logged in user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingApi()
authorization = 'authorization_example' # str | Base64 encoded session token
project_id = 56 # int | The ID of the project the task is associated with

try:
    # Gets any locked task on the project from logged in user
    api_instance.api_v1_project_project_id_has_user_locked_tasks_get(authorization, project_id)
except ApiException as e:
    print("Exception when calling MappingApi->api_v1_project_project_id_has_user_locked_tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **project_id** | **int**| The ID of the project the task is associated with | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_summary_get**
> api_v1_project_project_id_summary_get(accept_language, project_id)

Gets project summary

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingApi()
accept_language = 'accept_language_example' # str | Language user is requesting
project_id = 56 # int | The ID of the project

try:
    # Gets project summary
    api_instance.api_v1_project_project_id_summary_get(accept_language, project_id)
except ApiException as e:
    print("Exception when calling MappingApi->api_v1_project_project_id_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language user is requesting | 
 **project_id** | **int**| The ID of the project | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_task_task_id_comment_post**
> api_v1_project_project_id_task_task_id_comment_post(body, authorization, project_id, task_id)

Adds a comment to the task outside of mapping/validation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingApi()
body = swagger_client.TaskComment() # TaskComment | JSON object representing the comment
authorization = 'authorization_example' # str | Base64 encoded session token
project_id = 56 # int | The ID of the project the task is associated with
task_id = 56 # int | The unique task ID

try:
    # Adds a comment to the task outside of mapping/validation
    api_instance.api_v1_project_project_id_task_task_id_comment_post(body, authorization, project_id, task_id)
except ApiException as e:
    print("Exception when calling MappingApi->api_v1_project_project_id_task_task_id_comment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskComment**](TaskComment.md)| JSON object representing the comment | 
 **authorization** | **str**| Base64 encoded session token | 
 **project_id** | **int**| The ID of the project the task is associated with | 
 **task_id** | **int**| The unique task ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_task_task_id_get**
> api_v1_project_project_id_task_task_id_get(accept_language, project_id, task_id, authorization=authorization)

Get task for mapping

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingApi()
accept_language = 'accept_language_example' # str | Language user is requesting
project_id = 56 # int | The ID of the project the task is associated with
task_id = 56 # int | The unique task ID
authorization = 'authorization_example' # str | Base64 encoded session token (optional)

try:
    # Get task for mapping
    api_instance.api_v1_project_project_id_task_task_id_get(accept_language, project_id, task_id, authorization=authorization)
except ApiException as e:
    print("Exception when calling MappingApi->api_v1_project_project_id_task_task_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language user is requesting | 
 **project_id** | **int**| The ID of the project the task is associated with | 
 **task_id** | **int**| The unique task ID | 
 **authorization** | **str**| Base64 encoded session token | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_task_task_id_lock_for_mapping_post**
> api_v1_project_project_id_task_task_id_lock_for_mapping_post(authorization, accept_language, project_id, task_id)

Locks the task for mapping

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingApi()
authorization = 'authorization_example' # str | Base64 encoded session token
accept_language = 'accept_language_example' # str | Language user is requesting
project_id = 56 # int | The ID of the project the task is associated with
task_id = 56 # int | The unique task ID

try:
    # Locks the task for mapping
    api_instance.api_v1_project_project_id_task_task_id_lock_for_mapping_post(authorization, accept_language, project_id, task_id)
except ApiException as e:
    print("Exception when calling MappingApi->api_v1_project_project_id_task_task_id_lock_for_mapping_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **accept_language** | **str**| Language user is requesting | 
 **project_id** | **int**| The ID of the project the task is associated with | 
 **task_id** | **int**| The unique task ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_task_task_id_stop_mapping_post**
> api_v1_project_project_id_task_task_id_stop_mapping_post(body, authorization, accept_language, project_id, task_id)

Unlock task that is locked for mapping resetting it to it's last status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingApi()
body = swagger_client.TaskUpdateStop() # TaskUpdateStop | JSON object for unlocking a task
authorization = 'authorization_example' # str | Base64 encoded session token
accept_language = 'accept_language_example' # str | Language user is requesting
project_id = 56 # int | The ID of the project the task is associated with
task_id = 56 # int | The unique task ID

try:
    # Unlock task that is locked for mapping resetting it to it's last status
    api_instance.api_v1_project_project_id_task_task_id_stop_mapping_post(body, authorization, accept_language, project_id, task_id)
except ApiException as e:
    print("Exception when calling MappingApi->api_v1_project_project_id_task_task_id_stop_mapping_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskUpdateStop**](TaskUpdateStop.md)| JSON object for unlocking a task | 
 **authorization** | **str**| Base64 encoded session token | 
 **accept_language** | **str**| Language user is requesting | 
 **project_id** | **int**| The ID of the project the task is associated with | 
 **task_id** | **int**| The unique task ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_task_task_id_undo_mapping_post**
> api_v1_project_project_id_task_task_id_undo_mapping_post(authorization, accept_language, project_id, task_id)

Get task for mapping

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingApi()
authorization = 'authorization_example' # str | Base64 encoded session token
accept_language = 'accept_language_example' # str | Language user is requesting
project_id = 56 # int | The ID of the project the task is associated with
task_id = 56 # int | The unique task ID

try:
    # Get task for mapping
    api_instance.api_v1_project_project_id_task_task_id_undo_mapping_post(authorization, accept_language, project_id, task_id)
except ApiException as e:
    print("Exception when calling MappingApi->api_v1_project_project_id_task_task_id_undo_mapping_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **accept_language** | **str**| Language user is requesting | 
 **project_id** | **int**| The ID of the project the task is associated with | 
 **task_id** | **int**| The unique task ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_task_task_id_unlock_after_mapping_post**
> api_v1_project_project_id_task_task_id_unlock_after_mapping_post(body, authorization, project_id, task_id)

Unlocks the task after mapping completed

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingApi()
body = swagger_client.TaskUpdateUnlock() # TaskUpdateUnlock | JSON object for unlocking a task
authorization = 'authorization_example' # str | Base64 encoded session token
project_id = 56 # int | The ID of the project the task is associated with
task_id = 56 # int | The unique task ID

try:
    # Unlocks the task after mapping completed
    api_instance.api_v1_project_project_id_task_task_id_unlock_after_mapping_post(body, authorization, project_id, task_id)
except ApiException as e:
    print("Exception when calling MappingApi->api_v1_project_project_id_task_task_id_unlock_after_mapping_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskUpdateUnlock**](TaskUpdateUnlock.md)| JSON object for unlocking a task | 
 **authorization** | **str**| Base64 encoded session token | 
 **project_id** | **int**| The ID of the project the task is associated with | 
 **task_id** | **int**| The unique task ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_tasks_as_gpx_get**
> api_v1_project_project_id_tasks_as_gpx_get(project_id, tasks=tasks, as_file=as_file)

Get tasks as GPX

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingApi()
project_id = 56 # int | The ID of the project the task is associated with
tasks = 'tasks_example' # str | List of tasks; leave blank for all (optional)
as_file = true # bool | Set to true if file download preferred (optional)

try:
    # Get tasks as GPX
    api_instance.api_v1_project_project_id_tasks_as_gpx_get(project_id, tasks=tasks, as_file=as_file)
except ApiException as e:
    print("Exception when calling MappingApi->api_v1_project_project_id_tasks_as_gpx_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The ID of the project the task is associated with | 
 **tasks** | **str**| List of tasks; leave blank for all | [optional] 
 **as_file** | **bool**| Set to true if file download preferred | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_tasks_as_osm_xml_get**
> api_v1_project_project_id_tasks_as_osm_xml_get(project_id, tasks=tasks, as_file=as_file)

Get tasks as OSM XML

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingApi()
project_id = 56 # int | The ID of the project the task is associated with
tasks = 'tasks_example' # str | List of tasks; leave blank to retrieve all (optional)
as_file = true # bool | Set to true if file download preferred (optional)

try:
    # Get tasks as OSM XML
    api_instance.api_v1_project_project_id_tasks_as_osm_xml_get(project_id, tasks=tasks, as_file=as_file)
except ApiException as e:
    print("Exception when calling MappingApi->api_v1_project_project_id_tasks_as_osm_xml_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The ID of the project the task is associated with | 
 **tasks** | **str**| List of tasks; leave blank to retrieve all | [optional] 
 **as_file** | **bool**| Set to true if file download preferred | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_tasks_get**
> api_v1_project_project_id_tasks_get(project_id, as_file=as_file)

Get tasks as JSON

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingApi()
project_id = 56 # int | The ID of the project the task is associated with
as_file = true # bool | Set to true if file download preferred (optional)

try:
    # Get tasks as JSON
    api_instance.api_v1_project_project_id_tasks_get(project_id, as_file=as_file)
except ApiException as e:
    print("Exception when calling MappingApi->api_v1_project_project_id_tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The ID of the project the task is associated with | 
 **as_file** | **bool**| Set to true if file download preferred | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

