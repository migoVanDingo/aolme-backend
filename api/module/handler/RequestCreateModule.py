from api.module.AbstractModule import AbstractModule

class RequestCreateModule(AbstractModule):
    def __init__(self, payload):
        self.payload = payload

    def do_process(self):
        pass