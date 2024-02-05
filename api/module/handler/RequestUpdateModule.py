from api.module.AbstractModule import AbstractModule    

class RequestUpdateModule(AbstractModule):
    def __init__(self, payload):
        self.payload = payload

    def do_process(self):
        return self.update(self.payload)