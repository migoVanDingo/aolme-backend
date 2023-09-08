import json, requests, os
from dotenv import load_dotenv
load_dotenv()
class RequestUpdateTask:
    def __init__(self, project_id, task_id, data):
        self.project_id = project_id
        self.task_id = task_id
        self.data = data
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']
        self.url = "http://localhost:8080/api/tasks{}".format(self.task_id)

    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token),
            "Content-Type": "application/json"
        }

        data = json.dumps(self.data)
        x = requests.patch(self.url, data=data, headers=headers)

        return x.json()