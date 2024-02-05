from api.module.AbstractModule import AbstractModule

class RequestGetModuleListByProject(AbstractModule):
    def __init__(self, project_id):
        self.project_id = project_id

    def do_process(self):
        return self.read_list_project(self.project_id)