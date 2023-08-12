class RequestValidateLabelConfig:

    def __init__(self, project_id, config):
        self.project_id = project_id
        self.config = config

    def do(self):
        return "project {} config {}".format(self.project_id, self.config)