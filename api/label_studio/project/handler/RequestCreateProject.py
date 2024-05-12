from flask import current_app
import requests, json, os
from dotenv import load_dotenv
load_dotenv()
class RequestCreateProject:
    
    def __init__(self, data):
        self.data = data
        self.url = "http://localhost:8080/api/projects/"
        self.token= os.environ['LABEL_STUDIO_SECRET_KEY']
        

    def do(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: payload: {self.data}")   
            headers = {
                "Authorization":"Token {}".format(self.token),
                "Content-Type": "application/json"
            }

            print("headers: {}".format(headers))

            data = json.dumps(self.data)
            x = requests.post(self.url, data=data, headers=headers)


            current_app.logger.info(f"{self.__class__.__name__} :: Response: {x.json()}")
            return x.json()
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404
    