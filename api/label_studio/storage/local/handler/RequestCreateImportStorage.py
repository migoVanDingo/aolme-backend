import json, requests, os
from dotenv import load_dotenv
load_dotenv()
class RequestCreateImportStorage:
    def __init__(self, payload):
        self.payload = payload
        self.url = "http://localhost:8080/api/storages/localfiles"
        self.token= os.environ['LABEL_STUDIO_SECRET_KEY']
        


    def do(self):
        try:
            print("Token: {}".format(self.token))
            headers = {
                "Authorization":"Token {}".format(self.token),
                "Content-Type": "application/json"
            }
            

            data = json.dumps(self.payload)
            x = requests.post(self.url, data=data, headers=headers)

            return x.json()
        except Exception as e:
            return "Error: " + str(e), 404