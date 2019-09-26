import urllib3
from bs4 import BeautifulSoup as bs
import mechanize
import cookiejar
import base64
from swaggerAPIClient.swagger_client.rest import ApiException
import json
from swaggerAPIClient.swagger_client.api import authentication_api, project_admin_api, mapping_api, grid_api
import datetime

class UserLoginAPI:

    def __init__(self, authorization=""):
        #self.http = urllib3.PoolManager()
        self.username = "unspecified"
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

    def get_username(self):
        """ Returns username

        Parameters:

        Returns:
        string: last username used

        """
        return self.username

    def set_username(self, username):
        """ Sets the username
		
        Parameters:
        username (string): username

        Returns:
        void
		"""
        self.username = username

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
        #print("autheticity_token ", authenticity_token)
        #print("oauth_token ", oauth_token)

        br.select_form(nr=0)
        res = br.submit()

        #Obtaining the session_token from the url
        session_token = res.wrapped._url.split("&")[1].split("=")[1]
        #print("session_token ", session_token)
        content = res.read()

        #Encoding the token as a base64 string. Required format
        encoded_session_token = base64.b64encode(bytes(session_token, 'utf-8')).decode()
        #print("encoded_session_token ", encoded_session_token)

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
        authorization : header-ready string containing the base64 encoded session string
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
