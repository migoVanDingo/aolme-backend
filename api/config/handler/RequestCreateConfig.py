from api.config.AbstractConfig import AbstractConfig

class RequestCreateConfig(AbstractConfig):
    def __init__(self, payload):
        self.payload = payload

    def do_process(self):
        return self.create(self.payload)