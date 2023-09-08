import json, requests, os
from dotenv import load_dotenv
load_dotenv()
class RequestDeleteTask:

    def __init__(self, task_id):
        self.task_id = task_id
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']
        self.url = "http://localhost:8080/api/tasks/{}".format(self.task_id)
        
    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token)
        }

        x = requests.delete(self.url, headers=headers)

        return x.status_code
