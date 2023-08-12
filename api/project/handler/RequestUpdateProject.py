class RequestUpdateProject:
    def __init__(self, project_id, name):
        self.project_id = project_id
        self.name = name
        
    def do(self):
        return "update-project {}".format(self.project_id)