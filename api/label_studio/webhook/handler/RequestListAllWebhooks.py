from flask import current_app
import requests, os
from dotenv import load_dotenv
load_dotenv()

class RequestListAllWebhooks:
    def __init__(self, project_id):
        self.project_id = project_id
        self.url = "http://localhost:8080/api/webhooks?project={}".format(self.project_id)
        self.token= os.environ['LABEL_STUDIO_SECRET_KEY']
        
    def do(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: project_id: {self.project_id}")
            headers = {
            "Authorization":"Token {}".format(self.token)
            }
            response = requests.get(self.url, headers=headers)
            #print('Request List All Webhooks: {}'.format(response))

            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response.json()}")
            return response.json()
        
        except Exception as e:
            return "Error: " + str(e), 404
    
