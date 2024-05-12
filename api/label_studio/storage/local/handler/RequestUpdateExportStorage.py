from flask import current_app
import json, requests, os
from dotenv import load_dotenv
load_dotenv()
class RequestUpdateExportStorage:
    def __init__(self, file_id, payload):
        self.file_id = file_id
        self.payload = payload
        self.url = "http://localhost:8080/api/storages/export/localfiles/{}".format(file_id)
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']
        


    def do(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: file_id: {self.file_id}")
            headers = {
                "Authorization":"Token {}".format(self.token),
                "Content-Type": "application/json"
            }

            data = json.dumps(self.payload)
            x = requests.post(self.url, data=data, headers=headers)

            return x.json()
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404