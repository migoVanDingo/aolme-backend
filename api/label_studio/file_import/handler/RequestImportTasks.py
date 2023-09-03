import json, requests, os
class RequestImportTasks:
    def __init__(self, project_id, file_name):
        self.project_id = project_id
        self.url = "http://localhost:8080/api/projects/{}/import".format(self.project_id)
        self.token = "baa32e978ffcca4a0f0ec69f00d95f0bcef3fc7f"
        self.file_name = file_name

    def do(self):
        headers = {
            "Authorization":"Token {}".format(self.token),
            "Content-Type": "application/json"
        }
        current_directory = os.getcwd()
            
        uploads_directory = os.path.join(current_directory, 'uploads')
        uploads_directory = os.path.join(uploads_directory, self.file_name)
        files = {'file': open(uploads_directory, 'r')}

        x = requests.post(self.url, files=files, headers=headers)

        return x.json()