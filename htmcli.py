import argparse
import pickle
import datetime
from htm_msopenmaps_custom_api import UserLoginAPI
from swaggerAPIClient.swagger_client.api import project_admin_api, mapping_api, grid_api
from util import *
import htm_msopenmaps_custom_api
import urllib3
import subprocess
import os
import re
import json

parser = argparse.ArgumentParser(description='HOT Tasking Manager command line interface')
parser.add_argument('api', type=str, nargs=1)
parser.add_argument('operation', type=str, nargs=1)
parser.add_argument('-u', '--username', type=str)
parser.add_argument('-p', '--password', type=str)
#arbitraryTask: create?
parser.add_argument('-a', '--areaOfInterest', type=str)
parser.add_argument('-n', '--projectName', type=str)
parser.add_argument('-z', '--zoomLevel', type=str)
parser.add_argument('--cloneFromProjectId', type=str)

parser.add_argument('-i', '--projectId', type=str)
parser.add_argument('--allowedUsernames', type=str)
parser.add_argument('--campaignTag', type=str)
parser.add_argument('--changesetComment', type=str)
parser.add_argument('--defaultLocale', type=str)
parser.add_argument('--dueDate', type=str)
parser.add_argument('--enforceMapperLevel', type=str)
parser.add_argument('--enforceValidatorRole', type=str)
parser.add_argument('--entitiesToMap', type=str)
parser.add_argument('--imagery', type=str)
parser.add_argument('--josmPreset', type=str)
parser.add_argument('--licenseId', type=str)
parser.add_argument('--mapperLevel', type=str)
parser.add_argument('--mappingTypes', type=str)
parser.add_argument('--organisationTag', type=str)
parser.add_argument('--priorityAreas', type=str)
parser.add_argument('--private', type=str)
parser.add_argument('--description', type=str)
parser.add_argument('--instructions', type=str)
parser.add_argument('--locale', type=str)
#parser.add_argument('-n', '--name', type=str)
parser.add_argument('--perTaskInstructions', type=str)
parser.add_argument('--shortDescription', type=str)
parser.add_argument('--projectPriority', type=str)
parser.add_argument('--projectStatus', type=str)
parser.add_argument('--taskCreationMode', type=str)

parser.add_argument('-t', '--taskId', type=str)
parser.add_argument('-j', '--josmPath', type=str)

args = parser.parse_args()
print(args) #DEBUG_ONLY

if(args.api[0] == "user"):
    
    if(args.operation[0] == "login"):
        if(args.username == None or args.password == None):
            print("usage: htmcli.py user login [-u USERNAME] [-p PASSWORD]")
            exit(1)
        store = None
        login_api_instance = None
        try:
            store = open('authentication_info.obj', 'rb')
            login_api_instance = pickle.load(store)
        except:
            print("")
        finally:
            if(store != None):
                store.close()

        if(login_api_instance == None or int((datetime.datetime.now() - login_api_instance.timeCreated).total_seconds() / 60.) > 720):
            login_api_instance = UserLoginAPI()
            login_api_instance.obtain_authorization(args.username, args.password)
        
        store = open('authentication_info.obj', 'wb')
        pickle.dump(login_api_instance, store)
    
    else:
        print("User api operations are: login")
    
elif(args.api[0] == "project"):

    if(args.operation[0] == "create"):

        if(args.areaOfInterest == None or args.projectName == None or args.zoomLevel == None):
            print("usage: htmcli.py project create [-a AREAOFINTEREST] [-n PROJECTNAME] [-z ZOOMLEVEL]")
            exit(1)
        
        store = None
        login_api_instance = None
        try:
            store = open('authentication_info.obj', 'rb')
            login_api_instance = pickle.load(store)
        except:
            print("Authentication needed")
            exit(2)
        finally:
            if(store != None):
                store.close()
        
        if(int((datetime.datetime.now() - login_api_instance.timeCreated).total_seconds() / 60.) > 720):
            print("Reauthentication needed")
            exit(2)
        
        body = {
          "arbitraryTasks" : False,
          # to fill
        }

        pattern_1 = r"(\[.*\])"
        pattern_2 = r"\[\s*([0-9-\.]+)\s*,\s*([0-9-\.]+)\s*\]"
        matches_1 = re.findall(pattern_1, "[[44.796821, 20.367338], [44.798170, 20.394584], [44.814696, 20.382877], [44.807272, 20.365357], [44.796821, 20.367338]]")
        aoi_features = []
        for match_1 in matches_1:
            match_1 = match_1[1:-1]
            matches_2 = re.findall(pattern_2, match_1)
            polygon = []
            #print(matches_2)#DEBUG
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
        #print(aoi)

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

        zoom_create = int(args.zoomLevel)
        sw_tile = tileXY(bottom, left, zoom_create)
        se_tile = tileXY(bottom, right, zoom_create)
        ne_tile = tileXY(top, right, zoom_create)
        nw_tile = tileXY(top, left, zoom_create)

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

        grid_body = {
          "areaOfInterest" : aoi,
          "clipToAoi" : False,
          "grid" : grid
        }

        reply = grid_api.GridApi().api_v1_grid_intersecting_tiles_put(grid_body, "Token TVRBeE1qY3pOVEkuRUNIdjNnLjNLUzFuUWI3Nkx6UGhzQTNQcHpHRGVkT1hjNA==", _preload_content=False)
        #print(reply.data.decode())
        reply_json = json.loads(reply.data)

        body["projectName"] = args.projectName
        body["areaOfInterest"] = aoi
        body["tasks"] = reply_json
        if(args.cloneFromProjectId != None): body["cloneFromProjectId"] = int(args.cloneFromProjectId)

        #print(body)

        reply = project_admin_api.ProjectAdminApi().api_v1_admin_project_put(body, login_api_instance.get_authorization(), _preload_content=False)
        print(reply.data.decode())

    elif(args.operation[0] == "update"):

        if(args.projectId == None):
            print("usage: htmcli.py project update projectId ...[-a AREAOFINTEREST] [-n PROJECTNAME] [-t TASKS]")
            exit(1)

        store = None
        login_api_instance = None
        try:
            store = open('authentication_info.obj', 'rb')
            login_api_instance = pickle.load(store)
        except:
            print("Authentication needed")
            exit(2)
        finally:
            if(store != None):
                store.close()
        
        if(int((datetime.datetime.now() - login_api_instance.timeCreated).total_seconds() / 60.) > 720):
            print("Reauthentication needed")
            exit(2)

        reply = project_admin_api.ProjectAdminApi().api_v1_admin_project_project_id_get(login_api_instance.get_authorization(), int(args.projectId), _preload_content=False)
        reply_json = json.loads(reply.data.decode())
        print(reply_json)

        #print(args._get_kwargs())

        for arg_pair in args._get_kwargs():
            arg_name = arg_pair[0]
            arg_val = arg_pair[1]

            if(reply_json["mappingTypes"] == None):
                reply_json["mappingTypes"] = []

            if(arg_val == None or arg_name == "api" or arg_name == "operation"):
                #reply_json.pop(arg_name, None)
                continue

            if(arg_name == "allowedUsernames"):
                u_list = []
                if(arg_val != None):
                    for u in arg_val.split(","):
                        u_list.append(u.strip())
                reply_json["allowedUsernames"] = u_list
            
            elif(arg_name == "enforceMapperLevel"):
                if(arg_val == "true" or arg_val == "True"):
                    reply_json["enforceMapperLevel"] = True
                else:
                    reply_json["enforceMapperLevel"] = False

            elif(arg_name == "enforceValidatorRole"):
                if(arg_val == "true" or arg_val == "True"):
                    reply_json["enforceValidatorRole"] = True
                else:
                    reply_json["enforceValidatorRole"] = False

            elif(arg_name == "licenseId"):
                reply_json["licenseId"] = int(arg_val)

            elif(arg_name == "mappingTypes"):
                pattern = r"[^A-Za-z]*([A-Za-z]+)[^A-Za-z]*"
                matches = re.findall(pattern, arg_val)
                mt_list = []

                for match in matches:
                    mt_list.append(match)

                reply_json["mappingTypes"] = mt_list

            elif(arg_name == "description" or arg_name == "instructions" or arg_name == "projectName" or arg_name == "locale" or arg_name == "perTaskInstructions" or arg_name == "shortDescription"):
                if(arg_name == "projectName"):
                    reply_json["projectInfoLocales"][0]["name"] = arg_val
                else:
                    reply_json["projectInfoLocales"][0][arg_name] = arg_val

            elif(arg_name == "entitiesToMap"):
                entities = arg_val.split(",")
                for i in range(len(entities)):
                    entities[i] = entities[i].strip()
                reply_json[arg_name] = "".join(str(e)+"," for e in entities)
                reply_json[arg_name] = reply_json[arg_name].strip(",")

            else:
                reply_json[arg_name] = arg_val

        print(reply_json)
        reply = project_admin_api.ProjectAdminApi().api_v1_admin_project_project_id_post(reply_json, login_api_instance.get_authorization(), int(args.projectId), _preload_content=False)
        print(reply.data.decode())

    else:
        print("Project api operations are: create, update")

elif(args.api[0] == "task"):
    
    if(args.operation[0] == "map"):

        if(args.projectId == None or args.taskId == None):
            print("usage: htmcli.py task map [-i PROJECTID] [-t TASKID] [-j JOSMPATH]")
            exit(1)
        
        store = None
        login_api_instance = None
        try:
            store = open('authentication_info.obj', 'rb')
            login_api_instance = pickle.load(store)
        except:
            print("Authentication needed")
            exit(2)
        finally:
            if(store != None):
                store.close()
        
        if(int((datetime.datetime.now() - login_api_instance.timeCreated).total_seconds() / 60.) > 720):
            print("Reauthentication needed")
            exit(2)
        
        project_id = int(args.projectId)
        task_id = int(args.taskId)

        #Locking the task for mapping.
        reply = mapping_api.MappingApi().api_v1_project_project_id_task_task_id_lock_for_mapping_post(login_api_instance.get_authorization(), "en", project_id, task_id, _preload_content=False)
        #print(reply.data.decode())

        project_json = htm_msopenmaps_custom_api.ProjectsApi().api_custom_project_project_id_get(login_api_instance.get_authorization(), project_id)
        #print("DEBUG", project_json)
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
        #print(task_bbox)#DEBUG
        
        #print("JOSM path?")
        #josm_command = input()
        josm_command = args.josmPath + " " + os.getcwd() + "\\default_data\\bing_aerial_imagery.wms"
        #print(josm_command)
        #josm_command = "C:\\Program Files (x86)\\JOSM\\josm.exe D:\\Test1\\bing_aerial_imagery.wms"
        #josm_java_commant = "java -jar \"C:\Program Files (x86)\JOSM\josm-tested.jar\" runjosm --download \"D:\Test1\\bing_aerial_imagery.wms\""
        
        josm = subprocess.Popen(josm_command, stdout=subprocess.PIPE)
        
        import threading
        def thr_foo(josm, event_started):
        	#print("JOSM LISTENER: LISTENING")
        	while True:
        		line = josm.stdout.readline().rstrip()
        		#print("JOSM LISTENER:", line)
        		if("INFO: Changeset updater active (checks every 60 minutes if open changesets have been closed)" in line.decode()):
        			event_started.set()
        		if("RemoteControl received: GET /load_data?new_layer=true&layer_name=Queried+Data" in line.decode()):
        			break
        	#print("JOSM LISTENER: STOPPING")
        
        event = threading.Event()
        thr = threading.Thread(target=thr_foo, args=[josm, event])
        thr.start()
        event.wait()
        #print("Went through")

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
        #print(reply.data.decode())
        
        #Create an overpass querry
        overpass_query = {
        	"timeout" : 20,
        	"types" : ["node", "way", "relation"],
        	"tag_filter" : {
        		"building" : None
        	},
        	"bbox" : task_bbox
        }
              
        #print(stringifyOverpassQuery(overpass_query))
        
        #reply = urllib3.PoolManager().request("GET", "http://127.0.0.1:8111/import?url=http://overpass-api.de/api/interpreter?data="+stringifyOverpassQuery(overpass_query))
        reply = urllib3.PoolManager().request("GET", "http://overpass-api.de/api/interpreter?data="+stringifyOverpassQuery(overpass_query))
        #print(reply.data.decode())
        
        fields = {
        	"new_layer" : "true",
        	"layer_name" : "Queried Data",
        	"data" : reply.data.decode()
        }
        
        reply = urllib3.PoolManager().request("GET", "http://127.0.0.1:8111/load_data", fields=fields)
        #print(reply.data.decode())

    else:
        print("Task api operations are: map")