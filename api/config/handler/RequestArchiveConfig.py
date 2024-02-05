from api.config.AbstractConfig import AbstractConfig

class RequestArchiveConfig(AbstractConfig):
    def __init__(self, config_id):
        self.config_id = config_id

    def do_process(self):
        return self.archive(self.config_id)