from flask import current_app
import json, requests,os
from dotenv import load_dotenv
load_dotenv()
class RequestDeleteProject:
    def __init__(self, project_id):
        self.project_id = project_id
        self.token= os.environ['LABEL_STUDIO_SECRET_KEY']
        self.url = "http://localhost:8080/api/projects/{}".format(self.project_id)
        
    def do(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: project_id: {self.project_id}")
            headers = {
                "Authorization":"Token {}".format(self.token)
            }

            x = requests.delete(self.url, headers=headers)
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {x.status_code}")
            print(x)
            return x.status_code
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404
        