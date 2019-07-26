from htm_msopenmaps_custom_api import UserLoginAPI
from swaggerAPIClient.swagger_client.api import project_admin_api, grid_api, mapping_api
import json
import re
from shapely.geometry import Point,Polygon,MultiPolygon
import geojson
import urllib3

""" my_api_instance = UserLoginAPI()
my_api_instance.obtain_authorization("v-fita@microsoft.com", "Vvardenfello1")
project_admin_api_instance = project_admin_api.ProjectAdminApi()

body["tasks"] = MyAPI.util_split_quad_multipolygon_tasks(body["tasks"])
print(body["tasks"])
encoded_body = json.dumps(body)
reply = project_admin_api_instance.api_v1_admin_project_put(body, my_api_instance.get_authorization(), _preload_content=False)
print(reply.data.decode()) """
""" pattern_1 = r"(\[.*\])"
pattern_2 = r"\[\s*([0-9\.]+)\s*,\s*([0-9\.]+)\s*\]"
matches_1 = re.findall(pattern_1, "[ [1.5, 2.33], [22.12, 3], [3, 4], [4, 5] ]")
for match_1 in matches_1:
    match_1 = match_1[1:-1]
    matches_2 = re.findall(pattern_2, match_1)
    for match_2 in matches_2:
      print(match_2[0], match_2[1]) """

""" body = {
  "arbitraryTasks" : False,
  "areaOfInterest" : {
    "features": [
      {
        "geometry": {
          "type": "MultiPolygon",
          "coordinates": [
            [
              [ [21, 45], [21, 44.7], [20, 44.7], [20, 45], [21, 45] ]
            ]
          ]
        },
        "properties": {
          "isSquare": True,
          "x": 2400,
          "y": 1750,
          "zoom": 15
        },
        "type": "Feature"
      }
    ],
    "type": "FeatureCollection"
  },
  "projectName" : "My project",
  "tasks" : {
    "features": [
      {
        "geometry": {
          "type": "MultiPolygon",
          "coordinates": [
              [
                [ [21, 45.3], [21, 44.5], [20, 44.7], [20, 45], [21, 45.3] ]
              ]
            ]
        },
        "properties": {

          "isSquare": True,
          "x": 2400,
          "y": 1750,
          "zoom": 15
        },
        "type": "Feature"
      }
    ],
    "type" : "FeatureCollection"
  }
}

p1 = Polygon([ (21.402567, 44.818087), (21.414927, 44.817600), (21.413725, 44.825027), (21.603254, 44.823444), (21.402567, 44.818087) ])
p1.is_valid


reply = grid_api_instance.api_v1_grid_intersecting_tiles_put(body_grid, my_api_instance.get_authorization(), _preload_content=False)
print(reply.data.decode())
newTasks = json.loads(reply.data.decode())


"""

""" import re

pattern = r"^\s*\[(.*)\]\s*$"
matches = re.findall(pattern, "[BUILDINGS , ROADS]    ")
print(matches)
pattern = pattern.strip('[')
pattern = pattern.strip(']')
pattern = r"[^A-Za-z]*([A-Za-z]+)[^A-Za-z]*"
matches = re.findall(pattern, matches[0])
print(matches) """

body_string = """{
  \"areaOfInterest\": {
    \"features\": [
      {
        \"geometry\": {
          \"coordinates\": [
            [
              [
                [
                  -4.0237,
                  56.0904
                ],
                [
                  -3.9111,
                  56.1715
                ],
                [
                  -3.8122,
                  56.098
                ],
                [
                  -4.0237,
                  56.0904
                ]
              ]
            ]
          ],
          \"type\": \"MultiPolygon\"
        },
        \"properties\": {
          \"isSquare\": false,
          \"x\": 2402,
          \"y\": 1736,
          \"zoom\": 12
        },
        \"type\": \"Feature\"
      }
    ],
    \"type\": \"FeatureCollection\"
  },
  \"clipToAoi\": false,
  \"grid\": {
    \"features\": [
      {
        \"geometry\": {
          \"coordinates\": [
            [
              [
                [
                  -4.0237,
                  56.0904
                ],
                [
                  -3.9111,
                  56.1715
                ],
                [
                  -3.8122,
                  56.098
                ],
                [
                  -4.0237,
                  56.0904
                ]
              ]
            ]
          ],
          \"type\": \"MultiPolygon\"
        },
        \"properties\": {
          \"isSquare\": false,
          \"x\": 2402,
          \"y\": 1736,
          \"zoom\": 12
        },
        \"type\": \"Feature\"
      }
    ],
    \"type\": \"FeatureCollection\"
  }
}"""
#print("string:", body_string)
#body = geojson.loads(body_string)
#print(body)

login_api_instance = UserLoginAPI()
login_api_instance.obtain_authorization("v-fita@microsoft.com", "Vvardenfello1")
""" grid_api_instance = grid_api.GridApi()
project_admin_api_instance = project_admin_api.ProjectAdminApi()

  
mapping_api_instance = mapping_api.MappingApi()
reply = mapping_api_instance.api_v1_project_project_id_task_task_id_lock_for_mapping_post(login_api_instance.get_authorization(), "en", 417, 1, _preload_content=False)
print(reply.data.decode()) """

#reply = urllib3.PoolManager().request("GET", "/load_and_zoom_ms?left=33.7772&bottom=-1.5383000000000209&right=33.7942&top=-1.5267000000000053&changeset_comment=&changeset_source=Bing&new_layer=true&resume_edit=false&task_id=1&project_id=417&validation_required=false&task_step=mapping&download_gpx=true&auth_token=TVRBeE1qY3pOVEkuRUJESDhRLnZQa29HNDY4NW5ZOEw2b1pDNEQ3d1I0UzBVWQ== HTTP/1.1")
#print(reply)


