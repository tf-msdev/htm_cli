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

def stringifyOverpassQuery(overpass_query):
	string_query = ""
	if("bbox" in overpass_query and len(overpass_query["bbox"]) == 4):
		string_query = string_query + "[bbox:" + str(overpass_query["bbox"]["bottom"]) + "," + str(overpass_query["bbox"]["left"]) + "," + str(overpass_query["bbox"]["top"]) + "," + str(overpass_query["bbox"]["right"]) + "]"
	if("timeout" in overpass_query):
		string_query = string_query + "[timeout:" + str(overpass_query["timeout"]) + "];"
	search_params = ""
	for type_of in overpass_query["types"]:
		search_params = search_params + type_of

		if("tag_filter" in overpass_query and len(overpass_query["tag_filter"]) > 0):
			for tag in overpass_query["tag_filter"]:
				search_params = search_params + "[\"" + tag + "\""
				if(overpass_query["tag_filter"][tag] != None):
					search_params = search_params + "=\"" + overpass_query["tag_filter"][tag] + "\"];"
				else:
					search_params = search_params + "];" + type_of + "[~\".*\"~\"^" + tag + "$\"];"
		
	string_query = string_query + "(" + search_params + ");out%20meta;>;out%20meta;"
	return string_query