from htm_msopenmaps_custom_api import UserLoginAPI
from swaggerAPIClient.swagger_client.api import project_admin_api, mapping_api
import os
import subprocess
import urllib3
import test_create
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

login_api_instance = UserLoginAPI()
#login_api_instance.obtain_authorization("v-fita@microsoft.com", "Vvardenfello1")

""" reply = mapping_api.MappingApi().api_v1_project_project_id_has_user_locked_tasks_details_get("Token TVRBeE1qY3pOVEkuRUNDYm9BLnlCbzNQNTBIR19PRFZvbTdsSVRJOVRlbVZUSQ==", "en", 445, _preload_content=False)
print(reply.data.decode())

project_id = 445
fields={
	"as_file" : "false",
	"abbreviated" : "false"
}
headers = {
	"Accept" : "application/json",
	"Accept-Language" : "en"
}
reply = urllib3.PoolManager().request("GET", "http://tasking-manager-msopenmaps.cloudapp.net/api/v1/project/"+str(project_id), fields=fields, headers=headers)
print(reply.data.decode()) """
#This part was about geting the tasks geometry. Unauthorized access on every way to get the info. Confidential maybe?

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


#get task

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
	"left" : -2.9972076410647,
	"bottom" : 43.04605992990042,
	"right" : -2.9968643183108394,
	"top" : 43.04631083144409,
	"changeset_comment" : "",
	"changeset_source" : "Bing",
	"new_layer" : False,
	"resume_edit" : False,
	"project_id" : 445,
	"task_id" : 3,
	"validation_required" : False,
	"task_step" : "mapping",
	"download_gpx" : True,
	"download_policy" : "never",
	"auth_token" : "TVRBeE1qY3pOVEkuRUNDYm9BLnlCbzNQNTBIR19PRFZvbTdsSVRJOVRlbVZUSQ=="#login_api_instance.get_authorization().split()[1]
}

reply = urllib3.PoolManager().request("GET", "http://127.0.0.1:8111/load_and_zoom_ms", fields=fields, headers=headers)
print(reply.data.decode())

reply = urllib3.PoolManager().request("GET", "http://127.0.0.1:8111/import?url=http://overpass-api.de/api/interpreter?data=[timeout:20];(node(43.04605992990042,-2.9972076410647,43.04631083144409,-2.9968643183108394);way(43.04605992990042,-2.9972076410647,43.04631083144409,-2.9968643183108394);relation(43.04605992990042,-2.9972076410647,43.04631083144409,-2.9968643183108394););out%20meta;>;out%20meta;")
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
