from flask import current_app
from api.project.AbstractProject import AbstractProject
from api.project.utility.validator.CreateProjectValidator import CreateProjectValidator

class RequestCreateProject(AbstractProject):
    def __init__(self, params):
        self.params = params

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {self.params}")
            validate = CreateProjectValidator(self.params)
            is_valid = validate.validate()
            if is_valid[0] is False:
                return is_valid[1]

            return self.create_project(self.params)
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}"