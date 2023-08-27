import json, requests
class RequestGetAllExportStorage:
    def __init__(self, project_id):
        self.project_id = project_id
        self.url = "http://localhost:8080/api/storages/export/localfiles?project={}".format(self.project_id)
        self.token="11e38f35519b1981642791bde53c2fb8fa4e0784"
        


    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token),
            "Content-Type": "application/json"
        }

    
        x = requests.get(self.url, headers=headers)

        return x.json()