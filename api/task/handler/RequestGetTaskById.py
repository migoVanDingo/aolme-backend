import requests
class RequestGetTaskById:

    def __init__(self, task_id):
        self.task_id = task_id
        self.url = "http://localhost:8080/api/tasks/{}".format(self.task_id)
        self.token="11e38f35519b1981642791bde53c2fb8fa4e0784"


    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token)
        }

        x = requests.get(self.url, headers=headers)

        return x.json()
