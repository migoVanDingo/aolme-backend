from api.label_studio.ls_project.AbstractLsProject  import AbstractLsProject

class RequestUpdateLsProject(AbstractLsProject):
    def __init__(self):
        pass

    def do_process(self, ls_project_id, payload):
        response = self.update_ls_project(ls_project_id, payload)
        return self.update_ls_project(ls_project_id, response)