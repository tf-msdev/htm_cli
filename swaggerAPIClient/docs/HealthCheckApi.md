# swagger_client.HealthCheckApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_health_check_get**](HealthCheckApi.md#api_health_check_get) | **GET** /api/health-check | Simple health-check, if this is unreachable load balancers should be configures to raise an alert

# **api_health_check_get**
> api_health_check_get()

Simple health-check, if this is unreachable load balancers should be configures to raise an alert

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HealthCheckApi()

try:
    # Simple health-check, if this is unreachable load balancers should be configures to raise an alert
    api_instance.api_health_check_get()
except ApiException as e:
    print("Exception when calling HealthCheckApi->api_health_check_get: %s\n" % e)
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

