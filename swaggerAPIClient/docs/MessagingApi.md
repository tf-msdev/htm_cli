# swagger_client.MessagingApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_admin_project_project_id_message_all_post**](MessagingApi.md#api_v1_admin_project_project_id_message_all_post) | **POST** /api/v1/admin/project/{project_id}/message-all | Send message to all contributors to a project
[**api_v1_messages_delete_multiple_delete**](MessagingApi.md#api_v1_messages_delete_multiple_delete) | **DELETE** /api/v1/messages/delete-multiple | Delete specified messages for logged in user
[**api_v1_messages_get_all_messages_get**](MessagingApi.md#api_v1_messages_get_all_messages_get) | **GET** /api/v1/messages/get-all-messages | Get all messages for logged in user
[**api_v1_messages_has_new_messages_get**](MessagingApi.md#api_v1_messages_has_new_messages_get) | **GET** /api/v1/messages/has-new-messages | Gets count of unread messages
[**api_v1_messages_message_id_delete**](MessagingApi.md#api_v1_messages_message_id_delete) | **DELETE** /api/v1/messages/{message_id} | Deletes the specified message
[**api_v1_messages_message_id_get**](MessagingApi.md#api_v1_messages_message_id_get) | **GET** /api/v1/messages/{message_id} | Gets the specified message
[**api_v1_messages_resend_email_verification_post**](MessagingApi.md#api_v1_messages_resend_email_verification_post) | **POST** /api/v1/messages/resend-email-verification | Resends the validation user to the logged in user
[**api_v1_project_project_id_chat_get**](MessagingApi.md#api_v1_project_project_id_chat_get) | **GET** /api/v1/project/{project_id}/chat | Get all chat messages for project
[**api_v1_project_project_id_chat_put**](MessagingApi.md#api_v1_project_project_id_chat_put) | **PUT** /api/v1/project/{project_id}/chat | Add a message to project chat

# **api_v1_admin_project_project_id_message_all_post**
> api_v1_admin_project_project_id_message_all_post(body, authorization, project_id)

Send message to all contributors to a project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
body = NULL # object | JSON object for creating draft project
authorization = 'authorization_example' # str | Base64 encoded session token
project_id = 56 # int | The unique project ID

try:
    # Send message to all contributors to a project
    api_instance.api_v1_admin_project_project_id_message_all_post(body, authorization, project_id)
except ApiException as e:
    print("Exception when calling MessagingApi->api_v1_admin_project_project_id_message_all_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON object for creating draft project | 
 **authorization** | **str**| Base64 encoded session token | 
 **project_id** | **int**| The unique project ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_messages_delete_multiple_delete**
> api_v1_messages_delete_multiple_delete(body, authorization)

Delete specified messages for logged in user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
body = NULL # object | JSON object containing message ids to delete
authorization = 'authorization_example' # str | Base64 encoded session token

try:
    # Delete specified messages for logged in user
    api_instance.api_v1_messages_delete_multiple_delete(body, authorization)
except ApiException as e:
    print("Exception when calling MessagingApi->api_v1_messages_delete_multiple_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON object containing message ids to delete | 
 **authorization** | **str**| Base64 encoded session token | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_messages_get_all_messages_get**
> api_v1_messages_get_all_messages_get(authorization, message_type=message_type, _from=_from, project=project, task_id=task_id, sort_by=sort_by, sort_direction=sort_direction, page=page, page_size=page_size)

Get all messages for logged in user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
authorization = 'authorization_example' # str | Base64 encoded session token
message_type = 56 # int | Optional message-type filter (optional)
_from = '_from_example' # str | Optional from username filter (optional)
project = 'project_example' # str | Optional project filter (optional)
task_id = 56 # int | Optional task filter (optional)
sort_by = 'sort_by_example' # str | field to sort by, defaults to date (optional)
sort_direction = 'sort_direction_example' # str | direction of sort, defaults to desc (optional)
page = 56 # int | Page of results user requested (optional)
page_size = 56 # int | Size of page, defaults to 10 (optional)

try:
    # Get all messages for logged in user
    api_instance.api_v1_messages_get_all_messages_get(authorization, message_type=message_type, _from=_from, project=project, task_id=task_id, sort_by=sort_by, sort_direction=sort_direction, page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling MessagingApi->api_v1_messages_get_all_messages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **message_type** | **int**| Optional message-type filter | [optional] 
 **_from** | **str**| Optional from username filter | [optional] 
 **project** | **str**| Optional project filter | [optional] 
 **task_id** | **int**| Optional task filter | [optional] 
 **sort_by** | **str**| field to sort by, defaults to date | [optional] 
 **sort_direction** | **str**| direction of sort, defaults to desc | [optional] 
 **page** | **int**| Page of results user requested | [optional] 
 **page_size** | **int**| Size of page, defaults to 10 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_messages_has_new_messages_get**
> api_v1_messages_has_new_messages_get(authorization)

Gets count of unread messages

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
authorization = 'authorization_example' # str | Base64 encoded session token

try:
    # Gets count of unread messages
    api_instance.api_v1_messages_has_new_messages_get(authorization)
except ApiException as e:
    print("Exception when calling MessagingApi->api_v1_messages_has_new_messages_get: %s\n" % e)
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

# **api_v1_messages_message_id_delete**
> api_v1_messages_message_id_delete(authorization, message_id)

Deletes the specified message

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
authorization = 'authorization_example' # str | Base64 encoded session token
message_id = 56 # int | The unique message

try:
    # Deletes the specified message
    api_instance.api_v1_messages_message_id_delete(authorization, message_id)
except ApiException as e:
    print("Exception when calling MessagingApi->api_v1_messages_message_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **message_id** | **int**| The unique message | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_messages_message_id_get**
> api_v1_messages_message_id_get(authorization, message_id)

Gets the specified message

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
authorization = 'authorization_example' # str | Base64 encoded session token
message_id = 56 # int | The unique message

try:
    # Gets the specified message
    api_instance.api_v1_messages_message_id_get(authorization, message_id)
except ApiException as e:
    print("Exception when calling MessagingApi->api_v1_messages_message_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **message_id** | **int**| The unique message | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_messages_resend_email_verification_post**
> api_v1_messages_resend_email_verification_post(authorization)

Resends the validation user to the logged in user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
authorization = 'authorization_example' # str | Base64 encoded session token

try:
    # Resends the validation user to the logged in user
    api_instance.api_v1_messages_resend_email_verification_post(authorization)
except ApiException as e:
    print("Exception when calling MessagingApi->api_v1_messages_resend_email_verification_post: %s\n" % e)
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

# **api_v1_project_project_id_chat_get**
> api_v1_project_project_id_chat_get(project_id, page=page)

Get all chat messages for project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
project_id = 56 # int | The ID of the project to attach the chat message to
page = 56 # int | Page of results user requested (optional)

try:
    # Get all chat messages for project
    api_instance.api_v1_project_project_id_chat_get(project_id, page=page)
except ApiException as e:
    print("Exception when calling MessagingApi->api_v1_project_project_id_chat_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The ID of the project to attach the chat message to | 
 **page** | **int**| Page of results user requested | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_chat_put**
> api_v1_project_project_id_chat_put(body, authorization, project_id)

Add a message to project chat

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
body = NULL # object | JSON object for creating a new mapping license
authorization = 'authorization_example' # str | Base64 encoded session token
project_id = 56 # int | The ID of the project to attach the chat message to

try:
    # Add a message to project chat
    api_instance.api_v1_project_project_id_chat_put(body, authorization, project_id)
except ApiException as e:
    print("Exception when calling MessagingApi->api_v1_project_project_id_chat_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON object for creating a new mapping license | 
 **authorization** | **str**| Base64 encoded session token | 
 **project_id** | **int**| The ID of the project to attach the chat message to | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

