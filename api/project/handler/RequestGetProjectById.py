class RequestGetProjectById:
    def __init__(self, project_id):
        self.project_id = project_id
        
    def do(self):
        return "get-project-by-id {}".format(self.project_id)