from flask import current_app
import requests, os
from dotenv import load_dotenv
load_dotenv()
class RequestDeleteExportStorage:
    def __init__(self, file_id):
        self.file_id = file_id
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']
        self.url = "http://localhost:8080/api/storages/localfiles/{}".format(self.file_id)
        
    def do(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: file_id: {self.file_id}")
            headers = {
                "Authorization":"Token {}".format(self.token)
            }

            x = requests.delete(self.url, headers=headers)

            print(x)
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {x.status_code}")
            return x.status_code
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404