class RequestGetTasksList:

    def __init__(self, project_id):
        self.project_id = project_id
        
    def do(self):
        return "Request Get Tasks List for project {}".format(self.project_id)