from swaggerAPIClient.swagger_client.api import project_admin_api
import math

def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return (xtile, ytile)

def num2deg(xtile, ytile, zoom):
    n = 2.0 ** zoom
    lon_deg = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1.0 - 2.0 * ytile / n)))
    lat_deg = math.degrees(lat_rad)
    return (lat_deg, lon_deg)

zoom = 15
latitude = 43.00048828125
longitude = -3

nw_xy = deg2num(longitude, latitude, zoom)
print(nw_xy)

nw_coord = num2deg(nw_xy[0], nw_xy[1], zoom)
ne_coord = num2deg(nw_xy[0] + 1, nw_xy[1], zoom)
se_coord = num2deg(nw_xy[0] + 1, nw_xy[1] + 1, zoom)
sw_coord = num2deg(nw_xy[0], nw_xy[1] + 1, zoom)

nw_xy = deg2num(-latitude, longitude, zoom)

body = {
  "arbitraryTasks" : False,
  "areaOfInterest" : {
    "features": [
      {
        "geometry": {
        "coordinates": [
          [
            [
              list(nw_coord),
              list(ne_coord),
              list(se_coord),
              list(sw_coord),
              list(nw_coord)
            ]
          ]
        ],
        "type": "MultiPolygon"
        },
        "properties": {
          "isSquare": True
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
        "coordinates": [
          [
            [
              list(nw_coord),
              list(ne_coord),
              list(se_coord),
              list(sw_coord),
              list(nw_coord)
            ]
          ]
        ],
        "type": "MultiPolygon"
        },
        "properties": {
          "isSquare": True,
          "x": nw_xy[0],
          "y": nw_xy[1],
          "zoom": zoom
        },
        "type": "Feature"
      }
    ],
    "type" : "FeatureCollection"
  }
}

#print(nw_coord, ne_coord, se_coord, sw_coord)
#print(body)

#reply = project_admin_api.ProjectAdminApi().api_v1_admin_project_put(body, "Token TVRBeE1qY3pOVEkuRUJ0cVN3LlpFbkowVkhhYlBQTEVLY2Y1aG5jTjNqTWd4OA==", _preload_content=False)
#print(reply.data.decode())