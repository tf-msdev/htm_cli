# swagger_client.LicensesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_license_license_id_delete**](LicensesApi.md#api_v1_license_license_id_delete) | **DELETE** /api/v1/license/{license_id} | Delete the specified mapping license
[**api_v1_license_license_id_get**](LicensesApi.md#api_v1_license_license_id_get) | **GET** /api/v1/license/{license_id} | Get specified mapping license
[**api_v1_license_license_id_post**](LicensesApi.md#api_v1_license_license_id_post) | **POST** /api/v1/license/{license_id} | Update  a new mapping license
[**api_v1_license_list_get**](LicensesApi.md#api_v1_license_list_get) | **GET** /api/v1/license/list | Get all imagery licenses
[**api_v1_license_put**](LicensesApi.md#api_v1_license_put) | **PUT** /api/v1/license | Creates a new mapping license

# **api_v1_license_license_id_delete**
> api_v1_license_license_id_delete(authorization, license_id)

Delete the specified mapping license

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicensesApi()
authorization = 'authorization_example' # str | Base64 encoded session token
license_id = 56 # int | The unique license ID

try:
    # Delete the specified mapping license
    api_instance.api_v1_license_license_id_delete(authorization, license_id)
except ApiException as e:
    print("Exception when calling LicensesApi->api_v1_license_license_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **license_id** | **int**| The unique license ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_license_license_id_get**
> api_v1_license_license_id_get(license_id)

Get specified mapping license

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicensesApi()
license_id = 56 # int | The unique license ID

try:
    # Get specified mapping license
    api_instance.api_v1_license_license_id_get(license_id)
except ApiException as e:
    print("Exception when calling LicensesApi->api_v1_license_license_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_id** | **int**| The unique license ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_license_license_id_post**
> api_v1_license_license_id_post(body, authorization, license_id)

Update  a new mapping license

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicensesApi()
body = NULL # object | JSON object for creating a new mapping license
authorization = 'authorization_example' # str | Base64 encoded session token
license_id = 56 # int | The unique license ID

try:
    # Update  a new mapping license
    api_instance.api_v1_license_license_id_post(body, authorization, license_id)
except ApiException as e:
    print("Exception when calling LicensesApi->api_v1_license_license_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON object for creating a new mapping license | 
 **authorization** | **str**| Base64 encoded session token | 
 **license_id** | **int**| The unique license ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_license_list_get**
> api_v1_license_list_get()

Get all imagery licenses

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicensesApi()

try:
    # Get all imagery licenses
    api_instance.api_v1_license_list_get()
except ApiException as e:
    print("Exception when calling LicensesApi->api_v1_license_list_get: %s\n" % e)
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

# **api_v1_license_put**
> api_v1_license_put(body, authorization)

Creates a new mapping license

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicensesApi()
body = NULL # object | JSON object for creating a new mapping license
authorization = 'authorization_example' # str | Base64 encoded session token

try:
    # Creates a new mapping license
    api_instance.api_v1_license_put(body, authorization)
except ApiException as e:
    print("Exception when calling LicensesApi->api_v1_license_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON object for creating a new mapping license | 
 **authorization** | **str**| Base64 encoded session token | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

