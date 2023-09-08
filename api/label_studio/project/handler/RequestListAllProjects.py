import json, requests,os
from dotenv import load_dotenv
load_dotenv()
class RequestListAllProjects:
    def __init__(self):
        self.url = "http://localhost:8080/api/projects"
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']
        
    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token)
        }

        #data = json.dumps(self.data)
        x = requests.get(self.url, headers=headers)

        return x.json()