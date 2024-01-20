from api.label_studio.ls_project.AbstractLsProject import AbstractLsProject

class RequestArchiveLsProject(AbstractLsProject):
    def __init__(self):
        pass

    def do_process(self, ls_project_id):
        return self.archive_ls_project(ls_project_id)