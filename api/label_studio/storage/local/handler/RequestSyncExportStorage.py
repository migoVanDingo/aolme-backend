from flask import current_app
import json, requests, os
from dotenv import load_dotenv
load_dotenv()
class RequestSyncExportStorage:
    def __init__(self, file_id, payload):
        self.payload = payload
        self.url = "http://localhost:8080/api/storages/export/localfiles/{}/sync".format(self.file_id)
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']
        


    def do(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: file_id: {self.file_id}")
            headers = {
                "Authorization":"Token {}".format(self.token),
                "Content-Type": "application/json"
            }

            data = json.dumps(self.payload)
            x = requests.post(self.url, data=data, headers=headers)
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {x.json()}")
            return x.json()
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404