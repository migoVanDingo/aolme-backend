from api.config.AbstractConfig import AbstractConfig

class RequestUpdateConfig(AbstractConfig):
    def __init__(self, config_id, params):
        self.config_id = config_id
        self.params = params

    def do_process(self):
        try:
            return self.update(self.config_id, self.params)
        except Exception as e:
            return "RequestUpdateConfig -- do_process() Error: " + str(e)