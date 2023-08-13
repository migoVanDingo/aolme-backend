class RequestCreateTask:

    def __init__(self, project_id, data):
        self.project_id = project_id
        self.data = data

    def do(self):
        return "project id {} data {}".format(self.project_id, self.data)
