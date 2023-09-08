import json, requests, os
from dotenv import load_dotenv
load_dotenv()
class RequestGetAllExportStorage:
    def __init__(self, project_id):
        self.project_id = project_id
        self.url = "http://localhost:8080/api/storages/export/localfiles?project={}".format(self.project_id)
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']
        


    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token),
            "Content-Type": "application/json"
        }

    
        x = requests.get(self.url, headers=headers)

        return x.json()