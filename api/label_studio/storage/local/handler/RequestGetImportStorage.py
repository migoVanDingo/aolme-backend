import requests, os
from dotenv import load_dotenv
load_dotenv()
class RequestGetImportStorage:
    def __init__(self, file_id):
        self.file_id = file_id
        self.url = "http://localhost:8080/api/storages/export/localfiles/{}".format(self.file_id)
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']
        


    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token),
            "Content-Type": "application/json"
        }

    
        x = requests.get(self.url, headers=headers)

        return x.json()