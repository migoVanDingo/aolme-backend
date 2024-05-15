from flask import current_app
import requests, os
from dotenv import load_dotenv
load_dotenv()
class RequestGetTaskById:

    def __init__(self, task_id):
        self.task_id = task_id
        self.url = "http://localhost:8080/api/tasks/{}".format(self.task_id)
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']


    def do(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: task_id: {self.task_id}")
            headers = {
                "Authorization":"Token {}".format(self.token)
            }

            x = requests.get(self.url, headers=headers)
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {x.json()}")
            return x.json()
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404
