# swagger_client.StatsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_stats_project_project_id_activity_get**](StatsApi.md#api_v1_stats_project_project_id_activity_get) | **GET** /api/v1/stats/project/{project_id}/activity | Get user actvity on a project
[**api_v1_stats_project_project_id_contributions_get**](StatsApi.md#api_v1_stats_project_project_id_contributions_get) | **GET** /api/v1/stats/project/{project_id}/contributions | Get all user contributions on a project
[**api_v1_stats_project_project_id_get**](StatsApi.md#api_v1_stats_project_project_id_get) | **GET** /api/v1/stats/project/{project_id} | Get Project Stats
[**api_v1_stats_summary_get**](StatsApi.md#api_v1_stats_summary_get) | **GET** /api/v1/stats/summary | Get HomePage Stats

# **api_v1_stats_project_project_id_activity_get**
> api_v1_stats_project_project_id_activity_get(project_id, page=page)

Get user actvity on a project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatsApi()
project_id = 56 # int | 
page = 56 # int | Page of results user requested (optional)

try:
    # Get user actvity on a project
    api_instance.api_v1_stats_project_project_id_activity_get(project_id, page=page)
except ApiException as e:
    print("Exception when calling StatsApi->api_v1_stats_project_project_id_activity_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **page** | **int**| Page of results user requested | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stats_project_project_id_contributions_get**
> api_v1_stats_project_project_id_contributions_get(project_id)

Get all user contributions on a project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatsApi()
project_id = 56 # int | 

try:
    # Get all user contributions on a project
    api_instance.api_v1_stats_project_project_id_contributions_get(project_id)
except ApiException as e:
    print("Exception when calling StatsApi->api_v1_stats_project_project_id_contributions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stats_project_project_id_get**
> api_v1_stats_project_project_id_get(accept_language, project_id)

Get Project Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatsApi()
accept_language = 'accept_language_example' # str | Language user is requesting
project_id = 56 # int | 

try:
    # Get Project Stats
    api_instance.api_v1_stats_project_project_id_get(accept_language, project_id)
except ApiException as e:
    print("Exception when calling StatsApi->api_v1_stats_project_project_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language user is requesting | 
 **project_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stats_summary_get**
> api_v1_stats_summary_get()

Get HomePage Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatsApi()

try:
    # Get HomePage Stats
    api_instance.api_v1_stats_summary_get()
except ApiException as e:
    print("Exception when calling StatsApi->api_v1_stats_summary_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

