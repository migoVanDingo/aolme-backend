import datetime
from api.project import AbstractProject

class RequestUpdateProject(AbstractProject):
    def __init__(self, params):
        self.params = params

    def do_process(self):
        self.params['updated_at'] = datetime.now()
        self.params['updated_by'] = self.params['updated_by']
        
        return self.update_project(self.params)