# swagger_client.ProjectAdminApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_admin_my_projects_get**](ProjectAdminApi.md#api_v1_admin_my_projects_get) | **GET** /api/v1/admin/my-projects | Get all projects for logged in admin
[**api_v1_admin_project_project_id_comments_get**](ProjectAdminApi.md#api_v1_admin_project_project_id_comments_get) | **GET** /api/v1/admin/project/{project_id}/comments | Gets all comments for project
[**api_v1_admin_project_project_id_delete**](ProjectAdminApi.md#api_v1_admin_project_project_id_delete) | **DELETE** /api/v1/admin/project/{project_id} | Deletes a Tasking-Manager project
[**api_v1_admin_project_project_id_get**](ProjectAdminApi.md#api_v1_admin_project_project_id_get) | **GET** /api/v1/admin/project/{project_id} | Retrieves a Tasking-Manager project
[**api_v1_admin_project_project_id_invalidate_all_post**](ProjectAdminApi.md#api_v1_admin_project_project_id_invalidate_all_post) | **POST** /api/v1/admin/project/{project_id}/invalidate-all | Invalidate all mapped tasks on a project
[**api_v1_admin_project_project_id_map_all_post**](ProjectAdminApi.md#api_v1_admin_project_project_id_map_all_post) | **POST** /api/v1/admin/project/{project_id}/map-all | Map all tasks on a project
[**api_v1_admin_project_project_id_post**](ProjectAdminApi.md#api_v1_admin_project_project_id_post) | **POST** /api/v1/admin/project/{project_id} | Updates a Tasking-Manager project
[**api_v1_admin_project_project_id_reset_all_badimagery_post**](ProjectAdminApi.md#api_v1_admin_project_project_id_reset_all_badimagery_post) | **POST** /api/v1/admin/project/{project_id}/reset-all-badimagery | Mark all bad imagery tasks ready for mapping
[**api_v1_admin_project_project_id_reset_all_post**](ProjectAdminApi.md#api_v1_admin_project_project_id_reset_all_post) | **POST** /api/v1/admin/project/{project_id}/reset-all | Reset all tasks on project back to ready, preserving history.
[**api_v1_admin_project_project_id_transfer_post**](ProjectAdminApi.md#api_v1_admin_project_project_id_transfer_post) | **POST** /api/v1/admin/project/{project_id}/transfer | Transfers a project to a new user.
[**api_v1_admin_project_project_id_validate_all_post**](ProjectAdminApi.md#api_v1_admin_project_project_id_validate_all_post) | **POST** /api/v1/admin/project/{project_id}/validate-all | Validate all mapped tasks on a project
[**api_v1_admin_project_put**](ProjectAdminApi.md#api_v1_admin_project_put) | **PUT** /api/v1/admin/project | Creates a tasking-manager project
[**api_v1_project_project_id_task_annotations_annotation_type_get**](ProjectAdminApi.md#api_v1_project_project_id_task_annotations_annotation_type_get) | **GET** /api/v1/project/{project_id}/task-annotations/{annotation_type} | Get all task annotations for a project
[**api_v1_project_project_id_task_annotations_annotation_type_post**](ProjectAdminApi.md#api_v1_project_project_id_task_annotations_annotation_type_post) | **POST** /api/v1/project/{project_id}/task-annotations/{annotation_type} | Store new task annotations for tasks of a project
[**api_v1_project_project_id_task_annotations_get**](ProjectAdminApi.md#api_v1_project_project_id_task_annotations_get) | **GET** /api/v1/project/{project_id}/task-annotations | Get all task annotations for a project
[**api_v1_project_project_id_task_annotations_post**](ProjectAdminApi.md#api_v1_project_project_id_task_annotations_post) | **POST** /api/v1/project/{project_id}/task-annotations | Store new task annotations for tasks of a project

# **api_v1_admin_my_projects_get**
> api_v1_admin_my_projects_get(authorization, accept_language)

Get all projects for logged in admin

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectAdminApi()
authorization = 'authorization_example' # str | Base64 encoded session token
accept_language = 'accept_language_example' # str | Language user is requesting

try:
    # Get all projects for logged in admin
    api_instance.api_v1_admin_my_projects_get(authorization, accept_language)
except ApiException as e:
    print("Exception when calling ProjectAdminApi->api_v1_admin_my_projects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **accept_language** | **str**| Language user is requesting | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_admin_project_project_id_comments_get**
> api_v1_admin_project_project_id_comments_get(project_id)

Gets all comments for project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectAdminApi()
project_id = 56 # int | The unique project ID

try:
    # Gets all comments for project
    api_instance.api_v1_admin_project_project_id_comments_get(project_id)
except ApiException as e:
    print("Exception when calling ProjectAdminApi->api_v1_admin_project_project_id_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The unique project ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_admin_project_project_id_delete**
> api_v1_admin_project_project_id_delete(authorization, project_id)

Deletes a Tasking-Manager project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectAdminApi()
authorization = 'authorization_example' # str | Base64 encoded session token
project_id = 56 # int | The unique project ID

try:
    # Deletes a Tasking-Manager project
    api_instance.api_v1_admin_project_project_id_delete(authorization, project_id)
except ApiException as e:
    print("Exception when calling ProjectAdminApi->api_v1_admin_project_project_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **project_id** | **int**| The unique project ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_admin_project_project_id_get**
> api_v1_admin_project_project_id_get(authorization, project_id)

Retrieves a Tasking-Manager project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectAdminApi()
authorization = 'authorization_example' # str | Base64 encoded session token
project_id = 56 # int | The unique project ID

try:
    # Retrieves a Tasking-Manager project
    api_instance.api_v1_admin_project_project_id_get(authorization, project_id)
except ApiException as e:
    print("Exception when calling ProjectAdminApi->api_v1_admin_project_project_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **project_id** | **int**| The unique project ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_admin_project_project_id_invalidate_all_post**
> api_v1_admin_project_project_id_invalidate_all_post(authorization, project_id)

Invalidate all mapped tasks on a project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectAdminApi()
authorization = 'authorization_example' # str | Base64 encoded session token
project_id = 56 # int | The unique project ID

try:
    # Invalidate all mapped tasks on a project
    api_instance.api_v1_admin_project_project_id_invalidate_all_post(authorization, project_id)
except ApiException as e:
    print("Exception when calling ProjectAdminApi->api_v1_admin_project_project_id_invalidate_all_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **project_id** | **int**| The unique project ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_admin_project_project_id_map_all_post**
> api_v1_admin_project_project_id_map_all_post(authorization, project_id)

Map all tasks on a project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectAdminApi()
authorization = 'authorization_example' # str | Base64 encoded session token
project_id = 56 # int | The unique project ID

try:
    # Map all tasks on a project
    api_instance.api_v1_admin_project_project_id_map_all_post(authorization, project_id)
except ApiException as e:
    print("Exception when calling ProjectAdminApi->api_v1_admin_project_project_id_map_all_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **project_id** | **int**| The unique project ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_admin_project_project_id_post**
> api_v1_admin_project_project_id_post(body, authorization, project_id)

Updates a Tasking-Manager project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectAdminApi()
body = NULL # object | JSON object for creating draft project
authorization = 'authorization_example' # str | Base64 encoded session token
project_id = 56 # int | The unique project ID

try:
    # Updates a Tasking-Manager project
    api_instance.api_v1_admin_project_project_id_post(body, authorization, project_id)
except ApiException as e:
    print("Exception when calling ProjectAdminApi->api_v1_admin_project_project_id_post: %s\n" % e)
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

# **api_v1_admin_project_project_id_reset_all_badimagery_post**
> api_v1_admin_project_project_id_reset_all_badimagery_post(authorization, project_id)

Mark all bad imagery tasks ready for mapping

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectAdminApi()
authorization = 'authorization_example' # str | Base64 encoded session token
project_id = 56 # int | The unique project ID

try:
    # Mark all bad imagery tasks ready for mapping
    api_instance.api_v1_admin_project_project_id_reset_all_badimagery_post(authorization, project_id)
except ApiException as e:
    print("Exception when calling ProjectAdminApi->api_v1_admin_project_project_id_reset_all_badimagery_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **project_id** | **int**| The unique project ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_admin_project_project_id_reset_all_post**
> api_v1_admin_project_project_id_reset_all_post(authorization, project_id)

Reset all tasks on project back to ready, preserving history.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectAdminApi()
authorization = 'authorization_example' # str | Base64 encoded session token
project_id = 56 # int | The unique project ID

try:
    # Reset all tasks on project back to ready, preserving history.
    api_instance.api_v1_admin_project_project_id_reset_all_post(authorization, project_id)
except ApiException as e:
    print("Exception when calling ProjectAdminApi->api_v1_admin_project_project_id_reset_all_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **project_id** | **int**| The unique project ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_admin_project_project_id_transfer_post**
> api_v1_admin_project_project_id_transfer_post(body, authorization, project_id)

Transfers a project to a new user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectAdminApi()
body = NULL # object | the username of the new owner
authorization = 'authorization_example' # str | Base64 encoded session token
project_id = 56 # int | The unique project ID

try:
    # Transfers a project to a new user.
    api_instance.api_v1_admin_project_project_id_transfer_post(body, authorization, project_id)
except ApiException as e:
    print("Exception when calling ProjectAdminApi->api_v1_admin_project_project_id_transfer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| the username of the new owner | 
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

# **api_v1_admin_project_project_id_validate_all_post**
> api_v1_admin_project_project_id_validate_all_post(authorization, project_id)

Validate all mapped tasks on a project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectAdminApi()
authorization = 'authorization_example' # str | Base64 encoded session token
project_id = 56 # int | The unique project ID

try:
    # Validate all mapped tasks on a project
    api_instance.api_v1_admin_project_project_id_validate_all_post(authorization, project_id)
except ApiException as e:
    print("Exception when calling ProjectAdminApi->api_v1_admin_project_project_id_validate_all_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **project_id** | **int**| The unique project ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_admin_project_put**
> api_v1_admin_project_put(body, authorization)

Creates a tasking-manager project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectAdminApi()
body = NULL # object | JSON object for creating draft project
authorization = 'authorization_example' # str | Base64 encoded session token

try:
    # Creates a tasking-manager project
    api_instance.api_v1_admin_project_put(body, authorization)
except ApiException as e:
    print("Exception when calling ProjectAdminApi->api_v1_admin_project_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON object for creating draft project | 
 **authorization** | **str**| Base64 encoded session token | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_task_annotations_annotation_type_get**
> api_v1_project_project_id_task_annotations_annotation_type_get(project_id, annotation_type)

Get all task annotations for a project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectAdminApi()
project_id = 56 # int | The ID of the project
annotation_type = 'annotation_type_example' # str | The type of annotation to fetch

try:
    # Get all task annotations for a project
    api_instance.api_v1_project_project_id_task_annotations_annotation_type_get(project_id, annotation_type)
except ApiException as e:
    print("Exception when calling ProjectAdminApi->api_v1_project_project_id_task_annotations_annotation_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The ID of the project | 
 **annotation_type** | **str**| The type of annotation to fetch | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_task_annotations_annotation_type_post**
> api_v1_project_project_id_task_annotations_annotation_type_post(body, content_type, application_token, project_id, annotation_type)

Store new task annotations for tasks of a project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectAdminApi()
body = NULL # object | JSON object for creating draft project
content_type = 'content_type_example' # str | Content type for post body
application_token = 'application_token_example' # str | Application token registered with TM
project_id = 56 # int | The unique project ID
annotation_type = 'annotation_type_example' # str | Annotation type

try:
    # Store new task annotations for tasks of a project
    api_instance.api_v1_project_project_id_task_annotations_annotation_type_post(body, content_type, application_token, project_id, annotation_type)
except ApiException as e:
    print("Exception when calling ProjectAdminApi->api_v1_project_project_id_task_annotations_annotation_type_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON object for creating draft project | 
 **content_type** | **str**| Content type for post body | 
 **application_token** | **str**| Application token registered with TM | 
 **project_id** | **int**| The unique project ID | 
 **annotation_type** | **str**| Annotation type | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_task_annotations_get**
> api_v1_project_project_id_task_annotations_get(project_id, annotation_type)

Get all task annotations for a project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectAdminApi()
project_id = 56 # int | The ID of the project
annotation_type = 'annotation_type_example' # str | The type of annotation to fetch

try:
    # Get all task annotations for a project
    api_instance.api_v1_project_project_id_task_annotations_get(project_id, annotation_type)
except ApiException as e:
    print("Exception when calling ProjectAdminApi->api_v1_project_project_id_task_annotations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The ID of the project | 
 **annotation_type** | **str**| The type of annotation to fetch | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_project_project_id_task_annotations_post**
> api_v1_project_project_id_task_annotations_post(body, content_type, application_token, project_id, annotation_type)

Store new task annotations for tasks of a project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectAdminApi()
body = NULL # object | JSON object for creating draft project
content_type = 'content_type_example' # str | Content type for post body
application_token = 'application_token_example' # str | Application token registered with TM
project_id = 56 # int | The unique project ID
annotation_type = 'annotation_type_example' # str | Annotation type

try:
    # Store new task annotations for tasks of a project
    api_instance.api_v1_project_project_id_task_annotations_post(body, content_type, application_token, project_id, annotation_type)
except ApiException as e:
    print("Exception when calling ProjectAdminApi->api_v1_project_project_id_task_annotations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| JSON object for creating draft project | 
 **content_type** | **str**| Content type for post body | 
 **application_token** | **str**| Application token registered with TM | 
 **project_id** | **int**| The unique project ID | 
 **annotation_type** | **str**| Annotation type | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

