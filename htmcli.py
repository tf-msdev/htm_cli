import argparse
import pickle
import datetime
from htm_msopenmaps_custom_api import UserLoginAPI
from swaggerAPIClient.swagger_client.api import project_admin_api, mapping_api, grid_api
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
parser.add_argument('-t', '--tasks', type=str)

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

        if(login_api_instance == None or (datetime.datetime.now() - login_api_instance.timeCreated).total_seconds() / 60. > 10.):
            login_api_instance = UserLoginAPI()
            login_api_instance.obtain_authorization(args.username, args.password)
        
        store = open('authentication_info.obj', 'wb')
        pickle.dump(login_api_instance, store)
    
    else:
        print("User api operations are: login")
    
elif(args.api[0] == "project"):

    if(args.operation[0] == "create"):

        if(args.areaOfInterest == None or args.projectName == None or args.tasks == None):
            print("usage: htmcli.py project create [-a AREAOFINTEREST] [-n PROJECTNAME] [-t TASKS]")
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
        
        if(int((datetime.datetime.now() - login_api_instance.timeCreated).total_seconds() / 60.) > 30):
            print("Reauthentication needed")
            exit(2)
        
        body = {
          "arbitraryTasks" : False,
          # to fill
        }

        pattern_1 = r"(\[.*\])"
        pattern_2 = r"\[\s*([0-9\.]+)\s*,\s*([0-9\.]+)\s*\]"
        matches_1 = re.findall(pattern_1, args.areaOfInterest)
        aoi_features = []
        for match_1 in matches_1:
            match_1 = match_1[1:-1]
            matches_2 = re.findall(pattern_2, match_1)
            polygon = []
            for match_2 in matches_2:
                x = float(match_2[0])
                y = float(match_2[1])
                point = [x, y]
                polygon.append(point)
            newFeature = {"geometry": {
                "type": "MultiPolygon"
                },
                "properties": {
                    "isSquare": True,
                    "x": 2400,
                    "y": 1750,
                    "zoom": 15
                },
                "type": "Feature"
            }
            newFeature["geometry"]["coordinates"] = [[polygon]]
            aoi_features.append(newFeature)
        aoi = {}
        aoi["type"] = "FeatureCollection"
        aoi["features"] = aoi_features
        #print(aoi)

        pattern_1 = r"(\[.*\])"
        pattern_2 = r"\[\s*([0-9\.]+)\s*,\s*([0-9\.]+)\s*\]"
        matches_1 = re.findall(pattern_1, args.areaOfInterest)
        tasks_features = []
        for match_1 in matches_1:
            match_1 = match_1[1:-1]
            matches_2 = re.findall(pattern_2, match_1)
            polygon = []
            for match_2 in matches_2:
                x = float(match_2[0])
                y = float(match_2[1])
                point = [x, y]
                polygon.append(point)
            newFeature = {"geometry": {
                "type": "MultiPolygon"
                },
                "properties": {
                    "isSquare": True,
                    "x": 2400,
                    "y": 1750,
                    "zoom": 15
                },
                "type": "Feature"
            }
            newFeature["geometry"]["coordinates"] = [[polygon]]
            tasks_features.append(newFeature)
        tasks = {}
        tasks["type"] = "FeatureCollection"
        tasks["features"] = tasks_features
        #print(tasks)

        body["projectName"] = args.projectName
        body["areaOfInterest"] = aoi
        body["tasks"] = tasks
        print(body)

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
        
        if(int((datetime.datetime.now() - login_api_instance.timeCreated).total_seconds() / 60.) > 30):
            print("Reauthentication needed")
            exit(2)

        reply = project_admin_api.ProjectAdminApi().api_v1_admin_project_project_id_get(login_api_instance.get_authorization(), int(args.projectId), _preload_content=False)
        reply = json.loads(reply.data.decode())
        #print(reply)

        print(args._get_kwargs())

        for arg_pair in args._get_kwargs():
            arg_name = arg_pair[0]
            arg_val = arg_pair[1]

            if(arg_val == None or arg_name == "api" or arg_name == "operation"):
                reply.pop(arg_name, None)
                continue

            if(arg_name == "allowedUsernames"):
                arg_val = arg_val.strip('[')
                arg_val = arg_val.strip(']')
                u_list = []
                for u in arg_val.split(","):
                    u_list.append(u)
                reply["allowedUsernames"] = u_list
            
            elif(arg_name == "enforceMapperLevel"):
                if(arg_val == "true" or arg_val == "True"):
                    reply["enforceMapperLevel"] = True
                else:
                    reply["enforceMapperLevel"] = False

            elif(arg_name == "enforceValidatorRole"):
                if(arg_val == "true" or arg_val == "True"):
                    reply["enforceValidatorRole"] = True
                else:
                    reply["enforceValidatorRole"] = False

            elif(arg_name == "licenseId"):
                reply["licenseId"] = int(arg_val)

            elif(arg_name == "mappingTypes"):
                pattern = r"[^A-Za-z]*([A-Za-z]+)[^A-Za-z]*"
                matches = re.findall(pattern, arg_val)
                mt_list = []

                for match in matches:
                    mt_list.append(match)

                reply["mappingTypes"] = mt_list

            elif(arg_name == "description" or arg_name == "instructions" or arg_name == "projectName" or arg_name == "locale" or arg_name == "perTaskInstructions" or arg_name == "shortDescription"):
                if(arg_name == "projectName"):
                    reply["projectInfoLocales"]["name"] = arg_val
                else:
                    reply["projectInfoLocales"][arg_name] = arg_val

            else:
                reply[arg_name] = arg_val

        print(reply)
        reply = project_admin_api.ProjectAdminApi().api_v1_admin_project_project_id_post(reply, login_api_instance.get_authorization(), int(args.projectId), _preload_content=False)
        print(reply.data.decode())

    else:
        print("Project api operations are: create, update")