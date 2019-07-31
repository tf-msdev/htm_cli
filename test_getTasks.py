import htm_msopenmaps_custom_api
from swaggerAPIClient.swagger_client.api import project_admin_api, mapping_api
import os
import subprocess
import urllib3
import urllib
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

leftmost = min([nw_coord[0], ne_coord[0], se_coord[0], sw_coord[0]])
rightmost = max([nw_coord[0], ne_coord[0], se_coord[0], sw_coord[0]])
downmost = min([nw_coord[1], ne_coord[1], se_coord[1], sw_coord[1]])
upmost = max([nw_coord[1], ne_coord[1], se_coord[1], sw_coord[1]])

login_api_instance = htm_msopenmaps_custom_api.UserLoginAPI()
login_api_instance.set_authorization_manually("TVRBeE1qY3pOVEkuRUNNRGZnLmktaWVQVkdVOTRSaF80NnJxZU1ENzd0ZXJRaw==")
#login_api_instance.obtain_authorization("v-fita@microsoft.com", "Vvardenfello1")

#Parameters
project_id = 475
task_id = 3

#Locking the task for mapping.
#reply = mapping_api.MappingApi().api_v1_project_project_id_task_task_id_lock_for_mapping_post(login_api_instance.get_authorization(), "en", project_id, task_id, _preload_content=False)
#print(reply.data.decode())

#Getting tasks geometry, boundaries.
project_json = htm_msopenmaps_custom_api.ProjectsApi().api_custom_project_project_id_get(login_api_instance.get_authorization(), project_id)
task_bbox = {
	"left": 500.0,
	"bottom": 500.0,
	"right": 0.0,
	"top": 0.0,
}
for task in project_json["tasks"]["features"]:
	if(task["properties"]["taskId"] == task_id):
		for coord in task["geometry"]["coordinates"][0][0]:
			if(coord[0] < task_bbox["left"]):
				task_bbox["left"] = coord[0]
			if(coord[0] > task_bbox["right"]):
				task_bbox["right"] = coord[0]
			if(coord[1] < task_bbox["bottom"]):
				task_bbox["bottom"] = coord[1]
			if(coord[1] > task_bbox["top"]):
				task_bbox["top"] = coord[1]
		break
print(task_bbox)#DEBUG

print("JOSM path?")
#josm_command = input()
josm_command = "C:\Program Files (x86)\JOSM\josm.exe D:\Test1\\bing_aerial_imagery.wms"
#josm_java_commant = "java -jar \"C:\Program Files (x86)\JOSM\josm-tested.jar\" runjosm --download \"D:\Test1\\bing_aerial_imagery.wms\""

josm = subprocess.Popen(josm_command, stdout=subprocess.PIPE)
while True:
	line = josm.stdout.readline().rstrip()
	print(line)
	if("INFO: Changeset updater active (checks every 60 minutes if open changesets have been closed)" in line.decode()):
		break

#Process started
headers = {
	"Host" : "127.0.0.1:8111",
	"Proxy-Connection" : "keep-alive",
	"Upgrade-Insecure-Requests" : 1,
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
	"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
	"Referer" : "http://tasking-manager-msopenmaps.cloudapp.net/project/417?task=1",
	"Accept-Encoding" : "gzip, deflate, br",
	"Accept-Language" : "en-US,en;q=0.9"
}

fields = {
	"left" : task_bbox["left"],
	"bottom" : task_bbox["bottom"],
	"right" : task_bbox["right"],
	"top" : task_bbox["top"],
	"changeset_comment" : "",
	"changeset_source" : "Bing",
	"new_layer" : False,
	"resume_edit" : False,
	"project_id" : project_id,
	"task_id" : task_id,
	"validation_required" : False,
	"task_step" : "mapping",
	"download_gpx" : True,
	"download_policy" : "never",
	"auth_token" : login_api_instance.get_authorization(token_only=True)
}

reply = urllib3.PoolManager().request("GET", "http://127.0.0.1:8111/load_and_zoom_ms", fields=fields, headers=headers)
print(reply.data.decode())

#Create an overpass querry
overpass_query = {
	"timeout" : 20,
	"types" : ["node", "way", "relation"],
	"tag_filter" : {
		"building" : None
	},
	"bbox" : task_bbox	
}

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
					search_params = search_params + "=\"" + overpass_query["tag_filter"][tag] + "\""
				search_params = search_params + "]"

		search_params = search_params + ";"
		
	string_query = string_query + "(" + search_params + ");out%20meta;>;out%20meta;"
	return string_query

print(stringifyOverpassQuery(overpass_query))

#reply = urllib3.PoolManager().request("GET", "http://127.0.0.1:8111/import?url=http://overpass-api.de/api/interpreter?data="+stringifyOverpassQuery(overpass_query))
reply = urllib3.PoolManager().request("GET", "http://overpass-api.de/api/interpreter?data="+stringifyOverpassQuery(overpass_query))
print(reply.data.decode())

fields = {
	"new_layer" : "true",
	"layer_name" : "Queried Data",
	"data" : reply.data.decode()
}

reply = urllib3.PoolManager().request("GET", "http://127.0.0.1:8111/load_data", fields=fields)
print(reply.data.decode())

""" [out:json][timeout:25];
// gather results
(
  // query part for: “shop=bicycle”
  node["shop"="bicycle"]({{bbox}});
  way["shop"="bicycle"]({{bbox}});
  relation["amenity"="cafe"]({{bbox}});
  // query part for: “shop=bicycle”
  node["amenity"="cafe"]({{bbox}});
  way["amenity"="cafe"]({{bbox}});
  relation["shop"="bicycle"]({{bbox}});
);
// print results
out body;
>;
out skel qt; 

https://forum.openstreetmap.org/viewtopic.php?id=56442
https://taginfo.openstreetmap.org/

"""
