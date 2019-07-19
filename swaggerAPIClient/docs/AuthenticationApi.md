# swagger_client.AuthenticationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_auth_email_get**](AuthenticationApi.md#api_auth_email_get) | **GET** /api/auth/email | Authenticates user owns email address
[**api_v1_auth_login_get**](AuthenticationApi.md#api_v1_auth_login_get) | **GET** /api/v1/auth/login | Redirects user to OSM to authenticate
[**api_v1_auth_oauth_callback_get**](AuthenticationApi.md#api_v1_auth_oauth_callback_get) | **GET** /api/v1/auth/oauth-callback | Handles the OSM OAuth callback

# **api_auth_email_get**
> api_auth_email_get(username=username, token=token)

Authenticates user owns email address

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
username = 'username_example' # str |  (optional)
token = 'token_example' # str |  (optional)

try:
    # Authenticates user owns email address
    api_instance.api_auth_email_get(username=username, token=token)
except ApiException as e:
    print("Exception when calling AuthenticationApi->api_auth_email_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] 
 **token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_auth_login_get**
> api_v1_auth_login_get(redirect_to=redirect_to)

Redirects user to OSM to authenticate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
redirect_to = 'redirect_to_example' # str | Route to redirect user once authenticated (optional)

try:
    # Redirects user to OSM to authenticate
    api_instance.api_v1_auth_login_get(redirect_to=redirect_to)
except ApiException as e:
    print("Exception when calling AuthenticationApi->api_v1_auth_login_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_to** | **str**| Route to redirect user once authenticated | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_auth_oauth_callback_get**
> api_v1_auth_oauth_callback_get()

Handles the OSM OAuth callback

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()

try:
    # Handles the OSM OAuth callback
    api_instance.api_v1_auth_oauth_callback_get()
except ApiException as e:
    print("Exception when calling AuthenticationApi->api_v1_auth_oauth_callback_get: %s\n" % e)
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

