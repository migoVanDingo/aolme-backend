import json, requests
class RequestListAllProjects:
    def __init__(self):
        self.url = "http://localhost:8080/api/projects"
        self.token="11e38f35519b1981642791bde53c2fb8fa4e0784"
        
    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token)
        }

        #data = json.dumps(self.data)
        x = requests.get(self.url, headers=headers)

        return x.json()