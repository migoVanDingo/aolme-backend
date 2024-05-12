from flask import current_app
from api.label_studio.ls_project.AbstractLsProject  import AbstractLsProject

class RequestGetLsProject(AbstractLsProject):
    def __init__(self):
        pass

    def do_process(self, ls_project_id):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: ls_project_id: {ls_project_id}")
            response = self.get_ls_project(ls_project_id)
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404