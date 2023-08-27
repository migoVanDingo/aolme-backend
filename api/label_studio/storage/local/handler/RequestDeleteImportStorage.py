import requests
class RequestDeleteImportStorage:
    def __init__(self, file_id):
        self.file_id = file_id
        self.token="11e38f35519b1981642791bde53c2fb8fa4e0784"
        self.url = "http://localhost:8080/api/storages/localfiles/{}".format(self.file_id)
        
    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token)
        }

        x = requests.delete(self.url, headers=headers)

        print(x)
        return x.status_code