from api.config.AbstractConfig import AbstractConfig
class RequestGetConfigByProject(AbstractConfig):
    def __init__(self, project_id):
        self.project_id = project_id

    def do_process(self):
        return self.read_item_project(self.project_id)