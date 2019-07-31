from swaggerAPIClient.swagger_client.api import project_admin_api, grid_api
import math
import pygeotile
import re
import json

def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return (xtile, ytile)

def num2deg(xtile, ytile, zoom):
    n = 2.0 ** zoom
    lon_deg = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
    lat_deg = math.degrees(lat_rad)
    return (lat_deg, lon_deg)

from math import *

def numTiles(z):
    return(pow(2,z))

def sec(x):
    return(1/cos(x))

def latlon2relativeXY(lat,lon):
    x = (lon + 180) / 360
    y = (1 - log(tan(radians(lat)) + sec(radians(lat))) / pi) / 2
    return(x,y)

def latlon2xy(lat,lon,z):
    n = numTiles(z)
    x,y = latlon2relativeXY(lat,lon)
    return(n*x, n*y)
  
def tileXY(lat, lon, z):
    x,y = latlon2xy(lat,lon,z)
    return(int(x),int(y))

def xy2latlon(x,y,z):
     n = numTiles(z)
     relY = y / n
     lat = mercatorToLat(pi * (1 - 2 * relY))
     lon = -180.0 + 360.0 * x / n
     return(lat,lon)
  
def latEdges(y,z):
    n = numTiles(z)
    unit = 1 / n
    relY1 = y * unit
    relY2 = relY1 + unit
    lat1 = mercatorToLat(pi * (1 - 2 * relY1))
    lat2 = mercatorToLat(pi * (1 - 2 * relY2))
    return(lat1,lat2)

def lonEdges(x,z):
    n = numTiles(z)
    unit = 360 / n
    lon1 = -180 + x * unit
    lon2 = lon1 + unit
    return(lon1,lon2)
  
def tileEdges(x,y,z):
     lat1,lat2 = latEdges(y,z)
     lon1,lon2 = lonEdges(x,z)
     return((lat2, lon1, lat1, lon2)) # S,W,N,E

def mercatorToLat(mercatorY):
    return(degrees(atan(sinh(mercatorY))))

def tileSizePixels():
    return(256)

def tileLayerExt(layer):
    if(layer in ('oam')):
        return('jpg')
    return('png')

def tileLayerBase(layer):
    layers = {
        "tah": "http://cassini.toolserver.org:8080/http://a.tile.openstreetmap.org/+http://toolserver.org/~cmarqu/hill/",
        	#"tah": "http://tah.openstreetmap.org/Tiles/tile/",
        "oam": "http://oam1.hypercube.telascience.org/tiles/1.0.0/openaerialmap-900913/",
        "mapnik": "http://tile.openstreetmap.org/mapnik/"
    }
    return(layers[layer])
  
def tileURL(x,y,z,layer):
    return "%s%d/%d/%d.%s" % (tileLayerBase(layer),z,x,y,tileLayerExt(layer))

#test
lat_coord = 44
lon_coord = 20.935
zoom = 15

tile_xy = tileXY(lat_coord, lon_coord, zoom)
print(tile_xy)
tile_edges = tileEdges(tile_xy[0], tile_xy[1], zoom)
print(tile_edges)
tile_edges = list(tile_edges)

tmp = tile_edges[0]
tile_edges[0] = tile_edges[1]
tile_edges[1] = tmp

tmp = tile_edges[2]
tile_edges[2] = tile_edges[3]
tile_edges[3] = tmp

coordinates = [[tile_edges[0], tile_edges[1]], [tile_edges[0], tile_edges[3]], [tile_edges[2], tile_edges[3]], [tile_edges[2], tile_edges[1]], [tile_edges[0], tile_edges[1]]]

#test grid api
tile_edges_2 = tileEdges(tile_xy[0], tile_xy[1] + 4, zoom)
print(tile_edges_2)
tile_edges_2 = list(tile_edges_2)

tmp = tile_edges_2[0]
tile_edges_2[0] = tile_edges_2[1]
tile_edges_2[1] = tmp

tmp = tile_edges_2[2]
tile_edges_2[2] = tile_edges_2[3]
tile_edges_2[3] = tmp

coordinates_2 = [[tile_edges_2[0], tile_edges_2[1]], [tile_edges_2[0], tile_edges_2[3]], [tile_edges_2[2], tile_edges_2[3]], [tile_edges_2[2], tile_edges_2[1]], [tile_edges_2[0], tile_edges_2[1]]]
#test grid api

pattern_1 = r"(\[.*\])"
pattern_2 = r"\[\s*([0-9-\.]+)\s*,\s*([0-9-\.]+)\s*\]"
matches_1 = re.findall(pattern_1, "[[44,20.925], [44, 20.95], [44.01, 20.95], [44.01, 20.925], [44,20.925]]")
aoi_features = []
for match_1 in matches_1:
    match_1 = match_1[1:-1]
    matches_2 = re.findall(pattern_2, match_1)
    polygon = []
    print(matches_2)#DEBUG
    for match_2 in matches_2:
        x = float(match_2[0])
        y = float(match_2[1])
        point = [x, y]
        polygon.append(point)
    newFeature = {"geometry": {
        "type": "Polygon"
        },
        "properties": None,
        "type": "Feature"
    }
    newFeature["geometry"]["coordinates"] = [polygon]
    aoi_features.append(newFeature)
aoi = {}
aoi["type"] = "FeatureCollection"
aoi["features"] = aoi_features

left = 500.
bottom = 500.
right = -1.
top = -1.

for coord in aoi["features"][0]["geometry"]["coordinates"][0]:
    if(coord[1] < left):
        left = coord[1]
    if(coord[1] > right):
        right = coord[1]
    if(coord[0] < bottom):
        bottom = coord[0]
    if(coord[0] > top):
        top = coord[0]

#Swap coordinates on AOI, it for some reason requires coordinates with swapped latitude and longitude(?)
for i in range(len(aoi["features"][0]["geometry"]["coordinates"][0])):
    tmp = aoi["features"][0]["geometry"]["coordinates"][0][i][0]
    aoi["features"][0]["geometry"]["coordinates"][0][i][0] = aoi["features"][0]["geometry"]["coordinates"][0][i][1]
    aoi["features"][0]["geometry"]["coordinates"][0][i][1] = tmp

#print(left)
#print(bottom)
#print(right)
#print(top)

zoom_create = 16
sw_tile = tileXY(bottom, left, zoom_create)
se_tile = tileXY(bottom, right, zoom_create)
ne_tile = tileXY(top, right, zoom_create)
nw_tile = tileXY(top, left, zoom_create)

#print(sw_tile)
#print(se_tile)
#print(ne_tile)
#print(nw_tile)

grid = {
    "features" : [],
    "type" : "FeatureCollection"
}
for x in range(nw_tile[0], se_tile[0]+1):
    for y in range(nw_tile[1], se_tile[1]+1):
        tile_edges = tileEdges(x, y, zoom_create)
        #print(tile_edges)
        tile_edges = list(tile_edges)

        tmp = tile_edges[0]
        tile_edges[0] = tile_edges[1]
        tile_edges[1] = tmp

        tmp = tile_edges[2]
        tile_edges[2] = tile_edges[3]
        tile_edges[3] = tmp

        coordinates = [[tile_edges[0], tile_edges[1]], [tile_edges[0], tile_edges[3]], [tile_edges[2], tile_edges[3]], [tile_edges[2], tile_edges[1]], [tile_edges[0], tile_edges[1]]]
        
        single_feature = {
            "geometry": {
                "coordinates": [
                  [
                    coordinates
                  ]
                ],
                "type": "MultiPolygon"
            },
            "properties": {
              "isSquare": True,
              "x": x,
              "y": 2**zoom_create - 1 - y,
              "zoom": zoom_create
            },
            "type": "Feature"
        }
        grid["features"].append(single_feature)

#print(grid)

grid_body = {
  "areaOfInterest" : aoi,
  "clipToAoi" : True,
  "grid" : grid
}

#print(aoi)
#print(grid)
print(len(grid["features"]))

reply = grid_api.GridApi().api_v1_grid_intersecting_tiles_put(grid_body, "Token TVRBeE1qY3pOVEkuRUNIdjNnLjNLUzFuUWI3Nkx6UGhzQTNQcHpHRGVkT1hjNA==", _preload_content=False)
#print(reply.data.decode())

reply_json = json.loads(reply.data)
print(len(reply_json["features"]))

body = {
  "arbitraryTasks" : False,
  "areaOfInterest" : aoi,
  "projectName" : "test_tiles_2",
  "tasks" : reply_json
}

#print(body)

reply = project_admin_api.ProjectAdminApi().api_v1_admin_project_put(body, "Token TVRBeE1qY3pOVEkuRUNIdjNnLjNLUzFuUWI3Nkx6UGhzQTNQcHpHRGVkT1hjNA==", _preload_content=False)
print(reply.data.decode())