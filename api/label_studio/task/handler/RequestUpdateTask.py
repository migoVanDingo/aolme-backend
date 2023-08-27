import json, requests
class RequestUpdateTask:
    def __init__(self, project_id, task_id, data):
        self.project_id = project_id
        self.task_id = task_id
        self.data = data
        self.token="11e38f35519b1981642791bde53c2fb8fa4e0784"
        self.url = "http://localhost:8080/api/tasks{}".format(self.task_id)

    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token),
            "Content-Type": "application/json"
        }

        data = json.dumps(self.data)
        x = requests.patch(self.url, data=data, headers=headers)

        return x.json()