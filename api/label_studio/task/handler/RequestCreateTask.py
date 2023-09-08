import json, requests, os
from dotenv import load_dotenv
load_dotenv()
class RequestCreateTask:

    def __init__(self, data):
        self.data = data
        self.url = "http://localhost:8080/api/tasks"
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']

    def do(self):

        headers = {
            "Authorization":"Token {}".format(self.token),
            "Content-Type": "application/json"
        }

        data = json.dumps(self.data)
        x = requests.post(self.url, data=data, headers=headers)

        return x.json()