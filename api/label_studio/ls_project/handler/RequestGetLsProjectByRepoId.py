from flask import current_app, jsonify
from api.label_studio.ls_project.AbstractLsProject import AbstractLsProject

class RequestGetLsProjectByRepoId(AbstractLsProject):
    def __init__(self, repo_id):
        super().__init__()
        self.repo_id = repo_id

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: repo_id: {self.repo_id}")
            ls_project = self.get_ls_project_by_repo_id(self.repo_id)

            
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {ls_project}")
            return jsonify(ls_project)
            
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404