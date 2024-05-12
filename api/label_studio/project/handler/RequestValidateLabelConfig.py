from flask import current_app
import json, requests
class RequestValidateLabelConfig:

    def __init__(self, config):
        self.config = config
        self.url = "http://localhost:8080/api/projects/validate"

    def do(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: project_id: {self.project_id}")
            headers = {
                "Authorization":"Token {}".format(self.token),
                "Content-Type": "application/json"
            }

            data = json.dumps(self.data)
            x = requests.post(self.url, data=self.config, headers=headers)
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {x.json()}")
            
            return x.json()
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404