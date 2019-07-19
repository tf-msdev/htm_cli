# swagger_client.SettingsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_settings_get**](SettingsApi.md#api_v1_settings_get) | **GET** /api/v1/settings | Gets all supported languages

# **api_v1_settings_get**
> api_v1_settings_get()

Gets all supported languages

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SettingsApi()

try:
    # Gets all supported languages
    api_instance.api_v1_settings_get()
except ApiException as e:
    print("Exception when calling SettingsApi->api_v1_settings_get: %s\n" % e)
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

