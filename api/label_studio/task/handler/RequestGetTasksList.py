import json, requests, os
from dotenv import load_dotenv
load_dotenv()
class RequestGetTasksList:

    def __init__(self, data):
        self.data = data
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']
        self.url = "http://localhost:8080/api/tasks"
        
    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token)
        }

        x = requests.get(self.url, headers=headers)

        return x.json()
    


    def addUrlParams(self):
        
        if self.data["view"] is not None:
            self.url += "?view={}&".format(self.data["view"])
        
        if self.data["project_id"] is not None:
            self.url += "?project={}&".format(self.data["project_id"])

        if self.data["resolve_uri"] is not None:
            self.url += "?resolve_uri={}".format(self.data["resolve_uri"])