from api.project.AbstractProject import AbstractProject

class RequestDeleteProject(AbstractProject):
    def __init__(self, project_id):
        self.project_id = project_id

    def do_process(self):
        return self.delete_project(self.project_id)