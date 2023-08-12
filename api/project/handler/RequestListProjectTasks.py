class RequestListProjectTasks:
    def __init__(self, project_id):
        self.project_id = project_id

    def do(self):
        return "List project tasks, project {}".format(self.project_id)