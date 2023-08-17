import json, requests
class RequestUpdateExportStorage:
    def __init__(self, file_id, payload):
        self.file_id = file_id
        self.payload = payload
        self.url = "http://localhost:8080/api/storages/export/localfiles/{}".format(file_id)
        self.token="11e38f35519b1981642791bde53c2fb8fa4e0784"
        


    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token),
            "Content-Type": "application/json"
        }

        data = json.dumps(self.payload)
        x = requests.post(self.url, data=data, headers=headers)

        return x.json()