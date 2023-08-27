import json, requests
class RequestCreateTask:

    def __init__(self, data):
        self.data = data
        self.url = "http://localhost:8080/api/tasks"
        self.token="11e38f35519b1981642791bde53c2fb8fa4e0784"

    def do(self):

        headers = {
            "Authorization":"Token {}".format(self.token),
            "Content-Type": "application/json"
        }

        data = json.dumps(self.data)
        x = requests.post(self.url, data=data, headers=headers)

        return x.json()