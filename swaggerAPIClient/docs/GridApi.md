# swagger_client.GridApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_grid_intersecting_tiles_put**](GridApi.md#api_v1_grid_intersecting_tiles_put) | **PUT** /api/v1/grid/intersecting-tiles | Gets the tiles intersecting the aoi
[**api_v1_project_project_id_task_task_id_split_post**](GridApi.md#api_v1_project_project_id_task_task_id_split_post) | **POST** /api/v1/project/{project_id}/task/{task_id}/split | Split a task

# **api_v1_grid_intersecting_tiles_put**
> api_v1_grid_intersecting_tiles_put(body, authorization)

Gets the tiles intersecting the aoi

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GridApi()
body = NULL # object | JSON object containing aoi and tasks and bool flag for controlling clip grid to aoi
authorization = 'authorization_example' # str | Base64 encoded session token

try:
    # Gets the tiles intersecting the aoi
    api_instance.api_v1_grid_intersecting_tiles_put(body, authorization)
except ApiException as e:
    print("Exception when calling GridApi->api_v1_grid_intersecting_tiles_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON object containing aoi and tasks and bool flag for controlling clip grid to aoi | 
 **authorization** | **str**| Base64 encoded session token | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_task_task_id_split_post**
> api_v1_project_project_id_task_task_id_split_post(authorization, accept_language, project_id, task_id)

Split a task

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GridApi()
authorization = 'authorization_example' # str | Base64 encoded session token
accept_language = 'accept_language_example' # str | Language user is requesting
project_id = 56 # int | The ID of the project the task is associated with
task_id = 56 # int | The unique task ID

try:
    # Split a task
    api_instance.api_v1_project_project_id_task_task_id_split_post(authorization, accept_language, project_id, task_id)
except ApiException as e:
    print("Exception when calling GridApi->api_v1_project_project_id_task_task_id_split_post: %s\n" % e)
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

