# swagger_client.SearchApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_project_search_get**](SearchApi.md#api_v1_project_search_get) | **GET** /api/v1/project/search | Search active projects
[**api_v1_projects_within_bounding_box_get**](SearchApi.md#api_v1_projects_within_bounding_box_get) | **GET** /api/v1/projects/within-bounding-box | Search for projects by bbox projects

# **api_v1_project_search_get**
> api_v1_project_search_get(accept_language, authorization=authorization, mapper_level=mapper_level, mapping_types=mapping_types, organisation_tag=organisation_tag, campaign_tag=campaign_tag, page=page, text_search=text_search, project_statuses=project_statuses)

Search active projects

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
accept_language = 'accept_language_example' # str | Language user is requesting
authorization = 'authorization_example' # str | Base64 encoded session token (optional)
mapper_level = 'mapper_level_example' # str |  (optional)
mapping_types = 'mapping_types_example' # str |  (optional)
organisation_tag = 'organisation_tag_example' # str |  (optional)
campaign_tag = 'campaign_tag_example' # str |  (optional)
page = 56 # int | Page of results user requested (optional)
text_search = 'text_search_example' # str | text to search (optional)
project_statuses = 'project_statuses_example' # str | Authenticated PMs can search for archived or draft statuses (optional)

try:
    # Search active projects
    api_instance.api_v1_project_search_get(accept_language, authorization=authorization, mapper_level=mapper_level, mapping_types=mapping_types, organisation_tag=organisation_tag, campaign_tag=campaign_tag, page=page, text_search=text_search, project_statuses=project_statuses)
except ApiException as e:
    print("Exception when calling SearchApi->api_v1_project_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Language user is requesting | 
 **authorization** | **str**| Base64 encoded session token | [optional] 
 **mapper_level** | **str**|  | [optional] 
 **mapping_types** | **str**|  | [optional] 
 **organisation_tag** | **str**|  | [optional] 
 **campaign_tag** | **str**|  | [optional] 
 **page** | **int**| Page of results user requested | [optional] 
 **text_search** | **str**| text to search | [optional] 
 **project_statuses** | **str**| Authenticated PMs can search for archived or draft statuses | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_projects_within_bounding_box_get**
> api_v1_projects_within_bounding_box_get(authorization, accept_language, created_by_me, bbox=bbox, srid=srid)

Search for projects by bbox projects

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
authorization = 'authorization_example' # str | Base64 encoded session token
accept_language = 'accept_language_example' # str | Language user is requesting
created_by_me = true # bool | limit to projects created by authenticated user
bbox = 'bbox_example' # str | comma separated list xmin, ymin, xmax, ymax (optional)
srid = 56 # int | srid of bbox coords (optional)

try:
    # Search for projects by bbox projects
    api_instance.api_v1_projects_within_bounding_box_get(authorization, accept_language, created_by_me, bbox=bbox, srid=srid)
except ApiException as e:
    print("Exception when calling SearchApi->api_v1_projects_within_bounding_box_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Base64 encoded session token | 
 **accept_language** | **str**| Language user is requesting | 
 **created_by_me** | **bool**| limit to projects created by authenticated user | 
 **bbox** | **str**| comma separated list xmin, ymin, xmax, ymax | [optional] 
 **srid** | **int**| srid of bbox coords | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

