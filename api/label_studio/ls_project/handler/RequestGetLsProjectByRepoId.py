from flask import jsonify
from api.label_studio.ls_project.AbstractLsProject import AbstractLsProject

class RequestGetLsProjectByRepoId(AbstractLsProject):
    def __init__(self, repo_id):
        super().__init__()
        self.repo_id = repo_id

    def do_process(self):
        try:
            ls_project = self.get_ls_project_by_repo_id(self.repo_id)
            print("ls_project: {}".format(ls_project))

            return jsonify(ls_project)
            
        except Exception as e:
            print("Error: {}".format(e))
            return None