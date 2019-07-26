from htm_msopenmaps_custom_api import UserLoginAPI
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
login_api_instance.obtain_authorization("v-fita@microsoft.com", "Vvardenfello1")

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

#reply = mapping_api_instance = mapping_api.MappingApi().api_v1_project_project_id_task_task_id_lock_for_mapping_post(login_api_instance.get_authorization(), "en", 418, 24, _preload_content=False)
#print(reply.data.decode())

#reply = mapping_api_instance = mapping_api.MappingApi().api_v1_project_project_id_tasks_as_gpx_get(445, _preload_content=False)
#print(reply.data.decode())

#reply = mapping_api_instance = mapping_api.MappingApi().api_v1_project_project_id_tasks_as_osm_xml_get(418, tasks="24", as_file="false", _preload_content=False)
#print(reply.data.decode())

fields = {
	"left" : leftmost-0.005,
	"bottom" : downmost-0.005,
	"right" : rightmost+0.005,
	"top" : upmost+0.005,
    "addtags" : "waterway=river",
	"changeset_comment" : "",
	"changeset_source" : "Bing",
	"new_layer" : True,
	"resume_edit" : False,
	"project_id" : 445,
	"task_id" : 3,
	"validation_required" : False,
	"task_step" : "mapping",
	"download_gpx" : True,
	"auth_token" : login_api_instance.get_authorization().split()[1]
}

print(login_api_instance.get_authorization().split()[1])
reply = urllib3.PoolManager().request("GET", "http://127.0.0.1:8111/load_and_zoom_ms", fields=fields, headers=headers)
print(reply.data.decode())