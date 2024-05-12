import datetime

from flask import current_app
from api.project.AbstractProject import AbstractProject

class RequestUpdateProject(AbstractProject):
    def __init__(self, params):
        self.params = params

    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: payload: {self.params}")
            self.params['updated_at'] = datetime.now()
            self.params['updated_by'] = self.params['updated_by']
            
            current_app.logger.info(f"{self.__class__.__name__} :: update-project-payload: {self.params}")
            response = self.update_project(self.params)
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}"