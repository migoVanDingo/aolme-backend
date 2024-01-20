from api.label_studio.ls_project.AbstractLsProject  import AbstractLsProject

class RequestGetLsProjectList(AbstractLsProject):
    def __init__(self):
        pass

    def do_process(self):
        return self.get_ls_project_list()