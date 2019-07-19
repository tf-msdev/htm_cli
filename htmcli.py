import argparse
import pickle
import datetime
from htm_msopenmaps_custom_api import UserLoginAPI
from swaggerAPIClient.swagger_client.api import project_admin_api, mapping_api, grid_api
import re

parser = argparse.ArgumentParser(description='HOT Tasking Manager command line interface')
parser.add_argument('api', type=str, nargs=1)
parser.add_argument('operation', type=str, nargs=1)
parser.add_argument('-u', '--username', type=str)
parser.add_argument('-p', '--password', type=str)
#arbitraryTask: create?
parser.add_argument('-a', '--areaOfInterest', type=str)
parser.add_argument('-n', '--projectName', type=str)
parser.add_argument('-t', '--tasks', type=str)

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
        finally:
            if(store != None):
                store.close()
        
        if((datetime.datetime.now() - login_api_instance.timeCreated).total_seconds() / 60. > 10.):
            ("Authentication needed")
        
        pattern_1 = r"(\[.*\])"
        pattern_2 = r"\[\s*([0-9\.]+)\s*,\s*([0-9\.]+)\s*\]"
        matches_1 = re.findall(pattern_1, "[ [1.5, 2.33], [22.12, 3], [3, 4], [4, 5] ]")
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
            
            



        