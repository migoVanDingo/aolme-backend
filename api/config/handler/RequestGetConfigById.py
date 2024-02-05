from api.config.AbstractConfig import AbstractConfig

class RequesetGetConfigById(AbstractConfig):
    def __init__(self, config_id):
        self.config_id = config_id

    def do_process(self):
        return self.read_item(self.config_id)