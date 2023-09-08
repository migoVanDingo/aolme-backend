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
            headers = {
                "Authorization":"Token {}".format(self.token)
            }

            response = requests.post(self.url, data=self.payload, headers=headers)

            print("response: {}".format(response.content.decode('utf-8')))

            
            return response.content.decode('utf-8')
        except Exception as e:
            return "Error: " + str(e), 404