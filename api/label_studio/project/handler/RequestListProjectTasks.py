import json
import requests, os
from dotenv import load_dotenv
load_dotenv()
class RequestListProjectTasks:
    def __init__(self, project_id):
        self.project_id = project_id
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']
        self.url = "http://localhost:8080/api/projects/{}/tasks/?page=1&page_size=10".format(self.project_id)

    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token)
        }

        x = requests.delete(self.url, headers=headers)

        print(x)
        return x