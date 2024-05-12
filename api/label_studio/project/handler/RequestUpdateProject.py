from flask import current_app
import json, requests

class RequestUpdateProject:
    def __init__(self, project_id, data):
        self.project_id = project_id
        self.data = data
        self.url = "http://localhost:8080/api/projects/{}".format(self.project_id)
        
    def do(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: project_id: {self.project_id}")
            headers = {
                "Authorization":"Token {}".format(self.token),
                "Content-Type": "application/json"
            }

            data = json.dumps(self.data)
            x = requests.patch(self.url, data=data, headers=headers)
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {x.json()}")

            return x.json()
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404