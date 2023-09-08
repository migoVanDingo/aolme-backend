import requests, os
from dotenv import load_dotenv
load_dotenv()
class RequestDeleteExportStorage:
    def __init__(self, file_id):
        self.file_id = file_id
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']
        self.url = "http://localhost:8080/api/storages/localfiles/{}".format(self.file_id)
        
    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token)
        }

        x = requests.delete(self.url, headers=headers)

        print(x)
        return x.status_code