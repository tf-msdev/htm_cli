import urllib3
from bs4 import BeautifulSoup as bs
import mechanize
import cookiejar
import base64
from swaggerAPIClient.swagger_client.rest import ApiException
import json
from swaggerAPIClient.swagger_client.api import authentication_api, project_admin_api, mapping_api, grid_api
import datetime

#Here You should define admin credentials
admin_username = "v-fita@microsoft.com"
admin_password = "Vvardenfello1"

#Example: This is how the body should look like when a project is created.
#It includes area of interest, name and tasks.
arbitraryTasks = False
areaOfInterest = {
  "features": [
    {
      "geometry": {
        "coordinates": [
          [
            [
              [
                -4.0237,
                56.0904
              ],
              [
                -3.9111,
                56.1715
              ],
              [
                -3.8122,
                56.098
              ],
              [
                -4.0237,
                56.0904
              ]
            ]
          ]
        ],
        "type": "MultiPolygon"
      },
      "properties": {
        "isSquare": True,
        "x": 2402,
        "y": 1736,
        "zoom": 12
      },
      "type": "Feature"
    }
  ],
  "type": "FeatureCollection"
}
cloneFromProjectId = 1
projectName = "My new project"
tasks = {
  "features": [
    {
      "geometry": {
        "coordinates": [
          [
            [
              [
                -4.0237,
                56.0904
              ],
              [
                -3.9111,
                56.1715
              ],
              [
                -3.8122,
                56.098
              ],
              [
                -4.0237,
                56.0904
              ]
            ]
          ]
        ],
        "type": "MultiPolygon"
      },
      "properties": {
        "isSquare": True,
        "x": 2402,
        "y": 1736,
        "zoom": 12
      },
      "type": "Feature"
    }
  ],
  "type": "FeatureCollection"
}

#Example: This is how the body should look like when a project is updated.
#It includes everything that is configurable on htm.
#Rogue field
allowNonBeginners = True,
allowedUsernames = [
  "Filip Tanic",
  "urosv"
]
campaignTag = "new campaign"
changesetComment = "hotosm-project-391"
defaultLocale = "en"
dueDate = "2020-04-11T12:38:49"
enforceMapperLevel = False
enforceValidatorRole = False
entitiesToMap = "Buildings only"
imagery = "https://www.bing.com/maps/"
josmPreset = "josm preset goes here"
licenseId = 1
mapperLevel = "BEGINNER"
#Rogue field
mappingEditors = [
  "ID",
  "JOSM",
  "POTLATCH_2",
  "FIELD_PAPERS"
]
mappingTypes = [
  "BUILDINGS",
  "ROADS"#,
  #"WATERWAYS",
  #LANDUSE,
  #OTHER
]
organisationTag = "my organization"
priorityAreas = [
  {
    "coordinates": [
      [
        [
          -4.0237,
          56.0904
        ],
        [
          -3.9111,
          56.1715
        ],
        [
          -3.8122,
          56.098
        ],
        [
          -4.0237,
          56.0904
        ]
      ]
    ],
    "type": "Polygon"
  }
]
private = True
projectInfoLocales = [
  {
    "description": "Awesome little project and a little bit more",
    "instructions": "Complete the tasks",
    "locale": "en",
    "name": "My new project 2",
    "perTaskInstructions": "Use Bingery Imagery Only",
    "shortDescription": "A short description indeed"
  }
]
projectPriority = "LOW"
projectStatus = "PUBLISHED"
taskCreationMode = "GRID"
#Rogue field
validationEditors = [
  "ID",
  "JOSM",
  "POTLATCH_2",
  "FIELD_PAPERS"
]

class UserLoginAPI:

    def __init__(self, authorization=""):
        #self.http = urllib3.PoolManager()
        self.authorization = authorization
        self.timeCreated = datetime.datetime.now()

    def set_authorization_manually(self, encoded_session_token):
        """ Sets the authorization token only
		
        Parameters:
        encoded_session_token (string): base64 encoded session token

        Returns:
        void
		"""
        self.authorization = encoded_session_token

    def get_authorization(self, token_only=False):
        """ Returns authorization

        Parameters:
        token_only (boolean): If True, returns token only, else it returns a string in format "Token <encoded_session_token>"

        Returns:
        string: token or header-ready token + session_token

        """
        if(token_only == True):
            return self.authorization

        return "Token " + self.authorization
        
    def obtain_authorization(self, admin_username, admin_password):
        """ Obtains authorization for the HTM

        Parameters:
        admin_username (string): username of an existing admin
        admin_password (string): password of an existing admin

        Returns:
        string: Header-ready token + session_token

        """
        #This is the login/authorization part. It manually submits forms and is equivalent to a user login scenario in a real browser
        urlLogIn = 'http://tasking-manager-msopenmaps.cloudapp.net/api/v1/auth/login'
        br = mechanize.Browser()
        br.set_handle_robots(False) # ignore robots
        br.open(urlLogIn)
        br.select_form(nr=0)
        br["username"] = admin_username
        br["password"] = admin_password
        res = br.submit()
        content = res.read()
        soupGrantAccess = bs(content.decode("utf-8"), 'html.parser')
        authenticity_token = ""
        for child in soupGrantAccess.find('form', action="https://www.openstreetmap.org/oauth/authorize").children:
            if (hasattr(child, 'attrs') and 'name' in child.attrs and child.attrs['name'] == "authenticity_token"):
                authenticity_token = child.attrs['value']
        oauth_token = soupGrantAccess.find(id="oauth_token")["value"]
        print("autheticity_token ", authenticity_token)
        print("oauth_token ", oauth_token)

        br.select_form(nr=0)
        res = br.submit()

        #Obtaining the session_token from the url
        session_token = res.wrapped._url.split("&")[1].split("=")[1]
        print("session_token ", session_token)
        content = res.read()

        #Encoding the token as a base64 string. Required format
        encoded_session_token = base64.b64encode(bytes(session_token, 'utf-8')).decode()
        print("encoded_session_token ", encoded_session_token)

        #This is what an Authorization header should look like
        self.authorization = encoded_session_token
        self.timeCreated = datetime.datetime.now()
        return self.authorization
    
    def api_v1_user_searchAll(self):
        """ DEPRECATED - Use swagger_client instead
        Returns all users

        Parameters:

        Returns:
        string: reply from the server
        
        """
        r = urllib3.PoolManager().request('GET', 'http://tasking-manager-msopenmaps.cloudapp.net/api/v1/user/search-all',
                  headers={'Authorization': self.authorization,
                          'Server': 'nginx',
                          'Content-Type': 'application/json',
                          'Vary': 'Accept-Encoding',
                          'Content-Encoding': 'gzip'})
        
        print(r.data.decode())
        return r.data.decode()
    
    def api_v1_admin_createProject(self,
                                arbitraryTasks,
                                areaOfInterest,
                                projectName,
                                tasks,
                                cloneFromProjectId=None):
      """ DEPRECATED - Use swagger_client instead
      Creates a new project for the user

      Parameters:
      Project parameters

      Returns:
      string: reply from the server
      
      """
      encoded_body = ""
      if(cloneFromProjectId == None):
          encoded_body = json.dumps({
            "arbitraryTasks": arbitraryTasks,
            "areaOfInterest": areaOfInterest,
            "projectName": projectName,
            "tasks": tasks
          })
      else:
          encoded_body = json.dumps({
            "arbitraryTasks": arbitraryTasks,
            "areaOfInterest": areaOfInterest,
            "cloneFromProjectId": cloneFromProjectId,
            "projectName": projectName,
            "tasks": tasks
          })
      r = urllib3.PoolManager().request('PUT', 'http://tasking-manager-msopenmaps.cloudapp.net/api/v1/admin/project',
                headers={'Authorization': self.authorization,
                        'Accept': 'text/html',
                        'Server': 'nginx',
                        'Content-Type': 'application/json',
                        'Vary': 'Accept-Encoding',
                        'Content-Encoding': 'gzip'},
                body = encoded_body)
      print(r.data.decode())
      return r.data.decode()

    def api_v1_admin_updateProject(self,
                                  project_id,
                                  allowNonBeginners=None,
                                  allowedUsernames=None,
                                  campaignTag=None,
                                  changesetComment=None,
                                  defaultLocale=None,
                                  dueDate=None,
                                  enforceMapperLevel=None,
                                  enforceValidatorRole=None,
                                  entitiesToMap=None,
                                  imagery=None,
                                  josmPreset=None,
                                  licenseId=None,
                                  mapperLevel=None,
                                  mappingEditors=None,
                                  mappingTypes=None,
                                  organisationTag=None,
                                  priorityAreas=None,
                                  private=None,
                                  projectInfoLocales=None,
                                  projectPriority=None,
                                  projectStatus=None,
                                  taskCreationMode=None,
                                  validationEditors=None):
        """ DEPRECATED - Use swagger_client instead.
        Updates the project with the given id
    
        Parameters:
        project_id (int): Id of the target project
    
        Returns:
        string: reply from the server
        
        """
        parameters = locals().copy()
        body_dict = {}
        for p in parameters:
          if(p != 'self' and parameters[p] != None):
            body_dict[p] = parameters[p]
    
        encoded_body = json.dumps(body_dict)
        r = urllib3.PoolManager().request('POST', 'http://tasking-manager-msopenmaps.cloudapp.net/api/v1/admin/project/' + str(project_id),
                    headers={'Authorization': self.authorization,
                            'Accept': 'text/html',
                            'Server': 'nginx',
                            'Content-Type': 'application/json',
                            'Vary': 'Accept-Encoding',
                            'Content-Encoding': 'gzip'},
                    body = encoded_body)
        print(r.data.decode())
        return r.data.decode()

class ProjectsApi:

    def api_custom_project_project_id_get(self, authorization, project_id):
        """ Returns a json object of the target project.

        Parameters:
        authorization : header-ready string containing the base64 encoded session string, "Token TVRBeE1qY...USQ=="
        project_id : target project id

        Returns:
        dict : json object containing project information
            
        """
        headers = {
            "Authorization" : authorization,
            "Accept" : "application/json, text/plain, */*",
            "Accept-Encoding" : "gzip, deflate",
            "Accept-Language" : "en",
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }

        reply = urllib3.PoolManager().request('GET', 'http://tasking-manager-msopenmaps.cloudapp.net/api/v1/project/'+str(project_id), headers=headers)
        #print(reply.data.decode())
        return json.loads(reply.data)


#my_api_instance = MyAPI()
#my_api_instance.obtain_authorization(admin_username, admin_password)
#my_api_instance.api_v1_admin_createProject(arbitraryTasks, areaOfInterest, cloneFromProjectId, projectName, tasks)

#project_admin_api_instance = project_admin_api.ProjectAdminApi()

#project_admin_api_instance.api_v1_admin_project_project_id_delete(my_api_instance.get_authorization(), 398)
#project_admin_api_instance.api_v1_admin_project_project_id_delete(my_api_instance.get_authorization(), 391)

""" body = {
  "arbitraryTasks" : False,
  "areaOfInterest" : {
    "features": [
      {
        "geometry": {
          "type": "MultiPolygon",
          "coordinates": [
            [
              [ [21.402567, 44.818087], [21.414927, 44.817600], [21.413725, 44.825027], [21.603254, 44.823444], [21.402567, 44.818087] ]
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
                [ [21, 45], [21, 44.7], [20, 44.7], [20, 45], [21, 45] ]
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
    "type" : "FeatureCollection"
  }
}
encoded_body = json.dumps(body)
reply = project_admin_api_instance.api_v1_admin_project_put(body, my_api_instance.get_authorization(), _preload_content=False)
print(reply.data.decode()) """

""" grid_api_instance = grid_api.GridApi()
body = {
  "areaOfInterest" : {
    "features" : [
      {
        "geometry": {
          "type": "MultiPolygon",
          "coordinates": [
            [
              [ [21, 45], [21, 44.7], [20, 44.7], [20, 45], [21, 45] ]
            ]
          ]
        },
        "properties": {
          "isSquare": True,
          "x": 1000,
          "y": 600,
          "zoom": 15
        },
        "type": "Feature"
      }
    ],
    "type": "FeatureCollection"
  },
  "clipToAoi" : False,
  "grid" :  {
    "features": [
      {
        "geometry": {
          "type": "MultiPolygon",
          "coordinates": [
              [
                [ [20.402567, 44.818087], [20.414927, 44.817600], [20.413725, 44.825027], [20.403254, 44.823444], [20.402567, 44.818087] ]
              ]
            ]
        },
        "properties": {

          "isSquare": True,
          "x": 1000,
          "y": 600,
          "zoom": 19
        },
        "type": "Feature"
      }
    ],
    "type" : "FeatureCollection"
  }
}
reply = grid_api_instance.api_v1_grid_intersecting_tiles_put(body, my_api_instance.get_authorization(), _preload_content=False)
print(reply.data.decode()) """

#UserLoginAPI().obtain_authorization("v-fita@microsoft.com", "Vvardenfello1")