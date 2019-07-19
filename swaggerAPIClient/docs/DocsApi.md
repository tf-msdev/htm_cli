# swagger_client.DocsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_docs_get**](DocsApi.md#api_docs_get) | **GET** /api/docs | Generates Swagger UI readable JSON

# **api_docs_get**
> api_docs_get()

Generates Swagger UI readable JSON

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DocsApi()

try:
    # Generates Swagger UI readable JSON
    api_instance.api_docs_get()
except ApiException as e:
    print("Exception when calling DocsApi->api_docs_get: %s\n" % e)
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

