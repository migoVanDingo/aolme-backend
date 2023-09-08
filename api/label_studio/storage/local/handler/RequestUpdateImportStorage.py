import json, requests, os
from dotenv import load_dotenv
load_dotenv()
class RequestUpdateImportStorage:
    def __init__(self, payload):
        self.payload = payload
        self.url = "http://localhost:8080/api/storages/export/localfiles"
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']
        


    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token),
            "Content-Type": "application/json"
        }

        data = json.dumps(self.payload)
        x = requests.post(self.url, data=data, headers=headers)

        return x.json()