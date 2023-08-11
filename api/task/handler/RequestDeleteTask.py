class RequestDeleteTask:

    def __init__(self, project_id, task_id):
        self.project_id = project_id
        self.task_id = task_id
        

    def do(self):
      
        return "delete task {} for project {}".format(self.task_id, self.project_id)
