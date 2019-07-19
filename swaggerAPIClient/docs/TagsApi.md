# swagger_client.TagsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_tags_campaigns_get**](TagsApi.md#api_v1_tags_campaigns_get) | **GET** /api/v1/tags/campaigns | Gets all campaign tags
[**api_v1_tags_organisations_get**](TagsApi.md#api_v1_tags_organisations_get) | **GET** /api/v1/tags/organisations | Gets all organisation tags

# **api_v1_tags_campaigns_get**
> api_v1_tags_campaigns_get()

Gets all campaign tags

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()

try:
    # Gets all campaign tags
    api_instance.api_v1_tags_campaigns_get()
except ApiException as e:
    print("Exception when calling TagsApi->api_v1_tags_campaigns_get: %s\n" % e)
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

# **api_v1_tags_organisations_get**
> api_v1_tags_organisations_get()

Gets all organisation tags

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()

try:
    # Gets all organisation tags
    api_instance.api_v1_tags_organisations_get()
except ApiException as e:
    print("Exception when calling TagsApi->api_v1_tags_organisations_get: %s\n" % e)
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

