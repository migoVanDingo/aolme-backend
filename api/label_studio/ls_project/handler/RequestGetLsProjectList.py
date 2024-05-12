from flask import current_app
from api.label_studio.ls_project.AbstractLsProject  import AbstractLsProject

class RequestGetLsProjectList(AbstractLsProject):
    def __init__(self):
        pass

    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: get_ls_project_list")
            response = self.get_ls_project_list()
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404