# swagger_client.MappingIssuesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_mapping_issue_categories_get**](MappingIssuesApi.md#api_v1_mapping_issue_categories_get) | **GET** /api/v1/mapping-issue-categories | Gets all mapping issue categories
[**api_v1_mapping_issue_category_category_id_delete**](MappingIssuesApi.md#api_v1_mapping_issue_category_category_id_delete) | **DELETE** /api/v1/mapping-issue-category/{category_id} | Delete the specified mapping-issue category. Note that categories can
[**api_v1_mapping_issue_category_category_id_get**](MappingIssuesApi.md#api_v1_mapping_issue_category_category_id_get) | **GET** /api/v1/mapping-issue-category/{category_id} | Get specified mapping-issue category
[**api_v1_mapping_issue_category_category_id_put**](MappingIssuesApi.md#api_v1_mapping_issue_category_category_id_put) | **PUT** /api/v1/mapping-issue-category/{category_id} | Update an existing mapping-issue category
[**api_v1_mapping_issue_category_post**](MappingIssuesApi.md#api_v1_mapping_issue_category_post) | **POST** /api/v1/mapping-issue-category | Creates a new mapping-issue category

# **api_v1_mapping_issue_categories_get**
> api_v1_mapping_issue_categories_get(include_archived=include_archived)

Gets all mapping issue categories

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingIssuesApi()
include_archived = true # bool | Optional filter to include archived categories (optional)

try:
    # Gets all mapping issue categories
    api_instance.api_v1_mapping_issue_categories_get(include_archived=include_archived)
except ApiException as e:
    print("Exception when calling MappingIssuesApi->api_v1_mapping_issue_categories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_archived** | **bool**| Optional filter to include archived categories | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_mapping_issue_category_category_id_delete**
> api_v1_mapping_issue_category_category_id_delete(authorization, category_id)

Delete the specified mapping-issue category. Note that categories can

be deleted only if they have never been associated with a task. To<br/>instead archive a used category that is no longer needed, update the<br/>category with its archived flag set to true.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingIssuesApi()
authorization = 'authorization_example' # str | Base64 encoded session token
category_id = 56 # int | The unique mapping-issue category ID

try:
    # Delete the specified mapping-issue category. Note that categories can
    api_instance.api_v1_mapping_issue_category_category_id_delete(authorization, category_id)
except ApiException as e:
    print("Exception when calling MappingIssuesApi->api_v1_mapping_issue_category_category_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **category_id** | **int**| The unique mapping-issue category ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_mapping_issue_category_category_id_get**
> api_v1_mapping_issue_category_category_id_get(category_id)

Get specified mapping-issue category

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingIssuesApi()
category_id = 56 # int | The unique mapping-issue category ID

try:
    # Get specified mapping-issue category
    api_instance.api_v1_mapping_issue_category_category_id_get(category_id)
except ApiException as e:
    print("Exception when calling MappingIssuesApi->api_v1_mapping_issue_category_category_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| The unique mapping-issue category ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_mapping_issue_category_category_id_put**
> api_v1_mapping_issue_category_category_id_put(body, authorization, category_id)

Update an existing mapping-issue category

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingIssuesApi()
body = NULL # object | JSON object for updating a mapping-issue category
authorization = 'authorization_example' # str | Base64 encoded session token
category_id = 56 # int | The unique mapping-issue category ID

try:
    # Update an existing mapping-issue category
    api_instance.api_v1_mapping_issue_category_category_id_put(body, authorization, category_id)
except ApiException as e:
    print("Exception when calling MappingIssuesApi->api_v1_mapping_issue_category_category_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON object for updating a mapping-issue category | 
 **authorization** | **str**| Base64 encoded session token | 
 **category_id** | **int**| The unique mapping-issue category ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_mapping_issue_category_post**
> api_v1_mapping_issue_category_post(body, authorization)

Creates a new mapping-issue category

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MappingIssuesApi()
body = NULL # object | JSON object for creating a new mapping-issue category
authorization = 'authorization_example' # str | Base64 encoded session token

try:
    # Creates a new mapping-issue category
    api_instance.api_v1_mapping_issue_category_post(body, authorization)
except ApiException as e:
    print("Exception when calling MappingIssuesApi->api_v1_mapping_issue_category_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON object for creating a new mapping-issue category | 
 **authorization** | **str**| Base64 encoded session token | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

