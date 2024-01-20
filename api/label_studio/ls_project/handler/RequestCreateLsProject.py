from api.label_studio.ls_project.AbstractLsProject  import AbstractLsProject

class RequestCreateLsProject(AbstractLsProject):
    def __init__(self):
        pass

    def do_process(self, payload):
        response = self.create_ls_project(payload)
        return self.insert_ls_project(response)
