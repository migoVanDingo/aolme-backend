class RequestCreateTask:

    def __init__(self, project_id, name):
        self.project_id = project_id
        self.name = name

    def do(self):
        return "create task {} for project {}".format(self.name, self.project_id)
