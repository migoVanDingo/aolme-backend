import json, requests

class RequestUpdateProject:
    def __init__(self, project_id, data):
        self.project_id = project_id
        self.data = data
        self.url = "http://localhost:8080/api/projects/{}".format(self.project_id)
        
    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token),
            "Content-Type": "application/json"
        }

        data = json.dumps(self.data)
        x = requests.patch(self.url, data=data, headers=headers)

        return x.json()