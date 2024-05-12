from flask import current_app
import json, requests,os
from dotenv import load_dotenv
load_dotenv()
class RequestListAllProjects:
    def __init__(self):
        self.url = "http://localhost:8080/api/projects"
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']
        
    def do(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: project_id: {self.project_id}")
            headers = {
                "Authorization":"Token {}".format(self.token)
            }

            #data = json.dumps(self.data)
            x = requests.get(self.url, headers=headers)
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {x.json()}")
            return x.json()
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404