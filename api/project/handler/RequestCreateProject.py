from api.project.AbstractProject import AbstractProject
from api.project.utility.validator.CreateProjectValidator import CreateProjectValidator

class RequestCreateProject(AbstractProject):
    def __init__(self, params):
        self.params = params

    def do_process(self):

        validate = CreateProjectValidator(self.params)
        is_valid = validate.validate()
        if is_valid[0] is False:
            return is_valid[1]

        return self.create_project(self.params)