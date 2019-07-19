# swagger_client.ApplicationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_application_application_key_delete**](ApplicationApi.md#api_v1_application_application_key_delete) | **DELETE** /api/v1/application/{application_key} | Deletes an application key for a user
[**api_v1_application_application_key_put**](ApplicationApi.md#api_v1_application_application_key_put) | **PUT** /api/v1/application/{application_key} | Checks the validity of an application key
[**api_v1_application_get**](ApplicationApi.md#api_v1_application_get) | **GET** /api/v1/application | Gets application keys for a user
[**api_v1_application_post**](ApplicationApi.md#api_v1_application_post) | **POST** /api/v1/application | Creates an application key for the user

# **api_v1_application_application_key_delete**
> api_v1_application_application_key_delete(authorization, application_key)

Deletes an application key for a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
authorization = 'authorization_example' # str | Base64 encoded session token
application_key = 'application_key_example' # str | Application key to remove

try:
    # Deletes an application key for a user
    api_instance.api_v1_application_application_key_delete(authorization, application_key)
except ApiException as e:
    print("Exception when calling ApplicationApi->api_v1_application_application_key_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **application_key** | **str**| Application key to remove | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_application_application_key_put**
> api_v1_application_application_key_put(application_key)

Checks the validity of an application key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
application_key = 'application_key_example' # str | Application key to test

try:
    # Checks the validity of an application key
    api_instance.api_v1_application_application_key_put(application_key)
except ApiException as e:
    print("Exception when calling ApplicationApi->api_v1_application_application_key_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_key** | **str**| Application key to test | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_application_get**
> api_v1_application_get(authorization)

Gets application keys for a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
authorization = 'authorization_example' # str | Base64 encoded session token

try:
    # Gets application keys for a user
    api_instance.api_v1_application_get(authorization)
except ApiException as e:
    print("Exception when calling ApplicationApi->api_v1_application_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_application_post**
> api_v1_application_post(authorization)

Creates an application key for the user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()
authorization = 'authorization_example' # str | Base64 encoded session token

try:
    # Creates an application key for the user
    api_instance.api_v1_application_post(authorization)
except ApiException as e:
    print("Exception when calling ApplicationApi->api_v1_application_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

