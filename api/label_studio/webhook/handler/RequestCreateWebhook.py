from flask import current_app
import os, requests
from dotenv import load_dotenv
load_dotenv()
class RequestCreateWebhook:
    def __init__(self, payload):
        self.payload = payload
        self.url = "http://localhost:8080/api/webhooks/"
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']

    def do(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {self.payload}")
            headers = {
                "Authorization":"Token {}".format(self.token)
            }

            response = requests.post(self.url, data=self.payload, headers=headers)

            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response.content.decode('utf-8')}")
            return response.content.decode('utf-8')
        except Exception as e:
            return "Error: " + str(e), 404