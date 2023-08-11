class RequestUpdateTask:
    def __init__(self, project_id, task_id, name):
        self.project_id = project_id
        self.task_id = task_id
        self.name = name

    def do(self):
        
        return "update project {} task {} with new name {}".format(self.project_id, self.task_id, self.name)