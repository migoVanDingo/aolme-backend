import requests, os
from dotenv import load_dotenv
load_dotenv()
class RequestGetTaskById:

    def __init__(self, task_id):
        self.task_id = task_id
        self.url = "http://localhost:8080/api/tasks/{}".format(self.task_id)
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']


    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token)
        }

        x = requests.get(self.url, headers=headers)

        return x.json()
