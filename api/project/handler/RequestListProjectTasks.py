import json
import requests
class RequestListProjectTasks:
    def __init__(self, project_id):
        self.project_id = project_id
        self.token="11e38f35519b1981642791bde53c2fb8fa4e0784"
        self.url = "http://localhost:8080/api/projects/{}/tasks/?page=1&page_size=10".format(self.project_id)

    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token)
        }

        x = requests.delete(self.url, headers=headers)

        print(x)
        return x