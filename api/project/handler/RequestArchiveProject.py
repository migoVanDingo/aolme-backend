from flask import current_app
from api.project.AbstractProject import AbstractProject

class RequestArchiveProject(AbstractProject):
    def __init__(self, project_id):
        self.project_id = project_id

    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: project_id: {self.project_id}")
            response = self.archive_project(self.project_id)

            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}"