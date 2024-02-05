from api.module.AbstractModule import AbstractModule

class RequestDeleteModule(AbstractModule):
    def __init__(self, module_id):
        self.module_id = module_id

    def do_process(self):
        return self.delete(self.module_id)