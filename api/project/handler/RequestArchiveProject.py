from api.project import AbstractProject

class RequestArchiveProject(AbstractProject):
    def __init__(self, project_id):
        self.project_id = project_id

    def do_process(self):
        return self.archive_project(self.project_id)