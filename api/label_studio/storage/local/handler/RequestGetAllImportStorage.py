from flask import current_app
import requests
import os
from dotenv import load_dotenv
load_dotenv()


class RequestGetAllImportStorage:
    def __init__(self, project_id):
        self.project_id = project_id
        self.url = "http://localhost:8080/api/storages/localfiles?project={}".format(
            self.project_id)
        self.token = os.environ['LABEL_STUDIO_SECRET_KEY']

    def do(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: project_id: {self.project_id}")
            headers = {
                "Authorization": "Token {}".format(self.token),
                "Content-Type": "application/json"
            }

            x = requests.get(self.url, headers=headers)
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {x.json()}")
            return x.json()
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404
