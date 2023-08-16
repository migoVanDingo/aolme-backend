import json, requests
class RequestValidateLabelConfig:

    def __init__(self, config):
        self.config = config
        self.url = "http://localhost:8080/api/projects/validate"

    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token),
            "Content-Type": "application/json"
        }

        data = json.dumps(self.data)
        x = requests.post(self.url, data=self.config, headers=headers)

        return x.json()