from flask import current_app
import json, requests, os
from dotenv import load_dotenv
load_dotenv()
class RequestValidateImportStorage:
    def __init__(self, payload):
        self.payload = payload
        self.url = "http://localhost:8080/api/storages/localfiles/validate"
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']
        


    def do(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {self.payload}")
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