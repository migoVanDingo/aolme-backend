from flask import current_app
import json, requests, os
from dotenv import load_dotenv
load_dotenv()
class RequestSyncImportStorage:
    def __init__(self,local_storage_id, payload):
        self.local_storage_id = local_storage_id
        self.payload = payload
        self.url = "http://localhost:8080/api/storages/localfiles/{}/sync".format(self.local_storage_id)
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']
        
        


    def do(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {self.payload}")    
            headers = {
                "Authorization":"token {}".format(self.token),
                "Content-Type": "application/json"
            }

            data = json.dumps(self.payload)
            x = requests.post(self.url, data=data, headers=headers)
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {x.json()}")
            return x.json()
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "RequestSyncImportStorage()::Error: " + str(e), 404