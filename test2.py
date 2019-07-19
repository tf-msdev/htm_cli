from htm_msopenmaps_custom_api import UserLoginAPI
from swaggerAPIClient.swagger_client.api import project_admin_api
import json
import re

body = {
  "arbitraryTasks" : False,
  "areaOfInterest" : {
    "features": [
      {
        "geometry": {
          "type": "MultiPolygon",
          "coordinates": [
            [
              [ [21., 45.], [21., 44.7], [20., 44.7], [20., 45.], [21., 45.] ]
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
                [ [21., 45.], [21., 44.7], [20., 44.7], [20., 45.], [21., 45.] ]
              ]
            ]
        },
        "properties": {

          "isSquare": True,
          "x": 57000,
          "y": 70000,
          "zoom": 15
        },
        "type": "Feature"
      }
    ],
    "type" : "FeatureCollection"
  }
}

""" my_api_instance = UserLoginAPI()
my_api_instance.obtain_authorization("v-fita@microsoft.com", "Vvardenfello1")
project_admin_api_instance = project_admin_api.ProjectAdminApi()

body["tasks"] = MyAPI.util_split_quad_multipolygon_tasks(body["tasks"])
print(body["tasks"])
encoded_body = json.dumps(body)
reply = project_admin_api_instance.api_v1_admin_project_put(body, my_api_instance.get_authorization(), _preload_content=False)
print(reply.data.decode()) """
pattern_1 = r"(\[.*\])"
pattern_2 = r"\[\s*([0-9\.]+)\s*,\s*([0-9\.]+)\s*\]"
matches_1 = re.findall(pattern_1, "[ [1.5, 2.33], [22.12, 3], [3, 4], [4, 5] ]")
for match_1 in matches_1:
    match_1 = match_1[1:-1]
    matches_2 = re.findall(pattern_2, match_1)
    for match_2 in matches_2:
      print(match_2[0], match_2[1])
    
      