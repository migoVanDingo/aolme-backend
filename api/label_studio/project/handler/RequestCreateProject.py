import requests, json
class RequestCreateProject:
    
    def __init__(self, data):
        self.data = data
        self.url = "http://localhost:8080/api/projects/"
        self.token="baa32e978ffcca4a0f0ec69f00d95f0bcef3fc7f"
        

    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token),
            "Content-Type": "application/json"
        }

        data = json.dumps(self.data)
        x = requests.post(self.url, data=data, headers=headers)

        return x.json()
    