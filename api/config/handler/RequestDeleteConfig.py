from api.config.AbstractConfig import AbstractConfig

class RequestDeleteConfig(AbstractConfig):
    def __init__(self, config_id):
        self.config_id = config_id

    def do_process(self):
        return self.delete(self.config_id)