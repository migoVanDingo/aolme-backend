from flask import current_app
import json, requests, os
from dotenv import load_dotenv
load_dotenv()
class RequestUpdateTask:
    def __init__(self, project_id, task_id, data):
        self.project_id = project_id
        self.task_id = task_id
        self.data = data
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']
        self.url = "http://localhost:8080/api/tasks{}".format(self.task_id)

    def do(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {self.data}")
            headers = {
                "Authorization":"Token {}".format(self.token),
                "Content-Type": "application/json"
            }

            data = json.dumps(self.data)
            x = requests.patch(self.url, data=data, headers=headers)
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {x.json()}")
            return x.json()
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404